"""
Main script for grammar AssignmentStatement1 (version 1)

## author
Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)

## date
20201029

## Required
- Compiler generator:   ANTLR 4.x
- Target language(s):   Python 3.8.x


## Changelog
### v2.0.0
- A lexer and parser for simple grammar without any attribute or listener


## Refs
- Reference: Compiler book by Dr. Saeed Parsa (http://parsa.iust.ac.ir/)
- Course website:   http://parsa.iust.ac.ir/courses/compilers/
- Laboratory website:   http://reverse.iust.ac.ir/

"""

__version__ = '0.1.0'
__author__ = 'Morteza'

from antlr4 import *
from antlr4.error import ErrorStrategy

from language_apps.assignment_statement_v1.gen.AssignmentStatement1Lexer import AssignmentStatement1Lexer
from language_apps.assignment_statement_v1.gen.AssignmentStatement1Parser import AssignmentStatement1Parser
from language_apps.assignment_statement_v1.gen.AssignmentStatement1Listener import AssignmentStatement1Listener

import argparse


class MyListener(AssignmentStatement1Listener):
    def exitFactor(self, ctx: AssignmentStatement1Parser.FactorContext):
        print('Dummy listener!')

    def exitNumber(self, ctx: AssignmentStatement1Parser.NumberContext):
        pass


def main(args):
    """
    Create lexer and parser

    Args:

        args (str):
        return (None):
    """
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    # input_stream = StdinStream()
    # Step 2: Create an instance of AssignmentStLexer
    lexer = AssignmentStatement1Lexer(stream)
    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)
    # Step 4: Create an instance of the AssignmentStParser
    parser = AssignmentStatement1Parser(token_stream)
    parser._interp.predictionMode = PredictionMode.SLL

    #x = DescriptiveErrorListener()
    #parser.addErrorListener()

    # Step 5: Create parse tree
    parse_tree = parser.start()

    # Step 6: Create an instance of AssignmentStListener
    my_listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=my_listener)
    quit()
    # return
    lexer.reset()
    token = lexer.nextToken()
    while token.type != Token.EOF:
        print('Token text: ', token.text, 'Token line: ', token.line)
        token = lexer.nextToken()


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-f', '--file',
        help='Input source', default=r'input.txt')
    args_ = argparser.parse_args()
    main(args_)
