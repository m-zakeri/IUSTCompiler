"""
Main script for grammar assignment_statement_v1

"""

from antlr4 import *

from code.assignment_statement_v1.gen.AssignmentStatement1Lexer import AssignmentStatement1Lexer
from code.assignment_statement_v1.gen.AssignmentStatement1Parser import AssignmentStatement1Parser
from code.assignment_statement_v1.gen.AssignmentStatement1Listener import AssignmentStatement1Listener

import argparse


class MyListener(AssignmentStatement1Listener):
    def exitFactor(self, ctx:AssignmentStatement1Parser.FactorContext):
        # print(type(ctx.number().getText()))
        pass

    def exitNumber(self, ctx:AssignmentStatement1Parser.NumberContext):
        pass


def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    # input_stream = StdinStream()
    # Step 2: Create an instance of AssignmentStLexer
    lexer = AssignmentStatement1Lexer(stream)
    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)
    # Step 4: Create an instance of the AssignmentStParser
    parser = AssignmentStatement1Parser(token_stream)
    # Step 5: Create parse tree
    parse_tree = parser.start()
    # Step 6: Create an instance of AssignmentStListener
    my_listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=my_listener)

    # return
    lexer.reset()
    token = lexer.nextToken()
    while token.type != Token.EOF:
        print('Token text: ', token.text, 'Token line: ', token.line)
        token = lexer.nextToken()


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'input.txt')
    args = argparser.parse_args()
    main(args)
