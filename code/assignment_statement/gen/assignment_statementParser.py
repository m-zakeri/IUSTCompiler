# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars\assignment_statement.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\33\n")
        buf.write("\3\f\3\16\3\36\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\7\4)\n\4\f\4\16\4,\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5\65\n\5\3\6\3\6\3\6\2\4\4\6\7\2\4\6\b\n\2\3\3\2\13")
        buf.write("\f\2:\2\f\3\2\2\2\4\21\3\2\2\2\6\37\3\2\2\2\b\64\3\2\2")
        buf.write("\2\n\66\3\2\2\2\f\r\7\n\2\2\r\16\7\3\2\2\16\17\5\4\3\2")
        buf.write("\17\20\7\2\2\3\20\3\3\2\2\2\21\22\b\3\1\2\22\23\5\6\4")
        buf.write("\2\23\34\3\2\2\2\24\25\f\5\2\2\25\26\7\4\2\2\26\33\5\6")
        buf.write("\4\2\27\30\f\4\2\2\30\31\7\5\2\2\31\33\5\6\4\2\32\24\3")
        buf.write("\2\2\2\32\27\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2\34\35")
        buf.write("\3\2\2\2\35\5\3\2\2\2\36\34\3\2\2\2\37 \b\4\1\2 !\5\b")
        buf.write("\5\2!*\3\2\2\2\"#\f\5\2\2#$\7\6\2\2$)\5\b\5\2%&\f\4\2")
        buf.write("\2&\'\7\7\2\2\')\5\b\5\2(\"\3\2\2\2(%\3\2\2\2),\3\2\2")
        buf.write("\2*(\3\2\2\2*+\3\2\2\2+\7\3\2\2\2,*\3\2\2\2-.\7\b\2\2")
        buf.write("./\5\4\3\2/\60\7\t\2\2\60\65\3\2\2\2\61\65\7\n\2\2\62")
        buf.write("\65\5\n\6\2\63\65\7\r\2\2\64-\3\2\2\2\64\61\3\2\2\2\64")
        buf.write("\62\3\2\2\2\64\63\3\2\2\2\65\t\3\2\2\2\66\67\t\2\2\2\67")
        buf.write("\13\3\2\2\2\7\32\34(*\64")
        return buf.getvalue()


class assignment_statementParser ( Parser ):

    grammarFileName = "assignment_statement.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'+'", "'-'", "'*'", "'/'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Id", "INT", "FLOAT", "String", "WS" ]

    RULE_ass = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3
    RULE_number = 4

    ruleNames =  [ "ass", "expr", "term", "factor", "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    Id=8
    INT=9
    FLOAT=10
    String=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AssContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(assignment_statementParser.Id, 0)

        def expr(self):
            return self.getTypedRuleContext(assignment_statementParser.ExprContext,0)


        def EOF(self):
            return self.getToken(assignment_statementParser.EOF, 0)

        def getRuleIndex(self):
            return assignment_statementParser.RULE_ass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAss" ):
                listener.enterAss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAss" ):
                listener.exitAss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss" ):
                return visitor.visitAss(self)
            else:
                return visitor.visitChildren(self)




    def ass(self):

        localctx = assignment_statementParser.AssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(assignment_statementParser.Id)
            self.state = 11
            self.match(assignment_statementParser.T__0)
            self.state = 12
            self.expr(0)
            self.state = 13
            self.match(assignment_statementParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(assignment_statementParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(assignment_statementParser.ExprContext,0)


        def getRuleIndex(self):
            return assignment_statementParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = assignment_statementParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 24
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = assignment_statementParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 18
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 19
                        self.match(assignment_statementParser.T__1)
                        self.state = 20
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = assignment_statementParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 22
                        self.match(assignment_statementParser.T__2)
                        self.state = 23
                        self.term(0)
                        pass

             
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(assignment_statementParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(assignment_statementParser.TermContext,0)


        def getRuleIndex(self):
            return assignment_statementParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = assignment_statementParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = assignment_statementParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 32
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 33
                        self.match(assignment_statementParser.T__3)
                        self.state = 34
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = assignment_statementParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 35
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 36
                        self.match(assignment_statementParser.T__4)
                        self.state = 37
                        self.factor()
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(assignment_statementParser.ExprContext,0)


        def Id(self):
            return self.getToken(assignment_statementParser.Id, 0)

        def number(self):
            return self.getTypedRuleContext(assignment_statementParser.NumberContext,0)


        def String(self):
            return self.getToken(assignment_statementParser.String, 0)

        def getRuleIndex(self):
            return assignment_statementParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = assignment_statementParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [assignment_statementParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(assignment_statementParser.T__5)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(assignment_statementParser.T__6)
                pass
            elif token in [assignment_statementParser.Id]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(assignment_statementParser.Id)
                pass
            elif token in [assignment_statementParser.INT, assignment_statementParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.number()
                pass
            elif token in [assignment_statementParser.String]:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.match(assignment_statementParser.String)
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(assignment_statementParser.INT, 0)

        def FLOAT(self):
            return self.getToken(assignment_statementParser.FLOAT, 0)

        def getRuleIndex(self):
            return assignment_statementParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = assignment_statementParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not(_la==assignment_statementParser.INT or _la==assignment_statementParser.FLOAT):
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
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




