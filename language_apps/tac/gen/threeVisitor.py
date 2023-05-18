# Generated from /home/loop/Desktop/Ass/Compiler/HW4/three.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .threeParser import threeParser
else:
    from threeParser import threeParser

# This class defines a complete generic visitor for a parse tree produced by threeParser.

class threeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by threeParser#program.
    def visitProgram(self, ctx:threeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#mainClass.
    def visitMainClass(self, ctx:threeParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#mainClassDecl.
    def visitMainClassDecl(self, ctx:threeParser.MainClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#mainMethodDecl.
    def visitMainMethodDecl(self, ctx:threeParser.MainMethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#mainMethodBody.
    def visitMainMethodBody(self, ctx:threeParser.MainMethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#classDecl.
    def visitClassDecl(self, ctx:threeParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#varDecl.
    def visitVarDecl(self, ctx:threeParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#methodDecl.
    def visitMethodDecl(self, ctx:threeParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#methodDeclName.
    def visitMethodDeclName(self, ctx:threeParser.MethodDeclNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#methodParam.
    def visitMethodParam(self, ctx:threeParser.MethodParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#methodBody.
    def visitMethodBody(self, ctx:threeParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#type.
    def visitType(self, ctx:threeParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#statement.
    def visitStatement(self, ctx:threeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#whileCondition.
    def visitWhileCondition(self, ctx:threeParser.WhileConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#whileSt.
    def visitWhileSt(self, ctx:threeParser.WhileStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#ifCondition.
    def visitIfCondition(self, ctx:threeParser.IfConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#elseSt.
    def visitElseSt(self, ctx:threeParser.ElseStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#exp.
    def visitExp(self, ctx:threeParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#methodInvocParams.
    def visitMethodInvocParams(self, ctx:threeParser.MethodInvocParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#binOp.
    def visitBinOp(self, ctx:threeParser.BinOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by threeParser#identifier.
    def visitIdentifier(self, ctx:threeParser.IdentifierContext):
        return self.visitChildren(ctx)



del threeParser