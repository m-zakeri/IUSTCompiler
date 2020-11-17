# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars\AssignmentStatement4.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3\33\n")
        buf.write("\3\f\3\16\3\36\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\7\5\67\n\5\f\5\16\5:\13\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6J\n\6\f\6\16\6M\13")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7Y\n\7\3")
        buf.write("\b\3\b\3\b\3\b\5\b_\n\b\3\b\2\5\4\b\n\t\2\4\6\b\n\f\16")
        buf.write("\2\3\3\3\20\20\2b\2\20\3\2\2\2\4\24\3\2\2\2\6\37\3\2\2")
        buf.write("\2\b%\3\2\2\2\n;\3\2\2\2\fX\3\2\2\2\16^\3\2\2\2\20\21")
        buf.write("\5\4\3\2\21\22\7\2\2\3\22\23\b\2\1\2\23\3\3\2\2\2\24\25")
        buf.write("\b\3\1\2\25\26\5\6\4\2\26\27\b\3\1\2\27\34\3\2\2\2\30")
        buf.write("\31\f\4\2\2\31\33\5\6\4\2\32\30\3\2\2\2\33\36\3\2\2\2")
        buf.write("\34\32\3\2\2\2\34\35\3\2\2\2\35\5\3\2\2\2\36\34\3\2\2")
        buf.write("\2\37 \7\r\2\2 !\7\3\2\2!\"\5\b\5\2\"#\t\2\2\2#$\b\4\1")
        buf.write("\2$\7\3\2\2\2%&\b\5\1\2&\'\5\n\6\2\'(\b\5\1\2(8\3\2\2")
        buf.write("\2)*\f\6\2\2*+\7\4\2\2+,\5\n\6\2,-\b\5\1\2-\67\3\2\2\2")
        buf.write("./\f\5\2\2/\60\7\5\2\2\60\61\5\n\6\2\61\62\b\5\1\2\62")
        buf.write("\67\3\2\2\2\63\64\f\4\2\2\64\65\7\16\2\2\65\67\5\n\6\2")
        buf.write("\66)\3\2\2\2\66.\3\2\2\2\66\63\3\2\2\2\67:\3\2\2\28\66")
        buf.write("\3\2\2\289\3\2\2\29\t\3\2\2\2:8\3\2\2\2;<\b\6\1\2<=\5")
        buf.write("\f\7\2=>\b\6\1\2>K\3\2\2\2?@\f\5\2\2@A\7\6\2\2AB\5\f\7")
        buf.write("\2BC\b\6\1\2CJ\3\2\2\2DE\f\4\2\2EF\7\7\2\2FG\5\f\7\2G")
        buf.write("H\b\6\1\2HJ\3\2\2\2I?\3\2\2\2ID\3\2\2\2JM\3\2\2\2KI\3")
        buf.write("\2\2\2KL\3\2\2\2L\13\3\2\2\2MK\3\2\2\2NO\7\b\2\2OP\5\b")
        buf.write("\5\2PQ\7\t\2\2QR\b\7\1\2RY\3\2\2\2ST\7\r\2\2TY\b\7\1\2")
        buf.write("UV\5\16\b\2VW\b\7\1\2WY\3\2\2\2XN\3\2\2\2XS\3\2\2\2XU")
        buf.write("\3\2\2\2Y\r\3\2\2\2Z[\7\n\2\2[_\b\b\1\2\\]\7\13\2\2]_")
        buf.write("\b\b\1\2^Z\3\2\2\2^\\\3\2\2\2_\17\3\2\2\2\t\34\668IKX")
        buf.write("^")
        return buf.getvalue()


class AssignmentStatement4Parser(Parser):
    grammarFileName = "AssignmentStatement4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "':='", "'+'", "'-'", "'*'", "'/'", "'('",
                    "')'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                    "<INVALID>", "<INVALID>", "'\n'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "INT", "FLOAT", "String", "ID", "RELOP", "WS", "NEWLINE"]

    RULE_start = 0
    RULE_prog = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_term = 4
    RULE_factor = 5
    RULE_number = 6

    ruleNames = ["start", "prog", "assign", "expr", "term", "factor",
                 "number"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    INT = 8
    FLOAT = 9
    String = 10
    ID = 11
    RELOP = 12
    WS = 13
    NEWLINE = 14

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    temp_counter = 0

    def create_temp(self):
        self.temp_counter += 1
        return 'T' + str(self.temp_counter)

    def remove_temp(self):
        self.temp_counter -= 1

    def get_temp(self):
        return 'T' + str(self.temp_counter)

    def is_temp(self, var: str):
        if var[0] == 'T':
            return True
        return False

    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.p = None  # ProgContext

        def EOF(self):
            return self.getToken(AssignmentStatement4Parser.EOF, 0)

        def prog(self):
            return self.getTypedRuleContext(AssignmentStatement4Parser.ProgContext, 0)

        def getRuleIndex(self):
            return AssignmentStatement4Parser.RULE_start

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStart"):
                listener.enterStart(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStart"):
                listener.exitStart(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStart"):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)

    def start(self):

        localctx = AssignmentStatement4Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            localctx.p = self.prog(0)
            self.state = 15
            self.match(AssignmentStatement4Parser.EOF)
            localctx.value_attr = localctx.p.value_attr
            localctx.type_attr = localctx.p.type_attr
            print('Parsing was done!')

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.a = None  # AssignContext

        def assign(self):
            return self.getTypedRuleContext(AssignmentStatement4Parser.AssignContext, 0)

        def prog(self):
            return self.getTypedRuleContext(AssignmentStatement4Parser.ProgContext, 0)

        def getRuleIndex(self):
            return AssignmentStatement4Parser.RULE_prog

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProg"):
                listener.enterProg(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProg"):
                listener.exitProg(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitProg"):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)

    def prog(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AssignmentStatement4Parser.ProgContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_prog, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            localctx.a = self.assign()
            localctx.value_attr = localctx.a.value_attr
            localctx.type_attr = localctx.a.type_attr
            print('----------')

            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 0, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AssignmentStatement4Parser.ProgContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_prog)
                    self.state = 22
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 23
                    localctx.a = self.assign()
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 0, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self._ID = None  # Token
            self.e = None  # ExprContext

        def ID(self):
            return self.getToken(AssignmentStatement4Parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement4Parser.ExprContext, 0)

        def NEWLINE(self):
            return self.getToken(AssignmentStatement4Parser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(AssignmentStatement4Parser.EOF, 0)

        def getRuleIndex(self):
            return AssignmentStatement4Parser.RULE_assign

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAssign"):
                listener.enterAssign(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAssign"):
                listener.exitAssign(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAssign"):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)

    def assign(self):

        localctx = AssignmentStatement4Parser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            localctx._ID = self.match(AssignmentStatement4Parser.ID)
            self.state = 30
            self.match(AssignmentStatement4Parser.T__0)
            self.state = 31
            localctx.e = self.expr(0)
            self.state = 32
            _la = self._input.LA(1)
            if not (_la == AssignmentStatement4Parser.EOF or _la == AssignmentStatement4Parser.NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            localctx.value_attr = localctx.e.value_attr
            localctx.type_attr = localctx.e.type_attr
            print('Assignment value:', (None if localctx._ID is None else localctx._ID.text), '=',
                  localctx.e.value_attr)
            print('Assignment type:', localctx.e.type_attr)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.e = None  # ExprContext
            self.t = None  # TermContext

        def term(self):
            return self.getTypedRuleContext(AssignmentStatement4Parser.TermContext, 0)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement4Parser.ExprContext, 0)

        def RELOP(self):
            return self.getToken(AssignmentStatement4Parser.RELOP, 0)

        def getRuleIndex(self):
            return AssignmentStatement4Parser.RULE_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpr"):
                listener.enterExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpr"):
                listener.exitExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpr"):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)

    def expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AssignmentStatement4Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            localctx.t = self.term(0)
            localctx.type_attr = localctx.t.type_attr
            localctx.value_attr = localctx.t.value_attr

            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 52
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatement4Parser.ExprContext(self, _parentctx, _parentState)
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 40
                        self.match(AssignmentStatement4Parser.T__1)
                        self.state = 41
                        localctx.t = self.term(0)

                        if localctx.e.type_attr != localctx.t.type_attr:
                            print('Semantic error4 in "+" operator: Inconsistent types!')
                        else:
                            localctx.type_attr = localctx.t.type_attr
                            if localctx.t.type_attr == 'float':
                                localctx.value_attr = str(float(localctx.e.value_attr) + float(localctx.t.value_attr))
                                print(localctx.value_attr, ' = ', localctx.e.value_attr, ' + ', localctx.t.value_attr)
                            elif localctx.t.type_attr == 'int':
                                localctx.value_attr = str(int(localctx.e.value_attr) + int(localctx.t.value_attr))
                                print(localctx.value_attr, ' = ', localctx.e.value_attr, ' + ', localctx.t.value_attr)
                            elif localctx.t.type_attr == 'str':
                                if self.is_temp(localctx.e.value_attr):
                                    localctx.value_attr = localctx.e.value_attr
                                    if self.is_temp(localctx.t.value_attr):
                                        self.remove_temp()
                                elif self.is_temp(localctx.t.value_attr):
                                    localctx.value_attr = localctx.t.value_attr
                                else:
                                    localctx.value_attr = self.create_temp()
                                print(localctx.value_attr, ' = ', localctx.e.value_attr, ' + ', localctx.t.value_attr)
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatement4Parser.ExprContext(self, _parentctx, _parentState)
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 45
                        self.match(AssignmentStatement4Parser.T__2)
                        self.state = 46
                        localctx.t = self.term(0)

                        if localctx.e.type_attr != localctx.t.type_attr:
                            print('Semantic error3 in "-" operator: Inconsistent types!')
                        else:
                            localctx.type_attr = localctx.t.type_attr
                            if localctx.t.type_attr == 'float':
                                localctx.value_attr = str(float(localctx.e.value_attr) - float(localctx.t.value_attr))
                                print(localctx.value_attr, ' = ', localctx.e.value_attr, ' - ', localctx.t.value_attr)
                            elif localctx.t.type_attr == 'int':
                                localctx.value_attr = str(int(localctx.e.value_attr) - int(localctx.t.value_attr))
                                print(localctx.value_attr, ' = ', localctx.e.value_attr, ' - ', localctx.t.value_attr)
                            elif localctx.t.type_attr == 'str':
                                if self.is_temp(localctx.e.value_attr):
                                    localctx.value_attr = localctx.e.value_attr
                                    if self.is_temp(localctx.t.value_attr):
                                        self.remove_temp()
                                elif self.is_temp(localctx.t.value_attr):
                                    localctx.value_attr = localctx.t.value_attr
                                else:
                                    localctx.value_attr = self.create_temp()
                                print(localctx.value_attr, ' = ', localctx.e.value_attr, ' - ', localctx.t.value_attr)

                        pass

                    elif la_ == 3:
                        localctx = AssignmentStatement4Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 50
                        self.match(AssignmentStatement4Parser.RELOP)
                        self.state = 51
                        self.term(0)
                        pass

                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.t = None  # TermContext
            self.f = None  # FactorContext

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatement4Parser.FactorContext, 0)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatement4Parser.TermContext, 0)

        def getRuleIndex(self):
            return AssignmentStatement4Parser.RULE_term

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTerm"):
                listener.enterTerm(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTerm"):
                listener.exitTerm(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTerm"):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)

    def term(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AssignmentStatement4Parser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            localctx.f = self.factor()
            localctx.type_attr = localctx.f.type_attr
            localctx.value_attr = localctx.f.value_attr

            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatement4Parser.TermContext(self, _parentctx, _parentState)
                        localctx.t = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 61
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 62
                        self.match(AssignmentStatement4Parser.T__3)
                        self.state = 63
                        localctx.f = self.factor()

                        if localctx.t.type_attr != localctx.f.type_attr:
                            print('Semantic error2 in "*" operator: Inconsistent types!')
                        else:
                            localctx.type_attr = localctx.f.type_attr
                            if localctx.f.type_attr == 'float':
                                localctx.value_attr = str(float(localctx.t.value_attr) * float(localctx.f.value_attr))
                                print(localctx.value_attr, ' = ', localctx.t.value_attr, ' * ', localctx.f.value_attr)
                            elif localctx.f.type_attr == 'int':
                                localctx.value_attr = str(int(localctx.t.value_attr) * int(localctx.f.value_attr))
                                print(localctx.value_attr, ' = ', localctx.t.value_attr, ' * ', localctx.f.value_attr)
                            elif localctx.f.type_attr == 'str':
                                if self.is_temp(localctx.t.value_attr):
                                    localctx.value_attr = localctx.t.value_attr
                                    if self.is_temp(localctx.f.value_attr):
                                        self.remove_temp()
                                elif self.is_temp(localctx.f.value_attr):
                                    localctx.value_attr = localctx.f.value_attr
                                else:
                                    localctx.value_attr = self.create_temp()
                                print(localctx.value_attr, ' = ', localctx.t.value_attr, ' * ', localctx.f.value_attr)
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatement4Parser.TermContext(self, _parentctx, _parentState)
                        localctx.t = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 66
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 67
                        self.match(AssignmentStatement4Parser.T__4)
                        self.state = 68
                        localctx.f = self.factor()

                        if localctx.t.type_attr != localctx.f.type_attr:
                            print('Semantic error1 in "/" operator: Inconsistent types!')
                        else:
                            localctx.type_attr = localctx.f.type_attr
                            if localctx.f.type_attr == 'float':
                                localctx.value_attr = str(float(localctx.t.value_attr) / float(localctx.f.value_attr))
                                print(localctx.value_attr, ' = ', localctx.t.value_attr, ' / ', localctx.f.value_attr)
                            elif localctx.f.type_attr == 'int':
                                localctx.value_attr = str(int(int(localctx.t.value_attr) / int(localctx.f.value_attr)))
                                print(localctx.value_attr, ' = ', localctx.t.value_attr, ' / ', localctx.f.value_attr)
                            elif localctx.f.type_attr == 'str':
                                if self.is_temp(localctx.t.value_attr):
                                    localctx.value_attr = localctx.t.value_attr
                                    if self.is_temp(localctx.f.value_attr):
                                        self.remove_temp()
                                elif self.is_temp(localctx.f.value_attr):
                                    localctx.value_attr = localctx.f.value_attr
                                else:
                                    localctx.value_attr = self.create_temp()
                                print(localctx.value_attr, ' = ', localctx.t.value_attr, ' / ', localctx.f.value_attr)

                        pass

                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.e = None  # ExprContext
            self._ID = None  # Token
            self.n = None  # NumberContext

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement4Parser.ExprContext, 0)

        def ID(self):
            return self.getToken(AssignmentStatement4Parser.ID, 0)

        def number(self):
            return self.getTypedRuleContext(AssignmentStatement4Parser.NumberContext, 0)

        def getRuleIndex(self):
            return AssignmentStatement4Parser.RULE_factor

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFactor"):
                listener.enterFactor(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFactor"):
                listener.exitFactor(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFactor"):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)

    def factor(self):

        localctx = AssignmentStatement4Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AssignmentStatement4Parser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(AssignmentStatement4Parser.T__5)
                self.state = 77
                localctx.e = self.expr(0)
                self.state = 78
                self.match(AssignmentStatement4Parser.T__6)
                localctx.type_attr = localctx.e.type_attr
                localctx.value_attr = localctx.e.value_attr

                pass
            elif token in [AssignmentStatement4Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                localctx._ID = self.match(AssignmentStatement4Parser.ID)
                localctx.type_attr = 'str'
                localctx.value_attr = (None if localctx._ID is None else localctx._ID.text)

                pass
            elif token in [AssignmentStatement4Parser.INT, AssignmentStatement4Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                localctx.n = self.number()
                localctx.type_attr = localctx.n.type_attr
                localctx.value_attr = localctx.n.value_attr

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self._INT = None  # Token
            self._FLOAT = None  # Token

        def INT(self):
            return self.getToken(AssignmentStatement4Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(AssignmentStatement4Parser.FLOAT, 0)

        def getRuleIndex(self):
            return AssignmentStatement4Parser.RULE_number

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNumber"):
                listener.enterNumber(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNumber"):
                listener.exitNumber(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNumber"):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)

    def number(self):

        localctx = AssignmentStatement4Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_number)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AssignmentStatement4Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                localctx._INT = self.match(AssignmentStatement4Parser.INT)
                localctx.value_attr = (None if localctx._INT is None else localctx._INT.text)
                localctx.type_attr = 'int'

                pass
            elif token in [AssignmentStatement4Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                localctx._FLOAT = self.match(AssignmentStatement4Parser.FLOAT)
                localctx.value_attr = (None if localctx._FLOAT is None else localctx._FLOAT.text)
                localctx.type_attr = 'float'

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.prog_sempred
        self._predicates[3] = self.expr_sempred
        self._predicates[4] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def prog_sempred(self, localctx: ProgContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 2)

    def expr_sempred(self, localctx: ExprContext, predIndex: int):
        if predIndex == 1:
            return self.precpred(self._ctx, 4)

        if predIndex == 2:
            return self.precpred(self._ctx, 3)

        if predIndex == 3:
            return self.precpred(self._ctx, 2)

    def term_sempred(self, localctx: TermContext, predIndex: int):
        if predIndex == 4:
            return self.precpred(self._ctx, 3)

        if predIndex == 5:
            return self.precpred(self._ctx, 2)
