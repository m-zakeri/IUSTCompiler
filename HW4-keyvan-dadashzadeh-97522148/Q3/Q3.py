# !/bin/python3

from antlr4 import *
import argparse

from gen.Q3Listener import Q3Listener
from gen.Q3Lexer import Q3Lexer
from gen.Q3Parser import Q3Parser

class Q3Lis(Q3Listener):
    def __init__(self):
        pass


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'./QuickSort.java')
    print("make sure that you fixed indentation in parse file(run fix)")
    args = argparser.parse_args()
    stream = FileStream("./QuickSort.java", encoding='utf8')
    print('Three Address Code:')
    lexer = Q3Lexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = Q3Parser(token_stream)
    parse_tree = parser.program()
    my_listener = Q3Lis()
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=my_listener)
