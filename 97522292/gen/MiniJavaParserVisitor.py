# Generated from C:/Users/asus/Desktop/desk/University/99002-CD (compiler)/A4\MiniJavaParser.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete generic visitor for a parse tree produced by MiniJavaParser.

class MiniJavaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniJavaParser#program.
    def visitProgram(self, ctx:MiniJavaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainClass.
    def visitMainClass(self, ctx:MiniJavaParser.MainClassContext):
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


    # Visit a parse tree produced by MiniJavaParser#type_.
    def visitType_(self, ctx:MiniJavaParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#statement.
    def visitStatement(self, ctx:MiniJavaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression.
    def visitExpression(self, ctx:MiniJavaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#identifier.
    def visitIdentifier(self, ctx:MiniJavaParser.IdentifierContext):
        return self.visitChildren(ctx)



del MiniJavaParser