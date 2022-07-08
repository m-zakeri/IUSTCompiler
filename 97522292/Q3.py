from gen.MiniJavaParser import MiniJavaParser
from gen.MiniJavaLexer import MiniJavaLexer
from gen.MiniJavaParserListener import MiniJavaParserListener
from antlr4 import *

file = FileStream('QuickSort.java')

lexer = MiniJavaLexer(file)
stream = CommonTokenStream(lexer)
parser = MiniJavaParser(stream)
tree = parser.program()
parser_listener = MiniJavaParserListener()

walker = ParseTreeWalker()
walker.walk(parser_listener, tree)
