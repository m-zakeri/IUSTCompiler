import argparse

from ..gen.MiniJavaLexer import MiniJavaLexer
from ..gen.MiniJavaParser import MiniJavaParser, CommonTokenStream
from ..gen.MiniJavaListener import MiniJavaListener, ParseTreeWalker, FileStream

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

