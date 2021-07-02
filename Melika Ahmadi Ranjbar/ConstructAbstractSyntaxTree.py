from antlr4 import *
from Gen.MiniJavaLexer import MiniJavaLexer
from Gen.MiniJavaParser import MiniJavaParser
from Gen.MiniJavaListener import MiniJavaListener

import queue
import argparse


class ConstructAbstractSyntaxTreeListener(MiniJavaListener):
    def __init__(self):
        self.AST = AbstractSyntaxTree()
        self.Q = queue.Queue()

    def exitOperations_expression(self, ctx:MiniJavaParser.Operations_expressionContext):
        Child1 = self.AST.MakeNode(ctx.expression(0).value_attr, None, None)
        Child2 = self.AST.MakeNode(ctx.expression(1).value_attr, None, None)
        self.AST.AddBrother(Child1, Child2)
        Parent = self.AST.MakeNode(ctx.operations().getText(), Child1, None)
        ctx.value_attr = Parent

    def exitEqual_statement(self, ctx: MiniJavaParser.Equal_statementContext):
        Child1 = self.AST.MakeNode(ctx.identifier().value_attr, None, None)
        Child2 = self.AST.MakeNode(ctx.expression().value_attr, None, None)
        self.AST.AddBrother(Child1, Child2)
        Parent = self.AST.MakeNode('=', Child1, None)
        ctx.value_attr = Parent
        self.AST.Root = Parent

    def exitIf_statement(self, ctx:MiniJavaParser.If_statementContext):
        Child0 = self.AST.MakeNode(ctx.expression().value_attr, None, None)
        Child1 = self.AST.MakeNode(ctx.statement(0).value_attr, None, None)
        Child2 = self.AST.MakeNode(ctx.statement(1).value_attr, None, None)
        self.AST.AddBrother(Child0, Child1)
        self.AST.AddBrother(Child1, Child2)
        Parent = self.AST.MakeNode('if', Child0, None)
        ctx.value_attr = Parent

    def enterWhile_statement(self, ctx:MiniJavaParser.While_statementContext):
        Child0 = self.AST.MakeNode(ctx.expression().value_attr, None, None)
        Child1 = self.AST.MakeNode(ctx.statement(0).value_attr, None, None)
        self.AST.AddBrother(Child0, Child1)
        Parent = self.AST.MakeNode('while', Child0, None)
        ctx.value_attr = Parent

    def exitKeywords(self, ctx:MiniJavaParser.KeywordsContext):
        Child = self.AST.MakeNode(ctx.getText(), None, None)
        ctx.value_attr = Child

    def exitWord(self, ctx:MiniJavaParser.WordContext):
        Child = self.AST.MakeNode(ctx.getText(), None, None)
        ctx.value_attr = Child

    def PrintTree(self, node=None, level=1):
        if node is None:
            print("--------Fenito----------")
            return
        if not self.Q.empty():
            print('Parent:', self.Q.get().Value)
            print('\t' * level, end='')
        while node is not None:
            print(node.Value, '\t───\t', end='')
            if node.Child is not None:
                self.Q.put(node.Child)
                self.Q.put(node)
            node = node.Brother
            if node is None:
                print('▓', end='\n')
        if not self.Q.empty():
            self.PrintTree(node=self.Q.get(), level=level + 1)


class TreeNode:
    def __init__(self, value, child, brother):
        self.Value = value
        self.Child = child
        self.Brother = brother


class AbstractSyntaxTree:
    def __init__(self):
        self.Current = None
        self.Root = None

    def MakeNode(self, Value, Child, Brother):
        Node = TreeNode(Value, Child, Brother)
        if self.Root is None:
            self.Root = Node
            self.Current = Node
        return Node

    def AddBrother(self, Node, Bro):
        if Node.Brother is None:
            Node.Brother = Bro
        else:
            self.Current = Node.Brother
            while self.Current.Brother is not None:
                self.Current = self.Current.Brother
            self.Current.Brother = Bro
        self.Current = Bro

    def AddChild(self, Node, Child):
        if Node.Child is None:
            Node.Child = Child
        else:
            self.Current = Node.Child
        while self.Current.Brother is not None:
            self.Current = self.Current.Brother
        self.Current.Brother = Child
        self.Current = Child


def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    print('Input code:\n{0}'.format(stream))
    print('Result:')

    # Step 2: Create an instance of AssignmentStLexer
    lexer = MiniJavaLexer(stream)

    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)

    # Step 4: Create an instance of the AssignmentStParser
    parser = MiniJavaParser(token_stream)

    # Step 5: Create parse tree
    parse_tree = parser.program()

    # Step 6: Create an instance of AssignmentStListener
    code_generator_listener = ConstructAbstractSyntaxTreeListener()

    # Step 7: Walk parse tree with a customized listener (Automatically)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=code_generator_listener)
    # code_generator_listener.PrintTree(code_generator_listener.AST.Root, 1)
    print('Done')


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'input.txt')
    args = argparser.parse_args()
    main(args)

