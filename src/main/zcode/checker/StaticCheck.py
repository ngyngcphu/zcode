from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class VarSymbol:
    def __init__(self, name: str, typ: Type = None):
        self.name = name
        self.typ = typ


class FuncSymbol:
    def __init__(self, name: str, param: List[VarSymbol] = [], rettype: Type = None, body: Stmt = None):
        self.name = name
        self.param = param
        self.rettype = rettype
        self.body = body


class StaticChecker(BaseVisitor, Utils):
    global_envi = [[
        FuncSymbol('readNumber', [], NumberType()),
        FuncSymbol('writeNumber', [VarSymbol('', NumberType())], VoidType()),
        FuncSymbol('readBool', [], BoolType()),
        FuncSymbol('writeBool', [VarSymbol('', BoolType())], VoidType()),
        FuncSymbol('readString', [], StringType()),
        FuncSymbol('writeString', [VarSymbol('', StringType())], VoidType())
    ]]

    def __init__(self, ast: AST):
        self.ast = ast
        self.origin_arrlit_ast = []
        self.func_is_called = False
        self.func_no_body = []
        self.func_has_returned = False
        self.func_current = None
        self.func_return_list = []
        self.in_loop = []
        self.var_current = None

    def __inferType(self, expr: Id | CallExpr | CallStmt | ArrayLiteral, typ: Type, param):
        if type(expr) is Id:
            updated_symbol = next((symbol for symbol_list in param for symbol in symbol_list if type(
                symbol) is VarSymbol and symbol.typ is None and symbol.name == expr.name), None)
            if not updated_symbol:
                return None
            updated_symbol.typ = typ
            return typ

        if type(expr) in [CallExpr, CallStmt]:
            updated_symbol = next((symbol for symbol in param[-1] if type(
                symbol) is FuncSymbol and symbol.rettype is None and symbol.name == expr.name.name), None)
            if not updated_symbol:
                return None
            updated_symbol.rettype = typ
            if updated_symbol.body is not None:
                self.func_is_called = True
                self.visit(FuncDecl(Id(updated_symbol.name), list(map(lambda symbol: VarDecl(
                    Id(symbol.name), symbol.typ, None, None), updated_symbol.param)), updated_symbol.body), param)
                self.func_is_called = False
            return typ

        if type(expr) is ArrayLiteral:
            if type(typ) is not ArrayType:
                return None
            if len(typ.size) == 1:
                return list(map(lambda expr: self.__inferType(expr, typ.eleType, param), expr.value))
            return list(map(lambda expr: self.__inferType(expr, ArrayType(typ.size[1:], typ.eleType), param), expr.value))

        return None

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast: Program, param):
        '''
        `decl`: List[Decl] - empty list if there is no statement in block
        '''
        reduce(lambda acc, cur: self.visit(cur, acc), ast.decl, param)
        if self.func_no_body:
            raise NoDefinition(self.func_no_body[0].name.name)
        found_main_function = next((True for symbol in param[-1] if type(
            symbol) is FuncSymbol and symbol.name == 'main' and type(symbol.rettype) is VoidType and symbol.param == []), None)
        if not found_main_function:
            raise NoEntryPoint()
        return param

    def visitVarDecl(self, ast: VarDecl, param):
        '''
        - `name`: Id
        - `varType`: Type = None - None if there is no type
        - `modifier`: str = None - None if there is no modifier
        - `varInit`: Expr = None - None if there is no initial
        '''
        if self.lookup(ast.name.name, param[0], lambda symbol: symbol.name):
            raise Redeclared(Variable(), ast.name.name)
        if ast.varInit is not None:
            if type(ast.varInit) is ArrayLiteral:
                self.origin_arrlit_ast = []
            var_init_type = self.visit(ast.varInit, param)
            if ast.varType is not None and var_init_type is not None:
                if type(ast.varType) is not type(var_init_type):
                    raise TypeMismatchInStatement(ast)
                if type(var_init_type) is ArrayType:
                    if ast.varType.size != var_init_type.size:
                        raise TypeMismatchInStatement(ast)
                    if var_init_type.eleType is None:
                        # The type of ArrayCell expression cannot be None
                        if type(ast.varInit) not in [Id, CallExpr, ArrayLiteral]:
                            raise TypeCannotBeInferred(ast)
                        var_init_type.eleType = self.__inferType(
                            ast.varInit, ast.varType, param)
                        if var_init_type.eleType is None:
                            raise TypeCannotBeInferred(ast)
                        return [param[0] + [VarSymbol(ast.name.name, ast.varType)]] + param[1:]
                    if type(var_init_type.eleType) is not type(ast.varType.eleType):
                        raise TypeMismatchInStatement(ast)
                return [param[0] + [VarSymbol(ast.name.name, ast.varType)]] + param[1:]
            elif ast.varType is None and var_init_type is None:
                raise TypeCannotBeInferred(ast)
            elif var_init_type is None and ast.varType is not None:
                # If the type of ArrayCell expression is None, raise TypeCannotBeInferred
                if type(ast.varInit) not in [Id, CallExpr, ArrayLiteral]:
                    raise TypeCannotBeInferred(ast)
                var_init_type = self.__inferType(
                    ast.varInit, ast.varType, param)
                if var_init_type is None:
                    raise TypeCannotBeInferred(ast)
                return [param[0] + [VarSymbol(ast.name.name, ast.varType)]] + param[1:]
            else:
                return [param[0] + [VarSymbol(ast.name.name, var_init_type)]] + param[1:]
        return [param[0] + [VarSymbol(ast.name.name, ast.varType)]] + param[1:]

    def visitFuncDecl(self, ast: FuncDecl, param):
        '''
        - `name`: Id
        - `param`: List[VarDecl] - empty list if there is no parameter
        - `body`: Stmt = None - None if this is just a declaration-part
        '''
        func = self.lookup(
            ast.name.name, param[-1], lambda symbol: symbol.name)
        if func is not None and func.body is not None and not self.func_is_called:
            raise Redeclared(Function(), ast.name.name)

        def lookup_param(acc, cur: VarDecl):
            if self.lookup(cur.name.name, acc, lambda symbol: symbol.name):
                raise Redeclared(Parameter(), cur.name.name)
            return acc + [VarSymbol(cur.name.name, cur.varType)]
        param_env = reduce(lookup_param, ast.param, [])

        if ast.body is None:
            if not self.func_is_called:
                self.func_no_body += [ast.name]
            return param[:-1] + [param[-1] + [FuncSymbol(ast.name.name, param_env, None, None)]]

        func_has_body = self.lookup(
            ast.name.name, self.func_no_body, lambda symbol: symbol.name)
        if func_has_body:
            self.func_no_body.remove(func_has_body)

        func_found = next((symbol for symbol in param[-1] if type(
            symbol) is FuncSymbol and symbol.name == ast.name.name), None)
        if func_found:
            if len(func_found.param) != len(param_env):
                raise Redeclared(Function(), ast.name.name)

            def check_param_type(param_src: VarSymbol, param_dest: VarSymbol):
                return type(param_src.typ) is type(param_dest.typ) and (
                    type(param_src.typ) is not ArrayType or (
                        param_src.typ.size == param_dest.typ.size and
                        type(param_src.typ.eleType) is type(
                            param_dest.typ.eleType
                        )
                    )
                )
            if not all(map(check_param_type, func_found.param, param_env)):
                raise Redeclared(Function(), ast.name.name)
            self.func_current = func_found.name
            return_type = self.visit(
                ast.body, [[param_env] + param[0]] + param[1:])
            func_found.rettype = return_type
            func_found.body = ast.body
            self.func_has_returned = False
            self.func_return_list = []
            return param

        self.func_current = ast.name.name
        return_type = self.visit(ast.body, [[param_env] + param[0]] + param[1:-1] + [
                                 param[-1] + [FuncSymbol(ast.name.name, param_env, None, ast.body)]])
        self.func_has_returned = False
        self.func_return_list = []
        return param[:-1] + [param[-1] + [FuncSymbol(ast.name.name, param_env, return_type, ast.body)]]

    def visitNumberType(self, ast: NumberType, param):
        pass

    def visitBoolType(self, ast: BoolType, param):
        pass

    def visitStringType(self, ast: StringType, param):
        pass

    def visitArrayType(self, ast: ArrayType, param):
        '''
        - `size`: List[number]
        - `eleType`: Type
        '''
        pass

    def visitBinaryOp(self, ast: BinaryOp, param):
        '''
        - `op`: str(`+`, `-`, `*`, `/`, `%`, `=`, `!=`, `<`, `>`, `<=`, `>=`, `and`, `or`, `==`, `...`)
        - `left`: Expr
        - `right`: Expr

        Do not infer the type for expressions of binary operator if:
        1. One of the expressions is a ArrayLiteral (because its type is ArrayType).
        2. One of the expressions is a ArrayCell (because there is not enough information to infer the type).
        For example, a[1] can be of type number (if declaring number a[2]) or can be of type ArrayType (if declaring number a[2, 3]).
        '''
        left_type = self.visit(ast.left, param)
        right_type = self.visit(ast.right, param)

        if ast.op in ['+', '-', '*', '/', '%' '=', '!=', '<', '>', '<=', '>=']:
            if left_type is None:
                if type(ast.left) not in [Id, CallExpr]:
                    return None
                left_type = self.__inferType(ast.left, NumberType(), param)
                if left_type is None:
                    return None
            if right_type is None:
                if type(ast.right) not in [Id, CallExpr]:
                    return None
                right_type = self.__inferType(ast.right, NumberType(), param)
                if right_type is None:
                    return None
            if type(left_type) is not NumberType or type(right_type) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType() if ast.op in ['+', '-', '*', '/', '%'] else BoolType()
        elif ast.op in ['and', 'or']:
            if left_type is None:
                if type(ast.left) not in [Id, CallExpr]:
                    return None
                left_type = self.__inferType(ast.left, BoolType(), param)
                if left_type is None:
                    return None
            if right_type is None:
                if type(ast.right) not in [Id, CallExpr]:
                    return None
                right_type = self.__inferType(ast.right, BoolType(), param)
                if right_type is None:
                    return None
            if type(left_type) is not BoolType or type(right_type) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        else:
            if left_type is None:
                if type(ast.left) not in [Id, CallExpr]:
                    return None
                left_type = self.__inferType(ast.left, StringType(), param)
                if left_type is None:
                    return None
            if right_type is None:
                if type(ast.right) not in [Id, CallExpr]:
                    return None
                right_type = self.__inferType(ast.right, StringType(), param)
                if right_type is None:
                    return None
            if type(left_type) is not StringType or type(right_type) is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType() if ast.op == '...' else BoolType()

    def visitUnaryOp(self, ast: UnaryOp, param):
        '''
        - `op`: str(`-`, `not`)
        - `operand`: Expr

        Do not infer the type for expression of unary operator if:
        1. Expression is a ArrayLiteral (because its type is ArrayType).
        2. Expression is a ArrayCell (because there is not enough information to infer the type).
        For example, a[1] can be of type number (if declaring number a[2]) or can be of type ArrayType (if declaring number a[2, 3]).
        '''
        operand_type = self.visit(ast.operand, param)
        if ast.op == '-':
            if operand_type is None:
                if type(ast.operand) not in [Id, CallExpr]:
                    return None
                operand_type = self.__inferType(
                    ast.operand, NumberType(), param)
                if operand_type is None:
                    return None
            elif type(operand_type) is not NumberType:
                raise TypeMismatchInExpression(ast)
        else:
            if operand_type is None:
                if type(ast.operand) not in [Id, CallExpr]:
                    return None
                operand_type = self.__inferType(
                    ast.operand, BoolType(), param)
                if operand_type is None:
                    return None
            elif type(operand_type) is not BoolType:
                raise TypeMismatchInExpression(ast)
        return operand_type

    def visitCallExpr(self, ast: CallExpr, param):
        '''
        - `name`: Id
        - `args`: List[Expr]
        '''
        if self.var_current is not None and ast.name.name == self.var_current:
            raise TypeMismatchInExpression(ast)
        if not all(map(lambda env: self.lookup(ast.name.name, env, lambda symbol: symbol.name) is None, param[:-1])):
            raise TypeMismatchInExpression(ast)
        func_found = self.lookup(
            ast.name.name, param[-1], lambda symbol: symbol.name)
        if func_found is None or (func_found is not None and type(func_found) is not FuncSymbol):
            raise Undeclared(Function(), ast.name.name)
        if type(func_found.rettype) is VoidType:
            raise TypeMismatchInExpression(ast)
        if len(func_found.param) != len(ast.args):
            raise TypeMismatchInExpression(ast)
        for i in range(len(ast.args)):
            if type(ast.args[i]) is ArrayLiteral:
                self.origin_arrlit_ast = []
            arg_type = self.visit(ast.args[i], param)
            if arg_type is None:
                if type(ast.args[i]) not in [Id, CallExpr, ArrayLiteral]:
                    return None
                arg_type = self.__inferType(
                    ast.args[i], func_found.param[i].typ, param)
                if arg_type is None:
                    return None
            elif type(arg_type) is not type(func_found.param[i].typ):
                raise TypeMismatchInExpression(ast)
            elif type(arg_type) is ArrayType:
                if arg_type.size != func_found.param[i].typ.size:
                    raise TypeMismatchInExpression(ast)
                if arg_type.eleType is None:
                    if type(ast.args[i]) not in [Id, CallExpr, ArrayLiteral]:
                        return None
                    arg_type.eleType = self.__inferType(
                        ast.args[i], func_found.param[i].typ, param)
                    if arg_type.eleType is None:
                        return None
                else:
                    if type(arg_type.eleType) is not type(func_found.param[i].typ.eleType):
                        raise TypeMismatchInExpression(ast)
        return func_found.rettype

    def visitId(self, ast: Id, param):
        '''
        `name`: str
        '''
        if self.var_current is not None and ast.name == self.var_current:
            raise Undeclared(Identifier(), ast.name)
        found_type = next((symbol.typ for symbol_list in param for symbol in symbol_list if type(
            symbol) is VarSymbol and symbol.name == ast.name), None)
        if not found_type:
            raise Undeclared(Identifier(), ast.name)
        return found_type

    def visitArrayCell(self, ast: ArrayCell, param):
        '''
        - `arr`: Expr
        - `idx`: List[Expr]
        '''
        arr_type = self.visit(ast.arr, param)
        if arr_type is None:
            return None
        if type(arr_type) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        if arr_type.eleType is None:
            return None
        if len(arr_type.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        for i in range(len(ast.idx)):
            ele_type = self.visit(ast.idx[i], param)
            if ele_type is None:
                if type(ast.idx[i]) not in [Id, CallExpr]:
                    return None
                ele_type = self.__inferType(ast.idx[i], NumberType(), param)
                if ele_type is None:
                    return None
            elif type(ele_type) is not NumberType:
                raise TypeMismatchInExpression(ast)
        return arr_type.eleType if len(arr_type.size) == len(ast.idx) else ArrayType(arr_type.size[len(ast.idx):], arr_type.eleType)

    def visitBlock(self, ast: Block, param):
        '''
        `stmt`: List[Stmt] - empty list if there is no statement in block
        '''
        reduce(lambda acc, cur: self.visit(cur, acc), ast.stmt, [[]] + param)
        self.func_has_returned = False
        return None

    def visitIf(self, ast: If, param):
        '''
        - `expr`: Expr
        - `thenStmt`: Stmt
        - `elifStmt`: List[Tuple[Expr, Stmt]] - empty list if there is no elif statement
        - `elseStmt`: Stmt = None - None if there is no else branch
        '''
        if type(ast.expr) is ArrayLiteral:
            self.origin_arrlit_ast = []
        expr_type = self.visit(ast.expr, param)

        if expr_type is None:
            if type(ast.expr) not in [Id, CallExpr, ArrayLiteral]:
                raise TypeCannotBeInferred(ast)
            expr_type = self.__inferType(ast.expr, BoolType(), param)
            if expr_type is None:
                raise TypeCannotBeInferred(ast)
        elif type(expr_type) is not BoolType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.thenStmt, param)
        self.func_has_returned = False
        for elif_expr, elif_stmt in ast.elifStmt:
            if type(elif_expr) is ArrayLiteral:
                self.origin_arrlit_ast = []
            elif_expr_type = self.visit(elif_expr, param)
            if elif_expr_type is None:
                if type(elif_expr) not in [Id, CallExpr, ArrayLiteral]:
                    raise TypeCannotBeInferred(ast)
                elif_expr_type = self.__inferType(elif_expr, BoolType(), param)
                if elif_expr_type is None:
                    raise TypeCannotBeInferred(ast)
            elif type(elif_expr_type) is not BoolType:
                raise TypeMismatchInStatement(ast)
            self.visit(elif_stmt, param)
            self.func_has_returned = False

        if ast.elseStmt:
            self.visit(ast.elseStmt, param)
            self.func_has_returned = False
        return None

    def visitFor(self, ast: For, param):
        '''
        - `name`: Id
        - `condExpr`: Expr
        - `updExpr`: Expr
        - `body`: Stmt
        '''
        self.in_loop += [True]
        id_type = self.visit(ast.name, param)
        if id_type is None:
            id_type = self.__inferType(ast.name, NumberType(), param)
            if id_type is None:
                raise TypeCannotBeInferred(ast)
        elif type(id_type) is not NumberType:
            raise TypeMismatchInStatement(ast)

        if type(ast.condExpr) is ArrayLiteral:
            self.origin_arrlit_ast = []
        condExpr_type = self.visit(ast.condExpr, param)
        if condExpr_type is None:
            if type(ast.condExpr) not in [Id, CallExpr]:
                raise TypeCannotBeInferred(ast)
            condExpr_type = self.__inferType(ast.condExpr, BoolType(), param)
            if condExpr_type is None:
                raise TypeCannotBeInferred(ast)
        elif type(condExpr_type) is not BoolType:
            raise TypeMismatchInStatement(ast)

        if type(ast.updExpr) is ArrayLiteral:
            self.origin_arrlit_ast = []
        updExpr_type = self.visit(ast.updExpr, param)
        if updExpr_type is None:
            if type(ast.updExpr) not in [Id, CallExpr]:
                raise TypeCannotBeInferred(ast)
            updExpr_type = self.__inferType(ast.updExpr, NumberType(), param)
            if updExpr_type is None:
                raise TypeCannotBeInferred(ast)
        elif type(updExpr_type) is not NumberType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.body, param)
        self.in_loop = self.in_loop[:-1]
        return None

    def visitContinue(self, ast: Continue, param):
        if not self.in_loop:
            raise MustInLoop(ast)
        return None

    def visitBreak(self, ast: Break, param):
        if not self.in_loop:
            raise MustInLoop(ast)
        return None

    def visitReturn(self, ast: Return, param):
        '''
        `expr`: Expr = None - None if there is no expression after return
        '''
        if self.func_has_returned:
            return None
        self.func_has_returned = True
        if ast.expr is None:
            return VoidType()
        if type(ast.expr) is ArrayLiteral:
            self.origin_arrlit_ast = []
        return_type = self.visit(ast.expr, param)
        func = self.lookup(self.func_current,
                           param[-1], lambda symbol: symbol.name)
        if func.typ is None:
            if return_type is None:
                self.func_return_list += [ast]
            else:
                func.typ = return_type
                if self.func_return_list:
                    for ret in self.func_return_list:
                        if type(ret.expr) not in [Id, CallExpr, ArrayLiteral]:
                            raise TypeCannotBeInferred(ast)
                        typ = self.__inferType(ret.expr, return_type, param)
                        if typ is None:
                            raise TypeCannotBeInferred(ast)
                    self.func_return_list = []
        else:
            if type(func.typ) is VoidType:
                raise TypeMismatchInStatement(ast)
            if return_type is None:
                if type(ast.expr) not in [Id, CallExpr, ArrayLiteral]:
                    raise TypeCannotBeInferred(ast)
                return_type = self.__inferType(ast.expr, func.typ, param)
                if return_type is None:
                    raise TypeCannotBeInferred(ast)
            elif type(return_type) is not type(func.typ):
                raise TypeMismatchInStatement(ast)
            elif type(return_type) is ArrayType:
                if return_type.size != func.typ.size:
                    raise TypeMismatchInStatement(ast)
                if return_type.eleType is None:
                    if type(ast.expr) not in [Id, CallExpr, ArrayLiteral]:
                        raise TypeCannotBeInferred(ast)
                    return_type.eleType = self.__inferType(
                        ast.expr, func.typ, param)
                    if return_type.eleType is None:
                        raise TypeCannotBeInferred(ast)
                else:
                    if type(return_type.eleType) is not type(func.typ.eleType):
                        raise TypeMismatchInStatement(ast)
        return return_type

    def visitAssign(self, ast: Assign, param):
        '''
        - `lhs`: Expr
        - `rhs`: Expr
        '''
        if type(ast.rhs) is ArrayLiteral:
            self.origin_arrlit_ast = []
        if type(ast.lhs) is ArrayLiteral:
            self.origin_arrlit_ast = []

        rhs_type = self.visit(ast.rhs, param)
        lhs_type = self.visit(ast.lhs, param)
        if rhs_type is None and lhs_type is None:
            raise TypeCannotBeInferred(ast)
        if rhs_type is not None and lhs_type is None:
            if type(lhs_type) is Id:
                lhs_type = self.__inferType(ast.lhs, rhs_type, param)
                if lhs_type is None:
                    raise TypeCannotBeInferred(ast)
            elif type(lhs_type) in [CallExpr, ArrayLiteral]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeCannotBeInferred(ast)
        elif rhs_type is None and lhs_type is not None:
            if type(ast.exp) not in [Id, CallExpr, ArrayLiteral]:
                raise TypeCannotBeInferred(ast)
            rhs_type = self.__inferType(ast.rhs, lhs_type, param)
            if rhs_type is None:
                raise TypeCannotBeInferred(ast)
        elif type(lhs_type) is VoidType:
            raise TypeMismatchInStatement(ast)
        elif type(lhs_type) is not type(rhs_type):
            raise TypeMismatchInStatement(ast)
        elif type(lhs_type) is ArrayType:
            if lhs_type.size != rhs_type.size:
                raise TypeMismatchInStatement(ast)
            if lhs_type.eleType is None:
                if type(ast.rhs) not in [Id, CallExpr, ArrayLiteral]:
                    raise TypeCannotBeInferred(ast)
                lhs_type.eleType = self.__inferType(ast.rhs, rhs_type, param)
                if lhs_type.eleType is None:
                    raise TypeCannotBeInferred(ast)
            else:
                if type(lhs_type.eleType) is not type(rhs_type.eleType):
                    raise TypeMismatchInStatement(ast)
        return None

    def visitCallStmt(self, ast: CallStmt, param):
        '''
        - `name`: Id
        - `args`: List[Expr] - empty list if there is no argument
        '''
        if not all(map(lambda env: self.lookup(ast.name.name, env, lambda symbol: symbol.name) is None, param[:-1])):
            raise TypeMismatchInStatement(ast)
        func_found = self.lookup(
            ast.name.name, param[-1], lambda symbol: symbol.name)
        if func_found is None or (func_found is not None and type(func_found) is not FuncSymbol):
            raise Undeclared(Function(), ast.name.name)
        if func_found.rettype is not None and type(func_found.rettype) is not VoidType:
            raise TypeMismatchInStatement(ast)
        if len(func_found.param) != len(ast.args):
            raise TypeMismatchInStatement(ast)
        for i in range(len(ast.args)):
            if type(ast.args[i]) is ArrayLiteral:
                self.origin_arrlit_ast = []
            arg_type = self.visit(ast.args[i], param)
            if arg_type is None:
                if type(ast.args[i]) not in [Id, CallExpr, ArrayLiteral]:
                    raise TypeCannotBeInferred(ast)
                arg_type = self.__inferType(
                    ast.args[i], func_found.param[i].typ, param)
                if arg_type is None:
                    raise TypeCannotBeInferred(ast)
            elif type(arg_type) is not type(func_found.param[i].typ):
                raise TypeMismatchInStatement(ast)
            elif type(arg_type) is ArrayType:
                if arg_type.size != func_found.param[i].typ.size:
                    raise TypeMismatchInStatement(ast)
                if arg_type.eleType is None:
                    if type(ast.args[i]) not in [Id, CallExpr, ArrayLiteral]:
                        raise TypeCannotBeInferred(ast)
                    arg_type.eleType = self.__inferType(
                        ast.args[i], func_found.param[i].typ, param)
                    if arg_type.eleType is None:
                        raise TypeCannotBeInferred(ast)
                else:
                    if type(arg_type.eleType) is not type(func_found.param[i].typ.eleType):
                        raise TypeMismatchInStatement(ast)
        if func_found.rettype is None:
            func_found.rettype = self.__inferType(ast, VoidType(), param)
            if func_found.rettype is None:
                raise TypeCannotBeInferred(ast)
        return func_found.rettype

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        '''
        `value`: List[Expr]
        '''
        self.origin_arrlit_ast += [ast]
        expr_type = next((self.visit(val, param) for val in ast.value), None)
        if expr_type is None:
            return None
        else:
            for i in range(len(ast.value)):
                val_type = self.visit(ast.value[i], param)
                if val_type is None:
                    if type(ast.value[i]) not in [Id, CallExpr, ArrayLiteral]:
                        return None
                    val_type = self.__inferType(ast.value[i], expr_type, param)
                    if val_type is None:
                        return None
                elif type(val_type) is not type(expr_type):
                    raise TypeMismatchInExpression(self.origin_arrlit_ast[0])
                elif type(val_type) is ArrayType:
                    if val_type.size != expr_type.size:
                        raise TypeMismatchInExpression(
                            self.origin_arrlit_ast[0])
                    if val_type.eleType is None:
                        if type(ast.value[i]) not in [Id, CallExpr, ArrayLiteral]:
                            return None
                        val_type.eleType = self.__inferType(
                            ast.value[i], expr_type, param)
                        if val_type.eleType is None:
                            return None
                    else:
                        if type(val_type.eleType) is not type(expr_type.eleType):
                            raise TypeMismatchInExpression(
                                self.origin_arrlit_ast[0])
            if type(expr_type) is not ArrayType:
                self.origin_arrlit_ast.pop()
                return ArrayType([len(ast.value)], expr_type)
            else:
                self.origin_arrlit_ast.pop()
                return ArrayType([len(ast.value)] + expr_type.size, expr_type.eleType)
