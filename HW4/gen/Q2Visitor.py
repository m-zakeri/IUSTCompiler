# Generated from /home/pouorix/Desktop/compilerHW4/Me/IUSTCompiler/HW4/Q2.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Q2Parser import Q2Parser
else:
    from Q2Parser import Q2Parser

# This class defines a complete generic visitor for a parse tree produced by Q2Parser.

class Q2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Q2Parser#program.
    def visitProgram(self, ctx:Q2Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#mainClass.
    def visitMainClass(self, ctx:Q2Parser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#classDeclaration.
    def visitClassDeclaration(self, ctx:Q2Parser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#varDeclaration.
    def visitVarDeclaration(self, ctx:Q2Parser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:Q2Parser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#array_int.
    def visitArray_int(self, ctx:Q2Parser.Array_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#bool.
    def visitBool(self, ctx:Q2Parser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#int.
    def visitInt(self, ctx:Q2Parser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#id.
    def visitId(self, ctx:Q2Parser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#braket_statement.
    def visitBraket_statement(self, ctx:Q2Parser.Braket_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#if_statement.
    def visitIf_statement(self, ctx:Q2Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#equal_statement.
    def visitEqual_statement(self, ctx:Q2Parser.Equal_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#while_statement.
    def visitWhile_statement(self, ctx:Q2Parser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#print.
    def visitPrint(self, ctx:Q2Parser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#equal_array_statement.
    def visitEqual_array_statement(self, ctx:Q2Parser.Equal_array_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#number.
    def visitNumber(self, ctx:Q2Parser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#not_expression.
    def visitNot_expression(self, ctx:Q2Parser.Not_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#new_identifier.
    def visitNew_identifier(self, ctx:Q2Parser.New_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#keywords.
    def visitKeywords(self, ctx:Q2Parser.KeywordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#dot_par_expression.
    def visitDot_par_expression(self, ctx:Q2Parser.Dot_par_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#in_par_expression.
    def visitIn_par_expression(self, ctx:Q2Parser.In_par_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#operations_expression.
    def visitOperations_expression(self, ctx:Q2Parser.Operations_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#array_expression.
    def visitArray_expression(self, ctx:Q2Parser.Array_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#word.
    def visitWord(self, ctx:Q2Parser.WordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#new_array_expression.
    def visitNew_array_expression(self, ctx:Q2Parser.New_array_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#length_expression.
    def visitLength_expression(self, ctx:Q2Parser.Length_expressionContext):
        return self.visitChildren(ctx)



del Q2Parser