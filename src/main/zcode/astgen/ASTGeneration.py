from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):
    # program: NEWLINE* ((varDecl NEWLINE+ | functionDecl))+ EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        listVarDecls = list(map(lambda x: self.visit(x), ctx.varDecl())) if ctx.varDecl() else []
        listFuncDecls = list(map(lambda x: self.visit(x), ctx.functionDecl())) if ctx.functionDecl() else []
        
        return Program(listVarDecls + listFuncDecls)

    # varDecl: (NUMBER | BOOL | STRING | DYNAMIC) IDENTIFIER (
    #         ASSIGN expression
    #     )?
    #     | VAR IDENTIFIER ASSIGN expression
    #     | array_type (ASSIGN expression)?;
    def visitVarDecl(self, ctx:ZCodeParser.VarDeclContext):
        if ctx.array_type():
            if ctx.ASSIGN():
                return Assign(self.visit(ctx.array_type()), self.visit(ctx.expression()))
            else:
                return self.visit(ctx.array_type())
        elif ctx.VAR():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.VAR().getText(), self.visit(ctx.expression()))
        else:
            if ctx.DYNAMIC():
                return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.DYNAMIC().getText(), self.visit(ctx.expression()) if ctx.ASSIGN() else None)
            else:
                return VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType() if ctx.NUMBER() else BoolType() if ctx.BOOL() else StringType(), None, self.visit(ctx.expression()) if ctx.ASSIGN() else None)

    # functionDecl:
    #     FUNC IDENTIFIER LB paramList RB NEWLINE* (
    #         return_stat
    #         | block_stat
    #     )?;
    def visitFunctionDecl(self, ctx:ZCodeParser.FunctionDeclContext):
        if ctx.return_stat():
            return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.paramList()), self.visit(ctx.return_stat()))
        elif ctx.block_stat():
            return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.paramList()), self.visit(ctx.block_stat()))
        else:
            return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.paramList()))

    # paramList: paramPrime |;
    def visitParamList(self, ctx:ZCodeParser.ParamListContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.paramPrime())
        else:
            return []

    # paramPrime: formalParameter COMMA paramPrime | formalParameter;
    def visitParamPrime(self, ctx:ZCodeParser.ParamPrimeContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.formalParameter()) + self.visit(ctx.paramPrime())
        else:
            return self.visit(ctx.formalParameter())

    # formalParameter: (NUMBER | BOOL | STRING) IDENTIFIER
	#     | array_type;
    def visitFormalParameter(self, ctx:ZCodeParser.FormalParameterContext):
        if ctx.IDENTIFIER():
            return [VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType() if ctx.NUMBER() else BoolType() if ctx.BOOL() else StringType())]
        else:
            return [self.visit(ctx.array_type())]

    # statement_type:
    #     varDecl
    #     | assign_stat
    #     | if_stat
    #     | for_stat
    #     | BREAK
    #     | CONTINUE
    #     | return_stat
    #     | func_call_stat
    #     | block_stat;
    def visitStatement_type(self, ctx:ZCodeParser.Statement_typeContext):
        if ctx.BREAK():
            return Break()
        elif ctx.CONTINUE():
            return Continue()
        else:
            return self.visit(ctx.getChild(0))

    # statement_list:
    #     statement_type NEWLINE+ statement_list
    #     | statement_type NEWLINE*;
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        if ctx.statement_list():
            return [self.visit(ctx.statement_type())] + self.visit(ctx.statement_list())
        else:
            return [self.visit(ctx.statement_type())]

    # assign_stat: lhs ASSIGN expression;
    def visitAssign_stat(self, ctx:ZCodeParser.Assign_statContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expression()))

    # lhs: IDENTIFIER | index_expr;
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.index_expr())

    # if_stat:
    #     if_fragment elif_stat
    #     | if_fragment elif_stat else_fragment
    #     | if_fragment else_fragment
    #     | if_fragment;
    def visitIf_stat(self, ctx:ZCodeParser.If_statContext):
        if_fragment_visit = self.visit(ctx.if_fragment())
        
        if ctx.getChildCount() == 1:
            return If(if_fragment_visit[0], if_fragment_visit[1])
        elif ctx.getChildCount() == 3:
            return If(if_fragment_visit[0], if_fragment_visit[1], self.visit(ctx.elif_stat()), self.visit(ctx.else_fragment()))
        elif ctx.else_fragment():
            return If(if_fragment_visit[0], if_fragment_visit[1], [], self.visit(ctx.else_fragment()))
        else:
            return If(if_fragment_visit[0], if_fragment_visit[1], self.visit(ctx.elif_stat()))
        
    # elif_stat: elif_fragment | elif_fragment elif_stat;
    def visitElif_stat(self, ctx:ZCodeParser.Elif_statContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.elif_fragment())
        else:
            return self.visit(ctx.elif_fragment()) + self.visit(ctx.elif_stat())

    # if_fragment: IF LB expression RB NEWLINE* statement_type NEWLINE*;
    def visitIf_fragment(self, ctx:ZCodeParser.If_fragmentContext):
        return (self.visit(ctx.expression()), self.visit(ctx.statement_type()))

    # elif_fragment: ELIF LB expression RB NEWLINE* statement_type NEWLINE*;
    def visitElif_fragment(self, ctx:ZCodeParser.Elif_fragmentContext):
        return [(self.visit(ctx.expression()), self.visit(ctx.statement_type()))]

    # else_fragment: ELSE statement_type NEWLINE*;
    def visitElse_fragment(self, ctx:ZCodeParser.Else_fragmentContext):
        return self.visit(ctx.statement_type())

    # for_stat:
	#     FOR IDENTIFIER UNTIL expression BY expression NEWLINE* statement_type NEWLINE*;
    def visitFor_stat(self, ctx:ZCodeParser.For_statContext):
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)), self.visit(ctx.statement_type()))

    # return_stat: RETURN expression?;
    def visitReturn_stat(self, ctx:ZCodeParser.Return_statContext):
        if ctx.getChildCount() == 2:
            return Return(self.visit(ctx.expression()))
        else:
            return Return()

    # func_call_stat: (IDENTIFIER LB arglist RB) | io_function;
    def visitFunc_call_stat(self, ctx:ZCodeParser.Func_call_statContext):
        if ctx.getChildCount() == 4:
            return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.arglist()))
        else:
            io_function_visit = self.visit(ctx.io_function())
            return CallStmt(io_function_visit[0], io_function_visit[1])

    # arglist: argprime |;
    def visitArglist(self, ctx:ZCodeParser.ArglistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.argprime())
        else:
            return []

    # argprime: expression COMMA argprime | expression;
    def visitArgprime(self, ctx:ZCodeParser.ArgprimeContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expression())] + self.visit(ctx.argprime())
        else:
            return [self.visit(ctx.expression())]

    # block_stat: BEGIN NEWLINE+ statement_list? END;
    def visitBlock_stat(self, ctx:ZCodeParser.Block_statContext):
        return Block(self.visit(ctx.statement_list()) if ctx.statement_list() else [])

    # io_function:
    #     read_number
    #     | write_number
    #     | read_bool
    #     | write_bool
    #     | read_string
    #     | write_string;
    def visitIo_function(self, ctx:ZCodeParser.Io_functionContext):
        return self.visit(ctx.getChild(0))

    # read_number: 'readNumber' LB RB;
    def visitRead_number(self, ctx:ZCodeParser.Read_numberContext):
        return (Id(ctx.getChild(0).getText()), [])

    # write_number: 'writeNumber' LB expression RB;
    def visitWrite_number(self, ctx:ZCodeParser.Write_numberContext):
        return (Id(ctx.getChild(0).getText()), [self.visit(ctx.expression())])

    # read_bool: 'readBool' LB RB;
    def visitRead_bool(self, ctx:ZCodeParser.Read_boolContext):
        return (Id(ctx.getChild(0).getText()), [])

    # write_bool: 'writeBool' LB expression RB;
    def visitWrite_bool(self, ctx:ZCodeParser.Write_boolContext):
        return (Id(ctx.getChild(0).getText()), [self.visit(ctx.expression())])

    # read_string: 'readString' LB RB;
    def visitRead_string(self, ctx:ZCodeParser.Read_stringContext):
        return (Id(ctx.getChild(0).getText()), [])

    # write_string: 'writeString' LB expression RB;
    def visitWrite_string(self, ctx:ZCodeParser.Write_stringContext):
        return (Id(ctx.getChild(0).getText()), [self.visit(ctx.expression())])

    # array_type: (NUMBER | STRING | BOOL) IDENTIFIER LS dimension_list RS;
    def visitArray_type(self, ctx:ZCodeParser.Array_typeContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.dimension_list()), NumberType() if ctx.NUMBER() else StringType() if ctx.STRING() else BoolType()))

    # dimension_list: NUMBERLIT COMMA dimension_list | NUMBERLIT;
    def visitDimension_list(self, ctx:ZCodeParser.Dimension_listContext):
        if ctx.getChildCount() == 3:
            return [NumberLiteral(float(ctx.NUMBERLIT().getText()))] + self.visit(ctx.dimension_list())
        else:
            return [NumberLiteral(float(ctx.NUMBERLIT().getText()))]

    # array_value: LS array_elements RS;
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return ArrayLiteral(self.visit(ctx.array_elements()))

    # array_elements:
    #     array_nested_or_expression COMMA array_elements
    #     | array_nested_or_expression;
    def visitArray_elements(self, ctx:ZCodeParser.Array_elementsContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.array_nested_or_expression()) + self.visit(ctx.array_elements())
        else:
            return self.visit(ctx.array_nested_or_expression())

    # array_nested_or_expression: array_value | exprlist;
    def visitArray_nested_or_expression(self, ctx:ZCodeParser.Array_nested_or_expressionContext):
        if ctx.array_value():
            return [self.visit(ctx.array_value())]
        else:
            return self.visit(ctx.exprlist())

    # exprlist: expression COMMA exprlist | expression;
    def visitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expression())] + self.visit(ctx.exprlist())
        else:
            return [self.visit(ctx.expression())]

    # index_expr: (IDENTIFIER | func_call_stat) LS exprlist RS;
    def visitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        if ctx.IDENTIFIER():
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))
        else:
            return ArrayCell(self.visit(ctx.func_call_stat()), self.visit(ctx.exprlist()))

    # expression: expression_1 CONCAT_OP expression_1 | expression_1;
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.CONCAT_OP().getText(), self.visit(ctx.expression_1(0)), self.visit(ctx.expression_1(1)))
        else:
            return self.visit(ctx.expression_1(0))

    # expression_1:
    #     expression_2 (
    #         EQUAL_OP
    #         | STRING_COMPARE_OP
    #         | NOT_EQUAL_OP
    #         | LESS_THAN_OP
    #         | GREATER_THAN_OP
    #         | LESS_EQUAL_OP
    #         | GREATER_EQUAL_OP
    #     ) expression_2
    #     | expression_2;
    def visitExpression_1(self, ctx:ZCodeParser.Expression_1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression_2(0)), self.visit(ctx.expression_2(1)))
        else:
            return self.visit(ctx.expression_2(0))

    # expression_2:
    #     expression_2 (AND_OP | OR_OP) expression_3
    #     | expression_3;
    def visitExpression_2(self, ctx:ZCodeParser.Expression_2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression_2()), self.visit(ctx.expression_3()))
        else:
            return self.visit(ctx.expression_3())

    # expression_3:
    #     expression_3 (ADD_OF | SUB_OF) expression_4
    #     | expression_4;
    def visitExpression_3(self, ctx:ZCodeParser.Expression_3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression_3()), self.visit(ctx.expression_4()))
        else:
            return self.visit(ctx.expression_4())

    # expression_4:
    #     expression_4 (MUL_OF | DIV_OF | MOD_OF) expression_5
    #     | expression_5;
    def visitExpression_4(self, ctx:ZCodeParser.Expression_4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression_4()), self.visit(ctx.expression_5()))
        else:
            return self.visit(ctx.expression_5())

    # expression_5: NOT_OP expression_5 | expression_6;
    def visitExpression_5(self, ctx:ZCodeParser.Expression_5Context):
        if ctx.NOT_OP():
            return UnaryOp(ctx.NOT_OP().getText(), self.visit(ctx.expression_5()))
        else:
            return self.visit(ctx.expression_6())

    # expression_6: SUB_OF expression_6 | expression_7;
    def visitExpression_6(self, ctx:ZCodeParser.Expression_6Context):
        if ctx.SUB_OF():
            return UnaryOp(ctx.SUB_OF().getText(), self.visit(ctx.expression_6()))
        else:
            return self.visit(ctx.expression_7())

    # expression_7:
    #     array_value
    #     | index_expr
    #     | (IDENTIFIER LB arglist RB | io_function)
    #     | LB expression RB
    #     | NUMBERLIT
    #     | TRUE
    #     | FALSE
    #     | STRINGLIT
    #     | IDENTIFIER;
    def visitExpression_7(self, ctx:ZCodeParser.Expression_7Context):
        if ctx.IDENTIFIER() and ctx.getChildCount() == 1:
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.NUMBERLIT():
            return NumberLiteral(float(ctx.NUMBERLIT().getText()))
        elif ctx.getChildCount() == 3:
            return self.visit(ctx.expression())
        elif ctx.index_expr():
            return self.visit(ctx.index_expr())
        elif ctx.array_value():
            return self.visit(ctx.array_value())
        else:
            if ctx.getChildCount() == 4:
                return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.arglist()))
            else:
                io_function_visit = self.visit(ctx.io_function())
                return CallExpr(io_function_visit[0], io_function_visit[1])