from antlr4 import *
from gen_3addr.MiniJava_3addrLexer import MiniJava_3addrLexer
from gen_3addr.MiniJava_3addrParser import MiniJava_3addrParser
from gen_3addr.MiniJava_3addrListener import MiniJava_3addrListener
from gen_AST.MiniJava_ASTLexer import MiniJava_ASTLexer
from gen_AST.MiniJava_ASTParser import MiniJava_ASTParser
from gen_AST.MiniJava_ASTListener import MiniJava_ASTListener
import queue
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout


def test_3addr(file):
    stream = FileStream(file)
    lexer = MiniJava_3addrLexer(stream)
    parser = MiniJava_3addrParser(CommonTokenStream(lexer))
    tree = parser.program()
    walker = ParseTreeWalker()
    walker.walk(t=tree, listener=MiniJava_3addrListener())


class TreeNode:
    def __init__(self, value, child, brother):
        self.value = value
        self.child = child
        self.brother = brother


class ASTListener(MiniJava_ASTListener):
    def __init__(self):
        self.q = queue.Queue()
        self.g = nx.DiGraph()

    def exitMethodDeclaration(self, ctx: MiniJava_ASTParser.MethodDeclarationContext):
        self.print_tree(node=ctx.val, level=1)
        self.draw(g=self.g, function_name=ctx.n.text)
        self.q = queue.Queue()
        self.g = nx.DiGraph()

    def exitMainClass(self, ctx: MiniJava_ASTParser.MainClassContext):
        self.print_tree(node=ctx.val, level=1)
        self.draw(g=self.g, function_name='main')
        self.q = queue.Queue()
        self.g = nx.DiGraph()

    def print_tree(self, node=None, level=1):
        if node is None:
            return
        while node is not None:
            current_node = node
            if node.child is not None:
                self.g.add_edge(current_node, node.child, edge_type='C', color='r')
                self.q.put(node.child)
            node = node.brother
            if node is not None:
                self.g.add_edge(current_node, node, edge_type='B', color='b')

        if not self.q.empty():
            self.print_tree(node=self.q.get(), level=level + 1)

    def draw(self, g: nx.DiGraph = None, function_name=None):
        plt.figure(3, figsize=(30, 30))
        pos = nx.kamada_kawai_layout(G=g)
        pos = graphviz_layout(G=g, prog='dot')
        colors = [g[u][v]['color'] for u, v in g.edges]
        nx.draw(g,
                with_labels=False,
                node_size=2000,
                node_color='black',
                edge_color=colors,
                pos=pos,
                )
        edge_labels = nx.get_edge_attributes(g, 'edge_type')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=16)

        node_labels = {}
        for node in g.nodes():
            node_labels[node] = node.value
        nx.draw_networkx_labels(g, pos, node_labels, font_size=16, font_color='w')
        plt.savefig('AST_Func_' + function_name + '.png')
        plt.show()


def test_AST(file):
    stream = FileStream(file)
    lexer = MiniJava_ASTLexer(stream)
    parser = MiniJava_ASTParser(CommonTokenStream(lexer))
    tree = parser.program()
    walker = ParseTreeWalker()
    listener = ASTListener()
    walker.walk(t=tree, listener=listener)


if __name__ == '__main__':
    file_path = r'program.java'
    test_3addr(file_path)
    test_AST(file_path)
