# Generated from /home/amiresm/Projects/personal/compiler/tac.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tacParser import tacParser
else:
    from tacParser import tacParser

# This class defines a complete generic visitor for a parse tree produced by tacParser.

class tacVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tacParser#program.
    def visitProgram(self, ctx:tacParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tacParser#mainClass.
    def visitMainClass(self, ctx:tacParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tacParser#classDecleration.
    def visitClassDecleration(self, ctx:tacParser.ClassDeclerationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tacParser#varDeclaration.
    def visitVarDeclaration(self, ctx:tacParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tacParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:tacParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tacParser#typeId.
    def visitTypeId(self, ctx:tacParser.TypeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tacParser#statement.
    def visitStatement(self, ctx:tacParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tacParser#expression.
    def visitExpression(self, ctx:tacParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tacParser#identifier.
    def visitIdentifier(self, ctx:tacParser.IdentifierContext):
        return self.visitChildren(ctx)



del tacParser