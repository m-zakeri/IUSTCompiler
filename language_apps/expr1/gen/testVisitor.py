# Generated from D:/AnacondaProjects/iust_start/grammars\expr3.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .testParser import testParser
else:
    from testParser import testParser

# This class defines a complete generic visitor for a parse tree produced by testParser.

class testVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by testParser#start.
    def visitStart(self, ctx:testParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#rule_minus.
    def visitRule_minus(self, ctx:testParser.Rule_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#rule_plus.
    def visitRule_plus(self, ctx:testParser.Rule_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#rule3.
    def visitRule3(self, ctx:testParser.Rule3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#term.
    def visitTerm(self, ctx:testParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#fact.
    def visitFact(self, ctx:testParser.FactContext):
        return self.visitChildren(ctx)



del testParser