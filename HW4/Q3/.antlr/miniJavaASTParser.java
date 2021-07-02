// Generated from c:\Users\Sajjad\Documents\University\Semester 8\Compiler\HW4\HW4\Q3\miniJavaAST.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class miniJavaASTParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, IDENTIFIER=36, DECIMAL_LITERAL=37, 
		HEX_LITERAL=38, OCT_LITERAL=39, BINARY_LITERAL=40, WS=41, COMMENT=42, 
		LINE_COMMENT=43;
	public static final int
		RULE_program = 0, RULE_main_class = 1, RULE_class_declaration = 2, RULE_var_declaration = 3, 
		RULE_method_declaration = 4, RULE_type_r = 5, RULE_statement = 6, RULE_expression = 7, 
		RULE_identifier_r = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main_class", "class_declaration", "var_declaration", "method_declaration", 
			"type_r", "statement", "expression", "identifier_r"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'{'", "'public'", "'static'", "'void'", "'main'", "'('", 
			"'String'", "'['", "']'", "')'", "'}'", "'extends'", "';'", "','", "'return'", 
			"'int'", "'boolean'", "'if'", "'else'", "'while'", "'System.out.println'", 
			"'='", "'+'", "'-'", "'*'", "'&&'", "'<'", "'.'", "'length'", "'true'", 
			"'false'", "'this'", "'new'", "'!'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"IDENTIFIER", "DECIMAL_LITERAL", "HEX_LITERAL", "OCT_LITERAL", "BINARY_LITERAL", 
			"WS", "COMMENT", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "miniJavaAST.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public miniJavaASTParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public  v = 'program';
		public Main_classContext main_class() {
			return getRuleContext(Main_classContext.class,0);
		}
		public TerminalNode EOF() { return getToken(miniJavaASTParser.EOF, 0); }
		public List<Class_declarationContext> class_declaration() {
			return getRuleContexts(Class_declarationContext.class);
		}
		public Class_declarationContext class_declaration(int i) {
			return getRuleContext(Class_declarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			main_class();
			setState(22);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0) {
				{
				{
				setState(19);
				class_declaration();
				}
				}
				setState(24);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(25);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Main_classContext extends ParserRuleContext {
		public  v = 'main_class';
		public StatementContext s;
		public List<Identifier_rContext> identifier_r() {
			return getRuleContexts(Identifier_rContext.class);
		}
		public Identifier_rContext identifier_r(int i) {
			return getRuleContext(Identifier_rContext.class,i);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public Main_classContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main_class; }
	}

	public final Main_classContext main_class() throws RecognitionException {
		Main_classContext _localctx = new Main_classContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_main_class);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			match(T__0);
			setState(28);
			identifier_r();
			setState(29);
			match(T__1);
			setState(30);
			match(T__2);
			setState(31);
			match(T__3);
			setState(32);
			match(T__4);
			setState(33);
			match(T__5);
			setState(34);
			match(T__6);
			setState(35);
			match(T__7);
			setState(36);
			match(T__8);
			setState(37);
			match(T__9);
			setState(38);
			identifier_r();
			setState(39);
			match(T__10);
			setState(40);
			match(T__1);
			setState(41);
			((Main_classContext)_localctx).s = statement();
			setState(42);
			match(T__11);
			setState(43);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_declarationContext extends ParserRuleContext {
		public  v = 'class_declaration';
		public List<Identifier_rContext> identifier_r() {
			return getRuleContexts(Identifier_rContext.class);
		}
		public Identifier_rContext identifier_r(int i) {
			return getRuleContext(Identifier_rContext.class,i);
		}
		public List<Var_declarationContext> var_declaration() {
			return getRuleContexts(Var_declarationContext.class);
		}
		public Var_declarationContext var_declaration(int i) {
			return getRuleContext(Var_declarationContext.class,i);
		}
		public List<Method_declarationContext> method_declaration() {
			return getRuleContexts(Method_declarationContext.class);
		}
		public Method_declarationContext method_declaration(int i) {
			return getRuleContext(Method_declarationContext.class,i);
		}
		public Class_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_declaration; }
	}

	public final Class_declarationContext class_declaration() throws RecognitionException {
		Class_declarationContext _localctx = new Class_declarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_class_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(T__0);
			setState(46);
			identifier_r();
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(47);
				match(T__12);
				setState(48);
				identifier_r();
				}
			}

			setState(51);
			match(T__1);
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__16) | (1L << T__17) | (1L << IDENTIFIER))) != 0)) {
				{
				{
				setState(52);
				var_declaration();
				}
				}
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2) {
				{
				{
				setState(58);
				method_declaration();
				}
				}
				setState(63);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(64);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_declarationContext extends ParserRuleContext {
		public  v = 'var_dec';
		public Type_rContext type_r() {
			return getRuleContext(Type_rContext.class,0);
		}
		public Identifier_rContext identifier_r() {
			return getRuleContext(Identifier_rContext.class,0);
		}
		public Var_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declaration; }
	}

	public final Var_declarationContext var_declaration() throws RecognitionException {
		Var_declarationContext _localctx = new Var_declarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_var_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			type_r();
			setState(67);
			identifier_r();
			setState(68);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_declarationContext extends ParserRuleContext {
		public  v = 'method';
		public List<Type_rContext> type_r() {
			return getRuleContexts(Type_rContext.class);
		}
		public Type_rContext type_r(int i) {
			return getRuleContext(Type_rContext.class,i);
		}
		public List<Identifier_rContext> identifier_r() {
			return getRuleContexts(Identifier_rContext.class);
		}
		public Identifier_rContext identifier_r(int i) {
			return getRuleContext(Identifier_rContext.class,i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<Var_declarationContext> var_declaration() {
			return getRuleContexts(Var_declarationContext.class);
		}
		public Var_declarationContext var_declaration(int i) {
			return getRuleContext(Var_declarationContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public Method_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_declaration; }
	}

	public final Method_declarationContext method_declaration() throws RecognitionException {
		Method_declarationContext _localctx = new Method_declarationContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_method_declaration);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(T__2);
			setState(71);
			type_r();
			setState(72);
			identifier_r();
			setState(73);
			match(T__6);
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__16) | (1L << T__17) | (1L << IDENTIFIER))) != 0)) {
				{
				setState(74);
				type_r();
				setState(75);
				identifier_r();
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__14) {
					{
					{
					setState(76);
					match(T__14);
					setState(77);
					type_r();
					setState(78);
					identifier_r();
					}
					}
					setState(84);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(87);
			match(T__10);
			setState(88);
			match(T__1);
			setState(92);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(89);
					var_declaration();
					}
					} 
				}
				setState(94);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__18) | (1L << T__20) | (1L << T__21) | (1L << IDENTIFIER))) != 0)) {
				{
				{
				setState(95);
				statement();
				}
				}
				setState(100);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(101);
			match(T__15);
			setState(102);
			expression(0);
			setState(103);
			match(T__13);
			setState(104);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Type_rContext extends ParserRuleContext {
		public  v = 'type';
		public Identifier_rContext identifier_r() {
			return getRuleContext(Identifier_rContext.class,0);
		}
		public Type_rContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_r; }
	}

	public final Type_rContext type_r() throws RecognitionException {
		Type_rContext _localctx = new Type_rContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_type_r);
		try {
			setState(112);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(106);
				match(T__16);
				setState(107);
				match(T__8);
				setState(108);
				match(T__9);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(109);
				match(T__17);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(110);
				match(T__16);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(111);
				identifier_r();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public  v = 'statement';
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Identifier_rContext identifier_r() {
			return getRuleContext(Identifier_rContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_statement);
		int _la;
		try {
			setState(155);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(114);
				match(T__1);
				setState(118);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__18) | (1L << T__20) | (1L << T__21) | (1L << IDENTIFIER))) != 0)) {
					{
					{
					setState(115);
					statement();
					}
					}
					setState(120);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(121);
				match(T__11);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(122);
				match(T__18);
				setState(123);
				match(T__6);
				setState(124);
				expression(0);
				setState(125);
				match(T__10);
				setState(126);
				statement();
				setState(127);
				match(T__19);
				setState(128);
				statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(130);
				match(T__20);
				setState(131);
				match(T__6);
				setState(132);
				expression(0);
				setState(133);
				match(T__10);
				setState(134);
				statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(136);
				match(T__21);
				setState(137);
				match(T__6);
				setState(138);
				expression(0);
				setState(139);
				match(T__10);
				setState(140);
				match(T__13);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(142);
				identifier_r();
				setState(143);
				match(T__22);
				setState(144);
				expression(0);
				setState(145);
				match(T__13);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(147);
				identifier_r();
				setState(148);
				match(T__8);
				setState(149);
				expression(0);
				setState(150);
				match(T__9);
				setState(151);
				match(T__22);
				setState(152);
				expression(0);
				setState(153);
				match(T__13);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public  v = 'expression';
		public TerminalNode DECIMAL_LITERAL() { return getToken(miniJavaASTParser.DECIMAL_LITERAL, 0); }
		public Identifier_rContext identifier_r() {
			return getRuleContext(Identifier_rContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 14;
		enterRecursionRule(_localctx, 14, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(158);
				match(DECIMAL_LITERAL);
				}
				break;
			case 2:
				{
				setState(159);
				match(T__30);
				}
				break;
			case 3:
				{
				setState(160);
				match(T__31);
				}
				break;
			case 4:
				{
				setState(161);
				identifier_r();
				}
				break;
			case 5:
				{
				setState(162);
				match(T__32);
				}
				break;
			case 6:
				{
				setState(163);
				match(T__33);
				setState(164);
				match(T__16);
				setState(165);
				match(T__8);
				setState(166);
				expression(0);
				setState(167);
				match(T__9);
				}
				break;
			case 7:
				{
				setState(169);
				match(T__33);
				setState(170);
				identifier_r();
				setState(171);
				match(T__6);
				setState(172);
				match(T__10);
				}
				break;
			case 8:
				{
				setState(174);
				match(T__34);
				setState(175);
				expression(2);
				}
				break;
			case 9:
				{
				setState(176);
				match(T__6);
				setState(177);
				expression(0);
				setState(178);
				match(T__10);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(211);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(209);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(182);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(183);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(184);
						expression(14);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(185);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(186);
						match(T__8);
						setState(187);
						expression(0);
						setState(188);
						match(T__9);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(190);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(191);
						match(T__28);
						setState(192);
						match(T__29);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(193);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(194);
						match(T__28);
						setState(195);
						identifier_r();
						setState(196);
						match(T__6);
						setState(205);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__6) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << IDENTIFIER) | (1L << DECIMAL_LITERAL))) != 0)) {
							{
							setState(197);
							expression(0);
							setState(202);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==T__14) {
								{
								{
								setState(198);
								match(T__14);
								setState(199);
								expression(0);
								}
								}
								setState(204);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(207);
						match(T__10);
						}
						break;
					}
					} 
				}
				setState(213);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Identifier_rContext extends ParserRuleContext {
		public  v = str();
		public Token IDENTIFIER;
		public TerminalNode IDENTIFIER() { return getToken(miniJavaASTParser.IDENTIFIER, 0); }
		public Identifier_rContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier_r; }
	}

	public final Identifier_rContext identifier_r() throws RecognitionException {
		Identifier_rContext _localctx = new Identifier_rContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_identifier_r);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			((Identifier_rContext)_localctx).IDENTIFIER = match(IDENTIFIER);
			_localctx.v=(((Identifier_rContext)_localctx).IDENTIFIER!=null?((Identifier_rContext)_localctx).IDENTIFIER.getText():null)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 7:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 13);
		case 1:
			return precpred(_ctx, 12);
		case 2:
			return precpred(_ctx, 11);
		case 3:
			return precpred(_ctx, 10);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-\u00dc\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2"+
		"\7\2\27\n\2\f\2\16\2\32\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\64\n\4\3\4"+
		"\3\4\7\48\n\4\f\4\16\4;\13\4\3\4\7\4>\n\4\f\4\16\4A\13\4\3\4\3\4\3\5\3"+
		"\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6S\n\6\f\6\16\6V"+
		"\13\6\5\6X\n\6\3\6\3\6\3\6\7\6]\n\6\f\6\16\6`\13\6\3\6\7\6c\n\6\f\6\16"+
		"\6f\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7s\n\7\3\b\3\b"+
		"\7\bw\n\b\f\b\16\bz\13\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\5\b\u009e\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00b7\n\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\7\t\u00cb\n\t\f\t\16\t\u00ce\13\t\5\t\u00d0\n\t\3\t\3\t\7\t\u00d4\n"+
		"\t\f\t\16\t\u00d7\13\t\3\n\3\n\3\n\3\n\2\3\20\13\2\4\6\b\n\f\16\20\22"+
		"\2\3\3\2\32\36\2\u00f1\2\24\3\2\2\2\4\35\3\2\2\2\6/\3\2\2\2\bD\3\2\2\2"+
		"\nH\3\2\2\2\fr\3\2\2\2\16\u009d\3\2\2\2\20\u00b6\3\2\2\2\22\u00d8\3\2"+
		"\2\2\24\30\5\4\3\2\25\27\5\6\4\2\26\25\3\2\2\2\27\32\3\2\2\2\30\26\3\2"+
		"\2\2\30\31\3\2\2\2\31\33\3\2\2\2\32\30\3\2\2\2\33\34\7\2\2\3\34\3\3\2"+
		"\2\2\35\36\7\3\2\2\36\37\5\22\n\2\37 \7\4\2\2 !\7\5\2\2!\"\7\6\2\2\"#"+
		"\7\7\2\2#$\7\b\2\2$%\7\t\2\2%&\7\n\2\2&\'\7\13\2\2\'(\7\f\2\2()\5\22\n"+
		"\2)*\7\r\2\2*+\7\4\2\2+,\5\16\b\2,-\7\16\2\2-.\7\16\2\2.\5\3\2\2\2/\60"+
		"\7\3\2\2\60\63\5\22\n\2\61\62\7\17\2\2\62\64\5\22\n\2\63\61\3\2\2\2\63"+
		"\64\3\2\2\2\64\65\3\2\2\2\659\7\4\2\2\668\5\b\5\2\67\66\3\2\2\28;\3\2"+
		"\2\29\67\3\2\2\29:\3\2\2\2:?\3\2\2\2;9\3\2\2\2<>\5\n\6\2=<\3\2\2\2>A\3"+
		"\2\2\2?=\3\2\2\2?@\3\2\2\2@B\3\2\2\2A?\3\2\2\2BC\7\16\2\2C\7\3\2\2\2D"+
		"E\5\f\7\2EF\5\22\n\2FG\7\20\2\2G\t\3\2\2\2HI\7\5\2\2IJ\5\f\7\2JK\5\22"+
		"\n\2KW\7\t\2\2LM\5\f\7\2MT\5\22\n\2NO\7\21\2\2OP\5\f\7\2PQ\5\22\n\2QS"+
		"\3\2\2\2RN\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UX\3\2\2\2VT\3\2\2\2W"+
		"L\3\2\2\2WX\3\2\2\2XY\3\2\2\2YZ\7\r\2\2Z^\7\4\2\2[]\5\b\5\2\\[\3\2\2\2"+
		"]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_d\3\2\2\2`^\3\2\2\2ac\5\16\b\2ba\3\2\2"+
		"\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2eg\3\2\2\2fd\3\2\2\2gh\7\22\2\2hi\5\20"+
		"\t\2ij\7\20\2\2jk\7\16\2\2k\13\3\2\2\2lm\7\23\2\2mn\7\13\2\2ns\7\f\2\2"+
		"os\7\24\2\2ps\7\23\2\2qs\5\22\n\2rl\3\2\2\2ro\3\2\2\2rp\3\2\2\2rq\3\2"+
		"\2\2s\r\3\2\2\2tx\7\4\2\2uw\5\16\b\2vu\3\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3"+
		"\2\2\2y{\3\2\2\2zx\3\2\2\2{\u009e\7\16\2\2|}\7\25\2\2}~\7\t\2\2~\177\5"+
		"\20\t\2\177\u0080\7\r\2\2\u0080\u0081\5\16\b\2\u0081\u0082\7\26\2\2\u0082"+
		"\u0083\5\16\b\2\u0083\u009e\3\2\2\2\u0084\u0085\7\27\2\2\u0085\u0086\7"+
		"\t\2\2\u0086\u0087\5\20\t\2\u0087\u0088\7\r\2\2\u0088\u0089\5\16\b\2\u0089"+
		"\u009e\3\2\2\2\u008a\u008b\7\30\2\2\u008b\u008c\7\t\2\2\u008c\u008d\5"+
		"\20\t\2\u008d\u008e\7\r\2\2\u008e\u008f\7\20\2\2\u008f\u009e\3\2\2\2\u0090"+
		"\u0091\5\22\n\2\u0091\u0092\7\31\2\2\u0092\u0093\5\20\t\2\u0093\u0094"+
		"\7\20\2\2\u0094\u009e\3\2\2\2\u0095\u0096\5\22\n\2\u0096\u0097\7\13\2"+
		"\2\u0097\u0098\5\20\t\2\u0098\u0099\7\f\2\2\u0099\u009a\7\31\2\2\u009a"+
		"\u009b\5\20\t\2\u009b\u009c\7\20\2\2\u009c\u009e\3\2\2\2\u009dt\3\2\2"+
		"\2\u009d|\3\2\2\2\u009d\u0084\3\2\2\2\u009d\u008a\3\2\2\2\u009d\u0090"+
		"\3\2\2\2\u009d\u0095\3\2\2\2\u009e\17\3\2\2\2\u009f\u00a0\b\t\1\2\u00a0"+
		"\u00b7\7\'\2\2\u00a1\u00b7\7!\2\2\u00a2\u00b7\7\"\2\2\u00a3\u00b7\5\22"+
		"\n\2\u00a4\u00b7\7#\2\2\u00a5\u00a6\7$\2\2\u00a6\u00a7\7\23\2\2\u00a7"+
		"\u00a8\7\13\2\2\u00a8\u00a9\5\20\t\2\u00a9\u00aa\7\f\2\2\u00aa\u00b7\3"+
		"\2\2\2\u00ab\u00ac\7$\2\2\u00ac\u00ad\5\22\n\2\u00ad\u00ae\7\t\2\2\u00ae"+
		"\u00af\7\r\2\2\u00af\u00b7\3\2\2\2\u00b0\u00b1\7%\2\2\u00b1\u00b7\5\20"+
		"\t\4\u00b2\u00b3\7\t\2\2\u00b3\u00b4\5\20\t\2\u00b4\u00b5\7\r\2\2\u00b5"+
		"\u00b7\3\2\2\2\u00b6\u009f\3\2\2\2\u00b6\u00a1\3\2\2\2\u00b6\u00a2\3\2"+
		"\2\2\u00b6\u00a3\3\2\2\2\u00b6\u00a4\3\2\2\2\u00b6\u00a5\3\2\2\2\u00b6"+
		"\u00ab\3\2\2\2\u00b6\u00b0\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b7\u00d5\3\2"+
		"\2\2\u00b8\u00b9\f\17\2\2\u00b9\u00ba\t\2\2\2\u00ba\u00d4\5\20\t\20\u00bb"+
		"\u00bc\f\16\2\2\u00bc\u00bd\7\13\2\2\u00bd\u00be\5\20\t\2\u00be\u00bf"+
		"\7\f\2\2\u00bf\u00d4\3\2\2\2\u00c0\u00c1\f\r\2\2\u00c1\u00c2\7\37\2\2"+
		"\u00c2\u00d4\7 \2\2\u00c3\u00c4\f\f\2\2\u00c4\u00c5\7\37\2\2\u00c5\u00c6"+
		"\5\22\n\2\u00c6\u00cf\7\t\2\2\u00c7\u00cc\5\20\t\2\u00c8\u00c9\7\21\2"+
		"\2\u00c9\u00cb\5\20\t\2\u00ca\u00c8\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc"+
		"\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2"+
		"\2\2\u00cf\u00c7\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1"+
		"\u00d2\7\r\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00b8\3\2\2\2\u00d3\u00bb\3\2"+
		"\2\2\u00d3\u00c0\3\2\2\2\u00d3\u00c3\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5"+
		"\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\21\3\2\2\2\u00d7\u00d5\3\2\2"+
		"\2\u00d8\u00d9\7&\2\2\u00d9\u00da\b\n\1\2\u00da\23\3\2\2\2\22\30\639?"+
		"TW^drx\u009d\u00b6\u00cc\u00cf\u00d3\u00d5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}