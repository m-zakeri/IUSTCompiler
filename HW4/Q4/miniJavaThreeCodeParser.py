# Generated from .\miniJavaThreeCode.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from AddressCodeConverter import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write("\u0124\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\7\2\32")
        buf.write("\n\2\f\2\16\2\35\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\5\48\n\4\3\4\3\4\7\4<\n\4\f\4\16\4?\13")
        buf.write("\4\3\4\7\4B\n\4\f\4\16\4E\13\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6W\n\6\f\6")
        buf.write("\16\6Z\13\6\5\6\\\n\6\3\6\3\6\3\6\7\6a\n\6\f\6\16\6d\13")
        buf.write("\6\3\6\3\6\3\6\7\6i\n\6\f\6\16\6l\13\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7y\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\7\b\u0080\n\b\f\b\16\b\u0083\13\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00bb\n\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00e3\n")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\7\t\u0111\n\t\f\t\16\t\u0114\13\t\5\t")
        buf.write("\u0116\n\t\3\t\3\t\7\t\u011a\n\t\f\t\16\t\u011d\13\t\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\2\3\20\f\2\4\6\b\n\f\16\20\22")
        buf.write("\24\2\5\3\2\32\34\3\2\35\36\3\2\'*\2\u0139\2\26\3\2\2")
        buf.write("\2\4 \3\2\2\2\6\63\3\2\2\2\bH\3\2\2\2\nL\3\2\2\2\fx\3")
        buf.write("\2\2\2\16\u00ba\3\2\2\2\20\u00e2\3\2\2\2\22\u011e\3\2")
        buf.write("\2\2\24\u0121\3\2\2\2\26\27\b\2\1\2\27\33\5\4\3\2\30\32")
        buf.write("\5\6\4\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33")
        buf.write("\34\3\2\2\2\34\36\3\2\2\2\35\33\3\2\2\2\36\37\7\2\2\3")
        buf.write("\37\3\3\2\2\2 !\7\3\2\2!\"\5\22\n\2\"#\7\4\2\2#$\7\5\2")
        buf.write("\2$%\7\6\2\2%&\7\7\2\2&\'\7\b\2\2\'(\7\t\2\2()\7\n\2\2")
        buf.write(")*\7\13\2\2*+\7\f\2\2+,\5\22\n\2,-\7\r\2\2-.\7\4\2\2.")
        buf.write("/\5\16\b\2/\60\7\16\2\2\60\61\7\16\2\2\61\62\b\3\1\2\62")
        buf.write("\5\3\2\2\2\63\64\7\3\2\2\64\67\5\22\n\2\65\66\7\17\2\2")
        buf.write("\668\5\22\n\2\67\65\3\2\2\2\678\3\2\2\289\3\2\2\29=\7")
        buf.write("\4\2\2:<\5\b\5\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2")
        buf.write("\2>C\3\2\2\2?=\3\2\2\2@B\5\n\6\2A@\3\2\2\2BE\3\2\2\2C")
        buf.write("A\3\2\2\2CD\3\2\2\2DF\3\2\2\2EC\3\2\2\2FG\7\16\2\2G\7")
        buf.write("\3\2\2\2HI\5\f\7\2IJ\5\22\n\2JK\7\20\2\2K\t\3\2\2\2LM")
        buf.write("\7\5\2\2MN\5\f\7\2NO\5\22\n\2O[\7\t\2\2PQ\5\f\7\2QX\5")
        buf.write("\22\n\2RS\7\21\2\2ST\5\f\7\2TU\5\22\n\2UW\3\2\2\2VR\3")
        buf.write("\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y\\\3\2\2\2ZX\3\2")
        buf.write("\2\2[P\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]^\7\r\2\2^b\7\4\2")
        buf.write("\2_a\5\b\5\2`_\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2c")
        buf.write("j\3\2\2\2db\3\2\2\2ef\5\16\b\2fg\b\6\1\2gi\3\2\2\2he\3")
        buf.write("\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2km\3\2\2\2lj\3\2\2")
        buf.write("\2mn\7\22\2\2no\5\20\t\2op\7\20\2\2pq\7\16\2\2q\13\3\2")
        buf.write("\2\2rs\7\23\2\2st\7\13\2\2ty\7\f\2\2uy\7\24\2\2vy\7\23")
        buf.write("\2\2wy\5\22\n\2xr\3\2\2\2xu\3\2\2\2xv\3\2\2\2xw\3\2\2")
        buf.write("\2y\r\3\2\2\2z{\7\4\2\2{\u0081\b\b\1\2|}\5\16\b\2}~\b")
        buf.write("\b\1\2~\u0080\3\2\2\2\177|\3\2\2\2\u0080\u0083\3\2\2\2")
        buf.write("\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2")
        buf.write("\2\2\u0083\u0081\3\2\2\2\u0084\u00bb\7\16\2\2\u0085\u0086")
        buf.write("\7\25\2\2\u0086\u0087\7\t\2\2\u0087\u0088\5\20\t\2\u0088")
        buf.write("\u0089\7\r\2\2\u0089\u008a\5\16\b\2\u008a\u008b\7\26\2")
        buf.write("\2\u008b\u008c\5\16\b\2\u008c\u008d\b\b\1\2\u008d\u008e")
        buf.write("\b\b\1\2\u008e\u008f\b\b\1\2\u008f\u0090\b\b\1\2\u0090")
        buf.write("\u0091\b\b\1\2\u0091\u0092\b\b\1\2\u0092\u0093\b\b\1\2")
        buf.write("\u0093\u0094\b\b\1\2\u0094\u00bb\3\2\2\2\u0095\u0096\7")
        buf.write("\27\2\2\u0096\u0097\7\t\2\2\u0097\u0098\5\20\t\2\u0098")
        buf.write("\u0099\7\r\2\2\u0099\u009a\5\16\b\2\u009a\u009b\b\b\1")
        buf.write("\2\u009b\u009c\b\b\1\2\u009c\u009d\b\b\1\2\u009d\u009e")
        buf.write("\b\b\1\2\u009e\u009f\b\b\1\2\u009f\u00a0\b\b\1\2\u00a0")
        buf.write("\u00bb\3\2\2\2\u00a1\u00a2\7\30\2\2\u00a2\u00a3\7\t\2")
        buf.write("\2\u00a3\u00a4\5\20\t\2\u00a4\u00a5\7\r\2\2\u00a5\u00a6")
        buf.write("\7\20\2\2\u00a6\u00bb\3\2\2\2\u00a7\u00a8\5\22\n\2\u00a8")
        buf.write("\u00a9\7\31\2\2\u00a9\u00aa\5\20\t\2\u00aa\u00ab\7\20")
        buf.write("\2\2\u00ab\u00ac\b\b\1\2\u00ac\u00ad\b\b\1\2\u00ad\u00bb")
        buf.write("\3\2\2\2\u00ae\u00af\5\22\n\2\u00af\u00b0\7\13\2\2\u00b0")
        buf.write("\u00b1\5\20\t\2\u00b1\u00b2\7\f\2\2\u00b2\u00b3\7\31\2")
        buf.write("\2\u00b3\u00b4\5\20\t\2\u00b4\u00b5\7\20\2\2\u00b5\u00b6")
        buf.write("\b\b\1\2\u00b6\u00b7\b\b\1\2\u00b7\u00b8\b\b\1\2\u00b8")
        buf.write("\u00b9\b\b\1\2\u00b9\u00bb\3\2\2\2\u00baz\3\2\2\2\u00ba")
        buf.write("\u0085\3\2\2\2\u00ba\u0095\3\2\2\2\u00ba\u00a1\3\2\2\2")
        buf.write("\u00ba\u00a7\3\2\2\2\u00ba\u00ae\3\2\2\2\u00bb\17\3\2")
        buf.write("\2\2\u00bc\u00bd\b\t\1\2\u00bd\u00be\5\24\13\2\u00be\u00bf")
        buf.write("\b\t\1\2\u00bf\u00e3\3\2\2\2\u00c0\u00c1\7!\2\2\u00c1")
        buf.write("\u00e3\b\t\1\2\u00c2\u00c3\7\"\2\2\u00c3\u00e3\b\t\1\2")
        buf.write("\u00c4\u00c5\5\22\n\2\u00c5\u00c6\b\t\1\2\u00c6\u00e3")
        buf.write("\3\2\2\2\u00c7\u00e3\7#\2\2\u00c8\u00c9\7$\2\2\u00c9\u00ca")
        buf.write("\7\23\2\2\u00ca\u00cb\7\13\2\2\u00cb\u00cc\5\20\t\2\u00cc")
        buf.write("\u00cd\7\f\2\2\u00cd\u00e3\3\2\2\2\u00ce\u00cf\7$\2\2")
        buf.write("\u00cf\u00d0\5\22\n\2\u00d0\u00d1\7\t\2\2\u00d1\u00d2")
        buf.write("\7\r\2\2\u00d2\u00e3\3\2\2\2\u00d3\u00d4\7%\2\2\u00d4")
        buf.write("\u00d5\5\20\t\4\u00d5\u00d6\b\t\1\2\u00d6\u00d7\b\t\1")
        buf.write("\2\u00d7\u00d8\b\t\1\2\u00d8\u00d9\b\t\1\2\u00d9\u00e3")
        buf.write("\3\2\2\2\u00da\u00db\7\t\2\2\u00db\u00dc\5\20\t\2\u00dc")
        buf.write("\u00dd\7\r\2\2\u00dd\u00de\b\t\1\2\u00de\u00df\b\t\1\2")
        buf.write("\u00df\u00e0\b\t\1\2\u00e0\u00e1\b\t\1\2\u00e1\u00e3\3")
        buf.write("\2\2\2\u00e2\u00bc\3\2\2\2\u00e2\u00c0\3\2\2\2\u00e2\u00c2")
        buf.write("\3\2\2\2\u00e2\u00c4\3\2\2\2\u00e2\u00c7\3\2\2\2\u00e2")
        buf.write("\u00c8\3\2\2\2\u00e2\u00ce\3\2\2\2\u00e2\u00d3\3\2\2\2")
        buf.write("\u00e2\u00da\3\2\2\2\u00e3\u011b\3\2\2\2\u00e4\u00e5\f")
        buf.write("\20\2\2\u00e5\u00e6\t\2\2\2\u00e6\u00e7\5\20\t\21\u00e7")
        buf.write("\u00e8\b\t\1\2\u00e8\u00e9\b\t\1\2\u00e9\u00ea\b\t\1\2")
        buf.write("\u00ea\u00eb\b\t\1\2\u00eb\u00ec\b\t\1\2\u00ec\u00ed\b")
        buf.write("\t\1\2\u00ed\u011a\3\2\2\2\u00ee\u00ef\f\17\2\2\u00ef")
        buf.write("\u00f0\t\3\2\2\u00f0\u00f1\5\20\t\20\u00f1\u00f2\b\t\1")
        buf.write("\2\u00f2\u00f3\b\t\1\2\u00f3\u00f4\b\t\1\2\u00f4\u00f5")
        buf.write("\b\t\1\2\u00f5\u00f6\b\t\1\2\u00f6\u00f7\b\t\1\2\u00f7")
        buf.write("\u011a\3\2\2\2\u00f8\u00f9\f\16\2\2\u00f9\u00fa\7\13\2")
        buf.write("\2\u00fa\u00fb\5\20\t\2\u00fb\u00fc\7\f\2\2\u00fc\u00fd")
        buf.write("\b\t\1\2\u00fd\u00fe\b\t\1\2\u00fe\u00ff\b\t\1\2\u00ff")
        buf.write("\u0100\b\t\1\2\u0100\u0101\b\t\1\2\u0101\u011a\3\2\2\2")
        buf.write("\u0102\u0103\f\r\2\2\u0103\u0104\7\37\2\2\u0104\u0105")
        buf.write("\7 \2\2\u0105\u0106\b\t\1\2\u0106\u0107\b\t\1\2\u0107")
        buf.write("\u0108\b\t\1\2\u0108\u011a\b\t\1\2\u0109\u010a\f\f\2\2")
        buf.write("\u010a\u010b\7\37\2\2\u010b\u010c\5\22\n\2\u010c\u0115")
        buf.write("\7\t\2\2\u010d\u0112\5\20\t\2\u010e\u010f\7\21\2\2\u010f")
        buf.write("\u0111\5\20\t\2\u0110\u010e\3\2\2\2\u0111\u0114\3\2\2")
        buf.write("\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0116")
        buf.write("\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u010d\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\7\r\2\2")
        buf.write("\u0118\u011a\3\2\2\2\u0119\u00e4\3\2\2\2\u0119\u00ee\3")
        buf.write("\2\2\2\u0119\u00f8\3\2\2\2\u0119\u0102\3\2\2\2\u0119\u0109")
        buf.write("\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\21\3\2\2\2\u011d\u011b\3\2\2\2\u011e")
        buf.write("\u011f\7&\2\2\u011f\u0120\b\n\1\2\u0120\23\3\2\2\2\u0121")
        buf.write("\u0122\t\4\2\2\u0122\25\3\2\2\2\22\33\67=CX[bjx\u0081")
        buf.write("\u00ba\u00e2\u0112\u0115\u0119\u011b")
        return buf.getvalue()


class miniJavaThreeCodeParser ( Parser ):

    grammarFileName = "miniJavaThreeCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'{'", "'public'", "'static'", 
                     "'void'", "'main'", "'('", "'String'", "'['", "']'", 
                     "')'", "'}'", "'extends'", "';'", "','", "'return'", 
                     "'int'", "'boolean'", "'if'", "'else'", "'while'", 
                     "'System.out.println'", "'='", "'+'", "'-'", "'*'", 
                     "'&&'", "'<'", "'.'", "'length'", "'true'", "'false'", 
                     "'this'", "'new'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "DECIMAL_LITERAL", "HEX_LITERAL", "OCT_LITERAL", 
                      "BINARY_LITERAL", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_main_class = 1
    RULE_class_declaration = 2
    RULE_var_declaration = 3
    RULE_method_declaration = 4
    RULE_type_r = 5
    RULE_statement = 6
    RULE_expression = 7
    RULE_identifier_r = 8
    RULE_integerLiteral = 9

    ruleNames =  [ "program", "main_class", "class_declaration", "var_declaration", 
                   "method_declaration", "type_r", "statement", "expression", 
                   "identifier_r", "integerLiteral" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    IDENTIFIER=36
    DECIMAL_LITERAL=37
    HEX_LITERAL=38
    OCT_LITERAL=39
    BINARY_LITERAL=40
    WS=41
    COMMENT=42
    LINE_COMMENT=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    child_ptrs={}
    tmp_counter=0
    label_counter=0

    def new_label(self):
        self.label_counter+=1
        return 'Label_{}'.format(str(self.label_counter))
    def new_tmp(self):
        self.tmp_counter+=1
        return 'T_{}'.format(str(self.tmp_counter))

    def current_tmp(self):
        return 'T_{}'.format(str(self.tmp_counter))




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_class(self):
            return self.getTypedRuleContext(miniJavaThreeCodeParser.Main_classContext,0)


        def EOF(self):
            return self.getToken(miniJavaThreeCodeParser.EOF, 0)

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.Class_declarationContext,i)


        def getRuleIndex(self):
            return miniJavaThreeCodeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = miniJavaThreeCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            print("BEGINS:")
            self.state = 21
            self.main_class()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miniJavaThreeCodeParser.T__0:
                self.state = 22
                self.class_declaration()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(miniJavaThreeCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None # StatementContext

        def identifier_r(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.Identifier_rContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.Identifier_rContext,i)


        def statement(self):
            return self.getTypedRuleContext(miniJavaThreeCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return miniJavaThreeCodeParser.RULE_main_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_class" ):
                listener.enterMain_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_class" ):
                listener.exitMain_class(self)




    def main_class(self):

        localctx = miniJavaThreeCodeParser.Main_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(miniJavaThreeCodeParser.T__0)
            self.state = 31
            self.identifier_r()
            self.state = 32
            self.match(miniJavaThreeCodeParser.T__1)
            self.state = 33
            self.match(miniJavaThreeCodeParser.T__2)
            self.state = 34
            self.match(miniJavaThreeCodeParser.T__3)
            self.state = 35
            self.match(miniJavaThreeCodeParser.T__4)
            self.state = 36
            self.match(miniJavaThreeCodeParser.T__5)
            self.state = 37
            self.match(miniJavaThreeCodeParser.T__6)
            self.state = 38
            self.match(miniJavaThreeCodeParser.T__7)
            self.state = 39
            self.match(miniJavaThreeCodeParser.T__8)
            self.state = 40
            self.match(miniJavaThreeCodeParser.T__9)
            self.state = 41
            self.identifier_r()
            self.state = 42
            self.match(miniJavaThreeCodeParser.T__10)
            self.state = 43
            self.match(miniJavaThreeCodeParser.T__1)
            self.state = 44
            localctx.s = self.statement()
            self.state = 45
            self.match(miniJavaThreeCodeParser.T__11)
            self.state = 46
            self.match(miniJavaThreeCodeParser.T__11)
            print(localctx.s.v)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_r(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.Identifier_rContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.Identifier_rContext,i)


        def var_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.Var_declarationContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.Var_declarationContext,i)


        def method_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.Method_declarationContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.Method_declarationContext,i)


        def getRuleIndex(self):
            return miniJavaThreeCodeParser.RULE_class_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_declaration" ):
                listener.enterClass_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_declaration" ):
                listener.exitClass_declaration(self)




    def class_declaration(self):

        localctx = miniJavaThreeCodeParser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(miniJavaThreeCodeParser.T__0)
            self.state = 50
            self.identifier_r()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==miniJavaThreeCodeParser.T__12:
                self.state = 51
                self.match(miniJavaThreeCodeParser.T__12)
                self.state = 52
                self.identifier_r()


            self.state = 55
            self.match(miniJavaThreeCodeParser.T__1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaThreeCodeParser.T__16) | (1 << miniJavaThreeCodeParser.T__17) | (1 << miniJavaThreeCodeParser.IDENTIFIER))) != 0):
                self.state = 56
                self.var_declaration()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miniJavaThreeCodeParser.T__2:
                self.state = 62
                self.method_declaration()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(miniJavaThreeCodeParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_a = None # Type_rContext
            self.identifier = None # Identifier_rContext

        def type_r(self):
            return self.getTypedRuleContext(miniJavaThreeCodeParser.Type_rContext,0)


        def identifier_r(self):
            return self.getTypedRuleContext(miniJavaThreeCodeParser.Identifier_rContext,0)


        def getRuleIndex(self):
            return miniJavaThreeCodeParser.RULE_var_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_declaration" ):
                listener.enterVar_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_declaration" ):
                listener.exitVar_declaration(self)




    def var_declaration(self):

        localctx = miniJavaThreeCodeParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            localctx.type_a = self.type_r()
            self.state = 71
            localctx.identifier = self.identifier_r()
            self.state = 72
            self.match(miniJavaThreeCodeParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None # StatementContext

        def type_r(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.Type_rContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.Type_rContext,i)


        def identifier_r(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.Identifier_rContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.Identifier_rContext,i)


        def expression(self):
            return self.getTypedRuleContext(miniJavaThreeCodeParser.ExpressionContext,0)


        def var_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.Var_declarationContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.Var_declarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.StatementContext,i)


        def getRuleIndex(self):
            return miniJavaThreeCodeParser.RULE_method_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_declaration" ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_declaration" ):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = miniJavaThreeCodeParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(miniJavaThreeCodeParser.T__2)
            self.state = 75
            self.type_r()
            self.state = 76
            self.identifier_r()
            self.state = 77
            self.match(miniJavaThreeCodeParser.T__6)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaThreeCodeParser.T__16) | (1 << miniJavaThreeCodeParser.T__17) | (1 << miniJavaThreeCodeParser.IDENTIFIER))) != 0):
                self.state = 78
                self.type_r()
                self.state = 79
                self.identifier_r()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==miniJavaThreeCodeParser.T__14:
                    self.state = 80
                    self.match(miniJavaThreeCodeParser.T__14)
                    self.state = 81
                    self.type_r()
                    self.state = 82
                    self.identifier_r()
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 91
            self.match(miniJavaThreeCodeParser.T__10)
            self.state = 92
            self.match(miniJavaThreeCodeParser.T__1)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 93
                    self.var_declaration() 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaThreeCodeParser.T__1) | (1 << miniJavaThreeCodeParser.T__18) | (1 << miniJavaThreeCodeParser.T__20) | (1 << miniJavaThreeCodeParser.T__21) | (1 << miniJavaThreeCodeParser.IDENTIFIER))) != 0):
                self.state = 99
                localctx.s = self.statement()
                print(localctx.s.v)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(miniJavaThreeCodeParser.T__15)
            self.state = 108
            self.expression(0)
            self.state = 109
            self.match(miniJavaThreeCodeParser.T__13)
            self.state = 110
            self.match(miniJavaThreeCodeParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_rContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.identifier = None # Identifier_rContext

        def identifier_r(self):
            return self.getTypedRuleContext(miniJavaThreeCodeParser.Identifier_rContext,0)


        def getRuleIndex(self):
            return miniJavaThreeCodeParser.RULE_type_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_r" ):
                listener.enterType_r(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_r" ):
                listener.exitType_r(self)




    def type_r(self):

        localctx = miniJavaThreeCodeParser.Type_rContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type_r)
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(miniJavaThreeCodeParser.T__16)
                self.state = 113
                self.match(miniJavaThreeCodeParser.T__8)
                self.state = 114
                self.match(miniJavaThreeCodeParser.T__9)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(miniJavaThreeCodeParser.T__17)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.match(miniJavaThreeCodeParser.T__16)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 117
                localctx.identifier = self.identifier_r()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = str()
            self.type_a = str()
            self.prev_v = str()
            self.s = None # StatementContext
            self.exp = None # ExpressionContext
            self.ifs = None # StatementContext
            self.es = None # StatementContext
            self.identifier = None # Identifier_rContext
            self._identifier_r = None # Identifier_rContext
            self.exp1 = None # ExpressionContext
            self.exp2 = None # ExpressionContext

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.StatementContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.ExpressionContext,i)


        def identifier_r(self):
            return self.getTypedRuleContext(miniJavaThreeCodeParser.Identifier_rContext,0)


        def getRuleIndex(self):
            return miniJavaThreeCodeParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = miniJavaThreeCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(miniJavaThreeCodeParser.T__1)
                localctx.v=''
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaThreeCodeParser.T__1) | (1 << miniJavaThreeCodeParser.T__18) | (1 << miniJavaThreeCodeParser.T__20) | (1 << miniJavaThreeCodeParser.T__21) | (1 << miniJavaThreeCodeParser.IDENTIFIER))) != 0):
                    self.state = 122
                    localctx.s = self.statement()
                    localctx.v+=localctx.s.v+'\n'
                    self.state = 129
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 130
                self.match(miniJavaThreeCodeParser.T__11)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(miniJavaThreeCodeParser.T__18)
                self.state = 132
                self.match(miniJavaThreeCodeParser.T__6)
                self.state = 133
                localctx.exp = self.expression(0)
                self.state = 134
                self.match(miniJavaThreeCodeParser.T__10)
                self.state = 135
                localctx.ifs = self.statement()
                self.state = 136
                self.match(miniJavaThreeCodeParser.T__19)
                self.state = 137
                localctx.es = self.statement()
                if_go = self.new_label()
                else_go = self.new_label()
                localctx.v += '\n'.join([item for item in localctx.exp.tmps])+'\n'
                localctx.v+='\t\t if ({}) goto {}\n'.format(localctx.exp.v , if_go)
                localctx.v+=localctx.es.v
                localctx.v+='\t\t goto {}\n'.format(else_go)
                localctx.v+='{}:{}'.format(if_go,localctx.ifs.v)
                localctx.v+='{}:{}'.format(else_go,'\t\t')
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.match(miniJavaThreeCodeParser.T__20)
                self.state = 148
                self.match(miniJavaThreeCodeParser.T__6)
                self.state = 149
                localctx.exp = self.expression(0)
                self.state = 150
                self.match(miniJavaThreeCodeParser.T__10)
                self.state = 151
                localctx.s = self.statement()
                go_while=self.new_label()
                inner_while=self.new_label()
                localctx.v+='\t\t goto {}\n'.format(go_while)
                localctx.v+='{}:{}'.format(inner_while,localctx.s.v)
                localctx.v+=go_while + '\n'.join([item for item in localctx.exp.tmps])+'\n'
                localctx.v+='\t\t if({}) goto {}\n'.format(localctx.exp.v,inner_while)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
                self.match(miniJavaThreeCodeParser.T__21)
                self.state = 160
                self.match(miniJavaThreeCodeParser.T__6)
                self.state = 161
                self.expression(0)
                self.state = 162
                self.match(miniJavaThreeCodeParser.T__10)
                self.state = 163
                self.match(miniJavaThreeCodeParser.T__13)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                localctx.identifier = self.identifier_r()
                self.state = 166
                self.match(miniJavaThreeCodeParser.T__22)
                self.state = 167
                localctx.exp = self.expression(0)
                self.state = 168
                self.match(miniJavaThreeCodeParser.T__13)
                localctx.v='\n'.join([item for item in localctx.exp.tmps])+'\n'
                localctx.v+='\t\t {} = {}'.format(localctx.identifier.v , localctx.exp.v)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 172
                localctx.identifier = localctx._identifier_r = self.identifier_r()
                self.state = 173
                self.match(miniJavaThreeCodeParser.T__8)
                self.state = 174
                localctx.exp1 = self.expression(0)
                self.state = 175
                self.match(miniJavaThreeCodeParser.T__9)
                self.state = 176
                self.match(miniJavaThreeCodeParser.T__22)
                self.state = 177
                localctx.exp2 = self.expression(0)
                self.state = 178
                self.match(miniJavaThreeCodeParser.T__13)
                localctx.v='\n'.join([item for item in localctx.exp1.tmps])+'\n'
                localctx.v+='\n'.join([item for item in localctx.exp2.tmps])+'\n'
                tmp=self.new_tmp()
                localctx.v+=AddressCodeConverter.array_initializer(localctx._identifier_r.v , localctx.exp1.v , localctx.exp2.v , tmp)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = str()
            self.type_a = str()
            self.prev_v = str()
            self.tmps = []
            self.expl = None # ExpressionContext
            self.exp1 = None # ExpressionContext
            self.exp = None # ExpressionContext
            self._integerLiteral = None # IntegerLiteralContext
            self.identifier = None # Identifier_rContext
            self.op = None # Token
            self.expr = None # ExpressionContext
            self.exp2 = None # ExpressionContext

        def integerLiteral(self):
            return self.getTypedRuleContext(miniJavaThreeCodeParser.IntegerLiteralContext,0)


        def identifier_r(self):
            return self.getTypedRuleContext(miniJavaThreeCodeParser.Identifier_rContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaThreeCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(miniJavaThreeCodeParser.ExpressionContext,i)


        def getRuleIndex(self):
            return miniJavaThreeCodeParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = miniJavaThreeCodeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 187
                localctx._integerLiteral = self.integerLiteral()
                localctx.type_a,localctx.v,localctx.prev_v='INT' , (None if localctx._integerLiteral is None else self._input.getText(localctx._integerLiteral.start,localctx._integerLiteral.stop)),None
                pass

            elif la_ == 2:
                self.state = 190
                self.match(miniJavaThreeCodeParser.T__30)
                localctx.type_a,localctx.v,localctx.prev_v='BOOL', 'true',None
                pass

            elif la_ == 3:
                self.state = 192
                self.match(miniJavaThreeCodeParser.T__31)
                localctx.type_a,localctx.v,localctx.prev_v='BOOL', 'false',None
                pass

            elif la_ == 4:
                self.state = 194
                localctx.identifier = self.identifier_r()
                localctx.type_a,localctx.v,localctx.prev_v= (localctx.identifier.type_a, localctx.identifier.v , None) if localctx.identifier.type_a=='NOTDEFIENED' else (localctx.type_a, localctx.v,localctx.prev_v)
                pass

            elif la_ == 5:
                self.state = 197
                self.match(miniJavaThreeCodeParser.T__32)
                pass

            elif la_ == 6:
                self.state = 198
                self.match(miniJavaThreeCodeParser.T__33)
                self.state = 199
                self.match(miniJavaThreeCodeParser.T__16)
                self.state = 200
                self.match(miniJavaThreeCodeParser.T__8)
                self.state = 201
                self.expression(0)
                self.state = 202
                self.match(miniJavaThreeCodeParser.T__9)
                pass

            elif la_ == 7:
                self.state = 204
                self.match(miniJavaThreeCodeParser.T__33)
                self.state = 205
                self.identifier_r()
                self.state = 206
                self.match(miniJavaThreeCodeParser.T__6)
                self.state = 207
                self.match(miniJavaThreeCodeParser.T__10)
                pass

            elif la_ == 8:
                self.state = 209
                self.match(miniJavaThreeCodeParser.T__34)
                self.state = 210
                localctx.exp = self.expression(2)
                localctx.tmps=localctx.exp.tmps
                localctx.type_a='BOOL'
                temp , localctx.tmps , localctx.exp.v = (self.new_tmp() ,localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),localctx.exp.prev_v)] , self.current_tmp()) if localctx.exp.prev_v is not None else (None , localctx.tmps , localctx.exp.v)
                localctx.prev_v = localctx.v = '!' + localctx.exp.v
                pass

            elif la_ == 9:
                self.state = 216
                self.match(miniJavaThreeCodeParser.T__6)
                self.state = 217
                localctx.exp = self.expression(0)
                self.state = 218
                self.match(miniJavaThreeCodeParser.T__10)
                localctx.type_a=localctx.exp.type_a
                localctx.v = localctx.exp.v
                localctx.prev_v=localctx.exp.prev_v
                localctx.tmps=localctx.exp.tmps
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 279
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = miniJavaThreeCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.expl = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 226
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 227
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaThreeCodeParser.T__23) | (1 << miniJavaThreeCodeParser.T__24) | (1 << miniJavaThreeCodeParser.T__25))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 228
                        localctx.expr = self.expression(15)
                        tmps = localctx.expl.tmps
                        localctx.type_a = 'INT'
                        temp , localctx.tmps , localctx.expl.v = (self.new_tmp() , localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),localctx.expl.prev_v)] , self.current_tmp() ) if localctx.expl.prev_v is not None else (None , localctx.tmps , localctx.expl.v)
                        localctx.tmps += localctx.expr.tmps
                        temp , localctx.tmps , localctx.expr.v = (self.new_tmp() , localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),localctx.expr.prev_v)] , self.current_tmp() ) if localctx.expr.prev_v is not None else (None , localctx.tmps , localctx.expr.v)
                        localctx.prev_v= localctx.v = localctx.expl.v + (None if localctx.op is None else localctx.op.text) + localctx.expr.v
                        pass

                    elif la_ == 2:
                        localctx = miniJavaThreeCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.expl = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 236
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 237
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==miniJavaThreeCodeParser.T__26 or _la==miniJavaThreeCodeParser.T__27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 238
                        localctx.expr = self.expression(14)
                        tmps = localctx.expl.tmps
                        localctx.type_a = 'BOOL'
                        temp , localctx.tmps , localctx.expl.v = (self.new_tmp() , localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),localctx.expl.prev_v)] , self.current_tmp()) if localctx.expl.prev_v is not None else (None , localctx.tmps , localctx.expl.v) 
                        localctx.tmps += localctx.expr.tmps
                        temp , localctx.tmps , localctx.expr.v = (self.new_tmp() , localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),localctx.expr.prev_v)] , self.current_tmp()) if localctx.expr.prev_v is not None else (None , localctx.tmps , localctx.expr.v)
                        localctx.prev_v= localctx.v = localctx.expl.v + (None if localctx.op is None else localctx.op.text) + localctx.expr.v
                        pass

                    elif la_ == 3:
                        localctx = miniJavaThreeCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.exp1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 246
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 247
                        self.match(miniJavaThreeCodeParser.T__8)
                        self.state = 248
                        localctx.exp2 = self.expression(0)
                        self.state = 249
                        self.match(miniJavaThreeCodeParser.T__9)
                        localctx.tmps , localctx.type_a = localctx.exp1.tmps + localctx.exp2.tmps , 'INT'
                        temp , localctx.tmps , localctx.exp2.v = (self.new_tmp() ,localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),localctx.exp2.prev_v)] , self.current_tmp()) if localctx.exp2.prev_v is not None else (None , localctx.tmps , localctx.exp2.v)
                        temp = self.new_tmp()
                        localctx.tmps += AddressCodeConverter.tmp_array(temp , localctx.exp1.v , localctx.exp2.v)
                        localctx.prev_v=localctx.v='*'+temp
                        pass

                    elif la_ == 4:
                        localctx = miniJavaThreeCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 256
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 257
                        self.match(miniJavaThreeCodeParser.T__28)
                        self.state = 258
                        self.match(miniJavaThreeCodeParser.T__29)
                        localctx.tmps=localctx.exp.tmps
                        localctx.type_a='INT'
                        temp , localctx.tmps , localctx.exp.v = (self.new_tmp() ,localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),localctx.exp.prev_v)] , self.current_tmp()) if localctx.exp.prev_v is not None else (None , localctx.tmps , localctx.exp.v)
                        localctx.prev_v = localctx.v = localctx.exp.v + '.length'
                        pass

                    elif la_ == 5:
                        localctx = miniJavaThreeCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 263
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 264
                        self.match(miniJavaThreeCodeParser.T__28)
                        self.state = 265
                        self.identifier_r()
                        self.state = 266
                        self.match(miniJavaThreeCodeParser.T__6)
                        self.state = 275
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaThreeCodeParser.T__6) | (1 << miniJavaThreeCodeParser.T__30) | (1 << miniJavaThreeCodeParser.T__31) | (1 << miniJavaThreeCodeParser.T__32) | (1 << miniJavaThreeCodeParser.T__33) | (1 << miniJavaThreeCodeParser.T__34) | (1 << miniJavaThreeCodeParser.IDENTIFIER) | (1 << miniJavaThreeCodeParser.DECIMAL_LITERAL) | (1 << miniJavaThreeCodeParser.HEX_LITERAL) | (1 << miniJavaThreeCodeParser.OCT_LITERAL) | (1 << miniJavaThreeCodeParser.BINARY_LITERAL))) != 0):
                            self.state = 267
                            self.expression(0)
                            self.state = 272
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==miniJavaThreeCodeParser.T__14:
                                self.state = 268
                                self.match(miniJavaThreeCodeParser.T__14)
                                self.state = 269
                                self.expression(0)
                                self.state = 274
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 277
                        self.match(miniJavaThreeCodeParser.T__10)
                        pass

             
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Identifier_rContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = str()
            self.type_a = str()
            self._IDENTIFIER = None # Token

        def IDENTIFIER(self):
            return self.getToken(miniJavaThreeCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return miniJavaThreeCodeParser.RULE_identifier_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier_r" ):
                listener.enterIdentifier_r(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier_r" ):
                listener.exitIdentifier_r(self)




    def identifier_r(self):

        localctx = miniJavaThreeCodeParser.Identifier_rContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifier_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            localctx._IDENTIFIER = self.match(miniJavaThreeCodeParser.IDENTIFIER)
            localctx.v , localctx.type_a = (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) , 'NOTDEFIENED'
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_LITERAL(self):
            return self.getToken(miniJavaThreeCodeParser.DECIMAL_LITERAL, 0)

        def HEX_LITERAL(self):
            return self.getToken(miniJavaThreeCodeParser.HEX_LITERAL, 0)

        def OCT_LITERAL(self):
            return self.getToken(miniJavaThreeCodeParser.OCT_LITERAL, 0)

        def BINARY_LITERAL(self):
            return self.getToken(miniJavaThreeCodeParser.BINARY_LITERAL, 0)

        def getRuleIndex(self):
            return miniJavaThreeCodeParser.RULE_integerLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerLiteral" ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerLiteral" ):
                listener.exitIntegerLiteral(self)




    def integerLiteral(self):

        localctx = miniJavaThreeCodeParser.IntegerLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_integerLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaThreeCodeParser.DECIMAL_LITERAL) | (1 << miniJavaThreeCodeParser.HEX_LITERAL) | (1 << miniJavaThreeCodeParser.OCT_LITERAL) | (1 << miniJavaThreeCodeParser.BINARY_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         




