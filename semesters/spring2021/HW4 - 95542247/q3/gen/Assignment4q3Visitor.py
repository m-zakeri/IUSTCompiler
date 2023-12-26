# Generated from C:/Users/novin/PycharmProjects/tamrin-compiler\Assignment4q3.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Assignment4q3Parser import Assignment4q3Parser
else:
    from Assignment4q3Parser import Assignment4q3Parser

# This class defines a complete generic visitor for a parse tree produced by Assignment4q3Parser.

class Assignment4q3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Assignment4q3Parser#program.
    def visitProgram(self, ctx:Assignment4q3Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q3Parser#mainClass.
    def visitMainClass(self, ctx:Assignment4q3Parser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q3Parser#classDeclaration.
    def visitClassDeclaration(self, ctx:Assignment4q3Parser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q3Parser#varDeclaration.
    def visitVarDeclaration(self, ctx:Assignment4q3Parser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q3Parser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:Assignment4q3Parser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q3Parser#type.
    def visitType(self, ctx:Assignment4q3Parser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q3Parser#statement.
    def visitStatement(self, ctx:Assignment4q3Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q3Parser#expression.
    def visitExpression(self, ctx:Assignment4q3Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q3Parser#identifier.
    def visitIdentifier(self, ctx:Assignment4q3Parser.IdentifierContext):
        return self.visitChildren(ctx)



del Assignment4q3Parser