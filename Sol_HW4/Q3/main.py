
from antlr4 import *
from gen.MiniJavaLexer import MiniJavaLexer
from gen.MiniJavaParser import MiniJavaParser
from gen.MiniJavaListener import MiniJavaListener

import argparse


class MyListener(MiniJavaListener):
    def __init__(self):
        pass


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'./QuickSortExample.java')
    args = argparser.parse_args()
    stream = FileStream("./QuickSortExample.java", encoding='utf8')
    lexer = MiniJavaLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniJavaParser(token_stream)
    parse_tree = parser.program()
    my_listener = MiniJavaListener()
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=my_listener)
