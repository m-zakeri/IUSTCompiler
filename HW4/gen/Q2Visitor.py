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


    # Visit a parse tree produced by Q2Parser#type_t.
    def visitType_t(self, ctx:Q2Parser.Type_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#statement.
    def visitStatement(self, ctx:Q2Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q2Parser#expression.
    def visitExpression(self, ctx:Q2Parser.ExpressionContext):
        return self.visitChildren(ctx)



del Q2Parser