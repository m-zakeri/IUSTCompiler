# Generated from C:/Users/Qafari/Desktop/hw4/IUSTCompiler/code/Q2\MiniJava.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete generic visitor for a parse tree produced by MiniJavaParser.

class MiniJavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniJavaParser#program.
    def visitProgram(self, ctx:MiniJavaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainClass.
    def visitMainClass(self, ctx:MiniJavaParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#type_t.
    def visitType_t(self, ctx:MiniJavaParser.Type_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#bracket_statmetn.
    def visitBracket_statmetn(self, ctx:MiniJavaParser.Bracket_statmetnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#if_statment.
    def visitIf_statment(self, ctx:MiniJavaParser.If_statmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#while_statment.
    def visitWhile_statment(self, ctx:MiniJavaParser.While_statmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#output_statment.
    def visitOutput_statment(self, ctx:MiniJavaParser.Output_statmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#equal_statment.
    def visitEqual_statment(self, ctx:MiniJavaParser.Equal_statmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#equal_array_statment.
    def visitEqual_array_statment(self, ctx:MiniJavaParser.Equal_array_statmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#bracket_exp.
    def visitBracket_exp(self, ctx:MiniJavaParser.Bracket_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#this_exp.
    def visitThis_exp(self, ctx:MiniJavaParser.This_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#num_exp.
    def visitNum_exp(self, ctx:MiniJavaParser.Num_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#len_exp.
    def visitLen_exp(self, ctx:MiniJavaParser.Len_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#dot_par_expression.
    def visitDot_par_expression(self, ctx:MiniJavaParser.Dot_par_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#and_exp.
    def visitAnd_exp(self, ctx:MiniJavaParser.And_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#identifier_exp.
    def visitIdentifier_exp(self, ctx:MiniJavaParser.Identifier_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mul_exp.
    def visitMul_exp(self, ctx:MiniJavaParser.Mul_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#false_exp.
    def visitFalse_exp(self, ctx:MiniJavaParser.False_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#new_array_exp.
    def visitNew_array_exp(self, ctx:MiniJavaParser.New_array_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#new_identifier.
    def visitNew_identifier(self, ctx:MiniJavaParser.New_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#not_exp.
    def visitNot_exp(self, ctx:MiniJavaParser.Not_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#plus_minus_exp.
    def visitPlus_minus_exp(self, ctx:MiniJavaParser.Plus_minus_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#in_par_expression.
    def visitIn_par_expression(self, ctx:MiniJavaParser.In_par_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#lt_exp.
    def visitLt_exp(self, ctx:MiniJavaParser.Lt_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#true_exp.
    def visitTrue_exp(self, ctx:MiniJavaParser.True_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#identifier.
    def visitIdentifier(self, ctx:MiniJavaParser.IdentifierContext):
        return self.visitChildren(ctx)



del MiniJavaParser