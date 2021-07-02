# Generated from .\miniJavaThreeCode.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniJavaThreeCodeParser import miniJavaThreeCodeParser
else:
    from miniJavaThreeCodeParser import miniJavaThreeCodeParser

    from AddressCodeConverter import *


# This class defines a complete listener for a parse tree produced by miniJavaThreeCodeParser.
class miniJavaThreeCodeListener(ParseTreeListener):

    # Enter a parse tree produced by miniJavaThreeCodeParser#program.
    def enterProgram(self, ctx:miniJavaThreeCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by miniJavaThreeCodeParser#program.
    def exitProgram(self, ctx:miniJavaThreeCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by miniJavaThreeCodeParser#main_class.
    def enterMain_class(self, ctx:miniJavaThreeCodeParser.Main_classContext):
        pass

    # Exit a parse tree produced by miniJavaThreeCodeParser#main_class.
    def exitMain_class(self, ctx:miniJavaThreeCodeParser.Main_classContext):
        pass


    # Enter a parse tree produced by miniJavaThreeCodeParser#class_declaration.
    def enterClass_declaration(self, ctx:miniJavaThreeCodeParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by miniJavaThreeCodeParser#class_declaration.
    def exitClass_declaration(self, ctx:miniJavaThreeCodeParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by miniJavaThreeCodeParser#var_declaration.
    def enterVar_declaration(self, ctx:miniJavaThreeCodeParser.Var_declarationContext):
        pass

    # Exit a parse tree produced by miniJavaThreeCodeParser#var_declaration.
    def exitVar_declaration(self, ctx:miniJavaThreeCodeParser.Var_declarationContext):
        pass


    # Enter a parse tree produced by miniJavaThreeCodeParser#method_declaration.
    def enterMethod_declaration(self, ctx:miniJavaThreeCodeParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by miniJavaThreeCodeParser#method_declaration.
    def exitMethod_declaration(self, ctx:miniJavaThreeCodeParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by miniJavaThreeCodeParser#type_r.
    def enterType_r(self, ctx:miniJavaThreeCodeParser.Type_rContext):
        pass

    # Exit a parse tree produced by miniJavaThreeCodeParser#type_r.
    def exitType_r(self, ctx:miniJavaThreeCodeParser.Type_rContext):
        pass


    # Enter a parse tree produced by miniJavaThreeCodeParser#statement.
    def enterStatement(self, ctx:miniJavaThreeCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by miniJavaThreeCodeParser#statement.
    def exitStatement(self, ctx:miniJavaThreeCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by miniJavaThreeCodeParser#expression.
    def enterExpression(self, ctx:miniJavaThreeCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by miniJavaThreeCodeParser#expression.
    def exitExpression(self, ctx:miniJavaThreeCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by miniJavaThreeCodeParser#identifier_r.
    def enterIdentifier_r(self, ctx:miniJavaThreeCodeParser.Identifier_rContext):
        pass

    # Exit a parse tree produced by miniJavaThreeCodeParser#identifier_r.
    def exitIdentifier_r(self, ctx:miniJavaThreeCodeParser.Identifier_rContext):
        pass


    # Enter a parse tree produced by miniJavaThreeCodeParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:miniJavaThreeCodeParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by miniJavaThreeCodeParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:miniJavaThreeCodeParser.IntegerLiteralContext):
        pass



del miniJavaThreeCodeParser