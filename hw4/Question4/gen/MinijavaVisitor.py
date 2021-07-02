# Generated from E:/New folder/hw4/final/Question4\Minijava.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MinijavaParser import MinijavaParser
else:
    from MinijavaParser import MinijavaParser

# This class defines a complete generic visitor for a parse tree produced by MinijavaParser.

class MinijavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MinijavaParser#start.
    def visitStart(self, ctx:MinijavaParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#mainClass.
    def visitMainClass(self, ctx:MinijavaParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MinijavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MinijavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MinijavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#typ_int.
    def visitTyp_int(self, ctx:MinijavaParser.Typ_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#typ_int_array.
    def visitTyp_int_array(self, ctx:MinijavaParser.Typ_int_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#typ_boolean.
    def visitTyp_boolean(self, ctx:MinijavaParser.Typ_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#typ_identifier.
    def visitTyp_identifier(self, ctx:MinijavaParser.Typ_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#statement_1.
    def visitStatement_1(self, ctx:MinijavaParser.Statement_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#statement_2.
    def visitStatement_2(self, ctx:MinijavaParser.Statement_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#statement_3.
    def visitStatement_3(self, ctx:MinijavaParser.Statement_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#statement_4.
    def visitStatement_4(self, ctx:MinijavaParser.Statement_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#statement_5.
    def visitStatement_5(self, ctx:MinijavaParser.Statement_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#statement_6.
    def visitStatement_6(self, ctx:MinijavaParser.Statement_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_13.
    def visitExpression_13(self, ctx:MinijavaParser.Expression_13Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_12.
    def visitExpression_12(self, ctx:MinijavaParser.Expression_12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_2.
    def visitExpression_2(self, ctx:MinijavaParser.Expression_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_1.
    def visitExpression_1(self, ctx:MinijavaParser.Expression_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_4.
    def visitExpression_4(self, ctx:MinijavaParser.Expression_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_3.
    def visitExpression_3(self, ctx:MinijavaParser.Expression_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_6.
    def visitExpression_6(self, ctx:MinijavaParser.Expression_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_11.
    def visitExpression_11(self, ctx:MinijavaParser.Expression_11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_5.
    def visitExpression_5(self, ctx:MinijavaParser.Expression_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_10.
    def visitExpression_10(self, ctx:MinijavaParser.Expression_10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_8.
    def visitExpression_8(self, ctx:MinijavaParser.Expression_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_7.
    def visitExpression_7(self, ctx:MinijavaParser.Expression_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#expression_9.
    def visitExpression_9(self, ctx:MinijavaParser.Expression_9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#param.
    def visitParam(self, ctx:MinijavaParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#binaryOperator_and.
    def visitBinaryOperator_and(self, ctx:MinijavaParser.BinaryOperator_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#binaryOperator_smaller.
    def visitBinaryOperator_smaller(self, ctx:MinijavaParser.BinaryOperator_smallerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#binaryOperator_plus.
    def visitBinaryOperator_plus(self, ctx:MinijavaParser.BinaryOperator_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#binaryOperator_minus.
    def visitBinaryOperator_minus(self, ctx:MinijavaParser.BinaryOperator_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#binaryOperator_multiple.
    def visitBinaryOperator_multiple(self, ctx:MinijavaParser.BinaryOperator_multipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinijavaParser#identifier.
    def visitIdentifier(self, ctx:MinijavaParser.IdentifierContext):
        return self.visitChildren(ctx)



del MinijavaParser