# Generated from D:/UNI/Compiler/Assignment 4/3Code\MJavaParser.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MJavaParser import MJavaParser
else:
    from MJavaParser import MJavaParser

# This class defines a complete generic visitor for a parse tree produced by MJavaParser.

class MJavaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MJavaParser#program.
    def visitProgram(self, ctx:MJavaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJavaParser#mainClass.
    def visitMainClass(self, ctx:MJavaParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MJavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJavaParser#type_.
    def visitType_(self, ctx:MJavaParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJavaParser#statement.
    def visitStatement(self, ctx:MJavaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJavaParser#expression.
    def visitExpression(self, ctx:MJavaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJavaParser#identifier.
    def visitIdentifier(self, ctx:MJavaParser.IdentifierContext):
        return self.visitChildren(ctx)



del MJavaParser