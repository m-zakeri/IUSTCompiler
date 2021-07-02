# !/bin/python3

from antlr4 import *
import argparse




def fix_indent(filename):
    print("Reading...")
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    print("Processing...")
    for i in range(len(lines)):
        space_count = 0
        while space_count < len(lines[i]) and lines[i][space_count] == ' ':
            space_count += 1
        if space_count > 10 and space_count % 4 == 2:
            lines[i] = lines[i][10:]

    print("Writing...")
    file = open(filename, "w")
    file.writelines(lines)
    file.close()

    print("Done.")


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'A.java')
    args = argparser.parse_args()
    fix_indent("./gen/threeParser.py")

    from gen.threeListener import threeListener
    from gen.threeLexer import threeLexer
    from gen.threeParser import threeParser

    class MyListener(threeListener):
        def __init__(self):
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
        lexer = threeLexer(stream)
        # Step 3: Convert the input source into a list of tokens
        token_stream = CommonTokenStream(lexer)
        # Step 4: Create an instance of the AssignmentStParser
        parser = threeParser(token_stream)
        # Step 5: Create parse tree
        parse_tree = parser.program()
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
    main(args)
