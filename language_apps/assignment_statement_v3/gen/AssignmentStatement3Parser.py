# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars/AssignmentStatement3.g4 by ANTLR 4.13.1
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
        4,1,14,95,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,25,8,1,10,1,12,1,28,
        9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,3,56,9,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,72,8,4,10,
        4,12,4,75,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,87,8,5,
        1,6,1,6,1,6,1,6,3,6,93,8,6,1,6,0,3,2,6,8,7,0,2,4,6,8,10,12,0,1,1,
        1,14,14,96,0,14,1,0,0,0,2,18,1,0,0,0,4,29,1,0,0,0,6,35,1,0,0,0,8,
        57,1,0,0,0,10,86,1,0,0,0,12,92,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,
        1,16,17,6,0,-1,0,17,1,1,0,0,0,18,19,6,1,-1,0,19,20,3,4,2,0,20,21,
        6,1,-1,0,21,26,1,0,0,0,22,23,10,2,0,0,23,25,3,4,2,0,24,22,1,0,0,
        0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,3,1,0,0,0,28,26,1,
        0,0,0,29,30,5,11,0,0,30,31,5,1,0,0,31,32,3,6,3,0,32,33,7,0,0,0,33,
        34,6,2,-1,0,34,5,1,0,0,0,35,36,6,3,-1,0,36,37,3,8,4,0,37,38,6,3,
        -1,0,38,54,1,0,0,0,39,40,10,4,0,0,40,41,5,2,0,0,41,42,3,8,4,0,42,
        43,6,3,-1,0,43,53,1,0,0,0,44,45,10,3,0,0,45,46,5,3,0,0,46,47,3,8,
        4,0,47,48,6,3,-1,0,48,53,1,0,0,0,49,50,10,2,0,0,50,51,5,12,0,0,51,
        53,3,8,4,0,52,39,1,0,0,0,52,44,1,0,0,0,52,49,1,0,0,0,53,56,1,0,0,
        0,54,52,1,0,0,0,54,55,1,0,0,0,55,7,1,0,0,0,56,54,1,0,0,0,57,58,6,
        4,-1,0,58,59,3,10,5,0,59,60,6,4,-1,0,60,73,1,0,0,0,61,62,10,3,0,
        0,62,63,5,4,0,0,63,64,3,10,5,0,64,65,6,4,-1,0,65,72,1,0,0,0,66,67,
        10,2,0,0,67,68,5,5,0,0,68,69,3,10,5,0,69,70,6,4,-1,0,70,72,1,0,0,
        0,71,61,1,0,0,0,71,66,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,9,1,0,0,0,75,73,1,0,0,0,76,77,5,6,0,0,77,78,3,6,3,0,78,
        79,5,7,0,0,79,80,6,5,-1,0,80,87,1,0,0,0,81,82,5,11,0,0,82,87,6,5,
        -1,0,83,84,3,12,6,0,84,85,6,5,-1,0,85,87,1,0,0,0,86,76,1,0,0,0,86,
        81,1,0,0,0,86,83,1,0,0,0,87,11,1,0,0,0,88,89,5,8,0,0,89,93,6,6,-1,
        0,90,91,5,9,0,0,91,93,6,6,-1,0,92,88,1,0,0,0,92,90,1,0,0,0,93,13,
        1,0,0,0,7,26,52,54,71,73,86,92
    ]

class AssignmentStatement3Parser ( Parser ):

    grammarFileName = "AssignmentStatement3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'+'", "'-'", "'*'", "'/'", "'('", 
                     "')'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "FLOAT", "String", "ID", "RELOP", "WS", "NEWLINE" ]

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
    INT=8
    FLOAT=9
    String=10
    ID=11
    RELOP=12
    WS=13
    NEWLINE=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
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



    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.p = None # ProgContext

        def EOF(self):
            return self.getToken(AssignmentStatement3Parser.EOF, 0)

        def prog(self):
            return self.getTypedRuleContext(AssignmentStatement3Parser.ProgContext,0)


        def getRuleIndex(self):
            return AssignmentStatement3Parser.RULE_start

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

        localctx = AssignmentStatement3Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            localctx.p = self.prog(0)
            self.state = 15
            self.match(AssignmentStatement3Parser.EOF)
            localctx.value_attr=localctx.p.value_attr
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.a = None # AssignContext

        def assign(self):
            return self.getTypedRuleContext(AssignmentStatement3Parser.AssignContext,0)


        def prog(self):
            return self.getTypedRuleContext(AssignmentStatement3Parser.ProgContext,0)


        def getRuleIndex(self):
            return AssignmentStatement3Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)



    def prog(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AssignmentStatement3Parser.ProgContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_prog, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            localctx.a = self.assign()
            localctx.value_attr=localctx.a.value_attr
            localctx.type_attr = localctx.a.type_attr
            print('----------')

            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AssignmentStatement3Parser.ProgContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_prog)
                    self.state = 22
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 23
                    localctx.a = self.assign() 
                self.state = 28
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
            self.value_attr = str()
            self.type_attr = str()
            self._ID = None # Token
            self.e = None # ExprContext

        def ID(self):
            return self.getToken(AssignmentStatement3Parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement3Parser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(AssignmentStatement3Parser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(AssignmentStatement3Parser.EOF, 0)

        def getRuleIndex(self):
            return AssignmentStatement3Parser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = AssignmentStatement3Parser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            localctx._ID = self.match(AssignmentStatement3Parser.ID)
            self.state = 30
            self.match(AssignmentStatement3Parser.T__0)
            self.state = 31
            localctx.e = self.expr(0)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==-1 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            localctx.value_attr=localctx.e.value_attr
            localctx.type_attr = localctx.e.type_attr
            print('Assignment value:', (None if localctx._ID is None else localctx._ID.text), '=', localctx.e.value_attr)
            print('Assignment type:', localctx.e.type_attr)

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
            self.value_attr = str()
            self.type_attr = str()
            self.e = None # ExprContext
            self.t = None # TermContext

        def term(self):
            return self.getTypedRuleContext(AssignmentStatement3Parser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement3Parser.ExprContext,0)


        def RELOP(self):
            return self.getToken(AssignmentStatement3Parser.RELOP, 0)

        def getRuleIndex(self):
            return AssignmentStatement3Parser.RULE_expr

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
        localctx = AssignmentStatement3Parser.ExprContext(self, self._ctx, _parentState)
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
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 52
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatement3Parser.ExprContext(self, _parentctx, _parentState)
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 40
                        self.match(AssignmentStatement3Parser.T__1)
                        self.state = 41
                        localctx.t = self.term(0)

                        if localctx.e.type_attr != localctx.t.type_attr:
                              print('Semantic error4 in "+" operator: Inconsistent types!')
                        else:
                              localctx.type_attr = localctx.t.type_attr
                              if localctx.t.type_attr=='float':
                                  localctx.value_attr = str(float(localctx.e.value_attr) + float(localctx.t.value_attr))
                                  print(localctx.value_attr, ' = ', localctx.e.value_attr, ' + ', localctx.t.value_attr)
                              elif localctx.t.type_attr=='int':
                                  localctx.value_attr = str(int(localctx.e.value_attr) + int(localctx.t.value_attr))
                                  print(localctx.value_attr, ' = ', localctx.e.value_attr, ' + ', localctx.t.value_attr)
                              elif localctx.t.type_attr=='str':
                                  temp = self.create_temp()
                                  print(temp, ' = ', localctx.e.value_attr, ' + ', localctx.t.value_attr)
                                  localctx.value_attr = temp
                                  
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatement3Parser.ExprContext(self, _parentctx, _parentState)
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 45
                        self.match(AssignmentStatement3Parser.T__2)
                        self.state = 46
                        localctx.t = self.term(0)

                        if localctx.e.type_attr != localctx.t.type_attr:
                              print('Semantic error3 in "-" operator: Inconsistent types!')
                        else:
                              localctx.type_attr = localctx.t.type_attr
                              if localctx.t.type_attr=='float':
                                  localctx.value_attr = str(float(localctx.e.value_attr) - float(localctx.t.value_attr))
                                  print(localctx.value_attr, ' = ', localctx.e.value_attr, ' - ', localctx.t.value_attr)
                              elif localctx.t.type_attr == 'int':
                                  localctx.value_attr = str(int(localctx.e.value_attr) - int(localctx.t.value_attr))
                                  print(localctx.value_attr, ' = ', localctx.e.value_attr, ' - ', localctx.t.value_attr)
                              elif localctx.t.type_attr=='str':
                                  temp = self.create_temp()
                                  print(temp, '=', localctx.e.value_attr, '-', localctx.t.value_attr)
                                  localctx.value_attr = temp

                        pass

                    elif la_ == 3:
                        localctx = AssignmentStatement3Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 50
                        self.match(AssignmentStatement3Parser.RELOP)
                        self.state = 51
                        self.term(0)
                        pass

             
                self.state = 56
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
            self.value_attr = str()
            self.type_attr = str()
            self.t = None # TermContext
            self.f = None # FactorContext

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatement3Parser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(AssignmentStatement3Parser.TermContext,0)


        def getRuleIndex(self):
            return AssignmentStatement3Parser.RULE_term

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
        localctx = AssignmentStatement3Parser.TermContext(self, self._ctx, _parentState)
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
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatement3Parser.TermContext(self, _parentctx, _parentState)
                        localctx.t = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 61
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 62
                        self.match(AssignmentStatement3Parser.T__3)
                        self.state = 63
                        localctx.f = self.factor()

                        if localctx.t.type_attr != localctx.f.type_attr:
                              print('Semantic error2 in "*" operator: Inconsistent types!')
                        else:
                              localctx.type_attr = localctx.f.type_attr
                              if localctx.f.type_attr=='float':
                                  localctx.value_attr = str(float(localctx.t.value_attr) * float(localctx.f.value_attr))
                                  print(localctx.value_attr, ' = ', localctx.t.value_attr, ' * ', localctx.f.value_attr)
                              elif localctx.f.type_attr=='int':
                                  localctx.value_attr = str(int(localctx.t.value_attr) * int(localctx.f.value_attr))
                                  print(localctx.value_attr, ' = ', localctx.t.value_attr, ' * ', localctx.f.value_attr)
                              elif localctx.f.type_attr=='str':
                                  temp = self.create_temp()
                                  print(temp, '=', localctx.t.value_attr, '*', localctx.f.value_attr)
                                  localctx.value_attr = temp
                                  
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatement3Parser.TermContext(self, _parentctx, _parentState)
                        localctx.t = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 66
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 67
                        self.match(AssignmentStatement3Parser.T__4)
                        self.state = 68
                        localctx.f = self.factor()

                        if localctx.t.type_attr != localctx.f.type_attr:
                              print('Semantic error1 in "/" operator: Inconsistent types!')
                        else:
                              localctx.type_attr = localctx.f.type_attr
                              if localctx.f.type_attr=='float':
                                  localctx.value_attr = str(float(localctx.t.value_attr) / float(localctx.f.value_attr))
                                  print(localctx.value_attr, ' = ', localctx.t.value_attr, ' / ', localctx.f.value_attr)
                              elif localctx.f.type_attr=='int':
                                  localctx.value_attr = str(int(int(localctx.t.value_attr) / int(localctx.f.value_attr)))
                                  print(localctx.value_attr, ' = ', localctx.t.value_attr, ' / ', localctx.f.value_attr)
                              elif localctx.f.type_attr=='str':
                                  temp = self.create_temp()
                                  print(temp, '=', localctx.t.value_attr, '/', localctx.f.value_attr)
                                  localctx.value_attr = temp
                                  
                        pass

             
                self.state = 75
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
            self.value_attr = str()
            self.type_attr = str()
            self.e = None # ExprContext
            self._ID = None # Token
            self.n = None # NumberContext

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement3Parser.ExprContext,0)


        def ID(self):
            return self.getToken(AssignmentStatement3Parser.ID, 0)

        def number(self):
            return self.getTypedRuleContext(AssignmentStatement3Parser.NumberContext,0)


        def getRuleIndex(self):
            return AssignmentStatement3Parser.RULE_factor

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

        localctx = AssignmentStatement3Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(AssignmentStatement3Parser.T__5)
                self.state = 77
                localctx.e = self.expr(0)
                self.state = 78
                self.match(AssignmentStatement3Parser.T__6)
                localctx.type_attr = localctx.e.type_attr
                localctx.value_attr = localctx.e.value_attr

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                localctx._ID = self.match(AssignmentStatement3Parser.ID)
                localctx.type_attr = 'str'
                localctx.value_attr = (None if localctx._ID is None else localctx._ID.text)

                pass
            elif token in [8, 9]:
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self._INT = None # Token
            self._FLOAT = None # Token

        def INT(self):
            return self.getToken(AssignmentStatement3Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(AssignmentStatement3Parser.FLOAT, 0)

        def getRuleIndex(self):
            return AssignmentStatement3Parser.RULE_number

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

        localctx = AssignmentStatement3Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_number)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                localctx._INT = self.match(AssignmentStatement3Parser.INT)
                localctx.value_attr = (None if localctx._INT is None else localctx._INT.text)
                localctx.type_attr = 'int'

                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                localctx._FLOAT = self.match(AssignmentStatement3Parser.FLOAT)
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
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




