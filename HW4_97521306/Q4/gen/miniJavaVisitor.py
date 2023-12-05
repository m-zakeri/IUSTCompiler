# Generated from E:/Compiler/HW4/Q4_2\miniJava.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniJavaParser import miniJavaParser
else:
    from miniJavaParser import miniJavaParser

# This class defines a complete generic visitor for a parse tree produced by miniJavaParser.

class miniJavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miniJavaParser#program.
    def visitProgram(self, ctx:miniJavaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#mainClass.
    def visitMainClass(self, ctx:miniJavaParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:miniJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx:miniJavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:miniJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#type.
    def visitType(self, ctx:miniJavaParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#statement_statement.
    def visitStatement_statement(self, ctx:miniJavaParser.Statement_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#statement_if.
    def visitStatement_if(self, ctx:miniJavaParser.Statement_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#statement_while.
    def visitStatement_while(self, ctx:miniJavaParser.Statement_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#statement_println.
    def visitStatement_println(self, ctx:miniJavaParser.Statement_printlnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#statement_value_assignment.
    def visitStatement_value_assignment(self, ctx:miniJavaParser.Statement_value_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#statement_array_cell_assignment.
    def visitStatement_array_cell_assignment(self, ctx:miniJavaParser.Statement_array_cell_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_not.
    def visitExpression_not(self, ctx:miniJavaParser.Expression_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_this.
    def visitExpression_this(self, ctx:miniJavaParser.Expression_thisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_identifier.
    def visitExpression_identifier(self, ctx:miniJavaParser.Expression_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_array_declaration.
    def visitExpression_array_declaration(self, ctx:miniJavaParser.Expression_array_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_lessthan_expression.
    def visitExpression_lessthan_expression(self, ctx:miniJavaParser.Expression_lessthan_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_paranthesis_expression.
    def visitExpression_paranthesis_expression(self, ctx:miniJavaParser.Expression_paranthesis_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_class_declaration.
    def visitExpression_class_declaration(self, ctx:miniJavaParser.Expression_class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_and_expression.
    def visitExpression_and_expression(self, ctx:miniJavaParser.Expression_and_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_array.
    def visitExpression_array(self, ctx:miniJavaParser.Expression_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_true.
    def visitExpression_true(self, ctx:miniJavaParser.Expression_trueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_array_length.
    def visitExpression_array_length(self, ctx:miniJavaParser.Expression_array_lengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_function_call.
    def visitExpression_function_call(self, ctx:miniJavaParser.Expression_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_plus_expression.
    def visitExpression_plus_expression(self, ctx:miniJavaParser.Expression_plus_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_multiply_expression.
    def visitExpression_multiply_expression(self, ctx:miniJavaParser.Expression_multiply_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_integer_literal.
    def visitExpression_integer_literal(self, ctx:miniJavaParser.Expression_integer_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_false.
    def visitExpression_false(self, ctx:miniJavaParser.Expression_falseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#expression_minus_expression.
    def visitExpression_minus_expression(self, ctx:miniJavaParser.Expression_minus_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#identifier.
    def visitIdentifier(self, ctx:miniJavaParser.IdentifierContext):
        return self.visitChildren(ctx)



del miniJavaParser