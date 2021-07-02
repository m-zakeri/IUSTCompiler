# Generated from /home/loop/Desktop/Ass/Compiler/HW4/three.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .threeParser import threeParser
else:
    from threeParser import threeParser

# This class defines a complete listener for a parse tree produced by threeParser.
class threeListener(ParseTreeListener):

    # Enter a parse tree produced by threeParser#program.
    def enterProgram(self, ctx:threeParser.ProgramContext):
        pass

    # Exit a parse tree produced by threeParser#program.
    def exitProgram(self, ctx:threeParser.ProgramContext):
        pass


    # Enter a parse tree produced by threeParser#mainClass.
    def enterMainClass(self, ctx:threeParser.MainClassContext):
        pass

    # Exit a parse tree produced by threeParser#mainClass.
    def exitMainClass(self, ctx:threeParser.MainClassContext):
        pass


    # Enter a parse tree produced by threeParser#mainClassDecl.
    def enterMainClassDecl(self, ctx:threeParser.MainClassDeclContext):
        pass

    # Exit a parse tree produced by threeParser#mainClassDecl.
    def exitMainClassDecl(self, ctx:threeParser.MainClassDeclContext):
        pass


    # Enter a parse tree produced by threeParser#mainMethodDecl.
    def enterMainMethodDecl(self, ctx:threeParser.MainMethodDeclContext):
        pass

    # Exit a parse tree produced by threeParser#mainMethodDecl.
    def exitMainMethodDecl(self, ctx:threeParser.MainMethodDeclContext):
        pass


    # Enter a parse tree produced by threeParser#mainMethodBody.
    def enterMainMethodBody(self, ctx:threeParser.MainMethodBodyContext):
        pass

    # Exit a parse tree produced by threeParser#mainMethodBody.
    def exitMainMethodBody(self, ctx:threeParser.MainMethodBodyContext):
        pass


    # Enter a parse tree produced by threeParser#classDecl.
    def enterClassDecl(self, ctx:threeParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by threeParser#classDecl.
    def exitClassDecl(self, ctx:threeParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by threeParser#varDecl.
    def enterVarDecl(self, ctx:threeParser.VarDeclContext):
        pass

    # Exit a parse tree produced by threeParser#varDecl.
    def exitVarDecl(self, ctx:threeParser.VarDeclContext):
        pass


    # Enter a parse tree produced by threeParser#methodDecl.
    def enterMethodDecl(self, ctx:threeParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by threeParser#methodDecl.
    def exitMethodDecl(self, ctx:threeParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by threeParser#methodDeclName.
    def enterMethodDeclName(self, ctx:threeParser.MethodDeclNameContext):
        pass

    # Exit a parse tree produced by threeParser#methodDeclName.
    def exitMethodDeclName(self, ctx:threeParser.MethodDeclNameContext):
        pass


    # Enter a parse tree produced by threeParser#methodParam.
    def enterMethodParam(self, ctx:threeParser.MethodParamContext):
        pass

    # Exit a parse tree produced by threeParser#methodParam.
    def exitMethodParam(self, ctx:threeParser.MethodParamContext):
        pass


    # Enter a parse tree produced by threeParser#methodBody.
    def enterMethodBody(self, ctx:threeParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by threeParser#methodBody.
    def exitMethodBody(self, ctx:threeParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by threeParser#type.
    def enterType(self, ctx:threeParser.TypeContext):
        pass

    # Exit a parse tree produced by threeParser#type.
    def exitType(self, ctx:threeParser.TypeContext):
        pass


    # Enter a parse tree produced by threeParser#statement.
    def enterStatement(self, ctx:threeParser.StatementContext):
        pass

    # Exit a parse tree produced by threeParser#statement.
    def exitStatement(self, ctx:threeParser.StatementContext):
        pass


    # Enter a parse tree produced by threeParser#whileCondition.
    def enterWhileCondition(self, ctx:threeParser.WhileConditionContext):
        pass

    # Exit a parse tree produced by threeParser#whileCondition.
    def exitWhileCondition(self, ctx:threeParser.WhileConditionContext):
        pass


    # Enter a parse tree produced by threeParser#whileSt.
    def enterWhileSt(self, ctx:threeParser.WhileStContext):
        pass

    # Exit a parse tree produced by threeParser#whileSt.
    def exitWhileSt(self, ctx:threeParser.WhileStContext):
        pass


    # Enter a parse tree produced by threeParser#ifCondition.
    def enterIfCondition(self, ctx:threeParser.IfConditionContext):
        pass

    # Exit a parse tree produced by threeParser#ifCondition.
    def exitIfCondition(self, ctx:threeParser.IfConditionContext):
        pass


    # Enter a parse tree produced by threeParser#elseSt.
    def enterElseSt(self, ctx:threeParser.ElseStContext):
        pass

    # Exit a parse tree produced by threeParser#elseSt.
    def exitElseSt(self, ctx:threeParser.ElseStContext):
        pass


    # Enter a parse tree produced by threeParser#exp.
    def enterExp(self, ctx:threeParser.ExpContext):
        pass

    # Exit a parse tree produced by threeParser#exp.
    def exitExp(self, ctx:threeParser.ExpContext):
        pass


    # Enter a parse tree produced by threeParser#methodInvocParams.
    def enterMethodInvocParams(self, ctx:threeParser.MethodInvocParamsContext):
        pass

    # Exit a parse tree produced by threeParser#methodInvocParams.
    def exitMethodInvocParams(self, ctx:threeParser.MethodInvocParamsContext):
        pass


    # Enter a parse tree produced by threeParser#binOp.
    def enterBinOp(self, ctx:threeParser.BinOpContext):
        pass

    # Exit a parse tree produced by threeParser#binOp.
    def exitBinOp(self, ctx:threeParser.BinOpContext):
        pass


    # Enter a parse tree produced by threeParser#identifier.
    def enterIdentifier(self, ctx:threeParser.IdentifierContext):
        pass

    # Exit a parse tree produced by threeParser#identifier.
    def exitIdentifier(self, ctx:threeParser.IdentifierContext):
        pass



del threeParser