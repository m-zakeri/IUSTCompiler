# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars\Expr2.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("D\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13\61\n\13\r\13\16\13")
        buf.write("\62\3\f\6\f\66\n\f\r\f\16\f\67\3\r\6\r;\n\r\r\r\16\r<")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\2\27\2\31\f\33\r\3\2\5\4\2C")
        buf.write("\\c|\3\2\62;\4\2\13\13\"\"\2D\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2")
        buf.write("\13%\3\2\2\2\r\'\3\2\2\2\17)\3\2\2\2\21+\3\2\2\2\23-\3")
        buf.write("\2\2\2\25\60\3\2\2\2\27\65\3\2\2\2\31:\3\2\2\2\33@\3\2")
        buf.write("\2\2\35\36\7*\2\2\36\4\3\2\2\2\37 \7+\2\2 \6\3\2\2\2!")
        buf.write("\"\7-\2\2\"\b\3\2\2\2#$\7/\2\2$\n\3\2\2\2%&\7,\2\2&\f")
        buf.write("\3\2\2\2\'(\7\61\2\2(\16\3\2\2\2)*\7?\2\2*\20\3\2\2\2")
        buf.write("+,\5\25\13\2,\22\3\2\2\2-.\5\27\f\2.\24\3\2\2\2/\61\t")
        buf.write("\2\2\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3")
        buf.write("\2\2\2\63\26\3\2\2\2\64\66\t\3\2\2\65\64\3\2\2\2\66\67")
        buf.write("\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\30\3\2\2\29;\t\4\2")
        buf.write("\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=>\3\2\2\2>")
        buf.write("?\b\r\2\2?\32\3\2\2\2@A\7\f\2\2AB\3\2\2\2BC\b\16\3\2C")
        buf.write("\34\3\2\2\2\6\2\62\67<\4\2\3\2\b\2\2")
        return buf.getvalue()


class Expr2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    Plus = 3
    MINUS = 4
    MUL = 5
    DIVIDE = 6
    ASSIGN = 7
    Id = 8
    Number = 9
    Whitespace = 10
    Newline = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'='", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "Plus", "MINUS", "MUL", "DIVIDE", "ASSIGN", "Id", "Number", 
            "Whitespace", "Newline" ]

    ruleNames = [ "T__0", "T__1", "Plus", "MINUS", "MUL", "DIVIDE", "ASSIGN", 
                  "Id", "Number", "IDENTIFIER", "NUMBER", "Whitespace", 
                  "Newline" ]

    grammarFileName = "Expr2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


