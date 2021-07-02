# Generated from Q4.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Q4Parser import Q4Parser
else:
    from Q4Parser import Q4Parser

# This class defines a complete listener for a parse tree produced by Q4Parser.
class Q4Listener(ParseTreeListener):

    # Enter a parse tree produced by Q4Parser#program.
    def enterProgram(self, ctx:Q4Parser.ProgramContext):
        pass

    # Exit a parse tree produced by Q4Parser#program.
    def exitProgram(self, ctx:Q4Parser.ProgramContext):
        pass


    # Enter a parse tree produced by Q4Parser#mainClass.
    def enterMainClass(self, ctx:Q4Parser.MainClassContext):
        pass

    # Exit a parse tree produced by Q4Parser#mainClass.
    def exitMainClass(self, ctx:Q4Parser.MainClassContext):
        pass


    # Enter a parse tree produced by Q4Parser#classDeclaration.
    def enterClassDeclaration(self, ctx:Q4Parser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by Q4Parser#classDeclaration.
    def exitClassDeclaration(self, ctx:Q4Parser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by Q4Parser#varDeclaration.
    def enterVarDeclaration(self, ctx:Q4Parser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by Q4Parser#varDeclaration.
    def exitVarDeclaration(self, ctx:Q4Parser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by Q4Parser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:Q4Parser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by Q4Parser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:Q4Parser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by Q4Parser#type.
    def enterType(self, ctx:Q4Parser.TypeContext):
        pass

    # Exit a parse tree produced by Q4Parser#type.
    def exitType(self, ctx:Q4Parser.TypeContext):
        pass


    # Enter a parse tree produced by Q4Parser#state_if.
    def enterState_if(self, ctx:Q4Parser.State_ifContext):
        pass

    # Exit a parse tree produced by Q4Parser#state_if.
    def exitState_if(self, ctx:Q4Parser.State_ifContext):
        pass


    # Enter a parse tree produced by Q4Parser#state_brace.
    def enterState_brace(self, ctx:Q4Parser.State_braceContext):
        pass

    # Exit a parse tree produced by Q4Parser#state_brace.
    def exitState_brace(self, ctx:Q4Parser.State_braceContext):
        pass


    # Enter a parse tree produced by Q4Parser#state_while.
    def enterState_while(self, ctx:Q4Parser.State_whileContext):
        pass

    # Exit a parse tree produced by Q4Parser#state_while.
    def exitState_while(self, ctx:Q4Parser.State_whileContext):
        pass


    # Enter a parse tree produced by Q4Parser#state_println.
    def enterState_println(self, ctx:Q4Parser.State_printlnContext):
        pass

    # Exit a parse tree produced by Q4Parser#state_println.
    def exitState_println(self, ctx:Q4Parser.State_printlnContext):
        pass


    # Enter a parse tree produced by Q4Parser#state_equal_assign.
    def enterState_equal_assign(self, ctx:Q4Parser.State_equal_assignContext):
        pass

    # Exit a parse tree produced by Q4Parser#state_equal_assign.
    def exitState_equal_assign(self, ctx:Q4Parser.State_equal_assignContext):
        pass


    # Enter a parse tree produced by Q4Parser#state_access_array_assign.
    def enterState_access_array_assign(self, ctx:Q4Parser.State_access_array_assignContext):
        pass

    # Exit a parse tree produced by Q4Parser#state_access_array_assign.
    def exitState_access_array_assign(self, ctx:Q4Parser.State_access_array_assignContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_useless_4.
    def enterExpr_term_useless_4(self, ctx:Q4Parser.Expr_term_useless_4Context):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_useless_4.
    def exitExpr_term_useless_4(self, ctx:Q4Parser.Expr_term_useless_4Context):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_useless_5.
    def enterExpr_term_useless_5(self, ctx:Q4Parser.Expr_term_useless_5Context):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_useless_5.
    def exitExpr_term_useless_5(self, ctx:Q4Parser.Expr_term_useless_5Context):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_useless_2.
    def enterExpr_term_useless_2(self, ctx:Q4Parser.Expr_term_useless_2Context):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_useless_2.
    def exitExpr_term_useless_2(self, ctx:Q4Parser.Expr_term_useless_2Context):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_useless_3.
    def enterExpr_term_useless_3(self, ctx:Q4Parser.Expr_term_useless_3Context):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_useless_3.
    def exitExpr_term_useless_3(self, ctx:Q4Parser.Expr_term_useless_3Context):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_useless_1.
    def enterExpr_term_useless_1(self, ctx:Q4Parser.Expr_term_useless_1Context):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_useless_1.
    def exitExpr_term_useless_1(self, ctx:Q4Parser.Expr_term_useless_1Context):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_plus.
    def enterExpr_term_plus(self, ctx:Q4Parser.Expr_term_plusContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_plus.
    def exitExpr_term_plus(self, ctx:Q4Parser.Expr_term_plusContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_false.
    def enterExpr_term_false(self, ctx:Q4Parser.Expr_term_falseContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_false.
    def exitExpr_term_false(self, ctx:Q4Parser.Expr_term_falseContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_less.
    def enterExpr_term_less(self, ctx:Q4Parser.Expr_term_lessContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_less.
    def exitExpr_term_less(self, ctx:Q4Parser.Expr_term_lessContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_minus.
    def enterExpr_term_minus(self, ctx:Q4Parser.Expr_term_minusContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_minus.
    def exitExpr_term_minus(self, ctx:Q4Parser.Expr_term_minusContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_int.
    def enterExpr_term_int(self, ctx:Q4Parser.Expr_term_intContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_int.
    def exitExpr_term_int(self, ctx:Q4Parser.Expr_term_intContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_paran.
    def enterExpr_term_paran(self, ctx:Q4Parser.Expr_term_paranContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_paran.
    def exitExpr_term_paran(self, ctx:Q4Parser.Expr_term_paranContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_true.
    def enterExpr_term_true(self, ctx:Q4Parser.Expr_term_trueContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_true.
    def exitExpr_term_true(self, ctx:Q4Parser.Expr_term_trueContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_not.
    def enterExpr_term_not(self, ctx:Q4Parser.Expr_term_notContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_not.
    def exitExpr_term_not(self, ctx:Q4Parser.Expr_term_notContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_call_function.
    def enterExpr_term_call_function(self, ctx:Q4Parser.Expr_term_call_functionContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_call_function.
    def exitExpr_term_call_function(self, ctx:Q4Parser.Expr_term_call_functionContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_id.
    def enterExpr_term_id(self, ctx:Q4Parser.Expr_term_idContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_id.
    def exitExpr_term_id(self, ctx:Q4Parser.Expr_term_idContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_and.
    def enterExpr_term_and(self, ctx:Q4Parser.Expr_term_andContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_and.
    def exitExpr_term_and(self, ctx:Q4Parser.Expr_term_andContext):
        pass


    # Enter a parse tree produced by Q4Parser#expr_term_multiply.
    def enterExpr_term_multiply(self, ctx:Q4Parser.Expr_term_multiplyContext):
        pass

    # Exit a parse tree produced by Q4Parser#expr_term_multiply.
    def exitExpr_term_multiply(self, ctx:Q4Parser.Expr_term_multiplyContext):
        pass


    # Enter a parse tree produced by Q4Parser#identifier.
    def enterIdentifier(self, ctx:Q4Parser.IdentifierContext):
        pass

    # Exit a parse tree produced by Q4Parser#identifier.
    def exitIdentifier(self, ctx:Q4Parser.IdentifierContext):
        pass



del Q4Parser