import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

from antlr4 import *

from gen.MiniJavaLexer import MiniJavaLexer
from gen.MiniJavaParser import MiniJavaParser
from solve import solve

import argparse


def main(args):
    stream = FileStream(args.file, encoding='utf8')
    lexer = MiniJavaLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniJavaParser(token_stream)
    parse_tree = parser.program()
    AST = solve()
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=AST)
    draw(g=AST.g)


def draw(g: nx.DiGraph = None):
    pos = nx.kamada_kawai_layout(G=g)
    pos = graphviz_layout(G=g,
                          prog='dot',
                          # prog='circo',
                          )
    colors = [g[u][v]['color'] for u, v in g.edges]
    nx.draw(g,
            with_labels=False,
            node_size=500,
            node_color='black',
            edge_color=colors,
            pos=pos,
            )
    edge_labels = nx.get_edge_attributes(g, 'edge_type')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, )
    node_labels = {}
    for node in g.nodes():
        node_labels[node] = node.value
    nx.draw_networkx_labels(g, pos, node_labels, font_size=12, font_color='w')
    plt.savefig('astSolve.png')
    plt.show()


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')
    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))
    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'./QuickSortExample.java')
    args = argparser.parse_args()
    main(args)
