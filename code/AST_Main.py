from antlr4 import *
from code.gen.AssignmentStatement2Lexer import AssignmentStatement2Lexer
from code.gen.AssignmentStatement2Parser import AssignmentStatement2Parser
from code.Ast import ASTListener
import argparse


def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    print('Input code:\n{0}'.format(stream))
    print('Result:')

    # Step 2: Create an instance of AssignmentStLexer
    lexer = AssignmentStatement2Lexer(stream)

    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)

    # Step 4: Create an instance of the AssignmentStParser
    parser = AssignmentStatement2Parser(token_stream)

    # Step 5: Create parse tree
    parse_tree = parser.start()

    # Step 6: Create an instance of AssignmentStListener
    # code_generator_listener = ThreeAddressCodeGeneratorListener()
    code_generator_listener = ASTListener()

    # Step 7(a): Walk parse tree with a customized listener (Automatically)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=code_generator_listener)

    # Step 7(b): Walk parse tree with a customize visitor (Manually)
    # code_generator_vistor = ThreeAddressCodeGeneratorVisitor()
    # code_generator_vistor = ThreeAddressCodeGenerator2Visitor()
    # code_generator_vistor.visitStart(ctx=parse_tree.getRuleContext())


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'input.txt')
    args = argparser.parse_args()
    main(args)
