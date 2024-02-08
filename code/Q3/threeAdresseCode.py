import argparse

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from Q3.gen.MiniJavaLexer import MiniJavaLexer
from Q3.gen.MiniJavaListener import MiniJavaListener
from Q3.gen.MiniJavaParser import MiniJavaParser


class ThreeAddressCode(MiniJavaListener):
    def __init__(self):
        self.temp_counter = 0
        self.label_counter = 0

    def CreateTemp(self):
        self.temp_counter += 1
        return 'T' + str(self.temp_counter)

    def CreateLabel(self):
        self.label_counter += 1
        return 'L' + str(self.label_counter)

    def is_temp(self, var:str):
        if var[0] == 'T':
            return True

    def remove_temp(self):
        self.temp_counter -= 1

    def exitIf_statment(self, ctx : MiniJavaParser.If_statmentContext):
        ctx.statement(1).value_attr = self.CreateLabel() + ' ' + ctx.statement(1).value_attr
        ctx.value_attr = 'if' + '!(' + ctx.expression().value_attr + ') ' + 'goto ' + ctx.statement(1).value_attr[0: 2]

        print(ctx.value_attr, ctx.statement(1).value_attr)

    def enterWhile_statment(self, ctx:MiniJavaParser.While_statmentContext):
        ctx.value_attr = self.CreateLabel() + ' if' + '!(' + ctx.expression().value_attr + ')' + 'goto' + ctx.statement().value_attr[0 : 2]
        ctx.statement().value_attr = ctx.statement().value_attr + 'goto'
        ctx.statement().value_attr = self.CreateLabel() + ctx.statement().value_attr

        print(ctx.value_attr)

    def exitEqual_statmentContext(self, ctx: MiniJavaParser.Equal_statmentContext):
        ctx.value_attr = ctx.identifier().getText() + ' = ' + ctx.expression().value_attr

        print(ctx.value_attr)

def main(args):
    stream = FileStream(args.file, encoding='utf8')
    print('Input code:\n{0}'.format(stream))
    print('Result:')

    lexer = MiniJavaLexer(stream)

    token_stream = CommonTokenStream(lexer)

    parser = MiniJavaParser(token_stream)

    parse_tree = parser.program()

    code_generator_listener = ThreeAddressCode()

    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=code_generator_listener)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'input.txt')
    args = argparser.parse_args()
    main(args)

