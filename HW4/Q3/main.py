from miniJavaASTLexer import miniJavaASTLexer
from miniJavaASTListener import miniJavaASTListener
from miniJavaASTParser import miniJavaASTParser
from antlr4 import *

from binarytree import Node

inp='Example.java'
file=FileStream(inp)
out='Example.out'
import sys
sys.stdout=open(out,'w')
lexer = miniJavaASTLexer(file)
stream = CommonTokenStream(lexer)
parser=miniJavaASTParser(stream)
tree = parser.program()
listener = miniJavaASTListener()

walker = ParseTreeWalker()
#walker.walk(listener,tree)

def print_tree(tree, lev):
    print((" " * lev) + "` " + str(tree.v if hasattr(tree , 'v') else tree.getText()))
    if hasattr(tree,'getChildren'):
        for c in tree.getChildren():
            print_tree(c, lev + 1)
    
    
print_tree(tree, 0)


sys.stdout.close()
