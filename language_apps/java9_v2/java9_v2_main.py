"""
Main script for grammer Java9_v2 (version 2)

@author: Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)
@date: 20201107

- Compiler generator:   ANTRL4.x
- Target language(s):   Python3.x,


-Changelog:
-- v4.2
--- Add name for grammar rules extensions
--- Remove Java attributes from grammar file.

- Course website:   http://parsa.iust.ac.ir/courses/compilers/
- Laboratory website:   http://reverse.iust.ac.ir/

"""

__version__ = '0.1.1'
__author__ = 'Morteza'

import argparse

from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter

from language_apps.java9_v2.gen.Java9_v2Lexer import Java9_v2Lexer
from language_apps.java9_v2.gen.Java9_v2Parser import Java9_v2Parser
from language_apps.java9_v2.refactors import EncapsulateFieldRefactoringListener, ManipulateComments, ManipulateComments2
from language_apps.java9_v2.metrics import DesignMetrics, DesignMetrics2


def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    # input_stream = StdinStream()
    # print('Input stream:')
    # print(stream)

    # Step 2: Create an instance of AssignmentStLexer
    lexer = Java9_v2Lexer(stream)
    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)



    # Step 4: Create an instance of the AssignmentStParser
    parser = Java9_v2Parser(token_stream)

    # parser.getTokenStream()
    # Step 5: Create parse tree
    parse_tree = parser.compilationUnit()

    token_stream_rewriter = TokenStreamRewriter(token_stream)
    for token in token_stream.tokens:
        if token.type in [117, 118]:
            token_stream_rewriter.replaceIndex(
                index=token.tokenIndex,
                text=f'{token.text[:2]} @author: Morteza {token.text[2:]}'
            )
    # print(token_stream_rewriter.getDefaultText())

    # Step 6: Create an instance of JavaListener based on the specific application, `--app`
    if args.app == 1:
        my_listener = EncapsulateFieldRefactoringListener(common_token_stream=token_stream, field_identifier='g')
    elif args.app == 2:
        my_listener = DesignMetrics()
    elif args.app == 3:
        my_listener = DesignMetrics2(class_name='C')
    elif args.app == 4:
        my_listener = ManipulateComments2(common_token_stream=token_stream, name='Morteza')
    else:
        raise ValueError('Invalid input application code')
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=my_listener)

    print('Results:')
    if args.app == 1 or args.app == 4:
        print(my_listener.token_stream_rewriter.getDefaultText())
        # with open('A.refactored.java', mode='w', newline='') as f:
        #     f.write(my_listener.token_stream_rewriter.getDefaultText())
    elif args.app == 2:
        print(f'DSC={my_listener.get_design_size}')
    elif args.app == 3:
        print(f'number of private field in class C is {my_listener.get_number_of_private_attr}')


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'A.java')
    argparser.add_argument('--app', type=int, required=True, default=2)
    args = argparser.parse_args()
    main(args)
