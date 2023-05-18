# Generated from /home/loop/Desktop/Ass/Compiler/HW4/ast.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .astParser import astParser
else:
    from astParser import astParser

# This class defines a complete generic visitor for a parse tree produced by astParser.

class astVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by astParser#program.
    def visitProgram(self, ctx:astParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#mainClass.
    def visitMainClass(self, ctx:astParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#mainClassDecl.
    def visitMainClassDecl(self, ctx:astParser.MainClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#mainMethodDecl.
    def visitMainMethodDecl(self, ctx:astParser.MainMethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#mainMethodBody.
    def visitMainMethodBody(self, ctx:astParser.MainMethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#classDecl.
    def visitClassDecl(self, ctx:astParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#varDecl.
    def visitVarDecl(self, ctx:astParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#methodDecl.
    def visitMethodDecl(self, ctx:astParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#methodBody.
    def visitMethodBody(self, ctx:astParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#type.
    def visitType(self, ctx:astParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#statement1.
    def visitStatement1(self, ctx:astParser.Statement1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#if.
    def visitIf(self, ctx:astParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#while.
    def visitWhile(self, ctx:astParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#print.
    def visitPrint(self, ctx:astParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#assignment.
    def visitAssignment(self, ctx:astParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#array_assignment.
    def visitArray_assignment(self, ctx:astParser.Array_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#exp.
    def visitExp(self, ctx:astParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#binOp.
    def visitBinOp(self, ctx:astParser.BinOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by astParser#identifier.
    def visitIdentifier(self, ctx:astParser.IdentifierContext):
        return self.visitChildren(ctx)



del astParser