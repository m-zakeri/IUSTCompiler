# Generated from E:/New folder/hw4/final/Question3\MJParser.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MJParser import MJParser
else:
    from MJParser import MJParser

# This class defines a complete generic visitor for a parse tree produced by MJParser.

class MJParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MJParser#program.
    def visitProgram(self, ctx:MJParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJParser#mainClass.
    def visitMainClass(self, ctx:MJParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MJParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MJParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MJParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJParser#typ.
    def visitTyp(self, ctx:MJParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJParser#statement.
    def visitStatement(self, ctx:MJParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJParser#expression.
    def visitExpression(self, ctx:MJParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MJParser#identifier.
    def visitIdentifier(self, ctx:MJParser.IdentifierContext):
        return self.visitChildren(ctx)



del MJParser