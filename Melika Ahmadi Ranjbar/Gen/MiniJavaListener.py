# Generated from D:/University/Sem6/Compiler/Assignment4\MiniJava.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete listener for a parse tree produced by MiniJavaParser.
class MiniJavaListener(ParseTreeListener):

    # Enter a parse tree produced by MiniJavaParser#program.
    def enterProgram(self, ctx:MiniJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#program.
    def exitProgram(self, ctx:MiniJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#mainClass.
    def enterMainClass(self, ctx:MiniJavaParser.MainClassContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#mainClass.
    def exitMainClass(self, ctx:MiniJavaParser.MainClassContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#mainClassEnter.
    def enterMainClassEnter(self, ctx:MiniJavaParser.MainClassEnterContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#mainClassEnter.
    def exitMainClassEnter(self, ctx:MiniJavaParser.MainClassEnterContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#mainClassBody.
    def enterMainClassBody(self, ctx:MiniJavaParser.MainClassBodyContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#mainClassBody.
    def exitMainClassBody(self, ctx:MiniJavaParser.MainClassBodyContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#varDeclaration.
    def enterVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#varDeclaration.
    def exitVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#array_int.
    def enterArray_int(self, ctx:MiniJavaParser.Array_intContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#array_int.
    def exitArray_int(self, ctx:MiniJavaParser.Array_intContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#bool.
    def enterBool(self, ctx:MiniJavaParser.BoolContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#bool.
    def exitBool(self, ctx:MiniJavaParser.BoolContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#int.
    def enterInt(self, ctx:MiniJavaParser.IntContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#int.
    def exitInt(self, ctx:MiniJavaParser.IntContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#id.
    def enterId(self, ctx:MiniJavaParser.IdContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#id.
    def exitId(self, ctx:MiniJavaParser.IdContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#braket_statement.
    def enterBraket_statement(self, ctx:MiniJavaParser.Braket_statementContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#braket_statement.
    def exitBraket_statement(self, ctx:MiniJavaParser.Braket_statementContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#if_statement.
    def enterIf_statement(self, ctx:MiniJavaParser.If_statementContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#if_statement.
    def exitIf_statement(self, ctx:MiniJavaParser.If_statementContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#while_statement.
    def enterWhile_statement(self, ctx:MiniJavaParser.While_statementContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#while_statement.
    def exitWhile_statement(self, ctx:MiniJavaParser.While_statementContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#print.
    def enterPrint(self, ctx:MiniJavaParser.PrintContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#print.
    def exitPrint(self, ctx:MiniJavaParser.PrintContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#equal_statement.
    def enterEqual_statement(self, ctx:MiniJavaParser.Equal_statementContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#equal_statement.
    def exitEqual_statement(self, ctx:MiniJavaParser.Equal_statementContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#equal_array_statement.
    def enterEqual_array_statement(self, ctx:MiniJavaParser.Equal_array_statementContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#equal_array_statement.
    def exitEqual_array_statement(self, ctx:MiniJavaParser.Equal_array_statementContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#number.
    def enterNumber(self, ctx:MiniJavaParser.NumberContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#number.
    def exitNumber(self, ctx:MiniJavaParser.NumberContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#new_identifier.
    def enterNew_identifier(self, ctx:MiniJavaParser.New_identifierContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#new_identifier.
    def exitNew_identifier(self, ctx:MiniJavaParser.New_identifierContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#not_expression.
    def enterNot_expression(self, ctx:MiniJavaParser.Not_expressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#not_expression.
    def exitNot_expression(self, ctx:MiniJavaParser.Not_expressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#keywords.
    def enterKeywords(self, ctx:MiniJavaParser.KeywordsContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#keywords.
    def exitKeywords(self, ctx:MiniJavaParser.KeywordsContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#dot_par_expression.
    def enterDot_par_expression(self, ctx:MiniJavaParser.Dot_par_expressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#dot_par_expression.
    def exitDot_par_expression(self, ctx:MiniJavaParser.Dot_par_expressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#in_par_expression.
    def enterIn_par_expression(self, ctx:MiniJavaParser.In_par_expressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#in_par_expression.
    def exitIn_par_expression(self, ctx:MiniJavaParser.In_par_expressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#operations_expression.
    def enterOperations_expression(self, ctx:MiniJavaParser.Operations_expressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#operations_expression.
    def exitOperations_expression(self, ctx:MiniJavaParser.Operations_expressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#array_expression.
    def enterArray_expression(self, ctx:MiniJavaParser.Array_expressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#array_expression.
    def exitArray_expression(self, ctx:MiniJavaParser.Array_expressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#word.
    def enterWord(self, ctx:MiniJavaParser.WordContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#word.
    def exitWord(self, ctx:MiniJavaParser.WordContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#new_array_expression.
    def enterNew_array_expression(self, ctx:MiniJavaParser.New_array_expressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#new_array_expression.
    def exitNew_array_expression(self, ctx:MiniJavaParser.New_array_expressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#length_expression.
    def enterLength_expression(self, ctx:MiniJavaParser.Length_expressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#length_expression.
    def exitLength_expression(self, ctx:MiniJavaParser.Length_expressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#identifier.
    def enterIdentifier(self, ctx:MiniJavaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#identifier.
    def exitIdentifier(self, ctx:MiniJavaParser.IdentifierContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#operations.
    def enterOperations(self, ctx:MiniJavaParser.OperationsContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#operations.
    def exitOperations(self, ctx:MiniJavaParser.OperationsContext):
        pass



del MiniJavaParser