from gen.MJavaParser import MJavaParser
from gen.MJavaLex import MJavaLex
from gen.MJavaParserListener import MJavaParserListener
from antlr4 import *


def walk():
    inp = "QS.java"
    file = FileStream(inp)
    print("\n...Loading...\n")

    lexer = MJavaLex(file)
    stream = CommonTokenStream(lexer)
    parser = MJavaParser(stream)
    tree = parser.program()
    parser_listener = MJavaParserListener()

    walker = ParseTreeWalker()
    walker.walk(parser_listener, tree)


if __name__ == '__main__':
    walk()
