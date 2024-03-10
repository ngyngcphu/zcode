# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varDecl.
    def visitVarDecl(self, ctx:ZCodeParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functionDecl.
    def visitFunctionDecl(self, ctx:ZCodeParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramList.
    def visitParamList(self, ctx:ZCodeParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramPrime.
    def visitParamPrime(self, ctx:ZCodeParser.ParamPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#formalParameter.
    def visitFormalParameter(self, ctx:ZCodeParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement_type.
    def visitStatement_type(self, ctx:ZCodeParser.Statement_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement_list.
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_stat.
    def visitAssign_stat(self, ctx:ZCodeParser.Assign_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stat.
    def visitIf_stat(self, ctx:ZCodeParser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_fragment.
    def visitIf_fragment(self, ctx:ZCodeParser.If_fragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_fragment.
    def visitElif_fragment(self, ctx:ZCodeParser.Elif_fragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_fragment.
    def visitElse_fragment(self, ctx:ZCodeParser.Else_fragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stat.
    def visitFor_stat(self, ctx:ZCodeParser.For_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stat.
    def visitReturn_stat(self, ctx:ZCodeParser.Return_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call_stat.
    def visitFunc_call_stat(self, ctx:ZCodeParser.Func_call_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arglist.
    def visitArglist(self, ctx:ZCodeParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argprime.
    def visitArgprime(self, ctx:ZCodeParser.ArgprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stat.
    def visitBlock_stat(self, ctx:ZCodeParser.Block_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#io_function.
    def visitIo_function(self, ctx:ZCodeParser.Io_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#read_number.
    def visitRead_number(self, ctx:ZCodeParser.Read_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#write_number.
    def visitWrite_number(self, ctx:ZCodeParser.Write_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#read_bool.
    def visitRead_bool(self, ctx:ZCodeParser.Read_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#write_bool.
    def visitWrite_bool(self, ctx:ZCodeParser.Write_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#read_string.
    def visitRead_string(self, ctx:ZCodeParser.Read_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#write_string.
    def visitWrite_string(self, ctx:ZCodeParser.Write_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_type.
    def visitArray_type(self, ctx:ZCodeParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dimension_list.
    def visitDimension_list(self, ctx:ZCodeParser.Dimension_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_value.
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_elements.
    def visitArray_elements(self, ctx:ZCodeParser.Array_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_nested_or_expression.
    def visitArray_nested_or_expression(self, ctx:ZCodeParser.Array_nested_or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprlist.
    def visitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_expr.
    def visitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_1.
    def visitExpression_1(self, ctx:ZCodeParser.Expression_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_2.
    def visitExpression_2(self, ctx:ZCodeParser.Expression_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_3.
    def visitExpression_3(self, ctx:ZCodeParser.Expression_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_4.
    def visitExpression_4(self, ctx:ZCodeParser.Expression_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_5.
    def visitExpression_5(self, ctx:ZCodeParser.Expression_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_6.
    def visitExpression_6(self, ctx:ZCodeParser.Expression_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_7.
    def visitExpression_7(self, ctx:ZCodeParser.Expression_7Context):
        return self.visitChildren(ctx)



del ZCodeParser