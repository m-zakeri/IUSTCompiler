# Generated from C:/Users/novin/PycharmProjects/tamrin-compiler\Assignment4q4.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Assignment4q4Parser import Assignment4q4Parser
else:
    from Assignment4q4Parser import Assignment4q4Parser

# This class defines a complete generic visitor for a parse tree produced by Assignment4q4Parser.

class Assignment4q4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Assignment4q4Parser#program.
    def visitProgram(self, ctx:Assignment4q4Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#mainClass.
    def visitMainClass(self, ctx:Assignment4q4Parser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#classDeclaration.
    def visitClassDeclaration(self, ctx:Assignment4q4Parser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#varDeclaration.
    def visitVarDeclaration(self, ctx:Assignment4q4Parser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:Assignment4q4Parser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#typeint0.
    def visitTypeint0(self, ctx:Assignment4q4Parser.Typeint0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#boolean.
    def visitBoolean(self, ctx:Assignment4q4Parser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#typeint.
    def visitTypeint(self, ctx:Assignment4q4Parser.TypeintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#typeid.
    def visitTypeid(self, ctx:Assignment4q4Parser.TypeidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#st0.
    def visitSt0(self, ctx:Assignment4q4Parser.St0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#st1.
    def visitSt1(self, ctx:Assignment4q4Parser.St1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#st2.
    def visitSt2(self, ctx:Assignment4q4Parser.St2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#st3.
    def visitSt3(self, ctx:Assignment4q4Parser.St3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#st4.
    def visitSt4(self, ctx:Assignment4q4Parser.St4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#st5.
    def visitSt5(self, ctx:Assignment4q4Parser.St5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp9.
    def visitExp9(self, ctx:Assignment4q4Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp8.
    def visitExp8(self, ctx:Assignment4q4Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp7.
    def visitExp7(self, ctx:Assignment4q4Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp6.
    def visitExp6(self, ctx:Assignment4q4Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp5.
    def visitExp5(self, ctx:Assignment4q4Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp4.
    def visitExp4(self, ctx:Assignment4q4Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp12.
    def visitExp12(self, ctx:Assignment4q4Parser.Exp12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp3.
    def visitExp3(self, ctx:Assignment4q4Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp11.
    def visitExp11(self, ctx:Assignment4q4Parser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp2.
    def visitExp2(self, ctx:Assignment4q4Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp10.
    def visitExp10(self, ctx:Assignment4q4Parser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp1.
    def visitExp1(self, ctx:Assignment4q4Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#exp0.
    def visitExp0(self, ctx:Assignment4q4Parser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assignment4q4Parser#identifier.
    def visitIdentifier(self, ctx:Assignment4q4Parser.IdentifierContext):
        return self.visitChildren(ctx)



del Assignment4q4Parser