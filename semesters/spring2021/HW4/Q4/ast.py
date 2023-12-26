import queue
import networkx as nx

from semesters.spring2021.HW4.gen.Q2Parser import Q2Parser
from semesters.spring2021.HW4.gen.Q2Listener import Q2Listener


# Listener pattern
class ASTListener(Q2Listener):
    def __init__(self):
        self.ast = AST()  # Data structure for holding the abstract syntax tree
        self.q = queue.Queue()  # Use to print and visualize AST
        self.g = nx.DiGraph()  # Use to visualize AST
        # self.q.empty()
        # print('Q=', )

    def print_tree(self, node=None, level=1):
        if node is None:
            print("--------Fenito----------")
            return
        if not self.q.empty():
            print('Parent:', self.q.get().value)
            print('\t' * level, end='')
        # print()
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

    def print_tree2(self, node=None):
        pass

    def exitProgram(self, ctx: Q2Parser.ProgramContext):
        self.print_tree(self.ast.root, 1)

    def exitEqual_statement(self, ctx: Q2Parser.Equal_statementContext):
        idPntr = self.ast.make_node(ctx.Identifier().getText(), None, ctx.expression().value_attr)
        assPntr = self.ast.make_node('=', idPntr, None)
        ctx.value_attr = assPntr
        self.ast.root = assPntr

    # self.print_tree(self.ast.root, 1)

    def exitOperations_expression(self, ctx: Q2Parser.Operations_expressionContext):
        idPntr = self.ast.make_node(ctx.expression(0).value_attr, None, ctx.expression(1).value_attr)
        assPntr = self.ast.make_node(ctx.OP().getText(), idPntr, None)
        ctx.value_attr = assPntr

    def enterWhile_statement(self, ctx: Q2Parser.While_statementContext):
        idPntr = self.ast.make_node(ctx.expression().value_attr, None, ctx.statement().value_attr)
        assPntr = self.ast.make_node('while', idPntr, None)
        ctx.value_attr = assPntr

    def exitKeywords(self, ctx: Q2Parser.KeywordsContext):
        idPntr = self.ast.make_node(ctx.getText(), None, None)
        ctx.value_attr = idPntr

    def exitWord(self, ctx: Q2Parser.WordContext):
        idPntr = self.ast.make_node(ctx.getText(), None, None)
        ctx.value_attr = idPntr

    def exitIf_statement(self, ctx: Q2Parser.If_statementContext):
        idPntr0 = self.ast.make_node(ctx.expression().value_attr, None, None)
        idPntr1 = self.ast.make_node(ctx.statement(0).value_attr, None, None)
        idPntr2 = self.ast.make_node(ctx.statement(1).value_attr, None, None)
        self.ast.add_brother(idPntr0, idPntr1)
        self.ast.add_brother(idPntr1, idPntr2)
        assPntr = self.ast.make_node('if', idPntr0, None)
        ctx.value_attr = assPntr


class TreeNode:
    def __init__(self, value, child, brother):
        self.value = value
        self.child = child
        self.brother = brother

    # def __repr__(self):
    #     return self.value


class AST:
    def __init__(self):
        self.root = None
        self.current = None

    def make_node(self, value, child, brother):
        # value = value + ' ' + repr(round(random.random(), 4))
        tree_node = TreeNode(value, child, brother)
        self.current = tree_node
        return tree_node

    def add_child(self, node, new_child):
        if node.child is None:
            node.child = new_child
        else:
            self.current = node.child
            while self.current.brother is not None:
                self.current = self.current.brother
            self.current.brother = new_child
        self.current = new_child

    def add_brother(self, node, new_brother):
        if node.brother is None:
            node.brother = new_brother
        else:
            self.current = node.brother
            while self.current.brother is not None:
                self.current = self.current.brother
            self.current.brother = new_brother
        self.current = new_brother
