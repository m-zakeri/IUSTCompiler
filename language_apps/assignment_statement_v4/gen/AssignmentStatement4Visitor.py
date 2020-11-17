# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars\AssignmentStatement4.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AssignmentStatement4Parser import AssignmentStatement4Parser
else:
    from AssignmentStatement4Parser import AssignmentStatement4Parser

# This class defines a complete generic visitor for a parse tree produced by AssignmentStatement4Parser.

class AssignmentStatement4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by AssignmentStatement4Parser#start.
    def visitStart(self, ctx:AssignmentStatement4Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement4Parser#prog.
    def visitProg(self, ctx:AssignmentStatement4Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement4Parser#assign.
    def visitAssign(self, ctx:AssignmentStatement4Parser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement4Parser#expr.
    def visitExpr(self, ctx:AssignmentStatement4Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement4Parser#term.
    def visitTerm(self, ctx:AssignmentStatement4Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement4Parser#factor.
    def visitFactor(self, ctx:AssignmentStatement4Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssignmentStatement4Parser#number.
    def visitNumber(self, ctx:AssignmentStatement4Parser.NumberContext):
        return self.visitChildren(ctx)



del AssignmentStatement4Parser