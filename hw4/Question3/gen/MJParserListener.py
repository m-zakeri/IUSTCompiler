# Generated from E:/New folder/hw4/final/Question3\MJParser.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MJParser import MJParser
else:
    from MJParser import MJParser

# This class defines a complete listener for a parse tree produced by MJParser.
class MJParserListener(ParseTreeListener):

    # Enter a parse tree produced by MJParser#program.
    def enterProgram(self, ctx:MJParser.ProgramContext):
        pass

    # Exit a parse tree produced by MJParser#program.
    def exitProgram(self, ctx:MJParser.ProgramContext):
        pass


    # Enter a parse tree produced by MJParser#mainClass.
    def enterMainClass(self, ctx:MJParser.MainClassContext):
        pass

    # Exit a parse tree produced by MJParser#mainClass.
    def exitMainClass(self, ctx:MJParser.MainClassContext):
        pass


    # Enter a parse tree produced by MJParser#classDeclaration.
    def enterClassDeclaration(self, ctx:MJParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by MJParser#classDeclaration.
    def exitClassDeclaration(self, ctx:MJParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by MJParser#varDeclaration.
    def enterVarDeclaration(self, ctx:MJParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MJParser#varDeclaration.
    def exitVarDeclaration(self, ctx:MJParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by MJParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:MJParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by MJParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:MJParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by MJParser#typ.
    def enterTyp(self, ctx:MJParser.TypContext):
        pass

    # Exit a parse tree produced by MJParser#typ.
    def exitTyp(self, ctx:MJParser.TypContext):
        pass


    # Enter a parse tree produced by MJParser#statement.
    def enterStatement(self, ctx:MJParser.StatementContext):
        pass

    # Exit a parse tree produced by MJParser#statement.
    def exitStatement(self, ctx:MJParser.StatementContext):
        pass


    # Enter a parse tree produced by MJParser#expression.
    def enterExpression(self, ctx:MJParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MJParser#expression.
    def exitExpression(self, ctx:MJParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MJParser#identifier.
    def enterIdentifier(self, ctx:MJParser.IdentifierContext):
        pass

    # Exit a parse tree produced by MJParser#identifier.
    def exitIdentifier(self, ctx:MJParser.IdentifierContext):
        pass



del MJParser