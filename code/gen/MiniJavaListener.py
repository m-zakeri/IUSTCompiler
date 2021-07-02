# Generated from C:/Users/Qafari/Desktop/hw4/IUSTCompiler/code/Q2\MiniJava.g4 by ANTLR 4.9.1
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


    # Enter a parse tree produced by MiniJavaParser#type_t.
    def enterType_t(self, ctx:MiniJavaParser.Type_tContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#type_t.
    def exitType_t(self, ctx:MiniJavaParser.Type_tContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#bracket_statmetn.
    def enterBracket_statmetn(self, ctx:MiniJavaParser.Bracket_statmetnContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#bracket_statmetn.
    def exitBracket_statmetn(self, ctx:MiniJavaParser.Bracket_statmetnContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#if_statment.
    def enterIf_statment(self, ctx:MiniJavaParser.If_statmentContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#if_statment.
    def exitIf_statment(self, ctx:MiniJavaParser.If_statmentContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#while_statment.
    def enterWhile_statment(self, ctx:MiniJavaParser.While_statmentContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#while_statment.
    def exitWhile_statment(self, ctx:MiniJavaParser.While_statmentContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#output_statment.
    def enterOutput_statment(self, ctx:MiniJavaParser.Output_statmentContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#output_statment.
    def exitOutput_statment(self, ctx:MiniJavaParser.Output_statmentContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#equal_statment.
    def enterEqual_statment(self, ctx:MiniJavaParser.Equal_statmentContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#equal_statment.
    def exitEqual_statment(self, ctx:MiniJavaParser.Equal_statmentContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#equal_array_statment.
    def enterEqual_array_statment(self, ctx:MiniJavaParser.Equal_array_statmentContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#equal_array_statment.
    def exitEqual_array_statment(self, ctx:MiniJavaParser.Equal_array_statmentContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#bracket_exp.
    def enterBracket_exp(self, ctx:MiniJavaParser.Bracket_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#bracket_exp.
    def exitBracket_exp(self, ctx:MiniJavaParser.Bracket_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#this_exp.
    def enterThis_exp(self, ctx:MiniJavaParser.This_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#this_exp.
    def exitThis_exp(self, ctx:MiniJavaParser.This_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#num_exp.
    def enterNum_exp(self, ctx:MiniJavaParser.Num_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#num_exp.
    def exitNum_exp(self, ctx:MiniJavaParser.Num_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#len_exp.
    def enterLen_exp(self, ctx:MiniJavaParser.Len_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#len_exp.
    def exitLen_exp(self, ctx:MiniJavaParser.Len_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#dot_par_expression.
    def enterDot_par_expression(self, ctx:MiniJavaParser.Dot_par_expressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#dot_par_expression.
    def exitDot_par_expression(self, ctx:MiniJavaParser.Dot_par_expressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#and_exp.
    def enterAnd_exp(self, ctx:MiniJavaParser.And_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#and_exp.
    def exitAnd_exp(self, ctx:MiniJavaParser.And_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#identifier_exp.
    def enterIdentifier_exp(self, ctx:MiniJavaParser.Identifier_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#identifier_exp.
    def exitIdentifier_exp(self, ctx:MiniJavaParser.Identifier_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#mul_exp.
    def enterMul_exp(self, ctx:MiniJavaParser.Mul_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#mul_exp.
    def exitMul_exp(self, ctx:MiniJavaParser.Mul_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#false_exp.
    def enterFalse_exp(self, ctx:MiniJavaParser.False_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#false_exp.
    def exitFalse_exp(self, ctx:MiniJavaParser.False_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#new_array_exp.
    def enterNew_array_exp(self, ctx:MiniJavaParser.New_array_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#new_array_exp.
    def exitNew_array_exp(self, ctx:MiniJavaParser.New_array_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#new_identifier.
    def enterNew_identifier(self, ctx:MiniJavaParser.New_identifierContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#new_identifier.
    def exitNew_identifier(self, ctx:MiniJavaParser.New_identifierContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#not_exp.
    def enterNot_exp(self, ctx:MiniJavaParser.Not_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#not_exp.
    def exitNot_exp(self, ctx:MiniJavaParser.Not_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#plus_minus_exp.
    def enterPlus_minus_exp(self, ctx:MiniJavaParser.Plus_minus_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#plus_minus_exp.
    def exitPlus_minus_exp(self, ctx:MiniJavaParser.Plus_minus_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#in_par_expression.
    def enterIn_par_expression(self, ctx:MiniJavaParser.In_par_expressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#in_par_expression.
    def exitIn_par_expression(self, ctx:MiniJavaParser.In_par_expressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#lt_exp.
    def enterLt_exp(self, ctx:MiniJavaParser.Lt_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#lt_exp.
    def exitLt_exp(self, ctx:MiniJavaParser.Lt_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#true_exp.
    def enterTrue_exp(self, ctx:MiniJavaParser.True_expContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#true_exp.
    def exitTrue_exp(self, ctx:MiniJavaParser.True_expContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#identifier.
    def enterIdentifier(self, ctx:MiniJavaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#identifier.
    def exitIdentifier(self, ctx:MiniJavaParser.IdentifierContext):
        pass



del MiniJavaParser