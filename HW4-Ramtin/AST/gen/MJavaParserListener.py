# Generated from D:/UNI/Compiler/Assignment 4/3Code\MJavaParser.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MJavaParser import MJavaParser
else:
    from MJavaParser import MJavaParser

# This class defines a complete listener for a parse tree produced by MJavaParser.
class MJavaParserListener(ParseTreeListener):

    # Enter a parse tree produced by MJavaParser#program.
    def enterProgram(self, ctx:MJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by MJavaParser#program.
    def exitProgram(self, ctx:MJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by MJavaParser#mainClass.
    def enterMainClass(self, ctx:MJavaParser.MainClassContext):
        pass

    # Exit a parse tree produced by MJavaParser#mainClass.
    def exitMainClass(self, ctx:MJavaParser.MainClassContext):
        pass


    # Enter a parse tree produced by MJavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:MJavaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by MJavaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:MJavaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by MJavaParser#varDeclaration.
    def enterVarDeclaration(self, ctx:MJavaParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MJavaParser#varDeclaration.
    def exitVarDeclaration(self, ctx:MJavaParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by MJavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:MJavaParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by MJavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:MJavaParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by MJavaParser#type_.
    def enterType_(self, ctx:MJavaParser.Type_Context):
        pass

    # Exit a parse tree produced by MJavaParser#type_.
    def exitType_(self, ctx:MJavaParser.Type_Context):
        pass


    # Enter a parse tree produced by MJavaParser#statement.
    def enterStatement(self, ctx:MJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by MJavaParser#statement.
    def exitStatement(self, ctx:MJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by MJavaParser#expression.
    def enterExpression(self, ctx:MJavaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MJavaParser#expression.
    def exitExpression(self, ctx:MJavaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MJavaParser#identifier.
    def enterIdentifier(self, ctx:MJavaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by MJavaParser#identifier.
    def exitIdentifier(self, ctx:MJavaParser.IdentifierContext):
        pass



del MJavaParser