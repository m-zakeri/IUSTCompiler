from gen.MiniJavaParser import MiniJavaParser
from gen.MiniJavaLexer import MiniJavaLexer
from gen.MiniJavaListener import MiniJavaListener
from antlr4 import *


def walk():
    inp = "Test.java"
    file = FileStream(inp)
    lexer = MiniJavaLexer(file)
    stream = CommonTokenStream(lexer)
    parser = MiniJavaParser(stream)
    tree = parser.program()
    parser_listener = MiniJavaListener()
    walker = ParseTreeWalker()
    walker.walk(parser_listener, tree)


if __name__ == '__main__':
    walk()