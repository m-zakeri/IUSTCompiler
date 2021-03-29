"""
Main script for grammar AssignmentStatement3 (version 3)
Contains semantic rules to perform type checking and
semantic routines to generate intermediate representation (three addresses codes)

## author
Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)

## date
20201028

## Required
- Compiler generator:   ANTLR 4.x
- Target language(s):   Python 3.8.x


## Changelog
### v3.0
- Add semantic rules to perferm type checking
- Add semantic routines to generate intermediate representation (three addresses codes)


## Refs
- Reference: Compiler book by Dr. Saeed Parsa (http://parsa.iust.ac.ir/)
- Course website:   http://parsa.iust.ac.ir/courses/compilers/
- Laboratory website:   http://reverse.iust.ac.ir/


"""

from antlr4 import *

from language_apps.assignment_statement_v3.gen.AssignmentStatement3Lexer import AssignmentStatement3Lexer
from language_apps.assignment_statement_v3.gen.AssignmentStatement3Parser import AssignmentStatement3Parser
from language_apps.assignment_statement_v3.gen.AssignmentStatement3Listener import AssignmentStatement3Listener

import argparse


class MyListener(AssignmentStatement3Listener):
    def exitFactor(self, ctx: AssignmentStatement3Parser.FactorContext):
        pass


def main(args):
    """
    Create lexer and parser for language application

    Args:

        args (string): command line arguments
        return (None):
    """

    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    # input_stream = StdinStream()
    print('Input stream:')
    print(stream)
    print('Compiler result:')

    # Step 2: Create an instance of AssignmentStLexer
    lexer = AssignmentStatement3Lexer(stream)
    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)
    # Step 4: Create an instance of the AssignmentStParser
    parser = AssignmentStatement3Parser(token_stream)
    # Step 5: Create parse tree
    parse_tree = parser.start()
    # Step 6: Create an instance of AssignmentStListener
    my_listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=my_listener)

    quit()
    lexer.reset()
    token = lexer.nextToken()
    while token.type != Token.EOF:
        print('Token text: ', token.text, 'Token line: ', token.line)
        token = lexer.nextToken()


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'A.java')
    args = argparser.parse_args()
    main(args)
