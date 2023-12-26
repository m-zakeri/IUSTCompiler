import queue
import random
import json

import networkx as nx

from antlr4 import *
from gen.Assignment4q4Lexer import Assignment4q4Lexer
from gen.Assignment4q4Parser import Assignment4q4Parser
from gen.Assignment4q4Listener import Assignment4q4Listener

from antlr4 import *

class ASTListener(Assignment4q4Listener):
    def __init__(self):
        self.ast = AST()
        self.q = queue.Queue()
        self.g = nx.DiGraph()

    def exitIdentifier(self, ctx:Assignment4q4Parser.IdentifierContext):
        idpntr = self.ast.makeNode(ctx.IDENTIFIER().getText(), None, None)
        ctx.value_attr = idpntr

    def exitExp12(self, ctx:Assignment4q4Parser.Exp12Context):
        pntr = self.ast.makeNode('()', None, None)
        self.ast.addBrother(pntr, ctx.expression().value_attr)
        ctx.value_attr = pntr

    def exitExp11(self, ctx:Assignment4q4Parser.Exp11Context):
        pntr = self.ast.makeNode('!', None, None)
        self.ast.addBrother(pntr, ctx.expression().value_attr)
        ctx.value_attr = pntr

    def exitExp10(self, ctx:Assignment4q4Parser.Exp10Context):
        pntr = self.ast.makeNode('new', None, None)
        self.ast.addChild(pntr, ctx.identifier().value_attr)
        ctx.value_attr = pntr

    def exitExp9(self, ctx:Assignment4q4Parser.Exp9Context):
        pntr = self.ast.makeNode('new int', None, None)
        self.ast.addChild(pntr, ctx.expression().value_attr)
        ctx.value_attr = pntr

    def exitExp8(self, ctx:Assignment4q4Parser.Exp8Context):
        ctx.value_attr = self.ast.makeNode('this', None, None)

    def exitExp7(self, ctx:Assignment4q4Parser.Exp7Context):
        ctx.value_attr = ctx.identifier().value_attr

    def exitExp6(self, ctx:Assignment4q4Parser.Exp6Context):
        ctx.value_attr = self.ast.makeNode('false', None, None)

    def exitExp5(self, ctx:Assignment4q4Parser.Exp5Context):
        ctx.value_attr = self.ast.makeNode('true', None, None)

    def exitExp4(self, ctx:Assignment4q4Parser.Exp4Context):
        ctx.value_attr = self.ast.makeNode(ctx.INTEGER_LITERAL().getText(), None, None)

    def exitExp3(self, ctx:Assignment4q4Parser.Exp3Context):
        pntr = self.ast.makeNode('call', None, None)
        self.ast.addChild(pntr, ctx.expression(0).value_attr)
        self.ast.addChild(pntr, ctx.identifier().value_attr)
        if ctx.e2 is not None:
            i = 1
            while ctx.expression(i):
                self.ast.addChild(pntr, ctx.expression(i).value_attr)
                i += 1
        ctx.value_attr = pntr

    def exitExp2(self, ctx:Assignment4q4Parser.Exp2Context):
        pntr = self.ast.makeNode('length', None, None)
        self.ast.addChild(pntr, ctx.expression().value_attr)
        ctx.value_attr = pntr

    def exitExp1(self, ctx:Assignment4q4Parser.Exp1Context):
        pntr = self.ast.makeNode('[ ]', ctx.expression(0).value_attr, None)
        self.ast.addBrother(ctx.expression(0).value_attr, ctx.expression(1).value_attr)
        ctx.value_attr = pntr

    def exitExp0(self, ctx:Assignment4q4Parser.Exp0Context):
        pntr = self.ast.makeNode('operand', ctx.expression(0).value_attr, None)
        self.ast.addBrother(ctx.expression(0).value_attr, ctx.expression(1).value_attr)
        ctx.value_attr = pntr

    def exitSt5(self, ctx:Assignment4q4Parser.St5Context):
        pntr = self.ast.makeNode('assgin []', ctx.identifier().value_attr, None)
        self.ast.addBrother(ctx.identifier().value_attr, ctx.expression(0).value_attr)
        self.ast.addBrother(ctx.identifier().value_attr, ctx.expression(1).value_attr)
        ctx.value_attr = pntr

    def exitSt4(self, ctx:Assignment4q4Parser.St4Context):
        pntr = self.ast.makeNode('assign', ctx.identifier().value_attr, None)
        self.ast.addBrother(ctx.identifier().value_attr, ctx.expression().value_attr)
        ctx.value_attr = pntr

    def exitSt3(self, ctx:Assignment4q4Parser.St3Context):
        pntr = self.ast.makeNode('print', ctx.expression().value_attr, None)
        ctx.value_attr = pntr

    def exitSt2(self, ctx:Assignment4q4Parser.St2Context):
        pntr = self.ast.makeNode('while', ctx.expression().value_attr, None)
        self.ast.addBrother(ctx.expression().value_attr, ctx.statement().value_attr)
        ctx.value_attr = pntr

    def exitSt1(self, ctx:Assignment4q4Parser.St1Context):
        pntr = self.ast.makeNode('if else', ctx.expression().value_attr, None)
        self.ast.addBrother(ctx.expression().value_attr, ctx.statement(0).value_attr)
        self.ast.addBrother(ctx.expression().value_attr, ctx.statement(1).value_attr)
        ctx.value_attr = pntr

    def exitSt0(self, ctx:Assignment4q4Parser.St0Context):
        pntr = self.ast.makeNode('{}', None, None)
        for c in ctx.statement():
            self.ast.addChild(pntr, c.value_attr)
        ctx.value_attr = pntr
        self.ast.root = ctx.value_attr
        self.print_tree(self.ast.root, 1)

    def print_tree(self, node=None, level=1):
        if node is None:
            print("--------Fenito----------")
            return
        if not self.q.empty():
            print('Parent:', self.q.get().value)
            print('\t' * level, end='')
        #           print()
        while node is not None:
            print(node.value, '\t───\t', end='')  # alt+196 = ───, alt+178=▓
            if node.child is not None:
                self.q.put(node.child)
                self.q.put(node)
            node = node.brother
            if node is None:
                print('▓', end='\n')
        if not self.q.empty():
            self.print_tree(node=self.q.get(), level=level + 1)

class treeNode:
        def __init__(self, value, child, brother):
            self.value = value
            self.child = child
            self.brother = brother

class AST:
        def __init__(self):
            self.root = None
            self.current = None

        def makeNode(self, value, child, brother):
            tree_node = treeNode(value, child, brother)
            # if self.root is None:
            #    self.root = tree_node
            self.current = tree_node
            return tree_node

        def addChild(self, node, new_child):
            if node.child is None:
                node.child = new_child
            else:
                self.current = node.child
                while (self.current.brother) is not None:
                    self.current = self.current.brother
                self.current.brother = new_child
            self.current = new_child

        def addBrother(self, node, new_brother):
            if node.brother is None:
                node.brother = new_brother
            else:
                self.current = node.brother
                while (self.current.brother) is not None:
                    self.current = self.current.brother
                self.current.brother = new_brother
            self.current = new_brother




import argparse

def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    print('Result:')

    # Step 2: Create an instance of AssignmentStLexer
    lexer = Assignment4q4Lexer(stream)

    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)

    # Step 4: Create an instance of the AssignmentStParser
    parser = Assignment4q4Parser(token_stream)

    # Step 5: Create parse tree
    parse_tree = parser.program()

    # Step 6: Create an instance of AssignmentStListener
    # code_generator_listener = ThreeAddressCodeGeneratorListener()
    code_generator_listener = ASTListener()

    # Step 7(a): Walk parse tree with a customized listener (Automatically)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=code_generator_listener)

    # Step 7(b): Walk parse tree with a customize visitor (Manually)
    # code_generator_vistor = ThreeAddressCodeGeneratorVisitor()
    # code_generator_vistor = ThreeAddressCodeGenerator2Visitor()
    # code_generator_vistor.visitStart(ctx=parse_tree.getRuleContext())


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'test.java')
    args = argparser.parse_args()
    main(args)