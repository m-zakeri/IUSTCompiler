# Generated from .\miniJavaAST.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write("\u00dc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\7\2\27\n\2\f\2\16\2\32")
        buf.write("\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\64")
        buf.write("\n\4\3\4\3\4\7\48\n\4\f\4\16\4;\13\4\3\4\7\4>\n\4\f\4")
        buf.write("\16\4A\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\7\6S\n\6\f\6\16\6V\13\6\5\6X\n")
        buf.write("\6\3\6\3\6\3\6\7\6]\n\6\f\6\16\6`\13\6\3\6\7\6c\n\6\f")
        buf.write("\6\16\6f\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\5\7s\n\7\3\b\3\b\7\bw\n\b\f\b\16\bz\13\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\5\b\u009e\n\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\5\t\u00b7\n\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t")
        buf.write("\u00cb\n\t\f\t\16\t\u00ce\13\t\5\t\u00d0\n\t\3\t\3\t\7")
        buf.write("\t\u00d4\n\t\f\t\16\t\u00d7\13\t\3\n\3\n\3\n\3\n\2\3\20")
        buf.write("\13\2\4\6\b\n\f\16\20\22\2\3\3\2\32\36\2\u00f1\2\24\3")
        buf.write("\2\2\2\4\35\3\2\2\2\6/\3\2\2\2\bD\3\2\2\2\nH\3\2\2\2\f")
        buf.write("r\3\2\2\2\16\u009d\3\2\2\2\20\u00b6\3\2\2\2\22\u00d8\3")
        buf.write("\2\2\2\24\30\5\4\3\2\25\27\5\6\4\2\26\25\3\2\2\2\27\32")
        buf.write("\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\33\3\2\2\2\32")
        buf.write("\30\3\2\2\2\33\34\7\2\2\3\34\3\3\2\2\2\35\36\7\3\2\2\36")
        buf.write("\37\5\22\n\2\37 \7\4\2\2 !\7\5\2\2!\"\7\6\2\2\"#\7\7\2")
        buf.write("\2#$\7\b\2\2$%\7\t\2\2%&\7\n\2\2&\'\7\13\2\2\'(\7\f\2")
        buf.write("\2()\5\22\n\2)*\7\r\2\2*+\7\4\2\2+,\5\16\b\2,-\7\16\2")
        buf.write("\2-.\7\16\2\2.\5\3\2\2\2/\60\7\3\2\2\60\63\5\22\n\2\61")
        buf.write("\62\7\17\2\2\62\64\5\22\n\2\63\61\3\2\2\2\63\64\3\2\2")
        buf.write("\2\64\65\3\2\2\2\659\7\4\2\2\668\5\b\5\2\67\66\3\2\2\2")
        buf.write("8;\3\2\2\29\67\3\2\2\29:\3\2\2\2:?\3\2\2\2;9\3\2\2\2<")
        buf.write(">\5\n\6\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@B\3")
        buf.write("\2\2\2A?\3\2\2\2BC\7\16\2\2C\7\3\2\2\2DE\5\f\7\2EF\5\22")
        buf.write("\n\2FG\7\20\2\2G\t\3\2\2\2HI\7\5\2\2IJ\5\f\7\2JK\5\22")
        buf.write("\n\2KW\7\t\2\2LM\5\f\7\2MT\5\22\n\2NO\7\21\2\2OP\5\f\7")
        buf.write("\2PQ\5\22\n\2QS\3\2\2\2RN\3\2\2\2SV\3\2\2\2TR\3\2\2\2")
        buf.write("TU\3\2\2\2UX\3\2\2\2VT\3\2\2\2WL\3\2\2\2WX\3\2\2\2XY\3")
        buf.write("\2\2\2YZ\7\r\2\2Z^\7\4\2\2[]\5\b\5\2\\[\3\2\2\2]`\3\2")
        buf.write("\2\2^\\\3\2\2\2^_\3\2\2\2_d\3\2\2\2`^\3\2\2\2ac\5\16\b")
        buf.write("\2ba\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2eg\3\2\2\2f")
        buf.write("d\3\2\2\2gh\7\22\2\2hi\5\20\t\2ij\7\20\2\2jk\7\16\2\2")
        buf.write("k\13\3\2\2\2lm\7\23\2\2mn\7\13\2\2ns\7\f\2\2os\7\24\2")
        buf.write("\2ps\7\23\2\2qs\5\22\n\2rl\3\2\2\2ro\3\2\2\2rp\3\2\2\2")
        buf.write("rq\3\2\2\2s\r\3\2\2\2tx\7\4\2\2uw\5\16\b\2vu\3\2\2\2w")
        buf.write("z\3\2\2\2xv\3\2\2\2xy\3\2\2\2y{\3\2\2\2zx\3\2\2\2{\u009e")
        buf.write("\7\16\2\2|}\7\25\2\2}~\7\t\2\2~\177\5\20\t\2\177\u0080")
        buf.write("\7\r\2\2\u0080\u0081\5\16\b\2\u0081\u0082\7\26\2\2\u0082")
        buf.write("\u0083\5\16\b\2\u0083\u009e\3\2\2\2\u0084\u0085\7\27\2")
        buf.write("\2\u0085\u0086\7\t\2\2\u0086\u0087\5\20\t\2\u0087\u0088")
        buf.write("\7\r\2\2\u0088\u0089\5\16\b\2\u0089\u009e\3\2\2\2\u008a")
        buf.write("\u008b\7\30\2\2\u008b\u008c\7\t\2\2\u008c\u008d\5\20\t")
        buf.write("\2\u008d\u008e\7\r\2\2\u008e\u008f\7\20\2\2\u008f\u009e")
        buf.write("\3\2\2\2\u0090\u0091\5\22\n\2\u0091\u0092\7\31\2\2\u0092")
        buf.write("\u0093\5\20\t\2\u0093\u0094\7\20\2\2\u0094\u009e\3\2\2")
        buf.write("\2\u0095\u0096\5\22\n\2\u0096\u0097\7\13\2\2\u0097\u0098")
        buf.write("\5\20\t\2\u0098\u0099\7\f\2\2\u0099\u009a\7\31\2\2\u009a")
        buf.write("\u009b\5\20\t\2\u009b\u009c\7\20\2\2\u009c\u009e\3\2\2")
        buf.write("\2\u009dt\3\2\2\2\u009d|\3\2\2\2\u009d\u0084\3\2\2\2\u009d")
        buf.write("\u008a\3\2\2\2\u009d\u0090\3\2\2\2\u009d\u0095\3\2\2\2")
        buf.write("\u009e\17\3\2\2\2\u009f\u00a0\b\t\1\2\u00a0\u00b7\7\'")
        buf.write("\2\2\u00a1\u00b7\7!\2\2\u00a2\u00b7\7\"\2\2\u00a3\u00b7")
        buf.write("\5\22\n\2\u00a4\u00b7\7#\2\2\u00a5\u00a6\7$\2\2\u00a6")
        buf.write("\u00a7\7\23\2\2\u00a7\u00a8\7\13\2\2\u00a8\u00a9\5\20")
        buf.write("\t\2\u00a9\u00aa\7\f\2\2\u00aa\u00b7\3\2\2\2\u00ab\u00ac")
        buf.write("\7$\2\2\u00ac\u00ad\5\22\n\2\u00ad\u00ae\7\t\2\2\u00ae")
        buf.write("\u00af\7\r\2\2\u00af\u00b7\3\2\2\2\u00b0\u00b1\7%\2\2")
        buf.write("\u00b1\u00b7\5\20\t\4\u00b2\u00b3\7\t\2\2\u00b3\u00b4")
        buf.write("\5\20\t\2\u00b4\u00b5\7\r\2\2\u00b5\u00b7\3\2\2\2\u00b6")
        buf.write("\u009f\3\2\2\2\u00b6\u00a1\3\2\2\2\u00b6\u00a2\3\2\2\2")
        buf.write("\u00b6\u00a3\3\2\2\2\u00b6\u00a4\3\2\2\2\u00b6\u00a5\3")
        buf.write("\2\2\2\u00b6\u00ab\3\2\2\2\u00b6\u00b0\3\2\2\2\u00b6\u00b2")
        buf.write("\3\2\2\2\u00b7\u00d5\3\2\2\2\u00b8\u00b9\f\17\2\2\u00b9")
        buf.write("\u00ba\t\2\2\2\u00ba\u00d4\5\20\t\20\u00bb\u00bc\f\16")
        buf.write("\2\2\u00bc\u00bd\7\13\2\2\u00bd\u00be\5\20\t\2\u00be\u00bf")
        buf.write("\7\f\2\2\u00bf\u00d4\3\2\2\2\u00c0\u00c1\f\r\2\2\u00c1")
        buf.write("\u00c2\7\37\2\2\u00c2\u00d4\7 \2\2\u00c3\u00c4\f\f\2\2")
        buf.write("\u00c4\u00c5\7\37\2\2\u00c5\u00c6\5\22\n\2\u00c6\u00cf")
        buf.write("\7\t\2\2\u00c7\u00cc\5\20\t\2\u00c8\u00c9\7\21\2\2\u00c9")
        buf.write("\u00cb\5\20\t\2\u00ca\u00c8\3\2\2\2\u00cb\u00ce\3\2\2")
        buf.write("\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00d0")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00c7\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\7\r\2\2")
        buf.write("\u00d2\u00d4\3\2\2\2\u00d3\u00b8\3\2\2\2\u00d3\u00bb\3")
        buf.write("\2\2\2\u00d3\u00c0\3\2\2\2\u00d3\u00c3\3\2\2\2\u00d4\u00d7")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("\21\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\7&\2\2\u00d9")
        buf.write("\u00da\b\n\1\2\u00da\23\3\2\2\2\22\30\639?TW^drx\u009d")
        buf.write("\u00b6\u00cc\u00cf\u00d3\u00d5")
        return buf.getvalue()


class miniJavaASTParser ( Parser ):

    grammarFileName = "miniJavaAST.g4"

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

    ruleNames =  [ "program", "main_class", "class_declaration", "var_declaration", 
                   "method_declaration", "type_r", "statement", "expression", 
                   "identifier_r" ]

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




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = 'program'

        def main_class(self):
            return self.getTypedRuleContext(miniJavaASTParser.Main_classContext,0)


        def EOF(self):
            return self.getToken(miniJavaASTParser.EOF, 0)

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.Class_declarationContext,i)


        def getRuleIndex(self):
            return miniJavaASTParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = miniJavaASTParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.main_class()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miniJavaASTParser.T__0:
                self.state = 19
                self.class_declaration()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self.match(miniJavaASTParser.EOF)
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
            self.v = 'main_class'
            self.s = None # StatementContext

        def identifier_r(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.Identifier_rContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.Identifier_rContext,i)


        def statement(self):
            return self.getTypedRuleContext(miniJavaASTParser.StatementContext,0)


        def getRuleIndex(self):
            return miniJavaASTParser.RULE_main_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_class" ):
                listener.enterMain_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_class" ):
                listener.exitMain_class(self)




    def main_class(self):

        localctx = miniJavaASTParser.Main_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(miniJavaASTParser.T__0)
            self.state = 28
            self.identifier_r()
            self.state = 29
            self.match(miniJavaASTParser.T__1)
            self.state = 30
            self.match(miniJavaASTParser.T__2)
            self.state = 31
            self.match(miniJavaASTParser.T__3)
            self.state = 32
            self.match(miniJavaASTParser.T__4)
            self.state = 33
            self.match(miniJavaASTParser.T__5)
            self.state = 34
            self.match(miniJavaASTParser.T__6)
            self.state = 35
            self.match(miniJavaASTParser.T__7)
            self.state = 36
            self.match(miniJavaASTParser.T__8)
            self.state = 37
            self.match(miniJavaASTParser.T__9)
            self.state = 38
            self.identifier_r()
            self.state = 39
            self.match(miniJavaASTParser.T__10)
            self.state = 40
            self.match(miniJavaASTParser.T__1)
            self.state = 41
            localctx.s = self.statement()
            self.state = 42
            self.match(miniJavaASTParser.T__11)
            self.state = 43
            self.match(miniJavaASTParser.T__11)
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
            self.v = 'class_declaration'

        def identifier_r(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.Identifier_rContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.Identifier_rContext,i)


        def var_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.Var_declarationContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.Var_declarationContext,i)


        def method_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.Method_declarationContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.Method_declarationContext,i)


        def getRuleIndex(self):
            return miniJavaASTParser.RULE_class_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_declaration" ):
                listener.enterClass_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_declaration" ):
                listener.exitClass_declaration(self)




    def class_declaration(self):

        localctx = miniJavaASTParser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(miniJavaASTParser.T__0)
            self.state = 46
            self.identifier_r()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==miniJavaASTParser.T__12:
                self.state = 47
                self.match(miniJavaASTParser.T__12)
                self.state = 48
                self.identifier_r()


            self.state = 51
            self.match(miniJavaASTParser.T__1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaASTParser.T__16) | (1 << miniJavaASTParser.T__17) | (1 << miniJavaASTParser.IDENTIFIER))) != 0):
                self.state = 52
                self.var_declaration()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miniJavaASTParser.T__2:
                self.state = 58
                self.method_declaration()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(miniJavaASTParser.T__11)
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
            self.v = 'var_dec'

        def type_r(self):
            return self.getTypedRuleContext(miniJavaASTParser.Type_rContext,0)


        def identifier_r(self):
            return self.getTypedRuleContext(miniJavaASTParser.Identifier_rContext,0)


        def getRuleIndex(self):
            return miniJavaASTParser.RULE_var_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_declaration" ):
                listener.enterVar_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_declaration" ):
                listener.exitVar_declaration(self)




    def var_declaration(self):

        localctx = miniJavaASTParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.type_r()
            self.state = 67
            self.identifier_r()
            self.state = 68
            self.match(miniJavaASTParser.T__13)
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
            self.v = 'method'

        def type_r(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.Type_rContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.Type_rContext,i)


        def identifier_r(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.Identifier_rContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.Identifier_rContext,i)


        def expression(self):
            return self.getTypedRuleContext(miniJavaASTParser.ExpressionContext,0)


        def var_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.Var_declarationContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.Var_declarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.StatementContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.StatementContext,i)


        def getRuleIndex(self):
            return miniJavaASTParser.RULE_method_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_declaration" ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_declaration" ):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = miniJavaASTParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(miniJavaASTParser.T__2)
            self.state = 71
            self.type_r()
            self.state = 72
            self.identifier_r()
            self.state = 73
            self.match(miniJavaASTParser.T__6)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaASTParser.T__16) | (1 << miniJavaASTParser.T__17) | (1 << miniJavaASTParser.IDENTIFIER))) != 0):
                self.state = 74
                self.type_r()
                self.state = 75
                self.identifier_r()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==miniJavaASTParser.T__14:
                    self.state = 76
                    self.match(miniJavaASTParser.T__14)
                    self.state = 77
                    self.type_r()
                    self.state = 78
                    self.identifier_r()
                    self.state = 84
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 87
            self.match(miniJavaASTParser.T__10)
            self.state = 88
            self.match(miniJavaASTParser.T__1)
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 89
                    self.var_declaration() 
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaASTParser.T__1) | (1 << miniJavaASTParser.T__18) | (1 << miniJavaASTParser.T__20) | (1 << miniJavaASTParser.T__21) | (1 << miniJavaASTParser.IDENTIFIER))) != 0):
                self.state = 95
                self.statement()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(miniJavaASTParser.T__15)
            self.state = 102
            self.expression(0)
            self.state = 103
            self.match(miniJavaASTParser.T__13)
            self.state = 104
            self.match(miniJavaASTParser.T__11)
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
            self.v = 'type'

        def identifier_r(self):
            return self.getTypedRuleContext(miniJavaASTParser.Identifier_rContext,0)


        def getRuleIndex(self):
            return miniJavaASTParser.RULE_type_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_r" ):
                listener.enterType_r(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_r" ):
                listener.exitType_r(self)




    def type_r(self):

        localctx = miniJavaASTParser.Type_rContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type_r)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(miniJavaASTParser.T__16)
                self.state = 107
                self.match(miniJavaASTParser.T__8)
                self.state = 108
                self.match(miniJavaASTParser.T__9)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(miniJavaASTParser.T__17)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.match(miniJavaASTParser.T__16)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.identifier_r()
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
            self.v = 'statement'

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.StatementContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.StatementContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.ExpressionContext,i)


        def identifier_r(self):
            return self.getTypedRuleContext(miniJavaASTParser.Identifier_rContext,0)


        def getRuleIndex(self):
            return miniJavaASTParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = miniJavaASTParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(miniJavaASTParser.T__1)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaASTParser.T__1) | (1 << miniJavaASTParser.T__18) | (1 << miniJavaASTParser.T__20) | (1 << miniJavaASTParser.T__21) | (1 << miniJavaASTParser.IDENTIFIER))) != 0):
                    self.state = 115
                    self.statement()
                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 121
                self.match(miniJavaASTParser.T__11)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.match(miniJavaASTParser.T__18)
                self.state = 123
                self.match(miniJavaASTParser.T__6)
                self.state = 124
                self.expression(0)
                self.state = 125
                self.match(miniJavaASTParser.T__10)
                self.state = 126
                self.statement()
                self.state = 127
                self.match(miniJavaASTParser.T__19)
                self.state = 128
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.match(miniJavaASTParser.T__20)
                self.state = 131
                self.match(miniJavaASTParser.T__6)
                self.state = 132
                self.expression(0)
                self.state = 133
                self.match(miniJavaASTParser.T__10)
                self.state = 134
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.match(miniJavaASTParser.T__21)
                self.state = 137
                self.match(miniJavaASTParser.T__6)
                self.state = 138
                self.expression(0)
                self.state = 139
                self.match(miniJavaASTParser.T__10)
                self.state = 140
                self.match(miniJavaASTParser.T__13)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 142
                self.identifier_r()
                self.state = 143
                self.match(miniJavaASTParser.T__22)
                self.state = 144
                self.expression(0)
                self.state = 145
                self.match(miniJavaASTParser.T__13)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 147
                self.identifier_r()
                self.state = 148
                self.match(miniJavaASTParser.T__8)
                self.state = 149
                self.expression(0)
                self.state = 150
                self.match(miniJavaASTParser.T__9)
                self.state = 151
                self.match(miniJavaASTParser.T__22)
                self.state = 152
                self.expression(0)
                self.state = 153
                self.match(miniJavaASTParser.T__13)
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
            self.v = 'expression'

        def DECIMAL_LITERAL(self):
            return self.getToken(miniJavaASTParser.DECIMAL_LITERAL, 0)

        def identifier_r(self):
            return self.getTypedRuleContext(miniJavaASTParser.Identifier_rContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniJavaASTParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(miniJavaASTParser.ExpressionContext,i)


        def getRuleIndex(self):
            return miniJavaASTParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = miniJavaASTParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 158
                self.match(miniJavaASTParser.DECIMAL_LITERAL)
                pass

            elif la_ == 2:
                self.state = 159
                self.match(miniJavaASTParser.T__30)
                pass

            elif la_ == 3:
                self.state = 160
                self.match(miniJavaASTParser.T__31)
                pass

            elif la_ == 4:
                self.state = 161
                self.identifier_r()
                pass

            elif la_ == 5:
                self.state = 162
                self.match(miniJavaASTParser.T__32)
                pass

            elif la_ == 6:
                self.state = 163
                self.match(miniJavaASTParser.T__33)
                self.state = 164
                self.match(miniJavaASTParser.T__16)
                self.state = 165
                self.match(miniJavaASTParser.T__8)
                self.state = 166
                self.expression(0)
                self.state = 167
                self.match(miniJavaASTParser.T__9)
                pass

            elif la_ == 7:
                self.state = 169
                self.match(miniJavaASTParser.T__33)
                self.state = 170
                self.identifier_r()
                self.state = 171
                self.match(miniJavaASTParser.T__6)
                self.state = 172
                self.match(miniJavaASTParser.T__10)
                pass

            elif la_ == 8:
                self.state = 174
                self.match(miniJavaASTParser.T__34)
                self.state = 175
                self.expression(2)
                pass

            elif la_ == 9:
                self.state = 176
                self.match(miniJavaASTParser.T__6)
                self.state = 177
                self.expression(0)
                self.state = 178
                self.match(miniJavaASTParser.T__10)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 209
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = miniJavaASTParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 182
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 183
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaASTParser.T__23) | (1 << miniJavaASTParser.T__24) | (1 << miniJavaASTParser.T__25) | (1 << miniJavaASTParser.T__26) | (1 << miniJavaASTParser.T__27))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 184
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = miniJavaASTParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 186
                        self.match(miniJavaASTParser.T__8)
                        self.state = 187
                        self.expression(0)
                        self.state = 188
                        self.match(miniJavaASTParser.T__9)
                        pass

                    elif la_ == 3:
                        localctx = miniJavaASTParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 190
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 191
                        self.match(miniJavaASTParser.T__28)
                        self.state = 192
                        self.match(miniJavaASTParser.T__29)
                        pass

                    elif la_ == 4:
                        localctx = miniJavaASTParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 193
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 194
                        self.match(miniJavaASTParser.T__28)
                        self.state = 195
                        self.identifier_r()
                        self.state = 196
                        self.match(miniJavaASTParser.T__6)
                        self.state = 205
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miniJavaASTParser.T__6) | (1 << miniJavaASTParser.T__30) | (1 << miniJavaASTParser.T__31) | (1 << miniJavaASTParser.T__32) | (1 << miniJavaASTParser.T__33) | (1 << miniJavaASTParser.T__34) | (1 << miniJavaASTParser.IDENTIFIER) | (1 << miniJavaASTParser.DECIMAL_LITERAL))) != 0):
                            self.state = 197
                            self.expression(0)
                            self.state = 202
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==miniJavaASTParser.T__14:
                                self.state = 198
                                self.match(miniJavaASTParser.T__14)
                                self.state = 199
                                self.expression(0)
                                self.state = 204
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 207
                        self.match(miniJavaASTParser.T__10)
                        pass

             
                self.state = 213
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
            self._IDENTIFIER = None # Token

        def IDENTIFIER(self):
            return self.getToken(miniJavaASTParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return miniJavaASTParser.RULE_identifier_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier_r" ):
                listener.enterIdentifier_r(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier_r" ):
                listener.exitIdentifier_r(self)




    def identifier_r(self):

        localctx = miniJavaASTParser.Identifier_rContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifier_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            localctx._IDENTIFIER = self.match(miniJavaASTParser.IDENTIFIER)
            localctx.v=(None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)
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
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         




