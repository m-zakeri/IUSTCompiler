from gen.MiniJavaParser import MiniJavaParser
from gen.MiniJavaParserListener import MiniJavaParserListener
from gen.MiniJavaLex import MiniJavaLex
from antlr4 import *

if __name__ == '__main__':
    test = FileStream("test.java")

    lexer = MiniJavaLex(test)
    stream = CommonTokenStream(lexer)
    parser = MiniJavaParser(stream)
    tree = parser.program()
    parser_listener = MiniJavaParserListener()

    walker = ParseTreeWalker()
    walker.walk(parser_listener, tree)
