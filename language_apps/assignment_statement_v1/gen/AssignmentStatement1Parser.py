# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars/AssignmentStatement1.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,1,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,42,8,3,
        10,3,12,3,45,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,56,8,4,
        10,4,12,4,59,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,68,8,5,1,6,1,6,
        1,6,0,3,2,6,8,7,0,2,4,6,8,10,12,0,2,1,1,13,13,1,0,9,10,72,0,14,1,
        0,0,0,2,17,1,0,0,0,4,27,1,0,0,0,6,32,1,0,0,0,8,46,1,0,0,0,10,67,
        1,0,0,0,12,69,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,
        18,6,1,-1,0,18,19,3,4,2,0,19,24,1,0,0,0,20,21,10,2,0,0,21,23,3,4,
        2,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,
        1,0,0,0,26,24,1,0,0,0,27,28,5,8,0,0,28,29,5,1,0,0,29,30,3,6,3,0,
        30,31,7,0,0,0,31,5,1,0,0,0,32,33,6,3,-1,0,33,34,3,8,4,0,34,43,1,
        0,0,0,35,36,10,3,0,0,36,37,5,2,0,0,37,42,3,8,4,0,38,39,10,2,0,0,
        39,40,5,3,0,0,40,42,3,8,4,0,41,35,1,0,0,0,41,38,1,0,0,0,42,45,1,
        0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,7,1,0,0,0,45,43,1,0,0,0,46,
        47,6,4,-1,0,47,48,3,10,5,0,48,57,1,0,0,0,49,50,10,3,0,0,50,51,5,
        4,0,0,51,56,3,10,5,0,52,53,10,2,0,0,53,54,5,5,0,0,54,56,3,10,5,0,
        55,49,1,0,0,0,55,52,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,
        0,0,0,58,9,1,0,0,0,59,57,1,0,0,0,60,61,5,6,0,0,61,62,3,6,3,0,62,
        63,5,7,0,0,63,68,1,0,0,0,64,68,5,8,0,0,65,68,3,12,6,0,66,68,5,11,
        0,0,67,60,1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,11,
        1,0,0,0,69,70,7,1,0,0,70,13,1,0,0,0,6,24,41,43,55,57,67
    ]

class AssignmentStatement1Parser ( Parser ):

    grammarFileName = "AssignmentStatement1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'+'", "'-'", "'*'", "'/'", "'('", 
                     "')'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Id", "INT", "FLOAT", "String", "WS", "NEWLINE", "RELOP" ]

    RULE_start = 0
    RULE_prog = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_term = 4
    RULE_factor = 5
    RULE_number = 6

    ruleNames =  [ "start", "prog", "assign", "expr", "term", "factor", 
                   "number" ]

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
    NEWLINE=13
    RELOP=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog(self):
            return self.getTypedRuleContext(AssignmentStatement1Parser.ProgContext,0)


        def EOF(self):
            return self.getToken(AssignmentStatement1Parser.EOF, 0)

        def getRuleIndex(self):
            return AssignmentStatement1Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = AssignmentStatement1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.prog(0)
            self.state = 15
            self.match(AssignmentStatement1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(AssignmentStatement1Parser.AssignContext,0)


        def prog(self):
            return self.getTypedRuleContext(AssignmentStatement1Parser.ProgContext,0)


        def getRuleIndex(self):
            return AssignmentStatement1Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)



    def prog(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AssignmentStatement1Parser.ProgContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_prog, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.assign()
            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AssignmentStatement1Parser.ProgContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_prog)
                    self.state = 20
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 21
                    self.assign() 
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(AssignmentStatement1Parser.Id, 0)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement1Parser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(AssignmentStatement1Parser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(AssignmentStatement1Parser.EOF, 0)

        def getRuleIndex(self):
            return AssignmentStatement1Parser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = AssignmentStatement1Parser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(AssignmentStatement1Parser.Id)
            self.state = 28
            self.match(AssignmentStatement1Parser.T__0)
            self.state = 29
            self.expr(0)
            self.state = 30
            _la = self._input.LA(1)
            if not(_la==-1 or _la==13):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(AssignmentStatement1Parser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement1Parser.ExprContext,0)


        def getRuleIndex(self):
            return AssignmentStatement1Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AssignmentStatement1Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 41
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatement1Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 36
                        self.match(AssignmentStatement1Parser.T__1)
                        self.state = 37
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatement1Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 39
                        self.match(AssignmentStatement1Parser.T__2)
                        self.state = 40
                        self.term(0)
                        pass

             
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatement1Parser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(AssignmentStatement1Parser.TermContext,0)


        def getRuleIndex(self):
            return AssignmentStatement1Parser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AssignmentStatement1Parser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 55
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatement1Parser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 49
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 50
                        self.match(AssignmentStatement1Parser.T__3)
                        self.state = 51
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatement1Parser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 52
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 53
                        self.match(AssignmentStatement1Parser.T__4)
                        self.state = 54
                        self.factor()
                        pass

             
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement1Parser.ExprContext,0)


        def Id(self):
            return self.getToken(AssignmentStatement1Parser.Id, 0)

        def number(self):
            return self.getTypedRuleContext(AssignmentStatement1Parser.NumberContext,0)


        def String(self):
            return self.getToken(AssignmentStatement1Parser.String, 0)

        def getRuleIndex(self):
            return AssignmentStatement1Parser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = AssignmentStatement1Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(AssignmentStatement1Parser.T__5)
                self.state = 61
                self.expr(0)
                self.state = 62
                self.match(AssignmentStatement1Parser.T__6)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(AssignmentStatement1Parser.Id)
                pass
            elif token in [9, 10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.number()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.match(AssignmentStatement1Parser.String)
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(AssignmentStatement1Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(AssignmentStatement1Parser.FLOAT, 0)

        def getRuleIndex(self):
            return AssignmentStatement1Parser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = AssignmentStatement1Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
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
        self._predicates[1] = self.prog_sempred
        self._predicates[3] = self.expr_sempred
        self._predicates[4] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def prog_sempred(self, localctx:ProgContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




