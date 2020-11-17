"""
Main script for grammar Expr1

"""

__version__ = '0.1.0'
__author__ = 'Morteza'

from antlr4 import *

from language_apps.expr1.gen.testLexer import testLexer
from language_apps.expr1.gen.testParser import testParser

# Step 0: Input program
input_string = 'y = a + b * c -'
# Step 1: Convert input to stream
stream = InputStream(input_string)
# Step 2: Create lexer object
lexer = testLexer(stream)
# Step 3: Create a token stream
token_stream = CommonTokenStream(lexer)
# Step 4: Create a parser object
parser = testParser(token_stream)
# Step 5: Parse from start rule
parse_tree = parser.start()

lexer.reset()
for token in lexer.getAllTokens():
    print(token)
