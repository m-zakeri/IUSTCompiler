// Generated from C:/Users/asus/Desktop\q2.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class q2Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MainClass=1, ClassDeclaration=2, VarDeclaration=3, Type=4, MethodDeclaration=5, 
		Statement=6, Expression=7, Expression_prim=8, Identifier=9, COMMENT=10, 
		LINE_COMMENT=11, IDENTIFIER=12, INTEGER_LITERAL=13;
	public static final int
		RULE_program = 0;
	private static String[] makeRuleNames() {
		return new String[] {
			"program"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MainClass", "ClassDeclaration", "VarDeclaration", "Type", "MethodDeclaration", 
			"Statement", "Expression", "Expression_prim", "Identifier", "COMMENT", 
			"LINE_COMMENT", "IDENTIFIER", "INTEGER_LITERAL"
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
	public String getGrammarFileName() { return "q2.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public q2Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode MainClass() { return getToken(q2Parser.MainClass, 0); }
		public TerminalNode EOF() { return getToken(q2Parser.EOF, 0); }
		public List<TerminalNode> ClassDeclaration() { return getTokens(q2Parser.ClassDeclaration); }
		public TerminalNode ClassDeclaration(int i) {
			return getToken(q2Parser.ClassDeclaration, i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof q2Listener ) ((q2Listener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof q2Listener ) ((q2Listener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof q2Visitor ) return ((q2Visitor<? extends T>)visitor).visitProgram(this);
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
			setState(2);
			match(MainClass);
			setState(6);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ClassDeclaration) {
				{
				{
				setState(3);
				match(ClassDeclaration);
				}
				}
				setState(8);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(9);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17\16\4\2\t\2\3\2"+
		"\3\2\7\2\7\n\2\f\2\16\2\n\13\2\3\2\3\2\3\2\2\2\3\2\2\2\2\r\2\4\3\2\2\2"+
		"\4\b\7\3\2\2\5\7\7\4\2\2\6\5\3\2\2\2\7\n\3\2\2\2\b\6\3\2\2\2\b\t\3\2\2"+
		"\2\t\13\3\2\2\2\n\b\3\2\2\2\13\f\7\2\2\3\f\3\3\2\2\2\3\b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}