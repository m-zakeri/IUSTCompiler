# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars\AssignmentStatement2.g4 by ANTLR 4.8
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
        buf.write("N\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3\31\n\3\f\3\16")
        buf.write("\3\34\13\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\7\5/\n\5\f\5\16\5\62\13\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6=\n\6\f\6\16\6@\13")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7H\n\7\3\b\3\b\5\bL\n\b\3")
        buf.write("\b\2\5\4\b\n\t\2\4\6\b\n\f\16\2\3\3\3\17\17\2O\2\20\3")
        buf.write("\2\2\2\4\23\3\2\2\2\6\35\3\2\2\2\b\"\3\2\2\2\n\63\3\2")
        buf.write("\2\2\fG\3\2\2\2\16K\3\2\2\2\20\21\5\4\3\2\21\22\7\2\2")
        buf.write("\3\22\3\3\2\2\2\23\24\b\3\1\2\24\25\5\6\4\2\25\32\3\2")
        buf.write("\2\2\26\27\f\4\2\2\27\31\5\6\4\2\30\26\3\2\2\2\31\34\3")
        buf.write("\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\5\3\2\2\2\34\32")
        buf.write("\3\2\2\2\35\36\7\r\2\2\36\37\7\3\2\2\37 \5\b\5\2 !\t\2")
        buf.write("\2\2!\7\3\2\2\2\"#\b\5\1\2#$\5\n\6\2$\60\3\2\2\2%&\f\6")
        buf.write("\2\2&\'\7\4\2\2\'/\5\n\6\2()\f\5\2\2)*\7\5\2\2*/\5\n\6")
        buf.write("\2+,\f\4\2\2,-\7\20\2\2-/\5\n\6\2.%\3\2\2\2.(\3\2\2\2")
        buf.write(".+\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\t")
        buf.write("\3\2\2\2\62\60\3\2\2\2\63\64\b\6\1\2\64\65\5\f\7\2\65")
        buf.write(">\3\2\2\2\66\67\f\5\2\2\678\7\6\2\28=\5\f\7\29:\f\4\2")
        buf.write("\2:;\7\7\2\2;=\5\f\7\2<\66\3\2\2\2<9\3\2\2\2=@\3\2\2\2")
        buf.write("><\3\2\2\2>?\3\2\2\2?\13\3\2\2\2@>\3\2\2\2AB\7\b\2\2B")
        buf.write("C\5\b\5\2CD\7\t\2\2DH\3\2\2\2EH\7\r\2\2FH\5\16\b\2GA\3")
        buf.write("\2\2\2GE\3\2\2\2GF\3\2\2\2H\r\3\2\2\2IL\7\13\2\2JL\7\n")
        buf.write("\2\2KI\3\2\2\2KJ\3\2\2\2L\17\3\2\2\2\t\32.\60<>GK")
        return buf.getvalue()


class AssignmentStatement2Parser ( Parser ):

    grammarFileName = "AssignmentStatement2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'+'", "'-'", "'*'", "'/'", "'('", 
                     "')'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "FLOAT", "String", "ID", "WS", "NEWLINE", "RELOP" ]

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
    WS=12
    NEWLINE=13
    RELOP=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def prog(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.ProgContext,0)


        def EOF(self):
            return self.getToken(AssignmentStatement2Parser.EOF, 0)

        def getRuleIndex(self):
            return AssignmentStatement2Parser.RULE_start

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

        localctx = AssignmentStatement2Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.prog(0)
            self.state = 15
            self.match(AssignmentStatement2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def assign(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.AssignContext,0)


        def prog(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.ProgContext,0)


        def getRuleIndex(self):
            return AssignmentStatement2Parser.RULE_prog

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
        localctx = AssignmentStatement2Parser.ProgContext(self, self._ctx, _parentState)
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
                    localctx = AssignmentStatement2Parser.ProgContext(self, _parentctx, _parentState)
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(AssignmentStatement2Parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(AssignmentStatement2Parser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(AssignmentStatement2Parser.EOF, 0)

        def getRuleIndex(self):
            return AssignmentStatement2Parser.RULE_assign

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

        localctx = AssignmentStatement2Parser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(AssignmentStatement2Parser.ID)
            self.state = 28
            self.match(AssignmentStatement2Parser.T__0)
            self.state = 29
            self.expr(0)
            self.state = 30
            _la = self._input.LA(1)
            if not(_la==AssignmentStatement2Parser.EOF or _la==AssignmentStatement2Parser.NEWLINE):
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatement2Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr


    class Expr_term_minusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_minus" ):
                listener.enterExpr_term_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_minus" ):
                listener.exitExpr_term_minus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_minus" ):
                return visitor.visitExpr_term_minus(self)
            else:
                return visitor.visitChildren(self)


    class Expr_term_plusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_plus" ):
                listener.enterExpr_term_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_plus" ):
                listener.exitExpr_term_plus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_plus" ):
                return visitor.visitExpr_term_plus(self)
            else:
                return visitor.visitChildren(self)


    class Term4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm4" ):
                listener.enterTerm4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm4" ):
                listener.exitTerm4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm4" ):
                return visitor.visitTerm4(self)
            else:
                return visitor.visitChildren(self)


    class Expr_term_relopContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.ExprContext,0)

        def RELOP(self):
            return self.getToken(AssignmentStatement2Parser.RELOP, 0)
        def term(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_relop" ):
                listener.enterExpr_term_relop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_relop" ):
                listener.exitExpr_term_relop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_relop" ):
                return visitor.visitExpr_term_relop(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AssignmentStatement2Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AssignmentStatement2Parser.Term4Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 33
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatement2Parser.Expr_term_plusContext(self, AssignmentStatement2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 36
                        self.match(AssignmentStatement2Parser.T__1)
                        self.state = 37
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatement2Parser.Expr_term_minusContext(self, AssignmentStatement2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 39
                        self.match(AssignmentStatement2Parser.T__2)
                        self.state = 40
                        self.term(0)
                        pass

                    elif la_ == 3:
                        localctx = AssignmentStatement2Parser.Expr_term_relopContext(self, AssignmentStatement2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 42
                        self.match(AssignmentStatement2Parser.RELOP)
                        self.state = 43
                        self.term(0)
                        pass

             
                self.state = 48
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatement2Parser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr


    class Term_fact_divideContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_fact_divide" ):
                listener.enterTerm_fact_divide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_fact_divide" ):
                listener.exitTerm_fact_divide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_fact_divide" ):
                return visitor.visitTerm_fact_divide(self)
            else:
                return visitor.visitChildren(self)


    class Term_fact_mutiplyContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_fact_mutiply" ):
                listener.enterTerm_fact_mutiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_fact_mutiply" ):
                listener.exitTerm_fact_mutiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_fact_mutiply" ):
                return visitor.visitTerm_fact_mutiply(self)
            else:
                return visitor.visitChildren(self)


    class Factor3Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor3" ):
                listener.enterFactor3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor3" ):
                listener.exitFactor3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor3" ):
                return visitor.visitFactor3(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AssignmentStatement2Parser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AssignmentStatement2Parser.Factor3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 50
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 58
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = AssignmentStatement2Parser.Term_fact_mutiplyContext(self, AssignmentStatement2Parser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 52
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 53
                        self.match(AssignmentStatement2Parser.T__3)
                        self.state = 54
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = AssignmentStatement2Parser.Term_fact_divideContext(self, AssignmentStatement2Parser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 55
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 56
                        self.match(AssignmentStatement2Parser.T__4)
                        self.state = 57
                        self.factor()
                        pass

             
                self.state = 62
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatement2Parser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr



    class Fact_exprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_expr" ):
                listener.enterFact_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_expr" ):
                listener.exitFact_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_expr" ):
                return visitor.visitFact_expr(self)
            else:
                return visitor.visitChildren(self)


    class Fact_idContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AssignmentStatement2Parser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_id" ):
                listener.enterFact_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_id" ):
                listener.exitFact_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_id" ):
                return visitor.visitFact_id(self)
            else:
                return visitor.visitChildren(self)


    class Fact_numberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(AssignmentStatement2Parser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact_number" ):
                listener.enterFact_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact_number" ):
                listener.exitFact_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_number" ):
                return visitor.visitFact_number(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = AssignmentStatement2Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AssignmentStatement2Parser.T__5]:
                localctx = AssignmentStatement2Parser.Fact_exprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(AssignmentStatement2Parser.T__5)
                self.state = 64
                self.expr(0)
                self.state = 65
                self.match(AssignmentStatement2Parser.T__6)
                pass
            elif token in [AssignmentStatement2Parser.ID]:
                localctx = AssignmentStatement2Parser.Fact_idContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(AssignmentStatement2Parser.ID)
                pass
            elif token in [AssignmentStatement2Parser.INT, AssignmentStatement2Parser.FLOAT]:
                localctx = AssignmentStatement2Parser.Fact_numberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.number()
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
            self.value_attr = str()
            self.type_attr = str()


        def getRuleIndex(self):
            return AssignmentStatement2Parser.RULE_number

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr



    class Number_floatContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(AssignmentStatement2Parser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber_float" ):
                listener.enterNumber_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber_float" ):
                listener.exitNumber_float(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_float" ):
                return visitor.visitNumber_float(self)
            else:
                return visitor.visitChildren(self)


    class Number_intContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssignmentStatement2Parser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(AssignmentStatement2Parser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber_int" ):
                listener.enterNumber_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber_int" ):
                listener.exitNumber_int(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_int" ):
                return visitor.visitNumber_int(self)
            else:
                return visitor.visitChildren(self)



    def number(self):

        localctx = AssignmentStatement2Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_number)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AssignmentStatement2Parser.FLOAT]:
                localctx = AssignmentStatement2Parser.Number_floatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(AssignmentStatement2Parser.FLOAT)
                pass
            elif token in [AssignmentStatement2Parser.INT]:
                localctx = AssignmentStatement2Parser.Number_intContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(AssignmentStatement2Parser.INT)
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
         




