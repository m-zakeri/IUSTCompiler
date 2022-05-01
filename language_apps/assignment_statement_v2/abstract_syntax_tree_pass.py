"""
ANTLR 4.x listener and visitor implementation for intermediate code generation (abstract syntax trees)

@author: Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)
@date: 20201117

- Compiler generator:   ANTRL4.x
- Target language(s):   Python3.x,


-Changelog:
-- v2.1.0
--- Add support for AST visualization with dummy nodes
--- Add support for AST intermediate representation using module `ast_pass`
--- Change `compiler_pass` module to `three_address_code_pass`
-- v2.0.0
--- Add attributes for grammar rules which are used to hold type and intermediate language_apps of rules.

- Reference: Compiler book by Dr. Saeed Parsa (http://parsa.iust.ac.ir/)
- Course website:   http://parsa.iust.ac.ir/courses/compilers/
- Laboratory website:   http://reverse.iust.ac.ir/


"""

__version__ = '2.1.0'
__author__ = 'Morteza'

import queue
import networkx as nx

from antlr4 import *
from language_apps.assignment_statement_v2.gen.AssignmentStatement2Listener import AssignmentStatement2Listener
from language_apps.assignment_statement_v2.gen.AssignmentStatement2Visitor import AssignmentStatement2Visitor
from language_apps.assignment_statement_v2.gen.AssignmentStatement2Parser import AssignmentStatement2Parser


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


# ----------------------
# Listener pattern
class ASTListener(AssignmentStatement2Listener):
    """

    """
    def __init__(self):
        self.ast = AST()  # Data structure for holding the abstract syntax tree
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
                self.g.add_edge(current_node, node.child, edge_type='C', color='red')
                self.q.put(node.child)
            else:
                tn = TreeNode(value='▓', child=None, brother=None)
                self.g.add_edge(current_node, tn, edge_type='C', color='red')
            node = node.brother
            if node is not None:
                print('\t───\t', end='')
                self.g.add_edge(current_node, node, edge_type='B', color='blue')
            else:
                tn = TreeNode(value='▓', child=None, brother=None)
                self.g.add_edge(current_node, tn, edge_type='B', color='blue')

        if not self.q.empty():
            self.print_tree(node=self.q.get(), level=level + 1)

    def print_tree2(self, node=None):
        pass

    def exitAssign(self, ctx: AssignmentStatement2Parser.AssignContext):
        idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=ctx.expr().value_attr)
        assPntr = self.ast.make_node(value=":=", child=idPntr, brother=None)
        ctx.value_attr = assPntr
        self.ast.root = assPntr
        self.print_tree(node=self.ast.root, level=1)

    def exitExpr_term_plus(self, ctx: AssignmentStatement2Parser.Expr_term_plusContext):
        self.ast.add_brother(ctx.expr().value_attr, ctx.term().value_attr)
        exprPntr = self.ast.make_node(value="+", child=ctx.expr().value_attr, brother=None)
        ctx.value_attr = exprPntr

    def exitExpr_term_minus(self, ctx: AssignmentStatement2Parser.Expr_term_plusContext):
        self.ast.add_brother(ctx.expr().value_attr, ctx.term().value_attr)
        exprPntr = self.ast.make_node(value="-", child=ctx.expr().value_attr, brother=None)
        ctx.value_attr = exprPntr

    def exitTerm4(self, ctx: AssignmentStatement2Parser.Term4Context):
        ctx.value_attr = ctx.term().value_attr

    # ----------------------
    def exitTerm_fact_mutiply(self, ctx: AssignmentStatement2Parser.Term_fact_mutiplyContext):
        self.ast.add_brother(ctx.term().value_attr, ctx.factor().value_attr)
        termPntr = self.ast.make_node(value="*", child=ctx.term().value_attr, brother=None)
        ctx.value_attr = termPntr

    def exitTerm_fact_divide(self, ctx: AssignmentStatement2Parser.Term_fact_divideContext):
        self.ast.add_brother(ctx.term().value_attr, ctx.factor().value_attr)
        termPntr = self.ast.make_node(value="/", child=ctx.term().value_attr, brother=None)
        ctx.value_attr = termPntr

    def exitFactor3(self, ctx: AssignmentStatement2Parser.Factor3Context):
        ctx.value_attr = ctx.factor().value_attr

    # ---------------------
    def exitFact_expr(self, ctx: AssignmentStatement2Parser.Fact_exprContext):
        ctx.value_attr = ctx.expr().value_attr

    def exitFact_id(self, ctx: AssignmentStatement2Parser.Fact_idContext):
        idPntr = self.ast.make_node(value=ctx.ID().getText(), child=None, brother=None)
        ctx.value_attr = idPntr

    def exitFact_number(self, ctx: AssignmentStatement2Parser.Fact_numberContext):
        ctx.value_attr = ctx.number().value_attr

    # ----------------------
    def exitNumber_float(self, ctx: AssignmentStatement2Parser.Number_floatContext):
        numberPntr = self.ast.make_node(value=ctx.FLOAT().getText(), child=None, brother=None)
        ctx.value_attr = numberPntr

    def exitNumber_int(self, ctx: AssignmentStatement2Parser.Number_intContext):
        numberPntr = self.ast.make_node(value=ctx.INT().getText(), child=None, brother=None)
        ctx.value_attr = numberPntr


