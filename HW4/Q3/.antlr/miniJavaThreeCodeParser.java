// Generated from c:\Users\Sajjad\Documents\University\Semester 8\Compiler\HW4\HW4\Q3\miniJavaThreeCode.g4 by ANTLR 4.8

    from AddressCodeConverter import *

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class miniJavaThreeCodeParser extends Parser {
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
		RULE_identifier_r = 8, RULE_integerLiteral = 9;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main_class", "class_declaration", "var_declaration", "method_declaration", 
			"type_r", "statement", "expression", "identifier_r", "integerLiteral"
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
	public String getGrammarFileName() { return "miniJavaThreeCode.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }


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


	public miniJavaThreeCodeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public Main_classContext main_class() {
			return getRuleContext(Main_classContext.class,0);
		}
		public TerminalNode EOF() { return getToken(miniJavaThreeCodeParser.EOF, 0); }
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
			print("BEGINS:")
			setState(21);
			main_class();
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0) {
				{
				{
				setState(22);
				class_declaration();
				}
				}
				setState(27);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(28);
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
			setState(30);
			match(T__0);
			setState(31);
			identifier_r();
			setState(32);
			match(T__1);
			setState(33);
			match(T__2);
			setState(34);
			match(T__3);
			setState(35);
			match(T__4);
			setState(36);
			match(T__5);
			setState(37);
			match(T__6);
			setState(38);
			match(T__7);
			setState(39);
			match(T__8);
			setState(40);
			match(T__9);
			setState(41);
			identifier_r();
			setState(42);
			match(T__10);
			setState(43);
			match(T__1);
			setState(44);
			((Main_classContext)_localctx).s = statement();
			setState(45);
			match(T__11);
			setState(46);
			match(T__11);
			print(((Main_classContext)_localctx).s.v)
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
			setState(49);
			match(T__0);
			setState(50);
			identifier_r();
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(51);
				match(T__12);
				setState(52);
				identifier_r();
				}
			}

			setState(55);
			match(T__1);
			setState(59);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__16) | (1L << T__17) | (1L << IDENTIFIER))) != 0)) {
				{
				{
				setState(56);
				var_declaration();
				}
				}
				setState(61);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2) {
				{
				{
				setState(62);
				method_declaration();
				}
				}
				setState(67);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(68);
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
		public Type_rContext type_a;
		public Identifier_rContext identifier;
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
			setState(70);
			((Var_declarationContext)_localctx).type_a = type_r();
			setState(71);
			((Var_declarationContext)_localctx).identifier = identifier_r();
			setState(72);
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
		public StatementContext s;
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
			setState(74);
			match(T__2);
			setState(75);
			type_r();
			setState(76);
			identifier_r();
			setState(77);
			match(T__6);
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__16) | (1L << T__17) | (1L << IDENTIFIER))) != 0)) {
				{
				setState(78);
				type_r();
				setState(79);
				identifier_r();
				setState(86);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__14) {
					{
					{
					setState(80);
					match(T__14);
					setState(81);
					type_r();
					setState(82);
					identifier_r();
					}
					}
					setState(88);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(91);
			match(T__10);
			setState(92);
			match(T__1);
			setState(96);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(93);
					var_declaration();
					}
					} 
				}
				setState(98);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__18) | (1L << T__20) | (1L << T__21) | (1L << IDENTIFIER))) != 0)) {
				{
				{
				setState(99);
				((Method_declarationContext)_localctx).s = statement();
				print(((Method_declarationContext)_localctx).s.v)
				}
				}
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(107);
			match(T__15);
			setState(108);
			expression(0);
			setState(109);
			match(T__13);
			setState(110);
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
		public Identifier_rContext identifier;
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
			setState(118);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(112);
				match(T__16);
				setState(113);
				match(T__8);
				setState(114);
				match(T__9);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(115);
				match(T__17);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(116);
				match(T__16);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(117);
				((Type_rContext)_localctx).identifier = identifier_r();
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
		public  v = str();
		public  type_a = str();
		public  prev_v = str();
		public StatementContext s;
		public ExpressionContext exp;
		public StatementContext ifs;
		public StatementContext es;
		public Identifier_rContext identifier;
		public Identifier_rContext identifier_r;
		public ExpressionContext exp1;
		public ExpressionContext exp2;
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
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(120);
				match(T__1);
				_localctx.v=''
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__18) | (1L << T__20) | (1L << T__21) | (1L << IDENTIFIER))) != 0)) {
					{
					{
					setState(122);
					((StatementContext)_localctx).s = statement();
					_localctx.v+=((StatementContext)_localctx).s.v+'\n'
					}
					}
					setState(129);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(130);
				match(T__11);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(131);
				match(T__18);
				setState(132);
				match(T__6);
				setState(133);
				((StatementContext)_localctx).exp = expression(0);
				setState(134);
				match(T__10);
				setState(135);
				((StatementContext)_localctx).ifs = statement();
				setState(136);
				match(T__19);
				setState(137);
				((StatementContext)_localctx).es = statement();
				if_go = self.new_label()
				else_go = self.new_label()
				_localctx.v += '\n'.join([item for item in ((StatementContext)_localctx).exp.tmps])+'\n'
				_localctx.v+='\t\t if ({}) goto {}\n'.format(((StatementContext)_localctx).exp.v , if_go)
				_localctx.v+=((StatementContext)_localctx).es.v
				_localctx.v+='\t\t goto {}\n'.format(else_go)
				_localctx.v+='{}:{}'.format(if_go,((StatementContext)_localctx).ifs.v)
				_localctx.v+='{}:{}'.format(else_go,'\t\t')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(147);
				match(T__20);
				setState(148);
				match(T__6);
				setState(149);
				((StatementContext)_localctx).exp = expression(0);
				setState(150);
				match(T__10);
				setState(151);
				((StatementContext)_localctx).s = statement();
				go_while=self.new_label()
				inner_while=self.new_label()
				_localctx.v+='\t\t goto {}\n'.format(go_while)
				_localctx.v+='{}:{}'.format(inner_while,((StatementContext)_localctx).s.v)
				_localctx.v+=go_while + '\n'.join([item for item in ((StatementContext)_localctx).exp.tmps])+'\n'
				_localctx.v+='\t\t if({}) goto {}\n'.format(((StatementContext)_localctx).exp.v,inner_while)
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(159);
				match(T__21);
				setState(160);
				match(T__6);
				setState(161);
				expression(0);
				setState(162);
				match(T__10);
				setState(163);
				match(T__13);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(165);
				((StatementContext)_localctx).identifier = identifier_r();
				setState(166);
				match(T__22);
				setState(167);
				((StatementContext)_localctx).exp = expression(0);
				setState(168);
				match(T__13);
				_localctx.v='\n'.join([item for item in ((StatementContext)_localctx).exp.tmps])+'\n'
				_localctx.v+='\t\t {} = {}'.format(((StatementContext)_localctx).identifier.v , ((StatementContext)_localctx).exp.v)
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(172);
				((StatementContext)_localctx).identifier = ((StatementContext)_localctx).identifier_r = identifier_r();
				setState(173);
				match(T__8);
				setState(174);
				((StatementContext)_localctx).exp1 = expression(0);
				setState(175);
				match(T__9);
				setState(176);
				match(T__22);
				setState(177);
				((StatementContext)_localctx).exp2 = expression(0);
				setState(178);
				match(T__13);
				_localctx.v='\n'.join([item for item in ((StatementContext)_localctx).exp1.tmps])+'\n'
				_localctx.v+='\n'.join([item for item in ((StatementContext)_localctx).exp2.tmps])+'\n'
				tmp=self.new_tmp()
				_localctx.v+=AddressCodeConverter.array_initializer(((StatementContext)_localctx).identifier_r.v , ((StatementContext)_localctx).exp1.v , ((StatementContext)_localctx).exp2.v , tmp)
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
		public  v = str();
		public  type_a = str();
		public  prev_v = str();
		public  tmps = [];
		public ExpressionContext expl;
		public ExpressionContext exp1;
		public ExpressionContext exp;
		public IntegerLiteralContext integerLiteral;
		public Identifier_rContext identifier;
		public Token op;
		public ExpressionContext expr;
		public ExpressionContext exp2;
		public IntegerLiteralContext integerLiteral() {
			return getRuleContext(IntegerLiteralContext.class,0);
		}
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
			setState(224);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(187);
				((ExpressionContext)_localctx).integerLiteral = integerLiteral();
				_localctx.type_a,_localctx.v,_localctx.prev_v='INT' , (((ExpressionContext)_localctx).integerLiteral!=null?_input.getText(((ExpressionContext)_localctx).integerLiteral.start,((ExpressionContext)_localctx).integerLiteral.stop):null),None
				}
				break;
			case 2:
				{
				setState(190);
				match(T__30);
				_localctx.type_a,_localctx.v,_localctx.prev_v='BOOL', 'true',None
				}
				break;
			case 3:
				{
				setState(192);
				match(T__31);
				_localctx.type_a,_localctx.v,_localctx.prev_v='BOOL', 'false',None
				}
				break;
			case 4:
				{
				setState(194);
				((ExpressionContext)_localctx).identifier = identifier_r();
				_localctx.type_a,_localctx.v,_localctx.prev_v= (((ExpressionContext)_localctx).identifier.type_a, ((ExpressionContext)_localctx).identifier.v , None) if ((ExpressionContext)_localctx).identifier.type_a=='NOTDEFIENED' else (_localctx.type_a, _localctx.v,_localctx.prev_v)
				}
				break;
			case 5:
				{
				setState(197);
				match(T__32);
				}
				break;
			case 6:
				{
				setState(198);
				match(T__33);
				setState(199);
				match(T__16);
				setState(200);
				match(T__8);
				setState(201);
				expression(0);
				setState(202);
				match(T__9);
				}
				break;
			case 7:
				{
				setState(204);
				match(T__33);
				setState(205);
				identifier_r();
				setState(206);
				match(T__6);
				setState(207);
				match(T__10);
				}
				break;
			case 8:
				{
				setState(209);
				match(T__34);
				setState(210);
				((ExpressionContext)_localctx).exp = expression(2);
				_localctx.tmps=((ExpressionContext)_localctx).exp.tmps
				_localctx.type_a='BOOL'
				temp , _localctx.tmps , ((ExpressionContext)_localctx).exp.v = (self.new_tmp() ,_localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),((ExpressionContext)_localctx).exp.prev_v)] , self.current_tmp()) if ((ExpressionContext)_localctx).exp.prev_v is not None else (None , _localctx.tmps , ((ExpressionContext)_localctx).exp.v)
				_localctx.prev_v = _localctx.v = '!' + ((ExpressionContext)_localctx).exp.v
				}
				break;
			case 9:
				{
				setState(216);
				match(T__6);
				setState(217);
				((ExpressionContext)_localctx).exp = expression(0);
				setState(218);
				match(T__10);
				_localctx.type_a=((ExpressionContext)_localctx).exp.type_a
				_localctx.v = ((ExpressionContext)_localctx).exp.v
				_localctx.prev_v=((ExpressionContext)_localctx).exp.prev_v
				_localctx.tmps=((ExpressionContext)_localctx).exp.tmps
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(281);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(279);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						_localctx.expl = _prevctx;
						_localctx.expl = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(226);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(227);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__23) | (1L << T__24) | (1L << T__25))) != 0)) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(228);
						((ExpressionContext)_localctx).expr = expression(15);
						tmps = ((ExpressionContext)_localctx).expl.tmps
						_localctx.type_a = 'INT'
						temp , _localctx.tmps , ((ExpressionContext)_localctx).expl.v = (self.new_tmp() , _localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),((ExpressionContext)_localctx).expl.prev_v)] , self.current_tmp() ) if ((ExpressionContext)_localctx).expl.prev_v is not None else (None , _localctx.tmps , ((ExpressionContext)_localctx).expl.v)
						_localctx.tmps += ((ExpressionContext)_localctx).expr.tmps
						temp , _localctx.tmps , ((ExpressionContext)_localctx).expr.v = (self.new_tmp() , _localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),((ExpressionContext)_localctx).expr.prev_v)] , self.current_tmp() ) if ((ExpressionContext)_localctx).expr.prev_v is not None else (None , _localctx.tmps , ((ExpressionContext)_localctx).expr.v)
						_localctx.prev_v= _localctx.v = ((ExpressionContext)_localctx).expl.v + (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getText():null) + ((ExpressionContext)_localctx).expr.v
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						_localctx.expl = _prevctx;
						_localctx.expl = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(236);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(237);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__26 || _la==T__27) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(238);
						((ExpressionContext)_localctx).expr = expression(14);
						tmps = ((ExpressionContext)_localctx).expl.tmps
						_localctx.type_a = 'BOOL'
						temp , _localctx.tmps , ((ExpressionContext)_localctx).expl.v = (self.new_tmp() , _localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),((ExpressionContext)_localctx).expl.prev_v)] , self.current_tmp()) if ((ExpressionContext)_localctx).expl.prev_v is not None else (None , _localctx.tmps , ((ExpressionContext)_localctx).expl.v) 
						_localctx.tmps += ((ExpressionContext)_localctx).expr.tmps
						temp , _localctx.tmps , ((ExpressionContext)_localctx).expr.v = (self.new_tmp() , _localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),((ExpressionContext)_localctx).expr.prev_v)] , self.current_tmp()) if ((ExpressionContext)_localctx).expr.prev_v is not None else (None , _localctx.tmps , ((ExpressionContext)_localctx).expr.v)
						_localctx.prev_v= _localctx.v = ((ExpressionContext)_localctx).expl.v + (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getText():null) + ((ExpressionContext)_localctx).expr.v
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						_localctx.exp1 = _prevctx;
						_localctx.exp1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(246);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(247);
						match(T__8);
						setState(248);
						((ExpressionContext)_localctx).exp2 = expression(0);
						setState(249);
						match(T__9);
						_localctx.tmps , _localctx.type_a = ((ExpressionContext)_localctx).exp1.tmps + ((ExpressionContext)_localctx).exp2.tmps , 'INT'
						temp , _localctx.tmps , ((ExpressionContext)_localctx).exp2.v = (self.new_tmp() ,_localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),((ExpressionContext)_localctx).exp2.prev_v)] , self.current_tmp()) if ((ExpressionContext)_localctx).exp2.prev_v is not None else (None , _localctx.tmps , ((ExpressionContext)_localctx).exp2.v)
						temp = self.new_tmp()
						_localctx.tmps += AddressCodeConverter.tmp_array(temp , ((ExpressionContext)_localctx).exp1.v , ((ExpressionContext)_localctx).exp2.v)
						_localctx.prev_v=_localctx.v='*'+temp
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						_localctx.exp = _prevctx;
						_localctx.exp = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(256);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(257);
						match(T__28);
						setState(258);
						match(T__29);
						_localctx.tmps=((ExpressionContext)_localctx).exp.tmps
						_localctx.type_a='INT'
						temp , _localctx.tmps , ((ExpressionContext)_localctx).exp.v = (self.new_tmp() ,_localctx.tmps + ['\t\t {} = {}'.format(self.current_tmp(),((ExpressionContext)_localctx).exp.prev_v)] , self.current_tmp()) if ((ExpressionContext)_localctx).exp.prev_v is not None else (None , _localctx.tmps , ((ExpressionContext)_localctx).exp.v)
						_localctx.prev_v = _localctx.v = ((ExpressionContext)_localctx).exp.v + '.length'
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(263);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(264);
						match(T__28);
						setState(265);
						identifier_r();
						setState(266);
						match(T__6);
						setState(275);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__6) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << IDENTIFIER) | (1L << DECIMAL_LITERAL) | (1L << HEX_LITERAL) | (1L << OCT_LITERAL) | (1L << BINARY_LITERAL))) != 0)) {
							{
							setState(267);
							expression(0);
							setState(272);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==T__14) {
								{
								{
								setState(268);
								match(T__14);
								setState(269);
								expression(0);
								}
								}
								setState(274);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(277);
						match(T__10);
						}
						break;
					}
					} 
				}
				setState(283);
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
		public  type_a = str();
		public Token IDENTIFIER;
		public TerminalNode IDENTIFIER() { return getToken(miniJavaThreeCodeParser.IDENTIFIER, 0); }
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
			setState(284);
			((Identifier_rContext)_localctx).IDENTIFIER = match(IDENTIFIER);
			_localctx.v , _localctx.type_a = (((Identifier_rContext)_localctx).IDENTIFIER!=null?((Identifier_rContext)_localctx).IDENTIFIER.getText():null) , 'NOTDEFIENED'
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

	public static class IntegerLiteralContext extends ParserRuleContext {
		public TerminalNode DECIMAL_LITERAL() { return getToken(miniJavaThreeCodeParser.DECIMAL_LITERAL, 0); }
		public TerminalNode HEX_LITERAL() { return getToken(miniJavaThreeCodeParser.HEX_LITERAL, 0); }
		public TerminalNode OCT_LITERAL() { return getToken(miniJavaThreeCodeParser.OCT_LITERAL, 0); }
		public TerminalNode BINARY_LITERAL() { return getToken(miniJavaThreeCodeParser.BINARY_LITERAL, 0); }
		public IntegerLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_integerLiteral; }
	}

	public final IntegerLiteralContext integerLiteral() throws RecognitionException {
		IntegerLiteralContext _localctx = new IntegerLiteralContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_integerLiteral);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(287);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DECIMAL_LITERAL) | (1L << HEX_LITERAL) | (1L << OCT_LITERAL) | (1L << BINARY_LITERAL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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
			return precpred(_ctx, 14);
		case 1:
			return precpred(_ctx, 13);
		case 2:
			return precpred(_ctx, 12);
		case 3:
			return precpred(_ctx, 11);
		case 4:
			return precpred(_ctx, 10);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-\u0124\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\3\2\3\2\3\2\7\2\32\n\2\f\2\16\2\35\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4"+
		"\3\4\5\48\n\4\3\4\3\4\7\4<\n\4\f\4\16\4?\13\4\3\4\7\4B\n\4\f\4\16\4E\13"+
		"\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6"+
		"W\n\6\f\6\16\6Z\13\6\5\6\\\n\6\3\6\3\6\3\6\7\6a\n\6\f\6\16\6d\13\6\3\6"+
		"\3\6\3\6\7\6i\n\6\f\6\16\6l\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\5\7y\n\7\3\b\3\b\3\b\3\b\3\b\7\b\u0080\n\b\f\b\16\b\u0083\13\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\5\b\u00bb\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00e3\n\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\7\t\u0111\n\t\f\t\16\t\u0114\13\t\5\t\u0116\n\t\3\t\3\t\7"+
		"\t\u011a\n\t\f\t\16\t\u011d\13\t\3\n\3\n\3\n\3\13\3\13\3\13\2\3\20\f\2"+
		"\4\6\b\n\f\16\20\22\24\2\5\3\2\32\34\3\2\35\36\3\2\'*\2\u0139\2\26\3\2"+
		"\2\2\4 \3\2\2\2\6\63\3\2\2\2\bH\3\2\2\2\nL\3\2\2\2\fx\3\2\2\2\16\u00ba"+
		"\3\2\2\2\20\u00e2\3\2\2\2\22\u011e\3\2\2\2\24\u0121\3\2\2\2\26\27\b\2"+
		"\1\2\27\33\5\4\3\2\30\32\5\6\4\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2"+
		"\2\2\33\34\3\2\2\2\34\36\3\2\2\2\35\33\3\2\2\2\36\37\7\2\2\3\37\3\3\2"+
		"\2\2 !\7\3\2\2!\"\5\22\n\2\"#\7\4\2\2#$\7\5\2\2$%\7\6\2\2%&\7\7\2\2&\'"+
		"\7\b\2\2\'(\7\t\2\2()\7\n\2\2)*\7\13\2\2*+\7\f\2\2+,\5\22\n\2,-\7\r\2"+
		"\2-.\7\4\2\2./\5\16\b\2/\60\7\16\2\2\60\61\7\16\2\2\61\62\b\3\1\2\62\5"+
		"\3\2\2\2\63\64\7\3\2\2\64\67\5\22\n\2\65\66\7\17\2\2\668\5\22\n\2\67\65"+
		"\3\2\2\2\678\3\2\2\289\3\2\2\29=\7\4\2\2:<\5\b\5\2;:\3\2\2\2<?\3\2\2\2"+
		"=;\3\2\2\2=>\3\2\2\2>C\3\2\2\2?=\3\2\2\2@B\5\n\6\2A@\3\2\2\2BE\3\2\2\2"+
		"CA\3\2\2\2CD\3\2\2\2DF\3\2\2\2EC\3\2\2\2FG\7\16\2\2G\7\3\2\2\2HI\5\f\7"+
		"\2IJ\5\22\n\2JK\7\20\2\2K\t\3\2\2\2LM\7\5\2\2MN\5\f\7\2NO\5\22\n\2O[\7"+
		"\t\2\2PQ\5\f\7\2QX\5\22\n\2RS\7\21\2\2ST\5\f\7\2TU\5\22\n\2UW\3\2\2\2"+
		"VR\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2[P\3\2\2"+
		"\2[\\\3\2\2\2\\]\3\2\2\2]^\7\r\2\2^b\7\4\2\2_a\5\b\5\2`_\3\2\2\2ad\3\2"+
		"\2\2b`\3\2\2\2bc\3\2\2\2cj\3\2\2\2db\3\2\2\2ef\5\16\b\2fg\b\6\1\2gi\3"+
		"\2\2\2he\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2km\3\2\2\2lj\3\2\2\2mn\7"+
		"\22\2\2no\5\20\t\2op\7\20\2\2pq\7\16\2\2q\13\3\2\2\2rs\7\23\2\2st\7\13"+
		"\2\2ty\7\f\2\2uy\7\24\2\2vy\7\23\2\2wy\5\22\n\2xr\3\2\2\2xu\3\2\2\2xv"+
		"\3\2\2\2xw\3\2\2\2y\r\3\2\2\2z{\7\4\2\2{\u0081\b\b\1\2|}\5\16\b\2}~\b"+
		"\b\1\2~\u0080\3\2\2\2\177|\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3\2\2"+
		"\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u00bb"+
		"\7\16\2\2\u0085\u0086\7\25\2\2\u0086\u0087\7\t\2\2\u0087\u0088\5\20\t"+
		"\2\u0088\u0089\7\r\2\2\u0089\u008a\5\16\b\2\u008a\u008b\7\26\2\2\u008b"+
		"\u008c\5\16\b\2\u008c\u008d\b\b\1\2\u008d\u008e\b\b\1\2\u008e\u008f\b"+
		"\b\1\2\u008f\u0090\b\b\1\2\u0090\u0091\b\b\1\2\u0091\u0092\b\b\1\2\u0092"+
		"\u0093\b\b\1\2\u0093\u0094\b\b\1\2\u0094\u00bb\3\2\2\2\u0095\u0096\7\27"+
		"\2\2\u0096\u0097\7\t\2\2\u0097\u0098\5\20\t\2\u0098\u0099\7\r\2\2\u0099"+
		"\u009a\5\16\b\2\u009a\u009b\b\b\1\2\u009b\u009c\b\b\1\2\u009c\u009d\b"+
		"\b\1\2\u009d\u009e\b\b\1\2\u009e\u009f\b\b\1\2\u009f\u00a0\b\b\1\2\u00a0"+
		"\u00bb\3\2\2\2\u00a1\u00a2\7\30\2\2\u00a2\u00a3\7\t\2\2\u00a3\u00a4\5"+
		"\20\t\2\u00a4\u00a5\7\r\2\2\u00a5\u00a6\7\20\2\2\u00a6\u00bb\3\2\2\2\u00a7"+
		"\u00a8\5\22\n\2\u00a8\u00a9\7\31\2\2\u00a9\u00aa\5\20\t\2\u00aa\u00ab"+
		"\7\20\2\2\u00ab\u00ac\b\b\1\2\u00ac\u00ad\b\b\1\2\u00ad\u00bb\3\2\2\2"+
		"\u00ae\u00af\5\22\n\2\u00af\u00b0\7\13\2\2\u00b0\u00b1\5\20\t\2\u00b1"+
		"\u00b2\7\f\2\2\u00b2\u00b3\7\31\2\2\u00b3\u00b4\5\20\t\2\u00b4\u00b5\7"+
		"\20\2\2\u00b5\u00b6\b\b\1\2\u00b6\u00b7\b\b\1\2\u00b7\u00b8\b\b\1\2\u00b8"+
		"\u00b9\b\b\1\2\u00b9\u00bb\3\2\2\2\u00baz\3\2\2\2\u00ba\u0085\3\2\2\2"+
		"\u00ba\u0095\3\2\2\2\u00ba\u00a1\3\2\2\2\u00ba\u00a7\3\2\2\2\u00ba\u00ae"+
		"\3\2\2\2\u00bb\17\3\2\2\2\u00bc\u00bd\b\t\1\2\u00bd\u00be\5\24\13\2\u00be"+
		"\u00bf\b\t\1\2\u00bf\u00e3\3\2\2\2\u00c0\u00c1\7!\2\2\u00c1\u00e3\b\t"+
		"\1\2\u00c2\u00c3\7\"\2\2\u00c3\u00e3\b\t\1\2\u00c4\u00c5\5\22\n\2\u00c5"+
		"\u00c6\b\t\1\2\u00c6\u00e3\3\2\2\2\u00c7\u00e3\7#\2\2\u00c8\u00c9\7$\2"+
		"\2\u00c9\u00ca\7\23\2\2\u00ca\u00cb\7\13\2\2\u00cb\u00cc\5\20\t\2\u00cc"+
		"\u00cd\7\f\2\2\u00cd\u00e3\3\2\2\2\u00ce\u00cf\7$\2\2\u00cf\u00d0\5\22"+
		"\n\2\u00d0\u00d1\7\t\2\2\u00d1\u00d2\7\r\2\2\u00d2\u00e3\3\2\2\2\u00d3"+
		"\u00d4\7%\2\2\u00d4\u00d5\5\20\t\4\u00d5\u00d6\b\t\1\2\u00d6\u00d7\b\t"+
		"\1\2\u00d7\u00d8\b\t\1\2\u00d8\u00d9\b\t\1\2\u00d9\u00e3\3\2\2\2\u00da"+
		"\u00db\7\t\2\2\u00db\u00dc\5\20\t\2\u00dc\u00dd\7\r\2\2\u00dd\u00de\b"+
		"\t\1\2\u00de\u00df\b\t\1\2\u00df\u00e0\b\t\1\2\u00e0\u00e1\b\t\1\2\u00e1"+
		"\u00e3\3\2\2\2\u00e2\u00bc\3\2\2\2\u00e2\u00c0\3\2\2\2\u00e2\u00c2\3\2"+
		"\2\2\u00e2\u00c4\3\2\2\2\u00e2\u00c7\3\2\2\2\u00e2\u00c8\3\2\2\2\u00e2"+
		"\u00ce\3\2\2\2\u00e2\u00d3\3\2\2\2\u00e2\u00da\3\2\2\2\u00e3\u011b\3\2"+
		"\2\2\u00e4\u00e5\f\20\2\2\u00e5\u00e6\t\2\2\2\u00e6\u00e7\5\20\t\21\u00e7"+
		"\u00e8\b\t\1\2\u00e8\u00e9\b\t\1\2\u00e9\u00ea\b\t\1\2\u00ea\u00eb\b\t"+
		"\1\2\u00eb\u00ec\b\t\1\2\u00ec\u00ed\b\t\1\2\u00ed\u011a\3\2\2\2\u00ee"+
		"\u00ef\f\17\2\2\u00ef\u00f0\t\3\2\2\u00f0\u00f1\5\20\t\20\u00f1\u00f2"+
		"\b\t\1\2\u00f2\u00f3\b\t\1\2\u00f3\u00f4\b\t\1\2\u00f4\u00f5\b\t\1\2\u00f5"+
		"\u00f6\b\t\1\2\u00f6\u00f7\b\t\1\2\u00f7\u011a\3\2\2\2\u00f8\u00f9\f\16"+
		"\2\2\u00f9\u00fa\7\13\2\2\u00fa\u00fb\5\20\t\2\u00fb\u00fc\7\f\2\2\u00fc"+
		"\u00fd\b\t\1\2\u00fd\u00fe\b\t\1\2\u00fe\u00ff\b\t\1\2\u00ff\u0100\b\t"+
		"\1\2\u0100\u0101\b\t\1\2\u0101\u011a\3\2\2\2\u0102\u0103\f\r\2\2\u0103"+
		"\u0104\7\37\2\2\u0104\u0105\7 \2\2\u0105\u0106\b\t\1\2\u0106\u0107\b\t"+
		"\1\2\u0107\u0108\b\t\1\2\u0108\u011a\b\t\1\2\u0109\u010a\f\f\2\2\u010a"+
		"\u010b\7\37\2\2\u010b\u010c\5\22\n\2\u010c\u0115\7\t\2\2\u010d\u0112\5"+
		"\20\t\2\u010e\u010f\7\21\2\2\u010f\u0111\5\20\t\2\u0110\u010e\3\2\2\2"+
		"\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0116"+
		"\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u010d\3\2\2\2\u0115\u0116\3\2\2\2\u0116"+
		"\u0117\3\2\2\2\u0117\u0118\7\r\2\2\u0118\u011a\3\2\2\2\u0119\u00e4\3\2"+
		"\2\2\u0119\u00ee\3\2\2\2\u0119\u00f8\3\2\2\2\u0119\u0102\3\2\2\2\u0119"+
		"\u0109\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2"+
		"\2\2\u011c\21\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\7&\2\2\u011f\u0120"+
		"\b\n\1\2\u0120\23\3\2\2\2\u0121\u0122\t\4\2\2\u0122\25\3\2\2\2\22\33\67"+
		"=CX[bjx\u0081\u00ba\u00e2\u0112\u0115\u0119\u011b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}