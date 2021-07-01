import queue
import networkx as nx

from gen.MJavaParser import MJavaParser
from gen.MJavaLex import MJavaLex
from gen.MJavaParserListener import MJavaParserListener
from antlr4 import *


# Listener pattern
class ASTListener(MJavaParserListener):
    def __init__(self):
        self.ast = AST() # Data structure for holding the abstract syntax tree
        self.q = queue.Queue()  # Use to print and visualize AST
        self.g = nx.DiGraph()  # Use to visualize AST
        # self.q.empty()
        # print('Q=', )

    def print_tree(self, node=None, level=1):
        if node is None:
            # print()
            return
        # if not self.q.empty():
        #     print('Parent:', self.q.get().value)
        # print('\t'*level, end='')
        print()
        while node is not None:
            current_node = node
            print(current_node.value, end='')  # alt+196 = ───, alt+178=▓
            if node.child is not None:
                # self.q.put(node)
                self.g.add_edge(current_node, node.child, edge_type='C', color='r')
                self.q.put(node.child)
            else:
                tn = TreeNode(value='▓', child=None, brother=None)
                self.g.add_edge(current_node, tn, edge_type='C', color='r')
            node = node.brother
            if node is not None:
                print('\t───\t', end='')
                self.g.add_edge(current_node, node, edge_type='B', color='b')
            else:
                tn = TreeNode(value='▓', child=None, brother=None)
                self.g.add_edge(current_node, tn, edge_type='B', color='b')

        if not self.q.empty():
            self.print_tree(node=self.q.get(), level=level+1)

    def print_tree2(self, node=None):
        pass

    def exitAssign(self, ctx: MJavaParser.AssignContext):
        idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=ctx.expr().value_attr)
        assPntr = self.ast.make_node(value=":=", child=idPntr, brother=None)
        ctx.value_attr = assPntr
        self.ast.root = assPntr
        self.print_tree(node=self.ast.root, level=1)

    def exitExpr_term_plus(self, ctx: MJavaParser.Expr_term_plusContext):
        self.ast.add_brother(ctx.expr().value_attr, ctx.term().value_attr)
        exprPntr = self.ast.make_node(value="+", child=ctx.expr().value_attr, brother=None)
        ctx.value_attr = exprPntr

    def exitExpr_term_minus(self, ctx: MJavaParser.Expr_term_plusContext):
        self.ast.add_brother(ctx.expr().value_attr, ctx.term().value_attr)
        exprPntr = self.ast.make_node(value="-", child=ctx.expr().value_attr, brother=None)
        ctx.value_attr = exprPntr

    def exitTerm4(self, ctx: MJavaParser.Term4Context):
        ctx.value_attr = ctx.term().value_attr

    # ----------------------
    def exitTerm_fact_mutiply(self, ctx: MJavaParser.Term_fact_mutiplyContext):
        self.ast.add_brother(ctx.term().value_attr, ctx.factor().value_attr)
        termPntr = self.ast.make_node(value="*", child=ctx.term().value_attr, brother=None)
        ctx.value_attr = termPntr

    def exitTerm_fact_divide(self, ctx: MJavaParser.Term_fact_divideContext):
        self.ast.add_brother(ctx.term().value_attr, ctx.factor().value_attr)
        termPntr = self.ast.make_node(value="/", child=ctx.term().value_attr, brother=None)
        ctx.value_attr = termPntr

    def exitFactor3(self, ctx: MJavaParser.Factor3Context):
        ctx.value_attr = ctx.factor().value_attr

    # ---------------------
    def exitFact_expr(self, ctx: MJavaParser.Fact_exprContext):
        ctx.value_attr = ctx.expr().value_attr

    def exitFact_id(self, ctx: MJavaParser.Fact_idContext):
        idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=None)
        ctx.value_attr = idPntr

    def exitFact_number(self, ctx: MJavaParser.Fact_numberContext):
        ctx.value_attr = ctx.number().value_attr

    # ----------------------
    def exitNumber_float(self, ctx: MJavaParser.Number_floatContext):
        numberPntr = self.ast.make_node(value=ctx.FLOAT().getText(), child=None, brother=None)
        ctx.value_attr = numberPntr

    def exitNumber_int(self, ctx: MJavaParser.Number_intContext):
        numberPntr = self.ast.make_node(value=ctx.INT().getText(), child=None, brother=None)
        ctx.value_attr = numberPntr


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
