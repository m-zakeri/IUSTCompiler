# Generated from D:/AnacondaProjects/iust_start/grammars\expr3.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\64\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\31\n\3\f\3")
        buf.write("\16\3\34\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("\'\n\4\f\4\16\4*\13\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\62\n")
        buf.write("\5\3\5\2\4\4\6\6\2\4\6\b\2\2\2\65\2\n\3\2\2\2\4\17\3\2")
        buf.write("\2\2\6\35\3\2\2\2\b\61\3\2\2\2\n\13\7\n\2\2\13\f\7\t\2")
        buf.write("\2\f\r\5\4\3\2\r\16\7\2\2\3\16\3\3\2\2\2\17\20\b\3\1\2")
        buf.write("\20\21\5\6\4\2\21\32\3\2\2\2\22\23\f\5\2\2\23\24\7\5\2")
        buf.write("\2\24\31\5\6\4\2\25\26\f\4\2\2\26\27\7\6\2\2\27\31\5\6")
        buf.write("\4\2\30\22\3\2\2\2\30\25\3\2\2\2\31\34\3\2\2\2\32\30\3")
        buf.write("\2\2\2\32\33\3\2\2\2\33\5\3\2\2\2\34\32\3\2\2\2\35\36")
        buf.write("\b\4\1\2\36\37\5\b\5\2\37(\3\2\2\2 !\f\5\2\2!\"\7\7\2")
        buf.write("\2\"\'\5\b\5\2#$\f\4\2\2$%\7\b\2\2%\'\5\b\5\2& \3\2\2")
        buf.write("\2&#\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\7\3\2\2\2")
        buf.write("*(\3\2\2\2+\62\7\n\2\2,\62\7\13\2\2-.\7\3\2\2./\5\4\3")
        buf.write("\2/\60\7\4\2\2\60\62\3\2\2\2\61+\3\2\2\2\61,\3\2\2\2\61")
        buf.write("-\3\2\2\2\62\t\3\2\2\2\7\30\32&(\61")
        return buf.getvalue()


class testParser ( Parser ):

    grammarFileName = "expr3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "<INVALID>", "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Plus", "MINUS", 
                      "MUL", "DIVIDE", "ASSIGN", "Id", "Number", "Whitespace", 
                      "Newline" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_fact = 3

    ruleNames =  [ "start", "expr", "term", "fact" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Plus=3
    MINUS=4
    MUL=5
    DIVIDE=6
    ASSIGN=7
    Id=8
    Number=9
    Whitespace=10
    Newline=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(testParser.Id, 0)

        def ASSIGN(self):
            return self.getToken(testParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(testParser.ExprContext,0)


        def EOF(self):
            return self.getToken(testParser.EOF, 0)

        def getRuleIndex(self):
            return testParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = testParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(testParser.Id)
            self.state = 9
            self.match(testParser.ASSIGN)
            self.state = 10
            self.expr(0)
            self.state = 11
            self.match(testParser.EOF)
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


        def getRuleIndex(self):
            return testParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Rule_minusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(testParser.ExprContext,0)

        def MINUS(self):
            return self.getToken(testParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(testParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_minus" ):
                listener.enterRule_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_minus" ):
                listener.exitRule_minus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_minus" ):
                return visitor.visitRule_minus(self)
            else:
                return visitor.visitChildren(self)


    class Rule_plusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(testParser.ExprContext,0)

        def Plus(self):
            return self.getToken(testParser.Plus, 0)
        def term(self):
            return self.getTypedRuleContext(testParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_plus" ):
                listener.enterRule_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_plus" ):
                listener.exitRule_plus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule_plus" ):
                return visitor.visitRule_plus(self)
            else:
                return visitor.visitChildren(self)


    class Rule3Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(testParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule3" ):
                listener.enterRule3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule3" ):
                listener.exitRule3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule3" ):
                return visitor.visitRule3(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = testParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = testParser.Rule3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 14
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 22
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = testParser.Rule_plusContext(self, testParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 17
                        self.match(testParser.Plus)
                        self.state = 18
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = testParser.Rule_minusContext(self, testParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 20
                        self.match(testParser.MINUS)
                        self.state = 21
                        self.term(0)
                        pass

             
                self.state = 26
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

        def fact(self):
            return self.getTypedRuleContext(testParser.FactContext,0)


        def term(self):
            return self.getTypedRuleContext(testParser.TermContext,0)


        def MUL(self):
            return self.getToken(testParser.MUL, 0)

        def DIVIDE(self):
            return self.getToken(testParser.DIVIDE, 0)

        def getRuleIndex(self):
            return testParser.RULE_term

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
        localctx = testParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = testParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 30
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 31
                        self.match(testParser.MUL)
                        self.state = 32
                        self.fact()
                        pass

                    elif la_ == 2:
                        localctx = testParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 33
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 34
                        self.match(testParser.DIVIDE)
                        self.state = 35
                        self.fact()
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(testParser.Id, 0)

        def Number(self):
            return self.getToken(testParser.Number, 0)

        def expr(self):
            return self.getTypedRuleContext(testParser.ExprContext,0)


        def getRuleIndex(self):
            return testParser.RULE_fact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact" ):
                listener.enterFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact" ):
                listener.exitFact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact" ):
                return visitor.visitFact(self)
            else:
                return visitor.visitChildren(self)




    def fact(self):

        localctx = testParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fact)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [testParser.Id]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(testParser.Id)
                pass
            elif token in [testParser.Number]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(testParser.Number)
                pass
            elif token in [testParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(testParser.T__0)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(testParser.T__1)
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
         




