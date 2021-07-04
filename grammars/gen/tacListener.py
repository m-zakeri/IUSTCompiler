# Generated from /home/amiresm/Projects/personal/compiler/tac.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tacParser import tacParser
else:
    from tacParser import tacParser

# This class defines a complete listener for a parse tree produced by tacParser.
class tacListener(ParseTreeListener):

    # Enter a parse tree produced by tacParser#program.
    def enterProgram(self, ctx:tacParser.ProgramContext):
        pass

    # Exit a parse tree produced by tacParser#program.
    def exitProgram(self, ctx:tacParser.ProgramContext):
        pass


    # Enter a parse tree produced by tacParser#mainClass.
    def enterMainClass(self, ctx:tacParser.MainClassContext):
        pass

    # Exit a parse tree produced by tacParser#mainClass.
    def exitMainClass(self, ctx:tacParser.MainClassContext):
        pass


    # Enter a parse tree produced by tacParser#classDecleration.
    def enterClassDecleration(self, ctx:tacParser.ClassDeclerationContext):
        pass

    # Exit a parse tree produced by tacParser#classDecleration.
    def exitClassDecleration(self, ctx:tacParser.ClassDeclerationContext):
        pass


    # Enter a parse tree produced by tacParser#varDeclaration.
    def enterVarDeclaration(self, ctx:tacParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by tacParser#varDeclaration.
    def exitVarDeclaration(self, ctx:tacParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by tacParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:tacParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by tacParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:tacParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by tacParser#typeId.
    def enterTypeId(self, ctx:tacParser.TypeIdContext):
        pass

    # Exit a parse tree produced by tacParser#typeId.
    def exitTypeId(self, ctx:tacParser.TypeIdContext):
        pass


    # Enter a parse tree produced by tacParser#statement.
    def enterStatement(self, ctx:tacParser.StatementContext):
        pass

    # Exit a parse tree produced by tacParser#statement.
    def exitStatement(self, ctx:tacParser.StatementContext):
        pass


    # Enter a parse tree produced by tacParser#expression.
    def enterExpression(self, ctx:tacParser.ExpressionContext):
        pass

    # Exit a parse tree produced by tacParser#expression.
    def exitExpression(self, ctx:tacParser.ExpressionContext):
        pass


    # Enter a parse tree produced by tacParser#identifier.
    def enterIdentifier(self, ctx:tacParser.IdentifierContext):
        pass

    # Exit a parse tree produced by tacParser#identifier.
    def exitIdentifier(self, ctx:tacParser.IdentifierContext):
        pass



del tacParser