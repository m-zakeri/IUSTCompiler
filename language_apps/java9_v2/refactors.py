"""
The `refactors`script implements different refactoring operations for Java language


"""
__version__ = '0.1.1'
__author__ = 'Morteza'

from typing import List

from antlr4 import *
from antlr4.Token import CommonToken
from antlr4.TokenStreamRewriter import TokenStreamRewriter

from language_apps.java9_v2.gen.Java9_v2Lexer import Java9_v2Lexer
from language_apps.java9_v2.gen.Java9_v2Parser import Java9_v2Parser
from language_apps.java9_v2.gen.Java9_v2Listener import Java9_v2Listener
from language_apps.java9_v2.gen.Java9_v2Visitor import Java9_v2Visitor


class EncapsulateFieldRefactoringListener(Java9_v2Listener):
    """
    This class implements the encapsulate-filed refactoring.
    Encapsulate-field: Make a public field private and provide accessors.
    """

    def __init__(self, common_token_stream: CommonTokenStream = None,
                 field_identifier: str = None):
        """
        :param common_token_stream:
        """
        self.token_stream = common_token_stream
        self.field_identifier = field_identifier
        # Move all the tokens in the source language_apps in a buffer, token_stream_rewriter.
        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')

    def exitFieldDeclaration(self, ctx: Java9_v2Parser.FieldDeclarationContext):
        if ctx.variableDeclaratorList().getText() == self.field_identifier:
            if ctx.fieldModifier(0).getText() == 'public':
                self.token_stream_rewriter.replaceRange(
                    from_idx=ctx.fieldModifier(0).start.tokenIndex,
                    to_idx=ctx.fieldModifier(0).stop.tokenIndex,
                    text='private')

            # generate accessor and mutator methods
            # Accessor body
            new_code = '\n\t'
            new_code += 'public ' + ctx.unannType().getText() + ' get' + str.capitalize(self.field_identifier)
            new_code += '() { \n\t\t return this.' + self.field_identifier + ';' + '\n\t}'

            # Mutator body
            new_code += '\n\t'
            new_code += 'public void set' + str.capitalize(self.field_identifier)
            new_code += '(' + ctx.unannType().getText() + ' ' + self.field_identifier + ') { \n\t\t'
            new_code += 'this.' + self.field_identifier + ' = ' + self.field_identifier + ';' + '\n\t}\n'

            self.token_stream_rewriter.insertAfter(ctx.stop.tokenIndex, new_code)

            hidden = self.token_stream.getHiddenTokensToRight(ctx.stop.tokenIndex)
            self.token_stream_rewriter.replaceRange(from_idx=hidden[0].tokenIndex,
                                                    to_idx=hidden[-1].tokenIndex,
                                                    text='\t/*End of accessor and mutator methods!*/\n\n')

    def exitAssignment(self, ctx: Java9_v2Parser.AssignmentContext):
        if ctx.leftHandSide().getText() == self.field_identifier or \
                ctx.leftHandSide().getText() == 'this.' + self.field_identifier:
            expr_code = self.token_stream_rewriter.getText(program_name=self.token_stream_rewriter.DEFAULT_PROGRAM_NAME,
                                                           start=ctx.expression().start.tokenIndex,
                                                           stop=ctx.expression().stop.tokenIndex)
            # new_code = 'this.set' + str.capitalize(self.field_identifier) + '(' + ctx.expression().getText() + ')'
            new_code = 'this.set' + str.capitalize(self.field_identifier) + '(' + expr_code + ')'
            self.token_stream_rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_code)

    def exitPrimary(self, ctx: Java9_v2Parser.PrimaryContext):
        if ctx.getChildCount() == 2:
            if ctx.getText() == 'this.' + self.field_identifier or ctx.getText() == self.field_identifier:
                new_code = 'this.get' + str.capitalize(self.field_identifier) + '()'
                self.token_stream_rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_code)

    def enterCompilationUnit1(self, ctx: Java9_v2Parser.CompilationUnit1Context):
        hidden = self.token_stream.getHiddenTokensToLeft(ctx.start.tokenIndex)
        self.token_stream_rewriter.replaceRange(from_idx=hidden[0].tokenIndex,
                                                to_idx=hidden[-1].tokenIndex,
                                                text='/*After refactoring (Refactored version)*/\n')


class ManipulateComments(Java9_v2Listener):
    """
    Add the author name in the first of every comment in the program
    """

    def __init__(self, common_token_stream: CommonTokenStream = None, name: str = None):
        self.token_stream = common_token_stream
        self.name = name
        # Move all the tokens in the source language_apps in a buffer, token_stream_rewriter.
        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')

    def enterCompilationUnit1(self, ctx: Java9_v2Parser.CompilationUnit1Context):
        hidden: List[CommonToken] = self.token_stream.getHiddenTokensToLeft(
            ctx.start.tokenIndex,
            channel=-1
        )
        # print(hidden)
        # print(hidden[-1].start)
        self.token_stream_rewriter.replaceIndex(
            index=hidden[0].tokenIndex,
            text=f'{hidden[0].text[:2]} {self.name} {hidden[0].text[2:]}'
        )


class ManipulateComments2(Java9_v2Listener):
    """
    Add the author name in the first of every comment in the program
    """

    def __init__(self, common_token_stream: CommonTokenStream = None, name: str = None):
        self.token_stream = common_token_stream
        self.name = name
        # Move all the tokens in the source language_apps in a buffer, token_stream_rewriter.
        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')

    def enterEveryRule(self, ctx: ParserRuleContext):
        hidden_left: List[CommonToken] = self.token_stream.getHiddenTokensToLeft(
            ctx.start.tokenIndex,
            channel=-1
        )

        hidden_right: List[CommonToken] = self.token_stream.getHiddenTokensToRight(
            ctx.start.tokenIndex,
            channel=-1
        )

        if hidden_left is None and hidden_right is None:
            return
        elif hidden_left is None:
            hidden = hidden_right
        elif hidden_right is None:
            hidden = hidden_left
        else:
            hidden = hidden_left + hidden_right

        index = 0
        index_in_list = 0
        is_there_a_comment = False
        for i, token in enumerate(hidden):
            if token.type in [117, 118]:
                index = token.tokenIndex
                index_in_list = i
                is_there_a_comment = True
                break
        if is_there_a_comment:
            self.token_stream_rewriter.replaceIndex(
                index=index,
                text=f'{hidden[index_in_list].text[:2]} @author: {self.name} {hidden[index_in_list].text[2:]}'
            )

        # self.token_stream_rewriter.getDefaultText()
