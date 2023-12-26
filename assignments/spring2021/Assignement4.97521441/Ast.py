import queue
import random
import json

import networkx as nx

from antlr4 import *
from gen1.AssignmentStAss4Listener import AssignmentStAss4Listener
from gen1.AssignmentStAss4Visitor import AssignmentStAss4Visitor
from gen1.AssignmentStAss4Parser import AssignmentStAss4Parser
# ----------------------
from antlr4 import *

class ASTListener(AssignmentStAss4Listener):
    def __init__(self):
        self.ast = AST()
        self.q = queue.Queue()
        self.g = nx.DiGraph()

    def exitStatement_equl(self, ctx: AssignmentStAss4Parser.Statement_equalContext):
        idPntr = self.ast.makeNode(value=ctx.identifier().getText(), child=None, brother=ctx.exp().value_attr)
        assPntr = self.ast.makeNode(value="=", child=idPntr, brother=None)
        ctx.value_attr = assPntr
        self.ast.root = assPntr
        self.print_tree(self.ast.root, 1)

    def exitExp_sum(self, ctx:AssignmentStAss4Parser.Exp_sumContext):
        self.ast.addBrother(ctx.exp().value_atr, ctx.exp.value_attr)
        exprPntr = self.ast.makeNode(value="+", child=ctx.exp().value_attr,brother=None)
        ctx.value_attr = exprPntr


    def exitExp_minus(self, ctx:AssignmentStAss4Parser.Exp_minusContext):
            self.ast.addBrother(ctx.exp().value_atr, ctx.exp.value_attr)
            exprPntr = self.ast.makeNode(value="-", child=ctx.exp().value_attr, brother=None)
            ctx.value_attr = exprPntr
    def exitIfst(self, ctx:AssignmentStAss4Parser.IfstContext):
        self.ast.add_brother(ctx.exp().value_attr, ctx.statement(0).value_attr)
        if ctx.getChildCount() > 4 :
            self.ast.add_bذrother(ctx.statement(0).value_attr, ctx.statement(1).value_attr)
        ifPntr = self.ast.make_node(value="if", child=ctx.exp().value_attr, brother=None)
        ctx.value_attr = ifPntr
        self.ast.root = ifPntr
    def exitExp_gt(self, ctx:AssignmentStAss4Parser.Exp_gtContext):
        self.ast.add_brother(ctx.exp(0).value_attr, ctx.exp(1).value_attr)
        condPntr = self.ast.make_node(value=">", child=ctx.exp(0).value_attr, brother=None)
        ctx.value_attr = condPntr
        self.ast.root = condPntr
    def print_tree(self, node=None, level=1):
        if node is None:
            print("--------Fenito----------")
            return
        if not self.q.empty():
            print('Parent:', self.q.get().value)
            print('\t' * level, end='')
        #           print()
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

class treeNode:
        def __init__(self, value, child, brother):
            self.value = value
            self.child = child
            self.brother = brother

class AST:
        def __init__(self):
            self.root = None
            self.current = None

        def makeNode(self, value, child, brother):
            tree_node = treeNode(value, child, brother)
            # if self.root is None:
            #    self.root = tree_node
            self.current = tree_node
            return tree_node

        def addChild(self, node, new_child):
            if node.child is None:
                node.child = new_child
            else:
                self.current = node.child
                while (self.current.brother) is not None:
                    self.current = self.current.brother
                self.current.brother = new_child
            self.current = new_child

        def addBrother(self, node, new_brother):
            if node.brother is None:
                node.brother = new_brother
            else:
                self.current = node.brother
                while (self.current.brother) is not None:
                    self.current = self.current.brother
                self.current.brother = new_brother
            self.current = new_brother




