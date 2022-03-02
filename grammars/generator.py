from antlr4 import *
import argparse
from gen.tacParser import tacParser
from gen.tacLexer import tacLexer
from gen.tacListener import tacListener

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'A.java')
    args = argparser.parse_args()


    def main(args):
        stream = FileStream(args.file, encoding='utf8')
        print('Input stream:')
        print(stream)
        print('Compiler result:')

        lexer = tacLexer(stream)
        token_stream = CommonTokenStream(lexer)
        parser = tacParser(token_stream)
        parse_tree = parser.program()
        my_listener = tacListener()
        walker = ParseTreeWalker()
        walker.walk(t=parse_tree, listener=my_listener)

        quit()
        lexer.reset()
        token = lexer.nextToken()
        while token.type != Token.EOF:
            print('Token text: ', token.text, 'Token line: ', token.line)
            token = lexer.nextToken()


    main(args)
