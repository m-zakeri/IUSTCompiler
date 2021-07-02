# Generated from /home/kamyab/Desktop/compiler/IUSTCompiler/Sol_HW4/Q2/MiniJava.g4 by ANTLR 4.9.1
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


    # Visit a parse tree produced by MiniJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#type_t.
    def visitType_t(self, ctx:MiniJavaParser.Type_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#statement.
    def visitStatement(self, ctx:MiniJavaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression.
    def visitExpression(self, ctx:MiniJavaParser.ExpressionContext):
        return self.visitChildren(ctx)



del MiniJavaParser