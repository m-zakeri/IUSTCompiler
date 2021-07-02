from antlr4 import *
from Gen.MiniJavaLexer import MiniJavaLexer
from Gen.MiniJavaParser import MiniJavaParser
from Gen.MiniJavaListener import MiniJavaListener

import argparse


class ConstructThreeAddressCodeListener(MiniJavaListener):
    def __init__(self):
        self.TempCount = 0
        self.LabelCount = 0


    def CreateTemp(self):
        self.TempCount += 1
        return 'T' + str(self.TempCount)

    def CreateLabel(self):
        self.LabelCount += 1
        return 'L' + str(self.LabelCount)

    def exitOperations_expression(self, ctx: MiniJavaParser.Operations_expressionContext):
        if ctx.expression(0).type_attr != ctx.expression(1).type_attr:
            print('Semantic error: Cannot operate {0} and {1}'.format(ctx.expression(0).type_attr,
                                                                      ctx.expression(1).type_attr))
            quit(-1)
        else:
            ctx.type_attr = ctx.expression(0).type_attr
            ctx.value_attr = self.CreateTemp()

            print('{0} = {1} {2} {3}'.format(ctx.value_attr, ctx.expression(0).getText(), ctx.operations().getText(),
                                             ctx.expression(1).getText()))

    def exitNot_expression(self, ctx: MiniJavaParser.Not_expressionContext):
        ctx.type_attr = ctx.expression().type_attr
        ctx.value_attr = self.CreateTemp()

        print('{0} = !{1}'.format(ctx.value_attr, ctx.expression().value_attr))

    def exitEqual_statement(self, ctx: MiniJavaParser.Equal_statementContext):
        ctx.value_attr = ctx.identifier().getText() + ' = ' + ctx.expression().value_attr

        print(ctx.value_attr)

    def exitEqual_array_statement(self, ctx: MiniJavaParser.Equal_array_statementContext):
        ctx.value_attr = ctx.identifier().getText() + '[' + ctx.expression(0).value_attr + ']' + ' = ' + ctx.expression(
            1).value_attr

        print(ctx.value_attr)

    def exitIf_statement(self, ctx:MiniJavaParser.If_statementContext):
        ctx.statement(1).value_attr = self.CreateLabel() + ' ' + ctx.statement(1).value_attr
        ctx.value_attr = 'if' + '!(' + ctx.expression().value_attr + ') ' + 'goto ' + ctx.statement(1).value_attr[0 : 2]

        print(ctx.value_attr, ctx.statement(1).value_attr)

    def enterWhile_statement(self, ctx:MiniJavaParser.While_statementContext):
        ctx.value_attr = self.CreateLabel() + ' if' + '!(' + ctx.expression().value_attr + ')' + 'goto' + ctx.statement().value_attr[0 : 2]
        ctx.statement().value_attr = ctx.statement().value_attr + 'goto'
        ctx.statement().value_attr = self.CreateLabel() + ctx.statement().value_attr

        print(ctx.value_attr)


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
    code_generator_listener = ConstructThreeAddressCodeListener()

    # Step 7: Walk parse tree with a customized listener (Automatically)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=code_generator_listener)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'input.txt')
    args = argparser.parse_args()
    main(args)
