# Generated from /home/pouorix/Desktop/compilerHW4/Me/IUSTCompiler/HW4/Q2.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Q2Parser import Q2Parser
else:
    from Q2Parser import Q2Parser

# This class defines a complete listener for a parse tree produced by Q2Parser.
class Q2Listener(ParseTreeListener):

    # Enter a parse tree produced by Q2Parser#program.
    def enterProgram(self, ctx:Q2Parser.ProgramContext):
        pass

    # Exit a parse tree produced by Q2Parser#program.
    def exitProgram(self, ctx:Q2Parser.ProgramContext):
        pass


    # Enter a parse tree produced by Q2Parser#mainClass.
    def enterMainClass(self, ctx:Q2Parser.MainClassContext):
        pass

    # Exit a parse tree produced by Q2Parser#mainClass.
    def exitMainClass(self, ctx:Q2Parser.MainClassContext):
        pass


    # Enter a parse tree produced by Q2Parser#classDeclaration.
    def enterClassDeclaration(self, ctx:Q2Parser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by Q2Parser#classDeclaration.
    def exitClassDeclaration(self, ctx:Q2Parser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by Q2Parser#varDeclaration.
    def enterVarDeclaration(self, ctx:Q2Parser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by Q2Parser#varDeclaration.
    def exitVarDeclaration(self, ctx:Q2Parser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by Q2Parser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:Q2Parser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by Q2Parser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:Q2Parser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by Q2Parser#array_int.
    def enterArray_int(self, ctx:Q2Parser.Array_intContext):
        pass

    # Exit a parse tree produced by Q2Parser#array_int.
    def exitArray_int(self, ctx:Q2Parser.Array_intContext):
        pass


    # Enter a parse tree produced by Q2Parser#bool.
    def enterBool(self, ctx:Q2Parser.BoolContext):
        pass

    # Exit a parse tree produced by Q2Parser#bool.
    def exitBool(self, ctx:Q2Parser.BoolContext):
        pass


    # Enter a parse tree produced by Q2Parser#int.
    def enterInt(self, ctx:Q2Parser.IntContext):
        pass

    # Exit a parse tree produced by Q2Parser#int.
    def exitInt(self, ctx:Q2Parser.IntContext):
        pass


    # Enter a parse tree produced by Q2Parser#id.
    def enterId(self, ctx:Q2Parser.IdContext):
        pass

    # Exit a parse tree produced by Q2Parser#id.
    def exitId(self, ctx:Q2Parser.IdContext):
        pass


    # Enter a parse tree produced by Q2Parser#braket_statement.
    def enterBraket_statement(self, ctx:Q2Parser.Braket_statementContext):
        pass

    # Exit a parse tree produced by Q2Parser#braket_statement.
    def exitBraket_statement(self, ctx:Q2Parser.Braket_statementContext):
        pass


    # Enter a parse tree produced by Q2Parser#if_statement.
    def enterIf_statement(self, ctx:Q2Parser.If_statementContext):
        pass

    # Exit a parse tree produced by Q2Parser#if_statement.
    def exitIf_statement(self, ctx:Q2Parser.If_statementContext):
        pass


    # Enter a parse tree produced by Q2Parser#equal_statement.
    def enterEqual_statement(self, ctx:Q2Parser.Equal_statementContext):
        pass

    # Exit a parse tree produced by Q2Parser#equal_statement.
    def exitEqual_statement(self, ctx:Q2Parser.Equal_statementContext):
        pass


    # Enter a parse tree produced by Q2Parser#while_statement.
    def enterWhile_statement(self, ctx:Q2Parser.While_statementContext):
        pass

    # Exit a parse tree produced by Q2Parser#while_statement.
    def exitWhile_statement(self, ctx:Q2Parser.While_statementContext):
        pass


    # Enter a parse tree produced by Q2Parser#print.
    def enterPrint(self, ctx:Q2Parser.PrintContext):
        pass

    # Exit a parse tree produced by Q2Parser#print.
    def exitPrint(self, ctx:Q2Parser.PrintContext):
        pass


    # Enter a parse tree produced by Q2Parser#equal_array_statement.
    def enterEqual_array_statement(self, ctx:Q2Parser.Equal_array_statementContext):
        pass

    # Exit a parse tree produced by Q2Parser#equal_array_statement.
    def exitEqual_array_statement(self, ctx:Q2Parser.Equal_array_statementContext):
        pass


    # Enter a parse tree produced by Q2Parser#number.
    def enterNumber(self, ctx:Q2Parser.NumberContext):
        pass

    # Exit a parse tree produced by Q2Parser#number.
    def exitNumber(self, ctx:Q2Parser.NumberContext):
        pass


    # Enter a parse tree produced by Q2Parser#not_expression.
    def enterNot_expression(self, ctx:Q2Parser.Not_expressionContext):
        pass

    # Exit a parse tree produced by Q2Parser#not_expression.
    def exitNot_expression(self, ctx:Q2Parser.Not_expressionContext):
        pass


    # Enter a parse tree produced by Q2Parser#new_identifier.
    def enterNew_identifier(self, ctx:Q2Parser.New_identifierContext):
        pass

    # Exit a parse tree produced by Q2Parser#new_identifier.
    def exitNew_identifier(self, ctx:Q2Parser.New_identifierContext):
        pass


    # Enter a parse tree produced by Q2Parser#keywords.
    def enterKeywords(self, ctx:Q2Parser.KeywordsContext):
        pass

    # Exit a parse tree produced by Q2Parser#keywords.
    def exitKeywords(self, ctx:Q2Parser.KeywordsContext):
        pass


    # Enter a parse tree produced by Q2Parser#dot_par_expression.
    def enterDot_par_expression(self, ctx:Q2Parser.Dot_par_expressionContext):
        pass

    # Exit a parse tree produced by Q2Parser#dot_par_expression.
    def exitDot_par_expression(self, ctx:Q2Parser.Dot_par_expressionContext):
        pass


    # Enter a parse tree produced by Q2Parser#in_par_expression.
    def enterIn_par_expression(self, ctx:Q2Parser.In_par_expressionContext):
        pass

    # Exit a parse tree produced by Q2Parser#in_par_expression.
    def exitIn_par_expression(self, ctx:Q2Parser.In_par_expressionContext):
        pass


    # Enter a parse tree produced by Q2Parser#operations_expression.
    def enterOperations_expression(self, ctx:Q2Parser.Operations_expressionContext):
        pass

    # Exit a parse tree produced by Q2Parser#operations_expression.
    def exitOperations_expression(self, ctx:Q2Parser.Operations_expressionContext):
        pass


    # Enter a parse tree produced by Q2Parser#array_expression.
    def enterArray_expression(self, ctx:Q2Parser.Array_expressionContext):
        pass

    # Exit a parse tree produced by Q2Parser#array_expression.
    def exitArray_expression(self, ctx:Q2Parser.Array_expressionContext):
        pass


    # Enter a parse tree produced by Q2Parser#word.
    def enterWord(self, ctx:Q2Parser.WordContext):
        pass

    # Exit a parse tree produced by Q2Parser#word.
    def exitWord(self, ctx:Q2Parser.WordContext):
        pass


    # Enter a parse tree produced by Q2Parser#new_array_expression.
    def enterNew_array_expression(self, ctx:Q2Parser.New_array_expressionContext):
        pass

    # Exit a parse tree produced by Q2Parser#new_array_expression.
    def exitNew_array_expression(self, ctx:Q2Parser.New_array_expressionContext):
        pass


    # Enter a parse tree produced by Q2Parser#length_expression.
    def enterLength_expression(self, ctx:Q2Parser.Length_expressionContext):
        pass

    # Exit a parse tree produced by Q2Parser#length_expression.
    def exitLength_expression(self, ctx:Q2Parser.Length_expressionContext):
        pass



del Q2Parser