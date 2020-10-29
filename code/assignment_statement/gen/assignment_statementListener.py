# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars\assignment_statement.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .assignment_statementParser import assignment_statementParser
else:
    from assignment_statementParser import assignment_statementParser

# This class defines a complete listener for a parse tree produced by assignment_statementParser.
class assignment_statementListener(ParseTreeListener):

    # Enter a parse tree produced by assignment_statementParser#ass.
    def enterAss(self, ctx:assignment_statementParser.AssContext):
        pass

    # Exit a parse tree produced by assignment_statementParser#ass.
    def exitAss(self, ctx:assignment_statementParser.AssContext):
        pass


    # Enter a parse tree produced by assignment_statementParser#expr.
    def enterExpr(self, ctx:assignment_statementParser.ExprContext):
        pass

    # Exit a parse tree produced by assignment_statementParser#expr.
    def exitExpr(self, ctx:assignment_statementParser.ExprContext):
        pass


    # Enter a parse tree produced by assignment_statementParser#term.
    def enterTerm(self, ctx:assignment_statementParser.TermContext):
        pass

    # Exit a parse tree produced by assignment_statementParser#term.
    def exitTerm(self, ctx:assignment_statementParser.TermContext):
        pass


    # Enter a parse tree produced by assignment_statementParser#factor.
    def enterFactor(self, ctx:assignment_statementParser.FactorContext):
        pass

    # Exit a parse tree produced by assignment_statementParser#factor.
    def exitFactor(self, ctx:assignment_statementParser.FactorContext):
        pass


    # Enter a parse tree produced by assignment_statementParser#number.
    def enterNumber(self, ctx:assignment_statementParser.NumberContext):
        pass

    # Exit a parse tree produced by assignment_statementParser#number.
    def exitNumber(self, ctx:assignment_statementParser.NumberContext):
        pass



del assignment_statementParser