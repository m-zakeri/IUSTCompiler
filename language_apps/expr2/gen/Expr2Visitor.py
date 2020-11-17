# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars\Expr2.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Expr2Parser import Expr2Parser
else:
    from Expr2Parser import Expr2Parser

# This class defines a complete generic visitor for a parse tree produced by Expr2Parser.

class Expr2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Expr2Parser#start.
    def visitStart(self, ctx:Expr2Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2Parser#expr3.
    def visitExpr3(self, ctx:Expr2Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2Parser#expr2.
    def visitExpr2(self, ctx:Expr2Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2Parser#expr1.
    def visitExpr1(self, ctx:Expr2Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2Parser#term2.
    def visitTerm2(self, ctx:Expr2Parser.Term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2Parser#term3.
    def visitTerm3(self, ctx:Expr2Parser.Term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2Parser#term1.
    def visitTerm1(self, ctx:Expr2Parser.Term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2Parser#fact1.
    def visitFact1(self, ctx:Expr2Parser.Fact1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2Parser#fact2.
    def visitFact2(self, ctx:Expr2Parser.Fact2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2Parser#fact3.
    def visitFact3(self, ctx:Expr2Parser.Fact3Context):
        return self.visitChildren(ctx)



del Expr2Parser