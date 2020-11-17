# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars\AssignmentStatement1.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AssignmentStatement1Parser import AssignmentStatement1Parser
else:
    from AssignmentStatement1Parser import AssignmentStatement1Parser

# This class defines a complete generic visitor for a parse tree produced by AssignmentStatement1Parser.

class AssignmentStatement1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by AssignmentStatement1Parser#start.
    def visitStart(self, ctx:AssignmentStatement1Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement1Parser#prog.
    def visitProg(self, ctx:AssignmentStatement1Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement1Parser#assign.
    def visitAssign(self, ctx:AssignmentStatement1Parser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement1Parser#expr.
    def visitExpr(self, ctx:AssignmentStatement1Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement1Parser#term.
    def visitTerm(self, ctx:AssignmentStatement1Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement1Parser#factor.
    def visitFactor(self, ctx:AssignmentStatement1Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement1Parser#number.
    def visitNumber(self, ctx:AssignmentStatement1Parser.NumberContext):
        return self.visitChildren(ctx)



del AssignmentStatement1Parser