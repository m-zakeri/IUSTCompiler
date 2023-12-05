# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars/AssignmentStatement2.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AssignmentStatement2Parser import AssignmentStatement2Parser
else:
    from AssignmentStatement2Parser import AssignmentStatement2Parser

# This class defines a complete generic visitor for a parse tree produced by AssignmentStatement2Parser.

class AssignmentStatement2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by AssignmentStatement2Parser#start.
    def visitStart(self, ctx:AssignmentStatement2Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#prog.
    def visitProg(self, ctx:AssignmentStatement2Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#assign.
    def visitAssign(self, ctx:AssignmentStatement2Parser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#expr_term_minus.
    def visitExpr_term_minus(self, ctx:AssignmentStatement2Parser.Expr_term_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#expr_term_plus.
    def visitExpr_term_plus(self, ctx:AssignmentStatement2Parser.Expr_term_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#term4.
    def visitTerm4(self, ctx:AssignmentStatement2Parser.Term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#expr_term_relop.
    def visitExpr_term_relop(self, ctx:AssignmentStatement2Parser.Expr_term_relopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#term_fact_divide.
    def visitTerm_fact_divide(self, ctx:AssignmentStatement2Parser.Term_fact_divideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#term_fact_mutiply.
    def visitTerm_fact_mutiply(self, ctx:AssignmentStatement2Parser.Term_fact_mutiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#factor3.
    def visitFactor3(self, ctx:AssignmentStatement2Parser.Factor3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#fact_expr.
    def visitFact_expr(self, ctx:AssignmentStatement2Parser.Fact_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#fact_id.
    def visitFact_id(self, ctx:AssignmentStatement2Parser.Fact_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#fact_number.
    def visitFact_number(self, ctx:AssignmentStatement2Parser.Fact_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#number_float.
    def visitNumber_float(self, ctx:AssignmentStatement2Parser.Number_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement2Parser#number_int.
    def visitNumber_int(self, ctx:AssignmentStatement2Parser.Number_intContext):
        return self.visitChildren(ctx)



del AssignmentStatement2Parser