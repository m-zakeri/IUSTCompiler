"""
Main script for grammar Expr2

"""

__version__ = '0.1.0'
__author__ = 'Morteza'


from antlr4 import *

from code.expr2.gen.Expr2Lexer import Expr2Lexer
from code.expr2.gen.Expr2Parser import Expr2Parser
from code.expr2.expr2listener import *

# Step 0: Give an input
input_string = 'y = (2 + 5 + (3*6)) * 8 / 2'
# Step 1: Convert input to a byte stream
stream = InputStream(input_string)
# Step 2: Create lexer
lexer = Expr2Lexer(stream)
# Step 3: Create a list of tokens
token_stream = CommonTokenStream(lexer)
# Step 4: Create parser
parser = Expr2Parser(token_stream)
# Step 5: Create parse tree
parse_tree = parser.start()

# Step 6: Adding a listener
my_listener = DummyListener()
# my_listener = TreeAddressCode()

#ParseTreeWalker.DEFAULT.walk(t=parse_tree, listener=my_listener)
walker = ParseTreeWalker()
walker.walk(listener=my_listener, t=parse_tree)

# lexer.reset()
# for token in lexer.getAllTokens():
#     if token.channel != 1:
#         print(token.type)
