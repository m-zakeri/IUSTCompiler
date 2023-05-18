// Generated from /home/loop/Desktop/Ass/Compiler/HW4/ast.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class astParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, Class=3, Public=4, Static=5, Void=6, Main=7, LBrace=8, 
		RBrace=9, LPran=10, RPran=11, LBrack=12, RBrack=13, If=14, Else=15, While=16, 
		SemiColon=17, Equals=18, Dot=19, Comma=20, True=21, False=22, This=23, 
		New=24, IntType=25, StringType=26, BoolType=27, Exclamation=28, BinaryOperator=29, 
		Integer=30, Extends=31, Return=32, Identifier=33, WS=34, COMMENT=35, LINE_COMMENT=36;
	public static final int
		RULE_program = 0, RULE_mainClass = 1, RULE_mainClassDecl = 2, RULE_mainMethodDecl = 3, 
		RULE_mainMethodBody = 4, RULE_classDecl = 5, RULE_varDecl = 6, RULE_methodDecl = 7, 
		RULE_methodBody = 8, RULE_type = 9, RULE_statement = 10, RULE_exp = 11, 
		RULE_binOp = 12, RULE_identifier = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "mainClass", "mainClassDecl", "mainMethodDecl", "mainMethodBody", 
			"classDecl", "varDecl", "methodDecl", "methodBody", "type", "statement", 
			"exp", "binOp", "identifier"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'System.out.println'", "'length'", "'class'", "'public'", "'static'", 
			"'void'", "'main'", "'{'", "'}'", "'('", "')'", "'['", "']'", "'if'", 
			"'else'", "'while'", "';'", "'='", "'.'", "','", "'true'", "'false'", 
			"'this'", "'new'", "'int'", "'String'", "'bool'", "'!'", null, null, 
			"'extends'", "'return'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "Class", "Public", "Static", "Void", "Main", "LBrace", 
			"RBrace", "LPran", "RPran", "LBrack", "RBrack", "If", "Else", "While", 
			"SemiColon", "Equals", "Dot", "Comma", "True", "False", "This", "New", 
			"IntType", "StringType", "BoolType", "Exclamation", "BinaryOperator", 
			"Integer", "Extends", "Return", "Identifier", "WS", "COMMENT", "LINE_COMMENT"
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
	public String getGrammarFileName() { return "ast.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public astParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public MainClassContext mainClass() {
			return getRuleContext(MainClassContext.class,0);
		}
		public TerminalNode EOF() { return getToken(astParser.EOF, 0); }
		public List<ClassDeclContext> classDecl() {
			return getRuleContexts(ClassDeclContext.class);
		}
		public ClassDeclContext classDecl(int i) {
			return getRuleContext(ClassDeclContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			mainClass();
			setState(32);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Class) {
				{
				{
				setState(29);
				classDecl();
				}
				}
				setState(34);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(35);
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

	public static class MainClassContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode Class() { return getToken(astParser.Class, 0); }
		public MainClassDeclContext mainClassDecl() {
			return getRuleContext(MainClassDeclContext.class,0);
		}
		public MainClassContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mainClass; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterMainClass(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitMainClass(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitMainClass(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MainClassContext mainClass() throws RecognitionException {
		MainClassContext _localctx = new MainClassContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_mainClass);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			match(Class);
			setState(38);
			mainClassDecl();
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

	public static class MainClassDeclContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode LBrace() { return getToken(astParser.LBrace, 0); }
		public MainMethodDeclContext mainMethodDecl() {
			return getRuleContext(MainMethodDeclContext.class,0);
		}
		public TerminalNode RBrace() { return getToken(astParser.RBrace, 0); }
		public MainClassDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mainClassDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterMainClassDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitMainClassDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitMainClassDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MainClassDeclContext mainClassDecl() throws RecognitionException {
		MainClassDeclContext _localctx = new MainClassDeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_mainClassDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			identifier();
			setState(41);
			match(LBrace);
			setState(42);
			mainMethodDecl();
			setState(43);
			match(RBrace);
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

	public static class MainMethodDeclContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode Public() { return getToken(astParser.Public, 0); }
		public TerminalNode Static() { return getToken(astParser.Static, 0); }
		public TerminalNode Void() { return getToken(astParser.Void, 0); }
		public TerminalNode Main() { return getToken(astParser.Main, 0); }
		public TerminalNode LPran() { return getToken(astParser.LPran, 0); }
		public TerminalNode StringType() { return getToken(astParser.StringType, 0); }
		public TerminalNode LBrack() { return getToken(astParser.LBrack, 0); }
		public TerminalNode RBrack() { return getToken(astParser.RBrack, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode RPran() { return getToken(astParser.RPran, 0); }
		public MainMethodBodyContext mainMethodBody() {
			return getRuleContext(MainMethodBodyContext.class,0);
		}
		public MainMethodDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mainMethodDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterMainMethodDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitMainMethodDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitMainMethodDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MainMethodDeclContext mainMethodDecl() throws RecognitionException {
		MainMethodDeclContext _localctx = new MainMethodDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_mainMethodDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(Public);
			setState(46);
			match(Static);
			setState(47);
			match(Void);
			setState(48);
			match(Main);
			setState(49);
			match(LPran);
			setState(50);
			match(StringType);
			setState(51);
			match(LBrack);
			setState(52);
			match(RBrack);
			setState(53);
			identifier();
			setState(54);
			match(RPran);
			setState(55);
			mainMethodBody();
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

	public static class MainMethodBodyContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode LBrace() { return getToken(astParser.LBrace, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode RBrace() { return getToken(astParser.RBrace, 0); }
		public MainMethodBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mainMethodBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterMainMethodBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitMainMethodBody(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitMainMethodBody(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MainMethodBodyContext mainMethodBody() throws RecognitionException {
		MainMethodBodyContext _localctx = new MainMethodBodyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_mainMethodBody);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(LBrace);
			setState(58);
			statement();
			setState(59);
			match(RBrace);
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

	public static class ClassDeclContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode Class() { return getToken(astParser.Class, 0); }
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode LBrace() { return getToken(astParser.LBrace, 0); }
		public TerminalNode RBrace() { return getToken(astParser.RBrace, 0); }
		public TerminalNode Extends() { return getToken(astParser.Extends, 0); }
		public List<VarDeclContext> varDecl() {
			return getRuleContexts(VarDeclContext.class);
		}
		public VarDeclContext varDecl(int i) {
			return getRuleContext(VarDeclContext.class,i);
		}
		public List<MethodDeclContext> methodDecl() {
			return getRuleContexts(MethodDeclContext.class);
		}
		public MethodDeclContext methodDecl(int i) {
			return getRuleContext(MethodDeclContext.class,i);
		}
		public ClassDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterClassDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitClassDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitClassDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ClassDeclContext classDecl() throws RecognitionException {
		ClassDeclContext _localctx = new ClassDeclContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_classDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(Class);
			setState(62);
			identifier();
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Extends) {
				{
				setState(63);
				match(Extends);
				setState(64);
				identifier();
				}
			}

			setState(67);
			match(LBrace);
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntType) | (1L << BoolType) | (1L << Identifier))) != 0)) {
				{
				{
				setState(68);
				varDecl();
				}
				}
				setState(73);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Public) {
				{
				{
				setState(74);
				methodDecl();
				}
				}
				setState(79);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(80);
			match(RBrace);
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

	public static class VarDeclContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode SemiColon() { return getToken(astParser.SemiColon, 0); }
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterVarDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitVarDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitVarDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_varDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			type();
			setState(83);
			identifier();
			setState(84);
			match(SemiColon);
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

	public static class MethodDeclContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode Public() { return getToken(astParser.Public, 0); }
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode LPran() { return getToken(astParser.LPran, 0); }
		public TerminalNode RPran() { return getToken(astParser.RPran, 0); }
		public MethodBodyContext methodBody() {
			return getRuleContext(MethodBodyContext.class,0);
		}
		public List<TerminalNode> Comma() { return getTokens(astParser.Comma); }
		public TerminalNode Comma(int i) {
			return getToken(astParser.Comma, i);
		}
		public List<TerminalNode> Identifier() { return getTokens(astParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(astParser.Identifier, i);
		}
		public MethodDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterMethodDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitMethodDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitMethodDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MethodDeclContext methodDecl() throws RecognitionException {
		MethodDeclContext _localctx = new MethodDeclContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_methodDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(Public);
			setState(87);
			type();
			setState(88);
			identifier();
			setState(89);
			match(LPran);
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntType) | (1L << BoolType) | (1L << Identifier))) != 0)) {
				{
				setState(90);
				type();
				setState(91);
				identifier();
				setState(98);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==Comma) {
					{
					{
					setState(92);
					match(Comma);
					setState(93);
					type();
					setState(94);
					match(Identifier);
					}
					}
					setState(100);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(103);
			match(RPran);
			setState(104);
			methodBody();
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

	public static class MethodBodyContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode LBrace() { return getToken(astParser.LBrace, 0); }
		public TerminalNode Return() { return getToken(astParser.Return, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode SemiColon() { return getToken(astParser.SemiColon, 0); }
		public TerminalNode RBrace() { return getToken(astParser.RBrace, 0); }
		public List<VarDeclContext> varDecl() {
			return getRuleContexts(VarDeclContext.class);
		}
		public VarDeclContext varDecl(int i) {
			return getRuleContext(VarDeclContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public MethodBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterMethodBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitMethodBody(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitMethodBody(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MethodBodyContext methodBody() throws RecognitionException {
		MethodBodyContext _localctx = new MethodBodyContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_methodBody);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(LBrace);
			setState(110);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(107);
					varDecl();
					}
					} 
				}
				setState(112);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			setState(116);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << LBrace) | (1L << If) | (1L << While) | (1L << Identifier))) != 0)) {
				{
				{
				setState(113);
				statement();
				}
				}
				setState(118);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(119);
			match(Return);
			setState(120);
			exp(0);
			setState(121);
			match(SemiColon);
			setState(122);
			match(RBrace);
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

	public static class TypeContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode IntType() { return getToken(astParser.IntType, 0); }
		public TerminalNode LBrack() { return getToken(astParser.LBrack, 0); }
		public TerminalNode RBrack() { return getToken(astParser.RBrack, 0); }
		public TerminalNode BoolType() { return getToken(astParser.BoolType, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitType(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitType(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_type);
		try {
			setState(130);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(124);
				match(IntType);
				setState(125);
				match(LBrack);
				setState(126);
				match(RBrack);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				match(BoolType);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(128);
				match(IntType);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(129);
				identifier();
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
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode LBrace() { return getToken(astParser.LBrace, 0); }
		public TerminalNode RBrace() { return getToken(astParser.RBrace, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode If() { return getToken(astParser.If, 0); }
		public TerminalNode LPran() { return getToken(astParser.LPran, 0); }
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode RPran() { return getToken(astParser.RPran, 0); }
		public TerminalNode Else() { return getToken(astParser.Else, 0); }
		public TerminalNode While() { return getToken(astParser.While, 0); }
		public TerminalNode SemiColon() { return getToken(astParser.SemiColon, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode Equals() { return getToken(astParser.Equals, 0); }
		public TerminalNode LBrack() { return getToken(astParser.LBrack, 0); }
		public TerminalNode RBrack() { return getToken(astParser.RBrack, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_statement);
		int _la;
		try {
			setState(173);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(132);
				match(LBrace);
				setState(136);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << LBrace) | (1L << If) | (1L << While) | (1L << Identifier))) != 0)) {
					{
					{
					setState(133);
					statement();
					}
					}
					setState(138);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(139);
				match(RBrace);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(140);
				match(If);
				setState(141);
				match(LPran);
				setState(142);
				exp(0);
				setState(143);
				match(RPran);
				setState(144);
				statement();
				setState(145);
				match(Else);
				setState(146);
				statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(148);
				match(While);
				setState(149);
				match(LPran);
				setState(150);
				exp(0);
				setState(151);
				match(RPran);
				setState(152);
				statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(154);
				match(T__0);
				setState(155);
				match(LPran);
				setState(156);
				exp(0);
				setState(157);
				match(RPran);
				setState(158);
				match(SemiColon);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(160);
				identifier();
				setState(161);
				match(Equals);
				setState(162);
				exp(0);
				setState(163);
				match(SemiColon);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(165);
				identifier();
				setState(166);
				match(LBrack);
				setState(167);
				exp(0);
				setState(168);
				match(RBrack);
				setState(169);
				match(Equals);
				setState(170);
				exp(0);
				setState(171);
				match(SemiColon);
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

	public static class ExpContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode Integer() { return getToken(astParser.Integer, 0); }
		public TerminalNode True() { return getToken(astParser.True, 0); }
		public TerminalNode False() { return getToken(astParser.False, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode This() { return getToken(astParser.This, 0); }
		public TerminalNode New() { return getToken(astParser.New, 0); }
		public TerminalNode IntType() { return getToken(astParser.IntType, 0); }
		public TerminalNode LBrack() { return getToken(astParser.LBrack, 0); }
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode RBrack() { return getToken(astParser.RBrack, 0); }
		public TerminalNode LPran() { return getToken(astParser.LPran, 0); }
		public TerminalNode RPran() { return getToken(astParser.RPran, 0); }
		public TerminalNode Exclamation() { return getToken(astParser.Exclamation, 0); }
		public BinOpContext binOp() {
			return getRuleContext(BinOpContext.class,0);
		}
		public TerminalNode Dot() { return getToken(astParser.Dot, 0); }
		public List<TerminalNode> Comma() { return getTokens(astParser.Comma); }
		public TerminalNode Comma(int i) {
			return getToken(astParser.Comma, i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitExp(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitExp(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		return exp(0);
	}

	private ExpContext exp(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpContext _localctx = new ExpContext(_ctx, _parentState);
		ExpContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_exp, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(176);
				match(Integer);
				}
				break;
			case 2:
				{
				setState(177);
				match(True);
				}
				break;
			case 3:
				{
				setState(178);
				match(False);
				}
				break;
			case 4:
				{
				setState(179);
				identifier();
				}
				break;
			case 5:
				{
				setState(180);
				match(This);
				}
				break;
			case 6:
				{
				setState(181);
				match(New);
				setState(182);
				match(IntType);
				setState(183);
				match(LBrack);
				setState(184);
				exp(0);
				setState(185);
				match(RBrack);
				}
				break;
			case 7:
				{
				setState(187);
				match(New);
				setState(188);
				identifier();
				setState(189);
				match(LPran);
				setState(190);
				match(RPran);
				}
				break;
			case 8:
				{
				setState(192);
				match(Exclamation);
				setState(193);
				exp(2);
				}
				break;
			case 9:
				{
				setState(194);
				match(LPran);
				setState(195);
				exp(0);
				setState(196);
				match(RPran);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(230);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(228);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
					case 1:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(200);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						{
						setState(201);
						binOp();
						}
						setState(202);
						exp(14);
						}
						break;
					case 2:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(204);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(205);
						match(LBrack);
						setState(206);
						exp(0);
						setState(207);
						match(RBrack);
						}
						break;
					case 3:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(209);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(210);
						match(Dot);
						setState(211);
						match(T__1);
						}
						break;
					case 4:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(212);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(213);
						match(Dot);
						setState(214);
						identifier();
						setState(215);
						match(LPran);
						setState(224);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LPran) | (1L << True) | (1L << False) | (1L << This) | (1L << New) | (1L << Exclamation) | (1L << Integer) | (1L << Identifier))) != 0)) {
							{
							setState(216);
							exp(0);
							setState(221);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==Comma) {
								{
								{
								setState(217);
								match(Comma);
								setState(218);
								exp(0);
								}
								}
								setState(223);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(226);
						match(RPran);
						}
						break;
					}
					} 
				}
				setState(232);
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

	public static class BinOpContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode BinaryOperator() { return getToken(astParser.BinaryOperator, 0); }
		public BinOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binOp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterBinOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitBinOp(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitBinOp(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BinOpContext binOp() throws RecognitionException {
		BinOpContext _localctx = new BinOpContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_binOp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(233);
			match(BinaryOperator);
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

	public static class IdentifierContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode Identifier() { return getToken(astParser.Identifier, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).enterIdentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof astListener ) ((astListener)listener).exitIdentifier(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof astVisitor ) return ((astVisitor<? extends T>)visitor).visitIdentifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			match(Identifier);
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
		case 11:
			return exp_sempred((ExpContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean exp_sempred(ExpContext _localctx, int predIndex) {
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3&\u00f0\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\7\2!\n\2\f\2\16\2$\13"+
		"\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7D\n\7\3\7\3\7"+
		"\7\7H\n\7\f\7\16\7K\13\7\3\7\7\7N\n\7\f\7\16\7Q\13\7\3\7\3\7\3\b\3\b\3"+
		"\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\tc\n\t\f\t\16\tf\13\t"+
		"\5\th\n\t\3\t\3\t\3\t\3\n\3\n\7\no\n\n\f\n\16\nr\13\n\3\n\7\nu\n\n\f\n"+
		"\16\nx\13\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u0085"+
		"\n\13\3\f\3\f\7\f\u0089\n\f\f\f\16\f\u008c\13\f\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b0\n\f\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\5\r\u00c9\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00de\n\r\f\r\16\r\u00e1\13\r\5\r\u00e3"+
		"\n\r\3\r\3\r\7\r\u00e7\n\r\f\r\16\r\u00ea\13\r\3\16\3\16\3\17\3\17\3\17"+
		"\2\3\30\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\2\2\u0100\2\36\3\2\2"+
		"\2\4\'\3\2\2\2\6*\3\2\2\2\b/\3\2\2\2\n;\3\2\2\2\f?\3\2\2\2\16T\3\2\2\2"+
		"\20X\3\2\2\2\22l\3\2\2\2\24\u0084\3\2\2\2\26\u00af\3\2\2\2\30\u00c8\3"+
		"\2\2\2\32\u00eb\3\2\2\2\34\u00ed\3\2\2\2\36\"\5\4\3\2\37!\5\f\7\2 \37"+
		"\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\"\3\2\2\2%&\7\2\2"+
		"\3&\3\3\2\2\2\'(\7\5\2\2()\5\6\4\2)\5\3\2\2\2*+\5\34\17\2+,\7\n\2\2,-"+
		"\5\b\5\2-.\7\13\2\2.\7\3\2\2\2/\60\7\6\2\2\60\61\7\7\2\2\61\62\7\b\2\2"+
		"\62\63\7\t\2\2\63\64\7\f\2\2\64\65\7\34\2\2\65\66\7\16\2\2\66\67\7\17"+
		"\2\2\678\5\34\17\289\7\r\2\29:\5\n\6\2:\t\3\2\2\2;<\7\n\2\2<=\5\26\f\2"+
		"=>\7\13\2\2>\13\3\2\2\2?@\7\5\2\2@C\5\34\17\2AB\7!\2\2BD\5\34\17\2CA\3"+
		"\2\2\2CD\3\2\2\2DE\3\2\2\2EI\7\n\2\2FH\5\16\b\2GF\3\2\2\2HK\3\2\2\2IG"+
		"\3\2\2\2IJ\3\2\2\2JO\3\2\2\2KI\3\2\2\2LN\5\20\t\2ML\3\2\2\2NQ\3\2\2\2"+
		"OM\3\2\2\2OP\3\2\2\2PR\3\2\2\2QO\3\2\2\2RS\7\13\2\2S\r\3\2\2\2TU\5\24"+
		"\13\2UV\5\34\17\2VW\7\23\2\2W\17\3\2\2\2XY\7\6\2\2YZ\5\24\13\2Z[\5\34"+
		"\17\2[g\7\f\2\2\\]\5\24\13\2]d\5\34\17\2^_\7\26\2\2_`\5\24\13\2`a\7#\2"+
		"\2ac\3\2\2\2b^\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2eh\3\2\2\2fd\3\2\2"+
		"\2g\\\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\7\r\2\2jk\5\22\n\2k\21\3\2\2\2lp\7"+
		"\n\2\2mo\5\16\b\2nm\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2qv\3\2\2\2rp"+
		"\3\2\2\2su\5\26\f\2ts\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2wy\3\2\2\2"+
		"xv\3\2\2\2yz\7\"\2\2z{\5\30\r\2{|\7\23\2\2|}\7\13\2\2}\23\3\2\2\2~\177"+
		"\7\33\2\2\177\u0080\7\16\2\2\u0080\u0085\7\17\2\2\u0081\u0085\7\35\2\2"+
		"\u0082\u0085\7\33\2\2\u0083\u0085\5\34\17\2\u0084~\3\2\2\2\u0084\u0081"+
		"\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\25\3\2\2\2\u0086"+
		"\u008a\7\n\2\2\u0087\u0089\5\26\f\2\u0088\u0087\3\2\2\2\u0089\u008c\3"+
		"\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008d\3\2\2\2\u008c"+
		"\u008a\3\2\2\2\u008d\u00b0\7\13\2\2\u008e\u008f\7\20\2\2\u008f\u0090\7"+
		"\f\2\2\u0090\u0091\5\30\r\2\u0091\u0092\7\r\2\2\u0092\u0093\5\26\f\2\u0093"+
		"\u0094\7\21\2\2\u0094\u0095\5\26\f\2\u0095\u00b0\3\2\2\2\u0096\u0097\7"+
		"\22\2\2\u0097\u0098\7\f\2\2\u0098\u0099\5\30\r\2\u0099\u009a\7\r\2\2\u009a"+
		"\u009b\5\26\f\2\u009b\u00b0\3\2\2\2\u009c\u009d\7\3\2\2\u009d\u009e\7"+
		"\f\2\2\u009e\u009f\5\30\r\2\u009f\u00a0\7\r\2\2\u00a0\u00a1\7\23\2\2\u00a1"+
		"\u00b0\3\2\2\2\u00a2\u00a3\5\34\17\2\u00a3\u00a4\7\24\2\2\u00a4\u00a5"+
		"\5\30\r\2\u00a5\u00a6\7\23\2\2\u00a6\u00b0\3\2\2\2\u00a7\u00a8\5\34\17"+
		"\2\u00a8\u00a9\7\16\2\2\u00a9\u00aa\5\30\r\2\u00aa\u00ab\7\17\2\2\u00ab"+
		"\u00ac\7\24\2\2\u00ac\u00ad\5\30\r\2\u00ad\u00ae\7\23\2\2\u00ae\u00b0"+
		"\3\2\2\2\u00af\u0086\3\2\2\2\u00af\u008e\3\2\2\2\u00af\u0096\3\2\2\2\u00af"+
		"\u009c\3\2\2\2\u00af\u00a2\3\2\2\2\u00af\u00a7\3\2\2\2\u00b0\27\3\2\2"+
		"\2\u00b1\u00b2\b\r\1\2\u00b2\u00c9\7 \2\2\u00b3\u00c9\7\27\2\2\u00b4\u00c9"+
		"\7\30\2\2\u00b5\u00c9\5\34\17\2\u00b6\u00c9\7\31\2\2\u00b7\u00b8\7\32"+
		"\2\2\u00b8\u00b9\7\33\2\2\u00b9\u00ba\7\16\2\2\u00ba\u00bb\5\30\r\2\u00bb"+
		"\u00bc\7\17\2\2\u00bc\u00c9\3\2\2\2\u00bd\u00be\7\32\2\2\u00be\u00bf\5"+
		"\34\17\2\u00bf\u00c0\7\f\2\2\u00c0\u00c1\7\r\2\2\u00c1\u00c9\3\2\2\2\u00c2"+
		"\u00c3\7\36\2\2\u00c3\u00c9\5\30\r\4\u00c4\u00c5\7\f\2\2\u00c5\u00c6\5"+
		"\30\r\2\u00c6\u00c7\7\r\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00b1\3\2\2\2\u00c8"+
		"\u00b3\3\2\2\2\u00c8\u00b4\3\2\2\2\u00c8\u00b5\3\2\2\2\u00c8\u00b6\3\2"+
		"\2\2\u00c8\u00b7\3\2\2\2\u00c8\u00bd\3\2\2\2\u00c8\u00c2\3\2\2\2\u00c8"+
		"\u00c4\3\2\2\2\u00c9\u00e8\3\2\2\2\u00ca\u00cb\f\17\2\2\u00cb\u00cc\5"+
		"\32\16\2\u00cc\u00cd\5\30\r\20\u00cd\u00e7\3\2\2\2\u00ce\u00cf\f\16\2"+
		"\2\u00cf\u00d0\7\16\2\2\u00d0\u00d1\5\30\r\2\u00d1\u00d2\7\17\2\2\u00d2"+
		"\u00e7\3\2\2\2\u00d3\u00d4\f\r\2\2\u00d4\u00d5\7\25\2\2\u00d5\u00e7\7"+
		"\4\2\2\u00d6\u00d7\f\f\2\2\u00d7\u00d8\7\25\2\2\u00d8\u00d9\5\34\17\2"+
		"\u00d9\u00e2\7\f\2\2\u00da\u00df\5\30\r\2\u00db\u00dc\7\26\2\2\u00dc\u00de"+
		"\5\30\r\2\u00dd\u00db\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2"+
		"\u00df\u00e0\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00da"+
		"\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\7\r\2\2\u00e5"+
		"\u00e7\3\2\2\2\u00e6\u00ca\3\2\2\2\u00e6\u00ce\3\2\2\2\u00e6\u00d3\3\2"+
		"\2\2\u00e6\u00d6\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8"+
		"\u00e9\3\2\2\2\u00e9\31\3\2\2\2\u00ea\u00e8\3\2\2\2\u00eb\u00ec\7\37\2"+
		"\2\u00ec\33\3\2\2\2\u00ed\u00ee\7#\2\2\u00ee\35\3\2\2\2\22\"CIOdgpv\u0084"+
		"\u008a\u00af\u00c8\u00df\u00e2\u00e6\u00e8";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}