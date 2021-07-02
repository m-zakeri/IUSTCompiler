import queue
from .gen.MiniJavaListener import MiniJavaListener
from .gen.MiniJavaParser import MiniJavaParser


class ASTListener(MiniJavaListener):
    def __init__(self):
        self.ast = AST()
        self.q = queue.Queue()


    def print_tree(self, node=None, level=1):
        if node is None:
            print("--------Fenito----------")
            return
        if not self.q.empty():
            print('Parent:', self.q.get().value)
            print('\t'*level, end='')
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
        #if self.root is None:
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
