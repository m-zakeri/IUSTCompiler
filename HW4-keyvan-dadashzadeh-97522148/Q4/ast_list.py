import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

from antlr4 import *

from gen.Q4Listener import Q4Listener
from gen.Q4Parser import Q4Parser

import queue

import traceback



class Q4ASTListener(Q4Listener):
    def __init__(self):
        self.ast = AST()  # Data structure for holding the abstract syntax tree
        self.q = queue.Queue()  # Use to print and visualize AST
        self.g = nx.DiGraph()  # Use to visualize AST
        # self.q.empty()
        # print('Q=', )

    def print_tree(self, node=None, level=1):
        if node is None:
            return
        print()
        while node is not None:
            current_node = node
            print(current_node.value, end='')
            if node.child is not None and node.child != "":
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

    def print_tresecond(self, node=None):
        pass

    # state_terms
    def exitState_brace(self, ctx:Q4Parser.State_braceContext):
        state_term = self.ast.make_node(value="statements",child=None, brother=None)
        subchild = 1
        while subchild < (len(ctx.children)-1):
            self.ast.add_child(state_term,ctx.children[subchild].value_attr)
            subchild += 1
        ctx.value_attr=state_term
        self.ast.root = state_term
        self.print_tree(node=self.ast.root, level=1)

    def exitState_if(self, ctx: Q4Parser.State_ifContext):
        state_term = self.ast.make_node(value="if",child=None, brother=None)
        self.ast.add_child(state_term,ctx.expression().value_attr)
        self.ast.add_child(state_term,ctx.st1.value_attr)
        
        self.prepare_statement(ctx, state_term)
        self.prepare_statement(ctx, state_term)

    def exitState_while(self, ctx: Q4Parser.State_whileContext):
        state_term = self.ast.make_node(value="while", child=None, brother=None)
        self.ast.add_child(state_term, ctx.expression().value_attr)
        self.ast.add_child(state_term, ctx.st1.value_attr)
        
        self.prepare_statement(ctx, state_term)

    def exitState_println(self, ctx: Q4Parser.State_printlnContext):
        state_term = self.ast.make_node(value="println", child=None, brother=None)
        self.ast.add_child(state_term, ctx.expression().value_attr)
        
        self.prepare_statement(ctx, state_term)

    def exitState_equal_assign(self, ctx: Q4Parser.State_equal_assignContext):
        state_term = self.ast.make_node(value="=", child=None, brother=None)
        self.ast.add_child(state_term, ctx.expression().value_attr)
        
        self.prepare_statement(ctx, state_term)


    def exitState_access_array_assign(self, ctx: Q4Parser.State_access_array_assignContext):
        state_term = self.ast.make_node(value="=", child=None, brother=None)
        self.ast.add_child(state_term, ctx.second.value_attr)
        self.ast.add_child(ctx.identifier().value_attr, ctx.first.value_attr)
        
        self.prepare_statement(ctx, state_term)
        
    def prepare_statement(self, ctx, statement):
        ctx.value_attr = statement
        self.ast.root = statement
        self.print_tree(node=self.ast.root, level=1)
            
    # exper_terms
    def exitIdentifier(self, ctx:Q4Parser.IdentifierContext):
        numberPntr = self.ast.make_node(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = numberPntr

    def exitExpr_term_id(self, ctx:Q4Parser.Expr_term_idContext):
        ctx.value_attr = ctx.identifier().value_attr
    
    def exitExpr_term_and(self, ctx: Q4Parser.Expr_term_andContext):
        exper_term = self.ast.make_node(value="&&",child=None, brother=None)
        self.ast.add_child(exper_term,ctx.first.value_attr)
        self.ast.add_child(exper_term,ctx.second.value_attr)
        ctx.value_attr = exper_term
        
    def exitExpr_term_not(self, ctx:Q4Parser.Expr_term_notContext):
        exper_term=self.ast.make_node(value="!",child=ctx.expression().value_attr,brother=None)
        ctx.value_attr=exper_term
    
    def exitExpr_term_int(self, ctx:Q4Parser.Expr_term_intContext):
        exper_term = self.ast.make_node(value=ctx.INTEGER_LITERAL().getText(),child=None, brother=None)
        ctx.value_attr=exper_term
        
    def exitExpr_term_less(self, ctx: Q4Parser.Expr_term_lessContext):
        exper_term = self.ast.make_node(value="<",child=None, brother=None)
        self.ast.add_child(exper_term,ctx.first.value_attr)
        self.ast.add_child(exper_term,ctx.second.value_attr)
        ctx.value_attr = exper_term
        
    def exitExpr_term_plus(self, ctx:Q4Parser.Expr_term_plusContext):
        exper_term = self.ast.make_node(value="+",child=None, brother=None)
        self.ast.add_child(exper_term,ctx.first.value_attr)
        self.ast.add_child(exper_term,ctx.second.value_attr)
        ctx.value_attr = exper_term
        
    def exitExpr_term_true(self, ctx:Q4Parser.Expr_term_trueContext):
        exper_term=self.ast.make_node(value="true",child=None,brother=None)
        ctx.value_attr=exper_term
        
    def exitExpr_term_minus(self, ctx: Q4Parser.Expr_term_minusContext):
        exper_term = self.ast.make_node(value="-",child=None, brother=None)
        self.ast.add_child(exper_term,ctx.first.value_attr)
        self.ast.add_child(exper_term,ctx.second.value_attr)
        ctx.value_attr = exper_term

    def exitExpr_term_false(self, ctx:Q4Parser.Expr_term_falseContext):
        exper_term = self.ast.make_node(value="false", child=None, brother=None)
        ctx.value_attr = exper_term
        
    def exitExpr_term_paran(self, ctx: Q4Parser.Expr_term_paranContext):
        ctx.value_attr = ctx.expression().value_attr

    def exitExpr_term_multiply(self, ctx: Q4Parser.Expr_term_multiplyContext):
        exper_term = self.ast.make_node(value="*",child=None, brother=None)
        self.ast.add_child(exper_term,ctx.first.value_attr)
        self.ast.add_child(exper_term,ctx.second.value_attr)
        ctx.value_attr = exper_term

    def exitExpr_term_call_function(self, ctx:Q4Parser.Expr_term_call_functionContext):
        exper_term = ctx.identifier().value_attr
        i=4
        while i < len(ctx.children)-1:
            # print(type(ctx.children[i]))
            # print(dir(ctx.children[i]))
            # print(ctx.children[i].getText())
            self.ast.add_child(exper_term,ctx.children[i].value_attr)
            i+=2
            
        ctx.value_attr = exper_term

class TreeNode:
    def __init__(self, value, child, brother):
        self.value = value
        self.child = child
        self.brother = brother


class AST:
    def __init__(self):
        self.root = None
        self.current = None

    def make_node(self, value, child, brother):
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
