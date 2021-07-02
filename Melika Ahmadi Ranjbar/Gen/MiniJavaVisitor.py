# Generated from D:/University/Sem6/Compiler/Assignment4\MiniJava.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete generic visitor for a parse tree produced by MiniJavaParser.

class MiniJavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniJavaParser#program.
    def visitProgram(self, ctx:MiniJavaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainClass.
    def visitMainClass(self, ctx:MiniJavaParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainClassEnter.
    def visitMainClassEnter(self, ctx:MiniJavaParser.MainClassEnterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainClassBody.
    def visitMainClassBody(self, ctx:MiniJavaParser.MainClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#array_int.
    def visitArray_int(self, ctx:MiniJavaParser.Array_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#bool.
    def visitBool(self, ctx:MiniJavaParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#int.
    def visitInt(self, ctx:MiniJavaParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#id.
    def visitId(self, ctx:MiniJavaParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#braket_statement.
    def visitBraket_statement(self, ctx:MiniJavaParser.Braket_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#if_statement.
    def visitIf_statement(self, ctx:MiniJavaParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#while_statement.
    def visitWhile_statement(self, ctx:MiniJavaParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#print.
    def visitPrint(self, ctx:MiniJavaParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#equal_statement.
    def visitEqual_statement(self, ctx:MiniJavaParser.Equal_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#equal_array_statement.
    def visitEqual_array_statement(self, ctx:MiniJavaParser.Equal_array_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#number.
    def visitNumber(self, ctx:MiniJavaParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#new_identifier.
    def visitNew_identifier(self, ctx:MiniJavaParser.New_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#not_expression.
    def visitNot_expression(self, ctx:MiniJavaParser.Not_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#keywords.
    def visitKeywords(self, ctx:MiniJavaParser.KeywordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#dot_par_expression.
    def visitDot_par_expression(self, ctx:MiniJavaParser.Dot_par_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#in_par_expression.
    def visitIn_par_expression(self, ctx:MiniJavaParser.In_par_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#operations_expression.
    def visitOperations_expression(self, ctx:MiniJavaParser.Operations_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#array_expression.
    def visitArray_expression(self, ctx:MiniJavaParser.Array_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#word.
    def visitWord(self, ctx:MiniJavaParser.WordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#new_array_expression.
    def visitNew_array_expression(self, ctx:MiniJavaParser.New_array_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#length_expression.
    def visitLength_expression(self, ctx:MiniJavaParser.Length_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#identifier.
    def visitIdentifier(self, ctx:MiniJavaParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#operations.
    def visitOperations(self, ctx:MiniJavaParser.OperationsContext):
        return self.visitChildren(ctx)



del MiniJavaParser