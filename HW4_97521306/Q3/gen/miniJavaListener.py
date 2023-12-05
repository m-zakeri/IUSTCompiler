# Generated from E:/Compiler/HW4/Q3_2\miniJava.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniJavaParser import miniJavaParser
else:
    from miniJavaParser import miniJavaParser

# This class defines a complete listener for a parse tree produced by miniJavaParser.
class miniJavaListener(ParseTreeListener):

    # Enter a parse tree produced by miniJavaParser#program.
    def enterProgram(self, ctx:miniJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by miniJavaParser#program.
    def exitProgram(self, ctx:miniJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by miniJavaParser#mainClass.
    def enterMainClass(self, ctx:miniJavaParser.MainClassContext):
        pass

    # Exit a parse tree produced by miniJavaParser#mainClass.
    def exitMainClass(self, ctx:miniJavaParser.MainClassContext):
        pass


    # Enter a parse tree produced by miniJavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:miniJavaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by miniJavaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:miniJavaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by miniJavaParser#varDeclaration.
    def enterVarDeclaration(self, ctx:miniJavaParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by miniJavaParser#varDeclaration.
    def exitVarDeclaration(self, ctx:miniJavaParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by miniJavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:miniJavaParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by miniJavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:miniJavaParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by miniJavaParser#type.
    def enterType(self, ctx:miniJavaParser.TypeContext):
        pass

    # Exit a parse tree produced by miniJavaParser#type.
    def exitType(self, ctx:miniJavaParser.TypeContext):
        pass


    # Enter a parse tree produced by miniJavaParser#statement.
    def enterStatement(self, ctx:miniJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by miniJavaParser#statement.
    def exitStatement(self, ctx:miniJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression.
    def enterExpression(self, ctx:miniJavaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression.
    def exitExpression(self, ctx:miniJavaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by miniJavaParser#identifier.
    def enterIdentifier(self, ctx:miniJavaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by miniJavaParser#identifier.
    def exitIdentifier(self, ctx:miniJavaParser.IdentifierContext):
        pass



del miniJavaParser