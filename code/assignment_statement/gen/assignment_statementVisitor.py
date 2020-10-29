# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars\assignment_statement.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .assignment_statementParser import assignment_statementParser
else:
    from assignment_statementParser import assignment_statementParser

# This class defines a complete generic visitor for a parse tree produced by assignment_statementParser.

class assignment_statementVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by assignment_statementParser#ass.
    def visitAss(self, ctx:assignment_statementParser.AssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by assignment_statementParser#expr.
    def visitExpr(self, ctx:assignment_statementParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by assignment_statementParser#term.
    def visitTerm(self, ctx:assignment_statementParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by assignment_statementParser#factor.
    def visitFactor(self, ctx:assignment_statementParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by assignment_statementParser#number.
    def visitNumber(self, ctx:assignment_statementParser.NumberContext):
        return self.visitChildren(ctx)



del assignment_statementParser