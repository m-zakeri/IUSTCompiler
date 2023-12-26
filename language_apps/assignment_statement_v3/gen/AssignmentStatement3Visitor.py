# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars/AssignmentStatement3.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AssignmentStatement3Parser import AssignmentStatement3Parser
else:
    from AssignmentStatement3Parser import AssignmentStatement3Parser

# This class defines a complete generic visitor for a parse tree produced by AssignmentStatement3Parser.

class AssignmentStatement3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by AssignmentStatement3Parser#start.
    def visitStart(self, ctx:AssignmentStatement3Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement3Parser#prog.
    def visitProg(self, ctx:AssignmentStatement3Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement3Parser#assign.
    def visitAssign(self, ctx:AssignmentStatement3Parser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement3Parser#expr.
    def visitExpr(self, ctx:AssignmentStatement3Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement3Parser#term.
    def visitTerm(self, ctx:AssignmentStatement3Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement3Parser#factor.
    def visitFactor(self, ctx:AssignmentStatement3Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement3Parser#number.
    def visitNumber(self, ctx:AssignmentStatement3Parser.NumberContext):
        return self.visitChildren(ctx)



del AssignmentStatement3Parser