"""
Main script for grammar assignment_statement

"""

from antlr4 import *

from code.assignment_statement.gen.assignment_statementLexer import assignment_statementLexer
from code.assignment_statement.gen.assignment_statementParser import assignment_statementParser
from code.assignment_statement.gen.assignment_statementListener import assignment_statementListener

import argparse


class MyListener(assignment_statementListener):
    def exitFactor(self, ctx:assignment_statementParser.FactorContext):
        # print(type(ctx.number().getText()))
        pass

    def exitNumber(self, ctx:assignment_statementParser.NumberContext):
        print(ctx.getText(), type(ctx.getText()))


def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    # input_stream = StdinStream()
    # Step 2: Create an instance of AssignmentStLexer
    lexer = assignment_statementLexer(stream)
    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)
    # Step 4: Create an instance of the AssignmentStParser
    parser = assignment_statementParser(token_stream)
    # Step 5: Create parse tree
    parse_tree = parser.ass()
    # Step 6: Create an instance of AssignmentStListener
    my_listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=my_listener)

    return
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
