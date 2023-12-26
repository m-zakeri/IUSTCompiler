import queue
import random
import json

import networkx as nx

from gen.Assignment4q3Lexer import Assignment4q3Lexer
from gen.Assignment4q3Parser import Assignment4q3Parser
from gen.Assignment4q3Listener import Assignment4q3Listener

from antlr4 import *
import argparse

def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    print('Result:')

    # Step 2: Create an instance of AssignmentStLexer
    lexer = Assignment4q3Lexer(stream)

    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)

    # Step 4: Create an instance of the AssignmentStParser
    parser = Assignment4q3Parser(token_stream)

    # Step 5: Create parse tree
    parse_tree = parser.program()

    # Step 6: Create an instance of AssignmentStListener
    # code_generator_listener = ThreeAddressCodeGeneratorListener()
    listener = Assignment4q3Listener()

    # Step 7(a): Walk parse tree with a customized listener (Automatically)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=listener)

    # Step 7(b): Walk parse tree with a customize visitor (Manually)
    # code_generator_vistor = ThreeAddressCodeGeneratorVisitor()
    # code_generator_vistor = ThreeAddressCodeGenerator2Visitor()
    # code_generator_vistor.visitStart(ctx=parse_tree.getRuleContext())


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'test.java')
    args = argparser.parse_args()
    main(args)