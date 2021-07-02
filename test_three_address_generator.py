from antlr4 import *

from gen.Q3Lexer import Q3Lexer
from gen.Q3Parser import Q3Parser
from gen.Q3Listener import Q3Listener

import argparse


class ThreeAddressGenerator(Q3Listener):
    def exitFactor(self, ctx: Q3Parser.FactorContext):
        pass

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'playground.java')
    args = argparser.parse_args()

    stream = FileStream(args.file, encoding='utf8')
    lexer = Q3Lexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = Q3Parser(token_stream)
    parse_tree = parser.program()
    my_listener = ThreeAddressGenerator()
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=my_listener)

    quit()
    lexer.reset()
    token = lexer.nextToken()
    while token.type != Token.EOF:
        print('Token text: ', token.text, 'Token line: ', token.line)
        token = lexer.nextToken()
