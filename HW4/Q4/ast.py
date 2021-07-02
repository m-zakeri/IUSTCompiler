import queue
import networkx as nx

from HW4.gen.Q2Lexer import Q2Lexer
from HW4.gen.Q2Parser import Q2Parser
from HW4.gen.Q2Listener import Q2Listener
from antlr4 import *


# Listener pattern
class ASTListener(Q2Lexer):
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
