from miniJavaThreeCodeParser import miniJavaThreeCodeParser
from miniJavaThreeCodeListener import miniJavaThreeCodeListener
from miniJavaThreeCodeLexer import miniJavaThreeCodeLexer
from antlr4 import *


inp='Example.java'
out='Example.out'
import sys
sys.stdout=open(out,'w')
file=FileStream(inp)

lexer = miniJavaThreeCodeLexer(file)
stream = CommonTokenStream(lexer)
parser=miniJavaThreeCodeParser(stream)
tree = parser.program()
listener = miniJavaThreeCodeListener()

walker = ParseTreeWalker()
walker.walk(listener,tree)

sys.stdout.close()