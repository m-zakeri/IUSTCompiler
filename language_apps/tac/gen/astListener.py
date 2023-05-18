# Generated from /home/loop/Desktop/Ass/Compiler/HW4/ast.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .astParser import astParser
else:
    from astParser import astParser

# This class defines a complete listener for a parse tree produced by astParser.
class astListener(ParseTreeListener):

    # Enter a parse tree produced by astParser#program.
    def enterProgram(self, ctx:astParser.ProgramContext):
        pass

    # Exit a parse tree produced by astParser#program.
    def exitProgram(self, ctx:astParser.ProgramContext):
        pass


    # Enter a parse tree produced by astParser#mainClass.
    def enterMainClass(self, ctx:astParser.MainClassContext):
        pass

    # Exit a parse tree produced by astParser#mainClass.
    def exitMainClass(self, ctx:astParser.MainClassContext):
        pass


    # Enter a parse tree produced by astParser#mainClassDecl.
    def enterMainClassDecl(self, ctx:astParser.MainClassDeclContext):
        pass

    # Exit a parse tree produced by astParser#mainClassDecl.
    def exitMainClassDecl(self, ctx:astParser.MainClassDeclContext):
        pass


    # Enter a parse tree produced by astParser#mainMethodDecl.
    def enterMainMethodDecl(self, ctx:astParser.MainMethodDeclContext):
        pass

    # Exit a parse tree produced by astParser#mainMethodDecl.
    def exitMainMethodDecl(self, ctx:astParser.MainMethodDeclContext):
        pass


    # Enter a parse tree produced by astParser#mainMethodBody.
    def enterMainMethodBody(self, ctx:astParser.MainMethodBodyContext):
        pass

    # Exit a parse tree produced by astParser#mainMethodBody.
    def exitMainMethodBody(self, ctx:astParser.MainMethodBodyContext):
        pass


    # Enter a parse tree produced by astParser#classDecl.
    def enterClassDecl(self, ctx:astParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by astParser#classDecl.
    def exitClassDecl(self, ctx:astParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by astParser#varDecl.
    def enterVarDecl(self, ctx:astParser.VarDeclContext):
        pass

    # Exit a parse tree produced by astParser#varDecl.
    def exitVarDecl(self, ctx:astParser.VarDeclContext):
        pass


    # Enter a parse tree produced by astParser#methodDecl.
    def enterMethodDecl(self, ctx:astParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by astParser#methodDecl.
    def exitMethodDecl(self, ctx:astParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by astParser#methodBody.
    def enterMethodBody(self, ctx:astParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by astParser#methodBody.
    def exitMethodBody(self, ctx:astParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by astParser#type.
    def enterType(self, ctx:astParser.TypeContext):
        pass

    # Exit a parse tree produced by astParser#type.
    def exitType(self, ctx:astParser.TypeContext):
        pass


    # Enter a parse tree produced by astParser#statement1.
    def enterStatement1(self, ctx:astParser.Statement1Context):
        pass

    # Exit a parse tree produced by astParser#statement1.
    def exitStatement1(self, ctx:astParser.Statement1Context):
        pass


    # Enter a parse tree produced by astParser#if.
    def enterIf(self, ctx:astParser.IfContext):
        pass

    # Exit a parse tree produced by astParser#if.
    def exitIf(self, ctx:astParser.IfContext):
        pass


    # Enter a parse tree produced by astParser#while.
    def enterWhile(self, ctx:astParser.WhileContext):
        pass

    # Exit a parse tree produced by astParser#while.
    def exitWhile(self, ctx:astParser.WhileContext):
        pass


    # Enter a parse tree produced by astParser#print.
    def enterPrint(self, ctx:astParser.PrintContext):
        pass

    # Exit a parse tree produced by astParser#print.
    def exitPrint(self, ctx:astParser.PrintContext):
        pass


    # Enter a parse tree produced by astParser#assignment.
    def enterAssignment(self, ctx:astParser.AssignmentContext):
        pass

    # Exit a parse tree produced by astParser#assignment.
    def exitAssignment(self, ctx:astParser.AssignmentContext):
        pass


    # Enter a parse tree produced by astParser#array_assignment.
    def enterArray_assignment(self, ctx:astParser.Array_assignmentContext):
        pass

    # Exit a parse tree produced by astParser#array_assignment.
    def exitArray_assignment(self, ctx:astParser.Array_assignmentContext):
        pass


    # Enter a parse tree produced by astParser#exp.
    def enterExp(self, ctx:astParser.ExpContext):
        pass

    # Exit a parse tree produced by astParser#exp.
    def exitExp(self, ctx:astParser.ExpContext):
        pass


    # Enter a parse tree produced by astParser#binOp.
    def enterBinOp(self, ctx:astParser.BinOpContext):
        pass

    # Exit a parse tree produced by astParser#binOp.
    def exitBinOp(self, ctx:astParser.BinOpContext):
        pass


    # Enter a parse tree produced by astParser#identifier.
    def enterIdentifier(self, ctx:astParser.IdentifierContext):
        pass

    # Exit a parse tree produced by astParser#identifier.
    def exitIdentifier(self, ctx:astParser.IdentifierContext):
        pass



del astParser