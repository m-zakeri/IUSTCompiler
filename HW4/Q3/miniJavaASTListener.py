# Generated from .\miniJavaAST.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniJavaASTParser import miniJavaASTParser
else:
    from miniJavaASTParser import miniJavaASTParser

# This class defines a complete listener for a parse tree produced by miniJavaASTParser.
class miniJavaASTListener(ParseTreeListener):

    # Enter a parse tree produced by miniJavaASTParser#program.
    def enterProgram(self, ctx:miniJavaASTParser.ProgramContext):
        pass

    # Exit a parse tree produced by miniJavaASTParser#program.
    def exitProgram(self, ctx:miniJavaASTParser.ProgramContext):
        pass


    # Enter a parse tree produced by miniJavaASTParser#main_class.
    def enterMain_class(self, ctx:miniJavaASTParser.Main_classContext):
        pass

    # Exit a parse tree produced by miniJavaASTParser#main_class.
    def exitMain_class(self, ctx:miniJavaASTParser.Main_classContext):
        pass


    # Enter a parse tree produced by miniJavaASTParser#class_declaration.
    def enterClass_declaration(self, ctx:miniJavaASTParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by miniJavaASTParser#class_declaration.
    def exitClass_declaration(self, ctx:miniJavaASTParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by miniJavaASTParser#var_declaration.
    def enterVar_declaration(self, ctx:miniJavaASTParser.Var_declarationContext):
        pass

    # Exit a parse tree produced by miniJavaASTParser#var_declaration.
    def exitVar_declaration(self, ctx:miniJavaASTParser.Var_declarationContext):
        pass


    # Enter a parse tree produced by miniJavaASTParser#method_declaration.
    def enterMethod_declaration(self, ctx:miniJavaASTParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by miniJavaASTParser#method_declaration.
    def exitMethod_declaration(self, ctx:miniJavaASTParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by miniJavaASTParser#type_r.
    def enterType_r(self, ctx:miniJavaASTParser.Type_rContext):
        pass

    # Exit a parse tree produced by miniJavaASTParser#type_r.
    def exitType_r(self, ctx:miniJavaASTParser.Type_rContext):
        pass


    # Enter a parse tree produced by miniJavaASTParser#statement.
    def enterStatement(self, ctx:miniJavaASTParser.StatementContext):
        pass

    # Exit a parse tree produced by miniJavaASTParser#statement.
    def exitStatement(self, ctx:miniJavaASTParser.StatementContext):
        pass


    # Enter a parse tree produced by miniJavaASTParser#expression.
    def enterExpression(self, ctx:miniJavaASTParser.ExpressionContext):
        pass

    # Exit a parse tree produced by miniJavaASTParser#expression.
    def exitExpression(self, ctx:miniJavaASTParser.ExpressionContext):
        pass


    # Enter a parse tree produced by miniJavaASTParser#identifier_r.
    def enterIdentifier_r(self, ctx:miniJavaASTParser.Identifier_rContext):
        pass

    # Exit a parse tree produced by miniJavaASTParser#identifier_r.
    def exitIdentifier_r(self, ctx:miniJavaASTParser.Identifier_rContext):
        pass



del miniJavaASTParser