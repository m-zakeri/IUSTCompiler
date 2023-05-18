# Generated from /home/loop/Desktop/Ass/Compiler/HW4/ast.g4 by ANTLR 4.9.1
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3&")
        buf.write("\u00f0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\7\2!\n\2\f\2\16\2$\13\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\5\7D\n\7\3\7\3\7\7\7H\n\7\f\7\16\7K\13\7\3\7\7")
        buf.write("\7N\n\7\f\7\16\7Q\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\tc\n\t\f\t\16\tf\13")
        buf.write("\t\5\th\n\t\3\t\3\t\3\t\3\n\3\n\7\no\n\n\f\n\16\nr\13")
        buf.write("\n\3\n\7\nu\n\n\f\n\16\nx\13\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\5\13\u0085\n\13\3\f\3\f\7\f")
        buf.write("\u0089\n\f\f\f\16\f\u008c\13\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00b0\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\5\r\u00c9\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00de\n\r\f")
        buf.write("\r\16\r\u00e1\13\r\5\r\u00e3\n\r\3\r\3\r\7\r\u00e7\n\r")
        buf.write("\f\r\16\r\u00ea\13\r\3\16\3\16\3\17\3\17\3\17\2\3\30\20")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\2\2\u0100\2\36")
        buf.write("\3\2\2\2\4\'\3\2\2\2\6*\3\2\2\2\b/\3\2\2\2\n;\3\2\2\2")
        buf.write("\f?\3\2\2\2\16T\3\2\2\2\20X\3\2\2\2\22l\3\2\2\2\24\u0084")
        buf.write("\3\2\2\2\26\u00af\3\2\2\2\30\u00c8\3\2\2\2\32\u00eb\3")
        buf.write("\2\2\2\34\u00ed\3\2\2\2\36\"\5\4\3\2\37!\5\f\7\2 \37\3")
        buf.write("\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\"\3")
        buf.write("\2\2\2%&\7\2\2\3&\3\3\2\2\2\'(\7\5\2\2()\5\6\4\2)\5\3")
        buf.write("\2\2\2*+\5\34\17\2+,\7\n\2\2,-\5\b\5\2-.\7\13\2\2.\7\3")
        buf.write("\2\2\2/\60\7\6\2\2\60\61\7\7\2\2\61\62\7\b\2\2\62\63\7")
        buf.write("\t\2\2\63\64\7\f\2\2\64\65\7\34\2\2\65\66\7\16\2\2\66")
        buf.write("\67\7\17\2\2\678\5\34\17\289\7\r\2\29:\5\n\6\2:\t\3\2")
        buf.write("\2\2;<\7\n\2\2<=\5\26\f\2=>\7\13\2\2>\13\3\2\2\2?@\7\5")
        buf.write("\2\2@C\5\34\17\2AB\7!\2\2BD\5\34\17\2CA\3\2\2\2CD\3\2")
        buf.write("\2\2DE\3\2\2\2EI\7\n\2\2FH\5\16\b\2GF\3\2\2\2HK\3\2\2")
        buf.write("\2IG\3\2\2\2IJ\3\2\2\2JO\3\2\2\2KI\3\2\2\2LN\5\20\t\2")
        buf.write("ML\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2PR\3\2\2\2QO\3")
        buf.write("\2\2\2RS\7\13\2\2S\r\3\2\2\2TU\5\24\13\2UV\5\34\17\2V")
        buf.write("W\7\23\2\2W\17\3\2\2\2XY\7\6\2\2YZ\5\24\13\2Z[\5\34\17")
        buf.write("\2[g\7\f\2\2\\]\5\24\13\2]d\5\34\17\2^_\7\26\2\2_`\5\24")
        buf.write("\13\2`a\7#\2\2ac\3\2\2\2b^\3\2\2\2cf\3\2\2\2db\3\2\2\2")
        buf.write("de\3\2\2\2eh\3\2\2\2fd\3\2\2\2g\\\3\2\2\2gh\3\2\2\2hi")
        buf.write("\3\2\2\2ij\7\r\2\2jk\5\22\n\2k\21\3\2\2\2lp\7\n\2\2mo")
        buf.write("\5\16\b\2nm\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2qv\3")
        buf.write("\2\2\2rp\3\2\2\2su\5\26\f\2ts\3\2\2\2ux\3\2\2\2vt\3\2")
        buf.write("\2\2vw\3\2\2\2wy\3\2\2\2xv\3\2\2\2yz\7\"\2\2z{\5\30\r")
        buf.write("\2{|\7\23\2\2|}\7\13\2\2}\23\3\2\2\2~\177\7\33\2\2\177")
        buf.write("\u0080\7\16\2\2\u0080\u0085\7\17\2\2\u0081\u0085\7\35")
        buf.write("\2\2\u0082\u0085\7\33\2\2\u0083\u0085\5\34\17\2\u0084")
        buf.write("~\3\2\2\2\u0084\u0081\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\25\3\2\2\2\u0086\u008a\7\n\2\2\u0087")
        buf.write("\u0089\5\26\f\2\u0088\u0087\3\2\2\2\u0089\u008c\3\2\2")
        buf.write("\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008d")
        buf.write("\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u00b0\7\13\2\2\u008e")
        buf.write("\u008f\7\20\2\2\u008f\u0090\7\f\2\2\u0090\u0091\5\30\r")
        buf.write("\2\u0091\u0092\7\r\2\2\u0092\u0093\5\26\f\2\u0093\u0094")
        buf.write("\7\21\2\2\u0094\u0095\5\26\f\2\u0095\u00b0\3\2\2\2\u0096")
        buf.write("\u0097\7\22\2\2\u0097\u0098\7\f\2\2\u0098\u0099\5\30\r")
        buf.write("\2\u0099\u009a\7\r\2\2\u009a\u009b\5\26\f\2\u009b\u00b0")
        buf.write("\3\2\2\2\u009c\u009d\7\3\2\2\u009d\u009e\7\f\2\2\u009e")
        buf.write("\u009f\5\30\r\2\u009f\u00a0\7\r\2\2\u00a0\u00a1\7\23\2")
        buf.write("\2\u00a1\u00b0\3\2\2\2\u00a2\u00a3\5\34\17\2\u00a3\u00a4")
        buf.write("\7\24\2\2\u00a4\u00a5\5\30\r\2\u00a5\u00a6\7\23\2\2\u00a6")
        buf.write("\u00b0\3\2\2\2\u00a7\u00a8\5\34\17\2\u00a8\u00a9\7\16")
        buf.write("\2\2\u00a9\u00aa\5\30\r\2\u00aa\u00ab\7\17\2\2\u00ab\u00ac")
        buf.write("\7\24\2\2\u00ac\u00ad\5\30\r\2\u00ad\u00ae\7\23\2\2\u00ae")
        buf.write("\u00b0\3\2\2\2\u00af\u0086\3\2\2\2\u00af\u008e\3\2\2\2")
        buf.write("\u00af\u0096\3\2\2\2\u00af\u009c\3\2\2\2\u00af\u00a2\3")
        buf.write("\2\2\2\u00af\u00a7\3\2\2\2\u00b0\27\3\2\2\2\u00b1\u00b2")
        buf.write("\b\r\1\2\u00b2\u00c9\7 \2\2\u00b3\u00c9\7\27\2\2\u00b4")
        buf.write("\u00c9\7\30\2\2\u00b5\u00c9\5\34\17\2\u00b6\u00c9\7\31")
        buf.write("\2\2\u00b7\u00b8\7\32\2\2\u00b8\u00b9\7\33\2\2\u00b9\u00ba")
        buf.write("\7\16\2\2\u00ba\u00bb\5\30\r\2\u00bb\u00bc\7\17\2\2\u00bc")
        buf.write("\u00c9\3\2\2\2\u00bd\u00be\7\32\2\2\u00be\u00bf\5\34\17")
        buf.write("\2\u00bf\u00c0\7\f\2\2\u00c0\u00c1\7\r\2\2\u00c1\u00c9")
        buf.write("\3\2\2\2\u00c2\u00c3\7\36\2\2\u00c3\u00c9\5\30\r\4\u00c4")
        buf.write("\u00c5\7\f\2\2\u00c5\u00c6\5\30\r\2\u00c6\u00c7\7\r\2")
        buf.write("\2\u00c7\u00c9\3\2\2\2\u00c8\u00b1\3\2\2\2\u00c8\u00b3")
        buf.write("\3\2\2\2\u00c8\u00b4\3\2\2\2\u00c8\u00b5\3\2\2\2\u00c8")
        buf.write("\u00b6\3\2\2\2\u00c8\u00b7\3\2\2\2\u00c8\u00bd\3\2\2\2")
        buf.write("\u00c8\u00c2\3\2\2\2\u00c8\u00c4\3\2\2\2\u00c9\u00e8\3")
        buf.write("\2\2\2\u00ca\u00cb\f\17\2\2\u00cb\u00cc\5\32\16\2\u00cc")
        buf.write("\u00cd\5\30\r\20\u00cd\u00e7\3\2\2\2\u00ce\u00cf\f\16")
        buf.write("\2\2\u00cf\u00d0\7\16\2\2\u00d0\u00d1\5\30\r\2\u00d1\u00d2")
        buf.write("\7\17\2\2\u00d2\u00e7\3\2\2\2\u00d3\u00d4\f\r\2\2\u00d4")
        buf.write("\u00d5\7\25\2\2\u00d5\u00e7\7\4\2\2\u00d6\u00d7\f\f\2")
        buf.write("\2\u00d7\u00d8\7\25\2\2\u00d8\u00d9\5\34\17\2\u00d9\u00e2")
        buf.write("\7\f\2\2\u00da\u00df\5\30\r\2\u00db\u00dc\7\26\2\2\u00dc")
        buf.write("\u00de\5\30\r\2\u00dd\u00db\3\2\2\2\u00de\u00e1\3\2\2")
        buf.write("\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e3")
        buf.write("\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00da\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\7\r\2\2")
        buf.write("\u00e5\u00e7\3\2\2\2\u00e6\u00ca\3\2\2\2\u00e6\u00ce\3")
        buf.write("\2\2\2\u00e6\u00d3\3\2\2\2\u00e6\u00d6\3\2\2\2\u00e7\u00ea")
        buf.write("\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write("\31\3\2\2\2\u00ea\u00e8\3\2\2\2\u00eb\u00ec\7\37\2\2\u00ec")
        buf.write("\33\3\2\2\2\u00ed\u00ee\7#\2\2\u00ee\35\3\2\2\2\22\"C")
        buf.write("IOdgpv\u0084\u008a\u00af\u00c8\u00df\u00e2\u00e6\u00e8")
        return buf.getvalue()


class astParser ( Parser ):

    grammarFileName = "ast.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'System.out.println'", "'length'", "'class'", 
                     "'public'", "'static'", "'void'", "'main'", "'{'", 
                     "'}'", "'('", "')'", "'['", "']'", "'if'", "'else'", 
                     "'while'", "';'", "'='", "'.'", "','", "'true'", "'false'", 
                     "'this'", "'new'", "'int'", "'String'", "'bool'", "'!'", 
                     "<INVALID>", "<INVALID>", "'extends'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Class", "Public", 
                      "Static", "Void", "Main", "LBrace", "RBrace", "LPran", 
                      "RPran", "LBrack", "RBrack", "If", "Else", "While", 
                      "SemiColon", "Equals", "Dot", "Comma", "True", "False", 
                      "This", "New", "IntType", "StringType", "BoolType", 
                      "Exclamation", "BinaryOperator", "Integer", "Extends", 
                      "Return", "Identifier", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_mainClass = 1
    RULE_mainClassDecl = 2
    RULE_mainMethodDecl = 3
    RULE_mainMethodBody = 4
    RULE_classDecl = 5
    RULE_varDecl = 6
    RULE_methodDecl = 7
    RULE_methodBody = 8
    RULE_type = 9
    RULE_statement = 10
    RULE_exp = 11
    RULE_binOp = 12
    RULE_identifier = 13

    ruleNames =  [ "program", "mainClass", "mainClassDecl", "mainMethodDecl", 
                   "mainMethodBody", "classDecl", "varDecl", "methodDecl", 
                   "methodBody", "type", "statement", "exp", "binOp", "identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Class=3
    Public=4
    Static=5
    Void=6
    Main=7
    LBrace=8
    RBrace=9
    LPran=10
    RPran=11
    LBrack=12
    RBrack=13
    If=14
    Else=15
    While=16
    SemiColon=17
    Equals=18
    Dot=19
    Comma=20
    True=21
    False=22
    This=23
    New=24
    IntType=25
    StringType=26
    BoolType=27
    Exclamation=28
    BinaryOperator=29
    Integer=30
    Extends=31
    Return=32
    Identifier=33
    WS=34
    COMMENT=35
    LINE_COMMENT=36

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
            self.value_attr = str()
            self.type_attr = str()

        def mainClass(self):
            return self.getTypedRuleContext(astParser.MainClassContext,0)


        def EOF(self):
            return self.getToken(astParser.EOF, 0)

        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(astParser.ClassDeclContext,i)


        def getRuleIndex(self):
            return astParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = astParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.mainClass()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==astParser.Class:
                self.state = 29
                self.classDecl()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(astParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def Class(self):
            return self.getToken(astParser.Class, 0)

        def mainClassDecl(self):
            return self.getTypedRuleContext(astParser.MainClassDeclContext,0)


        def getRuleIndex(self):
            return astParser.RULE_mainClass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainClass" ):
                listener.enterMainClass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainClass" ):
                listener.exitMainClass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainClass" ):
                return visitor.visitMainClass(self)
            else:
                return visitor.visitChildren(self)




    def mainClass(self):

        localctx = astParser.MainClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainClass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(astParser.Class)
            self.state = 38
            self.mainClassDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def identifier(self):
            return self.getTypedRuleContext(astParser.IdentifierContext,0)


        def LBrace(self):
            return self.getToken(astParser.LBrace, 0)

        def mainMethodDecl(self):
            return self.getTypedRuleContext(astParser.MainMethodDeclContext,0)


        def RBrace(self):
            return self.getToken(astParser.RBrace, 0)

        def getRuleIndex(self):
            return astParser.RULE_mainClassDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainClassDecl" ):
                listener.enterMainClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainClassDecl" ):
                listener.exitMainClassDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainClassDecl" ):
                return visitor.visitMainClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def mainClassDecl(self):

        localctx = astParser.MainClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mainClassDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.identifier()
            self.state = 41
            self.match(astParser.LBrace)
            self.state = 42
            self.mainMethodDecl()
            self.state = 43
            self.match(astParser.RBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainMethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def Public(self):
            return self.getToken(astParser.Public, 0)

        def Static(self):
            return self.getToken(astParser.Static, 0)

        def Void(self):
            return self.getToken(astParser.Void, 0)

        def Main(self):
            return self.getToken(astParser.Main, 0)

        def LPran(self):
            return self.getToken(astParser.LPran, 0)

        def StringType(self):
            return self.getToken(astParser.StringType, 0)

        def LBrack(self):
            return self.getToken(astParser.LBrack, 0)

        def RBrack(self):
            return self.getToken(astParser.RBrack, 0)

        def identifier(self):
            return self.getTypedRuleContext(astParser.IdentifierContext,0)


        def RPran(self):
            return self.getToken(astParser.RPran, 0)

        def mainMethodBody(self):
            return self.getTypedRuleContext(astParser.MainMethodBodyContext,0)


        def getRuleIndex(self):
            return astParser.RULE_mainMethodDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainMethodDecl" ):
                listener.enterMainMethodDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainMethodDecl" ):
                listener.exitMainMethodDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainMethodDecl" ):
                return visitor.visitMainMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def mainMethodDecl(self):

        localctx = astParser.MainMethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mainMethodDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(astParser.Public)
            self.state = 46
            self.match(astParser.Static)
            self.state = 47
            self.match(astParser.Void)
            self.state = 48
            self.match(astParser.Main)
            self.state = 49
            self.match(astParser.LPran)
            self.state = 50
            self.match(astParser.StringType)
            self.state = 51
            self.match(astParser.LBrack)
            self.state = 52
            self.match(astParser.RBrack)
            self.state = 53
            self.identifier()
            self.state = 54
            self.match(astParser.RPran)
            self.state = 55
            self.mainMethodBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainMethodBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def LBrace(self):
            return self.getToken(astParser.LBrace, 0)

        def statement(self):
            return self.getTypedRuleContext(astParser.StatementContext,0)


        def RBrace(self):
            return self.getToken(astParser.RBrace, 0)

        def getRuleIndex(self):
            return astParser.RULE_mainMethodBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainMethodBody" ):
                listener.enterMainMethodBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainMethodBody" ):
                listener.exitMainMethodBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainMethodBody" ):
                return visitor.visitMainMethodBody(self)
            else:
                return visitor.visitChildren(self)




    def mainMethodBody(self):

        localctx = astParser.MainMethodBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mainMethodBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(astParser.LBrace)
            self.state = 58
            self.statement()
            self.state = 59
            self.match(astParser.RBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def Class(self):
            return self.getToken(astParser.Class, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(astParser.IdentifierContext,i)


        def LBrace(self):
            return self.getToken(astParser.LBrace, 0)

        def RBrace(self):
            return self.getToken(astParser.RBrace, 0)

        def Extends(self):
            return self.getToken(astParser.Extends, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(astParser.VarDeclContext,i)


        def methodDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.MethodDeclContext)
            else:
                return self.getTypedRuleContext(astParser.MethodDeclContext,i)


        def getRuleIndex(self):
            return astParser.RULE_classDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDecl" ):
                listener.enterClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDecl" ):
                listener.exitClassDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = astParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(astParser.Class)
            self.state = 62
            self.identifier()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==astParser.Extends:
                self.state = 63
                self.match(astParser.Extends)
                self.state = 64
                self.identifier()


            self.state = 67
            self.match(astParser.LBrace)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << astParser.IntType) | (1 << astParser.BoolType) | (1 << astParser.Identifier))) != 0):
                self.state = 68
                self.varDecl()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==astParser.Public:
                self.state = 74
                self.methodDecl()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(astParser.RBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def type(self):
            return self.getTypedRuleContext(astParser.TypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(astParser.IdentifierContext,0)


        def SemiColon(self):
            return self.getToken(astParser.SemiColon, 0)

        def getRuleIndex(self):
            return astParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = astParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.type()
            self.state = 83
            self.identifier()
            self.state = 84
            self.match(astParser.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def Public(self):
            return self.getToken(astParser.Public, 0)

        def type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.TypeContext)
            else:
                return self.getTypedRuleContext(astParser.TypeContext,i)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(astParser.IdentifierContext,i)


        def LPran(self):
            return self.getToken(astParser.LPran, 0)

        def RPran(self):
            return self.getToken(astParser.RPran, 0)

        def methodBody(self):
            return self.getTypedRuleContext(astParser.MethodBodyContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(astParser.Comma)
            else:
                return self.getToken(astParser.Comma, i)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(astParser.Identifier)
            else:
                return self.getToken(astParser.Identifier, i)

        def getRuleIndex(self):
            return astParser.RULE_methodDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDecl" ):
                listener.enterMethodDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDecl" ):
                listener.exitMethodDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = astParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(astParser.Public)
            self.state = 87
            self.type()
            self.state = 88
            self.identifier()
            self.state = 89
            self.match(astParser.LPran)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << astParser.IntType) | (1 << astParser.BoolType) | (1 << astParser.Identifier))) != 0):
                self.state = 90
                self.type()
                self.state = 91
                self.identifier()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==astParser.Comma:
                    self.state = 92
                    self.match(astParser.Comma)
                    self.state = 93
                    self.type()
                    self.state = 94
                    self.match(astParser.Identifier)
                    self.state = 100
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 103
            self.match(astParser.RPran)
            self.state = 104
            self.methodBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def LBrace(self):
            return self.getToken(astParser.LBrace, 0)

        def Return(self):
            return self.getToken(astParser.Return, 0)

        def exp(self):
            return self.getTypedRuleContext(astParser.ExpContext,0)


        def SemiColon(self):
            return self.getToken(astParser.SemiColon, 0)

        def RBrace(self):
            return self.getToken(astParser.RBrace, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(astParser.VarDeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.StatementContext)
            else:
                return self.getTypedRuleContext(astParser.StatementContext,i)


        def getRuleIndex(self):
            return astParser.RULE_methodBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodBody" ):
                listener.enterMethodBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodBody" ):
                listener.exitMethodBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodBody" ):
                return visitor.visitMethodBody(self)
            else:
                return visitor.visitChildren(self)




    def methodBody(self):

        localctx = astParser.MethodBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_methodBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(astParser.LBrace)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 107
                    self.varDecl() 
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << astParser.T__0) | (1 << astParser.LBrace) | (1 << astParser.If) | (1 << astParser.While) | (1 << astParser.Identifier))) != 0):
                self.state = 113
                self.statement()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self.match(astParser.Return)
            self.state = 120
            self.exp(0)
            self.state = 121
            self.match(astParser.SemiColon)
            self.state = 122
            self.match(astParser.RBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def IntType(self):
            return self.getToken(astParser.IntType, 0)

        def LBrack(self):
            return self.getToken(astParser.LBrack, 0)

        def RBrack(self):
            return self.getToken(astParser.RBrack, 0)

        def BoolType(self):
            return self.getToken(astParser.BoolType, 0)

        def identifier(self):
            return self.getTypedRuleContext(astParser.IdentifierContext,0)


        def getRuleIndex(self):
            return astParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type(self):

        localctx = astParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(astParser.IntType)
                self.state = 125
                self.match(astParser.LBrack)
                self.state = 126
                self.match(astParser.RBrack)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(astParser.BoolType)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.match(astParser.IntType)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.identifier()
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
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return astParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr



    class PrintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a astParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPran(self):
            return self.getToken(astParser.LPran, 0)
        def exp(self):
            return self.getTypedRuleContext(astParser.ExpContext,0)

        def RPran(self):
            return self.getToken(astParser.RPran, 0)
        def SemiColon(self):
            return self.getToken(astParser.SemiColon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a astParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(astParser.IdentifierContext,0)

        def Equals(self):
            return self.getToken(astParser.Equals, 0)
        def exp(self):
            return self.getTypedRuleContext(astParser.ExpContext,0)

        def SemiColon(self):
            return self.getToken(astParser.SemiColon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class Array_assignmentContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a astParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(astParser.IdentifierContext,0)

        def LBrack(self):
            return self.getToken(astParser.LBrack, 0)
        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.ExpContext)
            else:
                return self.getTypedRuleContext(astParser.ExpContext,i)

        def RBrack(self):
            return self.getToken(astParser.RBrack, 0)
        def Equals(self):
            return self.getToken(astParser.Equals, 0)
        def SemiColon(self):
            return self.getToken(astParser.SemiColon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_assignment" ):
                listener.enterArray_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_assignment" ):
                listener.exitArray_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_assignment" ):
                return visitor.visitArray_assignment(self)
            else:
                return visitor.visitChildren(self)


    class Statement1Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a astParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBrace(self):
            return self.getToken(astParser.LBrace, 0)
        def RBrace(self):
            return self.getToken(astParser.RBrace, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.StatementContext)
            else:
                return self.getTypedRuleContext(astParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement1" ):
                listener.enterStatement1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement1" ):
                listener.exitStatement1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement1" ):
                return visitor.visitStatement1(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a astParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def While(self):
            return self.getToken(astParser.While, 0)
        def LPran(self):
            return self.getToken(astParser.LPran, 0)
        def exp(self):
            return self.getTypedRuleContext(astParser.ExpContext,0)

        def RPran(self):
            return self.getToken(astParser.RPran, 0)
        def statement(self):
            return self.getTypedRuleContext(astParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a astParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def If(self):
            return self.getToken(astParser.If, 0)
        def LPran(self):
            return self.getToken(astParser.LPran, 0)
        def exp(self):
            return self.getTypedRuleContext(astParser.ExpContext,0)

        def RPran(self):
            return self.getToken(astParser.RPran, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.StatementContext)
            else:
                return self.getTypedRuleContext(astParser.StatementContext,i)

        def Else(self):
            return self.getToken(astParser.Else, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = astParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = astParser.Statement1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(astParser.LBrace)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << astParser.T__0) | (1 << astParser.LBrace) | (1 << astParser.If) | (1 << astParser.While) | (1 << astParser.Identifier))) != 0):
                    self.state = 133
                    self.statement()
                    self.state = 138
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 139
                self.match(astParser.RBrace)
                pass

            elif la_ == 2:
                localctx = astParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(astParser.If)
                self.state = 141
                self.match(astParser.LPran)
                self.state = 142
                self.exp(0)
                self.state = 143
                self.match(astParser.RPran)
                self.state = 144
                self.statement()
                self.state = 145
                self.match(astParser.Else)
                self.state = 146
                self.statement()
                pass

            elif la_ == 3:
                localctx = astParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.match(astParser.While)
                self.state = 149
                self.match(astParser.LPran)
                self.state = 150
                self.exp(0)
                self.state = 151
                self.match(astParser.RPran)
                self.state = 152
                self.statement()
                pass

            elif la_ == 4:
                localctx = astParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.match(astParser.T__0)
                self.state = 155
                self.match(astParser.LPran)
                self.state = 156
                self.exp(0)
                self.state = 157
                self.match(astParser.RPran)
                self.state = 158
                self.match(astParser.SemiColon)
                pass

            elif la_ == 5:
                localctx = astParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 160
                self.identifier()
                self.state = 161
                self.match(astParser.Equals)
                self.state = 162
                self.exp(0)
                self.state = 163
                self.match(astParser.SemiColon)
                pass

            elif la_ == 6:
                localctx = astParser.Array_assignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 165
                self.identifier()
                self.state = 166
                self.match(astParser.LBrack)
                self.state = 167
                self.exp(0)
                self.state = 168
                self.match(astParser.RBrack)
                self.state = 169
                self.match(astParser.Equals)
                self.state = 170
                self.exp(0)
                self.state = 171
                self.match(astParser.SemiColon)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def Integer(self):
            return self.getToken(astParser.Integer, 0)

        def True(self):
            return self.getToken(astParser.True, 0)

        def False(self):
            return self.getToken(astParser.False, 0)

        def identifier(self):
            return self.getTypedRuleContext(astParser.IdentifierContext,0)


        def This(self):
            return self.getToken(astParser.This, 0)

        def New(self):
            return self.getToken(astParser.New, 0)

        def IntType(self):
            return self.getToken(astParser.IntType, 0)

        def LBrack(self):
            return self.getToken(astParser.LBrack, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(astParser.ExpContext)
            else:
                return self.getTypedRuleContext(astParser.ExpContext,i)


        def RBrack(self):
            return self.getToken(astParser.RBrack, 0)

        def LPran(self):
            return self.getToken(astParser.LPran, 0)

        def RPran(self):
            return self.getToken(astParser.RPran, 0)

        def Exclamation(self):
            return self.getToken(astParser.Exclamation, 0)

        def binOp(self):
            return self.getTypedRuleContext(astParser.BinOpContext,0)


        def Dot(self):
            return self.getToken(astParser.Dot, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(astParser.Comma)
            else:
                return self.getToken(astParser.Comma, i)

        def getRuleIndex(self):
            return astParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = astParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 176
                self.match(astParser.Integer)
                pass

            elif la_ == 2:
                self.state = 177
                self.match(astParser.True)
                pass

            elif la_ == 3:
                self.state = 178
                self.match(astParser.False)
                pass

            elif la_ == 4:
                self.state = 179
                self.identifier()
                pass

            elif la_ == 5:
                self.state = 180
                self.match(astParser.This)
                pass

            elif la_ == 6:
                self.state = 181
                self.match(astParser.New)
                self.state = 182
                self.match(astParser.IntType)
                self.state = 183
                self.match(astParser.LBrack)
                self.state = 184
                self.exp(0)
                self.state = 185
                self.match(astParser.RBrack)
                pass

            elif la_ == 7:
                self.state = 187
                self.match(astParser.New)
                self.state = 188
                self.identifier()
                self.state = 189
                self.match(astParser.LPran)
                self.state = 190
                self.match(astParser.RPran)
                pass

            elif la_ == 8:
                self.state = 192
                self.match(astParser.Exclamation)
                self.state = 193
                self.exp(2)
                pass

            elif la_ == 9:
                self.state = 194
                self.match(astParser.LPran)
                self.state = 195
                self.exp(0)
                self.state = 196
                self.match(astParser.RPran)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 228
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = astParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 200
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")

                        self.state = 201
                        self.binOp()
                        self.state = 202
                        self.exp(14)
                        pass

                    elif la_ == 2:
                        localctx = astParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 204
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 205
                        self.match(astParser.LBrack)
                        self.state = 206
                        self.exp(0)
                        self.state = 207
                        self.match(astParser.RBrack)
                        pass

                    elif la_ == 3:
                        localctx = astParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 209
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 210
                        self.match(astParser.Dot)
                        self.state = 211
                        self.match(astParser.T__1)
                        pass

                    elif la_ == 4:
                        localctx = astParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 212
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 213
                        self.match(astParser.Dot)
                        self.state = 214
                        self.identifier()
                        self.state = 215
                        self.match(astParser.LPran)
                        self.state = 224
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << astParser.LPran) | (1 << astParser.True) | (1 << astParser.False) | (1 << astParser.This) | (1 << astParser.New) | (1 << astParser.Exclamation) | (1 << astParser.Integer) | (1 << astParser.Identifier))) != 0):
                            self.state = 216
                            self.exp(0)
                            self.state = 221
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==astParser.Comma:
                                self.state = 217
                                self.match(astParser.Comma)
                                self.state = 218
                                self.exp(0)
                                self.state = 223
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 226
                        self.match(astParser.RPran)
                        pass

             
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BinOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def BinaryOperator(self):
            return self.getToken(astParser.BinaryOperator, 0)

        def getRuleIndex(self):
            return astParser.RULE_binOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinOp" ):
                listener.enterBinOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinOp" ):
                listener.exitBinOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinOp" ):
                return visitor.visitBinOp(self)
            else:
                return visitor.visitChildren(self)




    def binOp(self):

        localctx = astParser.BinOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_binOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(astParser.BinaryOperator)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def Identifier(self):
            return self.getToken(astParser.Identifier, 0)

        def getRuleIndex(self):
            return astParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = astParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(astParser.Identifier)
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
        self._predicates[11] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         




