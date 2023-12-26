import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

from antlr4 import *

from gen.miniJavaListener import miniJavaListener
from gen.miniJavaVisitor import miniJavaVisitor

from gen.miniJavaParser import miniJavaParser

import queue


class ASTListener(miniJavaListener):
    def __init__(self):
        self.ast = AST()  # Data structure for holding the abstract syntax tree
        self.q = queue.Queue()  # Use to print and visualize AST
        self.g = nx.DiGraph()  # Use to visualize AST
        # self.q.empty()
        # print('Q=', )

    def print_tree(self, node=None, level=1):
        if node is None:
            # print()
            return
        # if not self.q.empty():
        #     print('Parent:', self.q.get().value)
        # print('\t'*level, end='')
        print()
        while node is not None:
            current_node = node
            print(current_node.value, end='')  # alt+196 = ───, alt+178=▓
            if node.child is not None and node.child != '':
                # print("*:",node.value,node.child.value)
                # self.q.put(node)
                self.g.add_edge(current_node, node.child, edge_type='C', color='r')
                self.q.put(node.child)
            else:
                tn = TreeNode(value='▓', child=None, brother=None)
                self.g.add_edge(current_node, tn, edge_type='C', color='r')
            node = node.brother
            if node is not None:
                print('\t───\t', end='')
                self.g.add_edge(current_node, node, edge_type='B', color='b')
            else:
                tn = TreeNode(value='▓', child=None, brother=None)
                self.g.add_edge(current_node, tn, edge_type='B', color='b')

        if not self.q.empty():
            self.print_tree(node=self.q.get(), level=level + 1)

    def print_tree2(self, node=None):
        pass

    # ------------------
    def exitIdentifier(self, ctx:miniJavaParser.IdentifierContext):
        numberPntr = self.ast.make_node(value=ctx.getText(), child=None, brother=None)
        ctx.value_attr = numberPntr

    def exitExpression_paranthesis_expression(self, ctx: miniJavaParser.Expression_paranthesis_expressionContext):
        ctx.value_attr = ctx.expression().value_attr

    def exitExpression_not(self, ctx:miniJavaParser.Expression_notContext):
        expressionPntr=self.ast.make_node(value="!",child=ctx.expression().value_attr,brother=None)
        ctx.value_attr=expressionPntr

    def exitExpression_identifier(self, ctx:miniJavaParser.Expression_identifierContext):
        ctx.value_attr = ctx.identifier().value_attr

    def exitExpression_true(self, ctx:miniJavaParser.Expression_trueContext):
        expressionPntr=self.ast.make_node(value="true",child=None,brother=None)
        ctx.value_attr=expressionPntr

    def exitExpression_false(self, ctx:miniJavaParser.Expression_falseContext):
        expressionPntr = self.ast.make_node(value="false", child=None, brother=None)
        ctx.value_attr = expressionPntr

    def exitExpression_integer_literal(self, ctx:miniJavaParser.Expression_integer_literalContext):
        expressionPntr = self.ast.make_node(value=ctx.INTEGER_LITERAL().getText(),child=None, brother=None)
        ctx.value_attr=expressionPntr

    #e1=expression '.' id=identifier '(' ( e2=expression ( ',' expression )* )? ')'
    def exitExpression_function_call(self, ctx:miniJavaParser.Expression_function_callContext):
        # expressionPntr = self.ast.make_node(value=ctx.identifier().value_attr,child=None, brother=None)
        # expressionPntr = self.ast.make_node(value=ctx.identifier().getText(),child=None, brother=None)
        expressionPntr = ctx.identifier().value_attr
        i=4
        while i < len(ctx.children)-1:
            # new_child=self.ast.make_node(value=ctx.children[i].value_attr,child=None,brother=None)
            # new_child=self.ast.make_node(value=ctx.children[i].getText(),child=None,brother=None)

            # self.ast.add_child(expressionPntr,new_child)
            self.ast.add_child(expressionPntr,ctx.children[i].value_attr)

            i+=2
        ctx.value_attr = expressionPntr

        # prev_child=self.ast.make_node(value=ctx.children[i],child=None, brother=None)
        # i+=2
        # while i<len(ctx.children):
        #     new_child=self.ast.make_node(value=ctx.children[i],child=None, brother=None)
        #     self.ast.add_brother(node=prev_child,new_brother=new_child)
        #     prev_child=new_child
        #     i+=2
    def exitExpression_plus_expression(self, ctx:miniJavaParser.Expression_plus_expressionContext):
        expressionPntr = self.ast.make_node(value="+",child=None, brother=None)
        self.ast.add_child(expressionPntr,ctx.e1.value_attr)
        self.ast.add_child(expressionPntr,ctx.e2.value_attr)
        ctx.value_attr = expressionPntr

    def exitExpression_minus_expression(self, ctx: miniJavaParser.Expression_minus_expressionContext):
        expressionPntr = self.ast.make_node(value="-",child=None, brother=None)
        self.ast.add_child(expressionPntr,ctx.e1.value_attr)
        self.ast.add_child(expressionPntr,ctx.e2.value_attr)
        ctx.value_attr = expressionPntr

    def exitExpression_multiply_expression(self, ctx: miniJavaParser.Expression_multiply_expressionContext):
        expressionPntr = self.ast.make_node(value="*",child=None, brother=None)
        self.ast.add_child(expressionPntr,ctx.e1.value_attr)
        self.ast.add_child(expressionPntr,ctx.e2.value_attr)
        ctx.value_attr = expressionPntr

    def exitExpression_lessthan_expression(self, ctx: miniJavaParser.Expression_lessthan_expressionContext):
        expressionPntr = self.ast.make_node(value="<",child=None, brother=None)
        self.ast.add_child(expressionPntr,ctx.e1.value_attr)
        self.ast.add_child(expressionPntr,ctx.e2.value_attr)
        ctx.value_attr = expressionPntr

    def exitExpression_and_expression(self, ctx: miniJavaParser.Expression_and_expressionContext):
        expressionPntr = self.ast.make_node(value="&&",child=None, brother=None)
        self.ast.add_child(expressionPntr,ctx.e1.value_attr)
        self.ast.add_child(expressionPntr,ctx.e2.value_attr)
        ctx.value_attr = expressionPntr

    #'{' ( statement )* '}'
    def exitStatement_statement(self, ctx:miniJavaParser.Statement_statementContext):
        statementPntr = self.ast.make_node(value="statements",child=None, brother=None)
        i=1
        while i<len(ctx.children)-1:
            self.ast.add_child(statementPntr,ctx.children[i].value_attr)
            i+=1
        ctx.value_attr=statementPntr
        self.ast.root = statementPntr
        self.print_tree(node=self.ast.root, level=1)

    def exitStatement_if(self, ctx: miniJavaParser.Statement_ifContext):
        statementPntr = self.ast.make_node(value="if",child=None, brother=None)
        self.ast.add_child(statementPntr,ctx.expression().value_attr)
        self.ast.add_child(statementPntr,ctx.st1.value_attr)
        else_node=self.ast.make_node(value="else",child=None, brother=None)
        self.ast.add_child(else_node,ctx.st2.value_attr)
        self.ast.add_child(statementPntr,else_node)
        ctx.value_attr = statementPntr
        self.ast.root = statementPntr
        self.print_tree(node=self.ast.root, level=1)

    def exitStatement_while(self, ctx: miniJavaParser.Statement_whileContext):
        statementPntr = self.ast.make_node(value="while", child=None, brother=None)
        self.ast.add_child(statementPntr, ctx.expression().value_attr)
        self.ast.add_child(statementPntr, ctx.st1.value_attr)
        ctx.value_attr = statementPntr
        self.ast.root = statementPntr
        self.print_tree(node=self.ast.root, level=1)

    def exitStatement_println(self, ctx: miniJavaParser.Statement_printlnContext):
        statementPntr = self.ast.make_node(value="println", child=None, brother=None)
        self.ast.add_child(statementPntr, ctx.expression().value_attr)
        ctx.value_attr = statementPntr
        self.ast.root = statementPntr
        self.print_tree(node=self.ast.root, level=1)

    def exitStatement_value_assignment(self, ctx: miniJavaParser.Statement_value_assignmentContext):
        statementPntr = self.ast.make_node(value="=", child=None, brother=None)
        self.ast.add_child(statementPntr, ctx.expression().value_attr)
        ctx.value_attr = statementPntr
        self.ast.root = statementPntr
        self.print_tree(node=self.ast.root, level=1)


    def exitStatement_array_cell_assignment(self, ctx: miniJavaParser.Statement_array_cell_assignmentContext):
        statementPntr = self.ast.make_node(value="=", child=None, brother=None)
        self.ast.add_child(statementPntr, ctx.e2.value_attr)
        self.ast.add_child(ctx.identifier().value_attr, ctx.e1.value_attr)
        ctx.value_attr = statementPntr
        self.ast.root = statementPntr
        self.print_tree(node=self.ast.root, level=1)


    # def exitMethodDeclaration(self, ctx:miniJavaParser.MethodDeclarationContext):
    #     method_declaration_pointer=self.ast.make_node(value="method",child=None, brother=None)
    #
    #     ctx.value_attr = method_declaration_pointer
    #
    #     self.ast.root = assPntr
    #     self.print_tree(node=self.ast.root, level=1)

    # def exitMainClass(self, ctx:miniJavaParser.MainClassContext):
    #
    #
    # def exitClassDeclaration(self, ctx: miniJavaParser.ClassDeclarationContext):
    #
    # def exitProgram(self, ctx: miniJavaParser.ProgramContext):
    #


class TreeNode:
    def __init__(self, value, child, brother):
        self.value = value
        self.child = child
        self.brother = brother

    # def __repr__(self):
    #     return self.value


class AST:
    def __init__(self):
        self.root = None
        self.current = None

    def make_node(self, value, child, brother):
        # value = value + ' ' + repr(round(random.random(), 4))
        tree_node = TreeNode(value, child, brother)
        self.current = tree_node
        return tree_node

    def add_child(self, node, new_child):
        if node.child is None:
            node.child = new_child
        else:
            self.current = node.child
            while self.current.brother is not None:
                self.current = self.current.brother
            self.current.brother = new_child
        self.current = new_child

    def add_brother(self, node, new_brother):
        if node.brother is None:
            node.brother = new_brother
        else:
            self.current = node.brother
            while self.current.brother is not None:
                self.current = self.current.brother
            self.current.brother = new_brother
        self.current = new_brother
