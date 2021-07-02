# Generated from E:/Compiler/HW4/Q3_2\miniJava.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniJavaParser import miniJavaParser
else:
    from miniJavaParser import miniJavaParser

# This class defines a complete generic visitor for a parse tree produced by miniJavaParser.

class miniJavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miniJavaParser#program.
    def visitProgram(self, ctx:miniJavaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#mainClass.
    def visitMainClass(self, ctx:miniJavaParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:miniJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx:miniJavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:miniJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#type.
    def visitType(self, ctx:miniJavaParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#statement.
    def visitStatement(self, ctx:miniJavaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression.
    def visitExpression(self, ctx:miniJavaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#identifier.
    def visitIdentifier(self, ctx:miniJavaParser.IdentifierContext):
        return self.visitChildren(ctx)



del miniJavaParser