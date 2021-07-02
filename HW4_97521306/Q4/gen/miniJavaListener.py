# Generated from E:/Compiler/HW4/Q4_2\miniJava.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miniJavaParser import miniJavaParser
else:
    from miniJavaParser import miniJavaParser

# This class defines a complete listener for a parse tree produced by miniJavaParser.
class miniJavaListener(ParseTreeListener):

    # Enter a parse tree produced by miniJavaParser#program.
    def enterProgram(self, ctx:miniJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by miniJavaParser#program.
    def exitProgram(self, ctx:miniJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by miniJavaParser#mainClass.
    def enterMainClass(self, ctx:miniJavaParser.MainClassContext):
        pass

    # Exit a parse tree produced by miniJavaParser#mainClass.
    def exitMainClass(self, ctx:miniJavaParser.MainClassContext):
        pass


    # Enter a parse tree produced by miniJavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:miniJavaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by miniJavaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:miniJavaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by miniJavaParser#varDeclaration.
    def enterVarDeclaration(self, ctx:miniJavaParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by miniJavaParser#varDeclaration.
    def exitVarDeclaration(self, ctx:miniJavaParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by miniJavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:miniJavaParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by miniJavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:miniJavaParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by miniJavaParser#type.
    def enterType(self, ctx:miniJavaParser.TypeContext):
        pass

    # Exit a parse tree produced by miniJavaParser#type.
    def exitType(self, ctx:miniJavaParser.TypeContext):
        pass


    # Enter a parse tree produced by miniJavaParser#statement_statement.
    def enterStatement_statement(self, ctx:miniJavaParser.Statement_statementContext):
        pass

    # Exit a parse tree produced by miniJavaParser#statement_statement.
    def exitStatement_statement(self, ctx:miniJavaParser.Statement_statementContext):
        pass


    # Enter a parse tree produced by miniJavaParser#statement_if.
    def enterStatement_if(self, ctx:miniJavaParser.Statement_ifContext):
        pass

    # Exit a parse tree produced by miniJavaParser#statement_if.
    def exitStatement_if(self, ctx:miniJavaParser.Statement_ifContext):
        pass


    # Enter a parse tree produced by miniJavaParser#statement_while.
    def enterStatement_while(self, ctx:miniJavaParser.Statement_whileContext):
        pass

    # Exit a parse tree produced by miniJavaParser#statement_while.
    def exitStatement_while(self, ctx:miniJavaParser.Statement_whileContext):
        pass


    # Enter a parse tree produced by miniJavaParser#statement_println.
    def enterStatement_println(self, ctx:miniJavaParser.Statement_printlnContext):
        pass

    # Exit a parse tree produced by miniJavaParser#statement_println.
    def exitStatement_println(self, ctx:miniJavaParser.Statement_printlnContext):
        pass


    # Enter a parse tree produced by miniJavaParser#statement_value_assignment.
    def enterStatement_value_assignment(self, ctx:miniJavaParser.Statement_value_assignmentContext):
        pass

    # Exit a parse tree produced by miniJavaParser#statement_value_assignment.
    def exitStatement_value_assignment(self, ctx:miniJavaParser.Statement_value_assignmentContext):
        pass


    # Enter a parse tree produced by miniJavaParser#statement_array_cell_assignment.
    def enterStatement_array_cell_assignment(self, ctx:miniJavaParser.Statement_array_cell_assignmentContext):
        pass

    # Exit a parse tree produced by miniJavaParser#statement_array_cell_assignment.
    def exitStatement_array_cell_assignment(self, ctx:miniJavaParser.Statement_array_cell_assignmentContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_not.
    def enterExpression_not(self, ctx:miniJavaParser.Expression_notContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_not.
    def exitExpression_not(self, ctx:miniJavaParser.Expression_notContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_this.
    def enterExpression_this(self, ctx:miniJavaParser.Expression_thisContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_this.
    def exitExpression_this(self, ctx:miniJavaParser.Expression_thisContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_identifier.
    def enterExpression_identifier(self, ctx:miniJavaParser.Expression_identifierContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_identifier.
    def exitExpression_identifier(self, ctx:miniJavaParser.Expression_identifierContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_array_declaration.
    def enterExpression_array_declaration(self, ctx:miniJavaParser.Expression_array_declarationContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_array_declaration.
    def exitExpression_array_declaration(self, ctx:miniJavaParser.Expression_array_declarationContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_lessthan_expression.
    def enterExpression_lessthan_expression(self, ctx:miniJavaParser.Expression_lessthan_expressionContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_lessthan_expression.
    def exitExpression_lessthan_expression(self, ctx:miniJavaParser.Expression_lessthan_expressionContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_paranthesis_expression.
    def enterExpression_paranthesis_expression(self, ctx:miniJavaParser.Expression_paranthesis_expressionContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_paranthesis_expression.
    def exitExpression_paranthesis_expression(self, ctx:miniJavaParser.Expression_paranthesis_expressionContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_class_declaration.
    def enterExpression_class_declaration(self, ctx:miniJavaParser.Expression_class_declarationContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_class_declaration.
    def exitExpression_class_declaration(self, ctx:miniJavaParser.Expression_class_declarationContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_and_expression.
    def enterExpression_and_expression(self, ctx:miniJavaParser.Expression_and_expressionContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_and_expression.
    def exitExpression_and_expression(self, ctx:miniJavaParser.Expression_and_expressionContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_array.
    def enterExpression_array(self, ctx:miniJavaParser.Expression_arrayContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_array.
    def exitExpression_array(self, ctx:miniJavaParser.Expression_arrayContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_true.
    def enterExpression_true(self, ctx:miniJavaParser.Expression_trueContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_true.
    def exitExpression_true(self, ctx:miniJavaParser.Expression_trueContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_array_length.
    def enterExpression_array_length(self, ctx:miniJavaParser.Expression_array_lengthContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_array_length.
    def exitExpression_array_length(self, ctx:miniJavaParser.Expression_array_lengthContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_function_call.
    def enterExpression_function_call(self, ctx:miniJavaParser.Expression_function_callContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_function_call.
    def exitExpression_function_call(self, ctx:miniJavaParser.Expression_function_callContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_plus_expression.
    def enterExpression_plus_expression(self, ctx:miniJavaParser.Expression_plus_expressionContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_plus_expression.
    def exitExpression_plus_expression(self, ctx:miniJavaParser.Expression_plus_expressionContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_multiply_expression.
    def enterExpression_multiply_expression(self, ctx:miniJavaParser.Expression_multiply_expressionContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_multiply_expression.
    def exitExpression_multiply_expression(self, ctx:miniJavaParser.Expression_multiply_expressionContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_integer_literal.
    def enterExpression_integer_literal(self, ctx:miniJavaParser.Expression_integer_literalContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_integer_literal.
    def exitExpression_integer_literal(self, ctx:miniJavaParser.Expression_integer_literalContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_false.
    def enterExpression_false(self, ctx:miniJavaParser.Expression_falseContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_false.
    def exitExpression_false(self, ctx:miniJavaParser.Expression_falseContext):
        pass


    # Enter a parse tree produced by miniJavaParser#expression_minus_expression.
    def enterExpression_minus_expression(self, ctx:miniJavaParser.Expression_minus_expressionContext):
        pass

    # Exit a parse tree produced by miniJavaParser#expression_minus_expression.
    def exitExpression_minus_expression(self, ctx:miniJavaParser.Expression_minus_expressionContext):
        pass


    # Enter a parse tree produced by miniJavaParser#identifier.
    def enterIdentifier(self, ctx:miniJavaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by miniJavaParser#identifier.
    def exitIdentifier(self, ctx:miniJavaParser.IdentifierContext):
        pass



del miniJavaParser