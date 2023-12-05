# Generated from C:/Users/1379fgh/Documents/Compiler/Assignment4\Threecode.g4 by ANTLR 4.9.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by ThreecodeParser.

class ThreecodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ThreecodeParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#mainClass.
    def visitMainClass(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#mainClassDeclare.
    def visitMainClassDeclare(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#mainMethodDecl.
    def visitMainMethodDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#mainMethodBody.
    def visitMainMethodBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#classDeclare.
    def visitClassDeclare(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#varDeclation.
    def visitVarDeclation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#methodDecl.
    def visitMethodDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#methodBody.
    def visitMethodBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#type.
    def visitType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#statement_if.
    def visitStatement_if(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#statement_lb.
    def visitStatement_lb(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#statement_while.
    def visitStatement_while(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#statement_system.
    def visitStatement_system(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#statement_equalwithbra.
    def visitStatement_equalwithbra(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#statement_equal.
    def visitStatement_equal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#ifst.
    def visitIfst(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#exp.
    def visitExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreecodeParser#binOperator.
    def visitBinOperator(self, ctx):
        return self.visitChildren(ctx)


