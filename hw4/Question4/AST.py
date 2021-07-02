from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gen.MinijavaParser import MinijavaParser
else:
    from gen.MinijavaParser import MinijavaParser
import  queue
from  gen.MinijavaListener import MinijavaListener
class TreeNode:
    def __init__(self, value, child, brother):
        self.value = value
        self.child = child
        self.brother = brother

class ASTListener(MinijavaListener):

    def __init__(self):
        self.ast = AST()
        self.q = queue.Queue()

    def exitStart(self, ctx: MinijavaParser.StartContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#mainClass.
        # Exit a parse tree produced by MinijavaParser#mainClass.

    def exitMainClass(self, ctx: MinijavaParser.MainClassContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#classDeclaration.
      # Exit a parse tree produced by MinijavaParser#classDeclaration.

    def exitClassDeclaration(self, ctx: MinijavaParser.ClassDeclarationContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#varDeclaration.

        # Exit a parse tree produced by MinijavaParser#varDeclaration.

    def exitVarDeclaration(self, ctx: MinijavaParser.VarDeclarationContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#methodDeclaration.

        # Exit a parse tree produced by MinijavaParser#methodDeclaration.

    def exitMethodDeclaration(self, ctx: MinijavaParser.MethodDeclarationContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#typ_int.


    def exitTyp_int(self, ctx: MinijavaParser.Typ_intContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#typ_int_array.
        # Exit a parse tree produced by MinijavaParser#typ_int_array.

    def exitTyp_int_array(self, ctx: MinijavaParser.Typ_int_arrayContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#typ_boolean.

    def exitTyp_boolean(self, ctx: MinijavaParser.Typ_booleanContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr
      # Exit a parse tree produced by MinijavaParser#typ_identifier.

    def exitTyp_identifier(self, ctx: MinijavaParser.Typ_identifierContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr


    def exitStatement_1(self, ctx: MinijavaParser.Statement_1Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr


    def exitStatement_2(self, ctx: MinijavaParser.Statement_2Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Exit a parse tree produced by MinijavaParser#statement_3.

    def exitStatement_3(self, ctx: MinijavaParser.Statement_3Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#statement_4.


    def exitStatement_4(self, ctx: MinijavaParser.Statement_4Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#statement_5.

    def exitStatement_5(self, ctx: MinijavaParser.Statement_5Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#statement_6.

    def exitStatement_6(self, ctx: MinijavaParser.Statement_6Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_13.
    def exitExpression_13(self, ctx: MinijavaParser.Expression_13Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_12.

    def exitExpression_12(self, ctx: MinijavaParser.Expression_12Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_2.

    def exitExpression_2(self, ctx: MinijavaParser.Expression_2Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_1.

    def exitExpression_1(self, ctx: MinijavaParser.Expression_1Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_4.

    def exitExpression_4(self, ctx: MinijavaParser.Expression_4Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_3.

        # Exit a parse tree produced by MinijavaParser#expression_3.

    def exitExpression_3(self, ctx: MinijavaParser.Expression_3Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_6.


    def exitExpression_6(self, ctx: MinijavaParser.Expression_6Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_11.


    def exitExpression_11(self, ctx: MinijavaParser.Expression_11Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_5.
    def exitExpression_5(self, ctx: MinijavaParser.Expression_5Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_10.
    def exitExpression_10(self, ctx: MinijavaParser.Expression_10Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_8.

    def exitExpression_8(self, ctx: MinijavaParser.Expression_8Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#expression_7.

    def exitExpression_7(self, ctx: MinijavaParser.Expression_7Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Exit a parse tree produced by MinijavaParser#expression_9.

    def exitExpression_9(self, ctx: MinijavaParser.Expression_9Context):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

    def exitParam(self, ctx: MinijavaParser.ParamContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#binaryOperator_and.

    def exitBinaryOperator_and(self, ctx: MinijavaParser.BinaryOperator_andContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#binaryOperator_smaller.

    def exitBinaryOperator_smaller(self, ctx: MinijavaParser.BinaryOperator_smallerContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

    def exitBinaryOperator_plus(self, ctx: MinijavaParser.BinaryOperator_plusContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#binaryOperator_minus.

    def exitBinaryOperator_minus(self, ctx: MinijavaParser.BinaryOperator_minusContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Exit a parse tree produced by MinijavaParser#binaryOperator_multiple.

    def exitBinaryOperator_multiple(self, ctx: MinijavaParser.BinaryOperator_multipleContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

        # Enter a parse tree produced by MinijavaParser#identifier.

    def exitIdentifier(self, ctx: MinijavaParser.IdentifierContext):
        idPntr = self.ast.makeNode(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = idPntr

    def print_tree(self, node=None, level=1):
        if node is None:
            print("--------Fenito----------")
            return
        if not self.q.empty():
            print('Parent:', self.q.get().value)
            print('\t'*level, end='')
        while node is not None:
            print(node.value, '\t───\t', end='')  # alt+196 = ───, alt+178=▓
            if node.child is not None:
                self.q.put(node.child)
                self.q.put(node)
            node = node.brother
            if node is None:
                print('▓', end='\n')
        if not self.q.empty():
            self.print_tree(node=self.q.get(), level=level + 1)

class AST:
    def __init__(self):
        self.root = None
        self.current = None

    def makeNode(self, value, child, brother):
        tree_node = TreeNode(value, child, brother)
        if self.root is None:
            self.root = tree_node
            self.current = tree_node
        return tree_node

    def addChild(self, node, new_child):
        if node.child is None:
            node.child = new_child
        else:
            self.current = node.child
            while self.current.brother is not None:
                self.current = self.current.brother
            self.current.brother = new_child
        self.current = new_child

    def addBrother(self, node, new_brother):
        if node.brother is None:
            node.brother = new_brother
        else:
            self.current = node.brother
            while self.current.brother is not None:
                self.current = self.current.brother
            self.current.brother = new_brother
        self.current = new_brother
