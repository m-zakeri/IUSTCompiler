"""
Main script for grammer AssignmentStatement4 (version 4)

@author: Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)
@date: 20201029

- Compiler generator:   ANTRL4.x
- Target language(s):     Python3.x,


-Changelog:
-- v4.0
--- Generate intermediate representation (three addresses codes) with minimum number of 'temp' variables
-- v3.0
--- Add semantic rules to perferm type checking
--- Add semantic routines to generate intermediate representation (three addresses codes)

- Reference: Compiler book by Dr. Saeed Parsa (http://parsa.iust.ac.ir/)
- Course website:   http://parsa.iust.ac.ir/courses/compilers/
- Laboratory website:   http://reverse.iust.ac.ir/

"""

__version__ = '0.1.0'
__author__ = 'Morteza'


from antlr4 import *

from code.assignment_statement_v4.gen.AssignmentStatement4Lexer import AssignmentStatement4Lexer
from code.assignment_statement_v4.gen.AssignmentStatement4Parser import AssignmentStatement4Parser
from code.assignment_statement_v4.gen.AssignmentStatement4Listener import AssignmentStatement4Listener

import argparse


class MyListener(AssignmentStatement4Listener):
    def exitFactor(self, ctx: AssignmentStatement4Parser.FactorContext):
        pass


def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    # input_stream = StdinStream()
    print('Input stream:')
    print(stream)
    print('Compiler result:')

    # Step 2: Create an instance of AssignmentStLexer
    lexer = AssignmentStatement4Lexer(stream)
    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)
    # Step 4: Create an instance of the AssignmentStParser
    parser = AssignmentStatement4Parser(token_stream)
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
        help='Input source', default=r'input.txt')
    args = argparser.parse_args()
    main(args)
