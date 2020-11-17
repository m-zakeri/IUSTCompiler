"""
Main script for grammer AssignmentStatement2 (version 2)

@author: Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)
@date: 20201029

- Compiler generator:   ANTRL4.x
- Target language(s):     Python3.x,


-Changelog:
-- v2.1.0
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
import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

from antlr4 import *

from language_apps.assignment_statement_v2.gen.AssignmentStatement2Lexer import AssignmentStatement2Lexer
from language_apps.assignment_statement_v2.gen.AssignmentStatement2Parser import AssignmentStatement2Parser
from language_apps.assignment_statement_v2.three_address_code_pass import ThreeAddressCodeGeneratorListener, \
    ThreeAddressCodeGenerator2Listener, ThreeAddressCodeGeneratorVisitor, ThreeAddressCodeGenerator2Visitor
from language_apps.assignment_statement_v2.ast_pass import ASTListener

import argparse


def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    print('Input language_apps:\n{0}'.format(stream))
    print('Result:')

    # Step 2: Create an instance of AssignmentStLexer
    lexer = AssignmentStatement2Lexer(stream)

    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)

    # Step 4: Create an instance of the AssignmentStParser
    parser = AssignmentStatement2Parser(token_stream)

    # Step 5: Create parse tree
    parse_tree = parser.start()

    # Step 6: Create an instance of AssignmentStListener
    # code_generator_listener = ThreeAddressCodeGeneratorListener()
    # code_generator_listener = ThreeAddressCodeGenerator2Listener()
    ast_generator = ASTListener()
    # Step 7(a): Walk parse tree with a customized listener (Automatically)
    walker = ParseTreeWalker()
    # walker.walk(t=parse_tree, listener=code_generator_listener)
    walker.walk(t=parse_tree, listener=ast_generator)

    # print_tree(node=ast_generator.ast.root, level=1)
    # print('\nG=', ast_generator.g.edges)
    draw(g=ast_generator.g)

    # Step 7(b): Walk parse tree with a customize visitor (Manually)
    # code_generator_vistor = ThreeAddressCodeGeneratorVisitor()
    # code_generator_vistor = ThreeAddressCodeGenerator2Visitor()
    # code_generator_vistor.visitStart(ctx=parse_tree.getRuleContext())


# def print_tree(root=None, level=1):
#     if root is not None:
#         print('.' * level, level, root.value)
#         print_tree(root=root.child, level=level + 1)
#         print_tree(root=root.brother, level=level + 1)


def draw(g: nx.DiGraph = None):
    """

    :param g:
    :return:
    """
    pos = nx.kamada_kawai_layout(G=g)
    pos = graphviz_layout(G=g,
                          prog='dot',
                          # prog='circo',
                          )
    # pos = nx.bipartite_layout(G=g, nodes=g.nodes)
    # pos = nx.spectral_layout(G=g)
    # pos = hierarchy_pos(G=g,)
    # pos = nx.spiral_layout(G=g)
    # pos = nx.spiral_layout(G=g)
    colors = [g[u][v]['color'] for u, v in g.edges]
    nx.draw(g,
            with_labels=False,
            node_size=500,
            node_color='black',
            edge_color=colors,
            pos=pos,
            )
    edge_labels = nx.get_edge_attributes(g, 'edge_type')
    # print('#', edge_labels)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, )

    node_labels = {}
    for node in g.nodes():
        # set the node name as the key and the label as its value
        node_labels[node] = node.value
    nx.draw_networkx_labels(g, pos, node_labels, font_size=12, font_color='w')
    plt.savefig('../../docs/figs/ast1.png')
    plt.show()


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under Creative Commons Attribution-Share Alike

    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch
    - if the tree is directed and this is not given,
      the root will be found and used
    - if the tree is directed and this is given, then
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given,
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

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
        help='Input source', default=r'input.txt')
    args = argparser.parse_args()
    main(args)
