from gen.MJParser import MJParser
from gen.MJParserListener import MJParserListener
from gen.MJLexer import MJLexer
from antlr4 import *

if __name__ == '__main__':
    test = FileStream("test.java")
    lexer = MJLexer(test)
    stream = CommonTokenStream(lexer)
    parser = MJParser(stream)
    tree = parser.program()
    parser_listener = MJParserListener()
    walker = ParseTreeWalker()
    walker.walk(parser_listener, tree)