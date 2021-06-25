from antlr4 import *
from gen.MiniJavaLexer import MiniJavaLexer
from gen.MiniJavaParser import MiniJavaParser
from MiniJavaListener import MiniJavaListener

def main():
    # input_address = "QuickSort.java"
    input_address = "test.java"
    print("Reading file ...")
    try:
        input_file = FileStream(input_address)
        lexer = MiniJavaLexer(input_file)
        stream = CommonTokenStream(lexer)
        parser = MiniJavaParser(stream)
        tree = parser.program()
        listener = MiniJavaListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        # print('{\'className\': ' + str(listener.get_class_names()) +
        #       ", \'methodName\': " + str(listener.get_method_name()) +
        #       ", \'variableName\': " + str(listener.variable_name) +
        #       "}")
        # print("-----")
    except UnicodeDecodeError:
        print("UnicodeDecodeError occurred in reading " + input_address)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


