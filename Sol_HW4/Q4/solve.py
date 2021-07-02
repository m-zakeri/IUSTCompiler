
import networkx as nx
from gen.MiniJavaListener import MiniJavaListener
from gen.MiniJavaParser import MiniJavaParser

import queue




class solve(MiniJavaListener):
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
            self.print_tree(node=self.q.get(), level=level + 1)

    def print_tresecond(self, node=None):
        pass

    # state_terms


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