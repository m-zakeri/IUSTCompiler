// Generated from /home/loop/Desktop/Ass/Compiler/HW4/ast.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class astLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "Class", "Public", "Static", "Void", "Main", "LBrace", 
			"RBrace", "LPran", "RPran", "LBrack", "RBrack", "If", "Else", "While", 
			"SemiColon", "Equals", "Dot", "Comma", "True", "False", "This", "New", 
			"IntType", "StringType", "BoolType", "Exclamation", "BinaryOperator", 
			"Integer", "Extends", "Return", "Identifier", "LetterOrDigit", "Letter", 
			"WS", "COMMENT", "LINE_COMMENT"
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


	public astLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ast.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2&\u0119\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n"+
		"\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20"+
		"\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24"+
		"\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30"+
		"\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33"+
		"\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36"+
		"\3\36\5\36\u00d3\n\36\3\37\6\37\u00d6\n\37\r\37\16\37\u00d7\3 \3 \3 \3"+
		" \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\7\"\u00eb\n\"\f\"\16\"\u00ee"+
		"\13\"\3#\3#\5#\u00f2\n#\3$\3$\3$\3$\5$\u00f8\n$\3%\6%\u00fb\n%\r%\16%"+
		"\u00fc\3%\3%\3&\3&\3&\3&\7&\u0105\n&\f&\16&\u0108\13&\3&\3&\3&\3&\3&\3"+
		"\'\3\'\3\'\3\'\7\'\u0113\n\'\f\'\16\'\u0116\13\'\3\'\3\'\3\u0106\2(\3"+
		"\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37"+
		"\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37="+
		" ?!A\"C#E\2G\2I$K%M&\3\2\n\5\2,-//>>\3\2\62;\6\2&&C\\aac|\4\2\2\u0081"+
		"\ud802\udc01\3\2\ud802\udc01\3\2\udc02\ue001\5\2\13\f\16\17\"\"\4\2\f"+
		"\f\17\17\2\u011f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2"+
		"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3"+
		"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2"+
		"\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2I"+
		"\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\3O\3\2\2\2\5b\3\2\2\2\7i\3\2\2\2\to\3\2"+
		"\2\2\13v\3\2\2\2\r}\3\2\2\2\17\u0082\3\2\2\2\21\u0087\3\2\2\2\23\u0089"+
		"\3\2\2\2\25\u008b\3\2\2\2\27\u008d\3\2\2\2\31\u008f\3\2\2\2\33\u0091\3"+
		"\2\2\2\35\u0093\3\2\2\2\37\u0096\3\2\2\2!\u009b\3\2\2\2#\u00a1\3\2\2\2"+
		"%\u00a3\3\2\2\2\'\u00a5\3\2\2\2)\u00a7\3\2\2\2+\u00a9\3\2\2\2-\u00ae\3"+
		"\2\2\2/\u00b4\3\2\2\2\61\u00b9\3\2\2\2\63\u00bd\3\2\2\2\65\u00c1\3\2\2"+
		"\2\67\u00c8\3\2\2\29\u00cd\3\2\2\2;\u00d2\3\2\2\2=\u00d5\3\2\2\2?\u00d9"+
		"\3\2\2\2A\u00e1\3\2\2\2C\u00e8\3\2\2\2E\u00f1\3\2\2\2G\u00f7\3\2\2\2I"+
		"\u00fa\3\2\2\2K\u0100\3\2\2\2M\u010e\3\2\2\2OP\7U\2\2PQ\7{\2\2QR\7u\2"+
		"\2RS\7v\2\2ST\7g\2\2TU\7o\2\2UV\7\60\2\2VW\7q\2\2WX\7w\2\2XY\7v\2\2YZ"+
		"\7\60\2\2Z[\7r\2\2[\\\7t\2\2\\]\7k\2\2]^\7p\2\2^_\7v\2\2_`\7n\2\2`a\7"+
		"p\2\2a\4\3\2\2\2bc\7n\2\2cd\7g\2\2de\7p\2\2ef\7i\2\2fg\7v\2\2gh\7j\2\2"+
		"h\6\3\2\2\2ij\7e\2\2jk\7n\2\2kl\7c\2\2lm\7u\2\2mn\7u\2\2n\b\3\2\2\2op"+
		"\7r\2\2pq\7w\2\2qr\7d\2\2rs\7n\2\2st\7k\2\2tu\7e\2\2u\n\3\2\2\2vw\7u\2"+
		"\2wx\7v\2\2xy\7c\2\2yz\7v\2\2z{\7k\2\2{|\7e\2\2|\f\3\2\2\2}~\7x\2\2~\177"+
		"\7q\2\2\177\u0080\7k\2\2\u0080\u0081\7f\2\2\u0081\16\3\2\2\2\u0082\u0083"+
		"\7o\2\2\u0083\u0084\7c\2\2\u0084\u0085\7k\2\2\u0085\u0086\7p\2\2\u0086"+
		"\20\3\2\2\2\u0087\u0088\7}\2\2\u0088\22\3\2\2\2\u0089\u008a\7\177\2\2"+
		"\u008a\24\3\2\2\2\u008b\u008c\7*\2\2\u008c\26\3\2\2\2\u008d\u008e\7+\2"+
		"\2\u008e\30\3\2\2\2\u008f\u0090\7]\2\2\u0090\32\3\2\2\2\u0091\u0092\7"+
		"_\2\2\u0092\34\3\2\2\2\u0093\u0094\7k\2\2\u0094\u0095\7h\2\2\u0095\36"+
		"\3\2\2\2\u0096\u0097\7g\2\2\u0097\u0098\7n\2\2\u0098\u0099\7u\2\2\u0099"+
		"\u009a\7g\2\2\u009a \3\2\2\2\u009b\u009c\7y\2\2\u009c\u009d\7j\2\2\u009d"+
		"\u009e\7k\2\2\u009e\u009f\7n\2\2\u009f\u00a0\7g\2\2\u00a0\"\3\2\2\2\u00a1"+
		"\u00a2\7=\2\2\u00a2$\3\2\2\2\u00a3\u00a4\7?\2\2\u00a4&\3\2\2\2\u00a5\u00a6"+
		"\7\60\2\2\u00a6(\3\2\2\2\u00a7\u00a8\7.\2\2\u00a8*\3\2\2\2\u00a9\u00aa"+
		"\7v\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7g\2\2\u00ad"+
		",\3\2\2\2\u00ae\u00af\7h\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7n\2\2\u00b1"+
		"\u00b2\7u\2\2\u00b2\u00b3\7g\2\2\u00b3.\3\2\2\2\u00b4\u00b5\7v\2\2\u00b5"+
		"\u00b6\7j\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7u\2\2\u00b8\60\3\2\2\2\u00b9"+
		"\u00ba\7p\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7y\2\2\u00bc\62\3\2\2\2\u00bd"+
		"\u00be\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\64\3\2\2\2\u00c1"+
		"\u00c2\7U\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7k\2\2"+
		"\u00c5\u00c6\7p\2\2\u00c6\u00c7\7i\2\2\u00c7\66\3\2\2\2\u00c8\u00c9\7"+
		"d\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc\7n\2\2\u00cc8"+
		"\3\2\2\2\u00cd\u00ce\7#\2\2\u00ce:\3\2\2\2\u00cf\u00d0\7(\2\2\u00d0\u00d3"+
		"\7(\2\2\u00d1\u00d3\t\2\2\2\u00d2\u00cf\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3"+
		"<\3\2\2\2\u00d4\u00d6\t\3\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2"+
		"\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8>\3\2\2\2\u00d9\u00da\7"+
		"g\2\2\u00da\u00db\7z\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de"+
		"\7p\2\2\u00de\u00df\7f\2\2\u00df\u00e0\7u\2\2\u00e0@\3\2\2\2\u00e1\u00e2"+
		"\7t\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7w\2\2\u00e5"+
		"\u00e6\7t\2\2\u00e6\u00e7\7p\2\2\u00e7B\3\2\2\2\u00e8\u00ec\5G$\2\u00e9"+
		"\u00eb\5E#\2\u00ea\u00e9\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2"+
		"\2\u00ec\u00ed\3\2\2\2\u00edD\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f2"+
		"\5G$\2\u00f0\u00f2\t\3\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2"+
		"F\3\2\2\2\u00f3\u00f8\t\4\2\2\u00f4\u00f8\n\5\2\2\u00f5\u00f6\t\6\2\2"+
		"\u00f6\u00f8\t\7\2\2\u00f7\u00f3\3\2\2\2\u00f7\u00f4\3\2\2\2\u00f7\u00f5"+
		"\3\2\2\2\u00f8H\3\2\2\2\u00f9\u00fb\t\b\2\2\u00fa\u00f9\3\2\2\2\u00fb"+
		"\u00fc\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\3\2"+
		"\2\2\u00fe\u00ff\b%\2\2\u00ffJ\3\2\2\2\u0100\u0101\7\61\2\2\u0101\u0102"+
		"\7,\2\2\u0102\u0106\3\2\2\2\u0103\u0105\13\2\2\2\u0104\u0103\3\2\2\2\u0105"+
		"\u0108\3\2\2\2\u0106\u0107\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0109\3\2"+
		"\2\2\u0108\u0106\3\2\2\2\u0109\u010a\7,\2\2\u010a\u010b\7\61\2\2\u010b"+
		"\u010c\3\2\2\2\u010c\u010d\b&\2\2\u010dL\3\2\2\2\u010e\u010f\7\61\2\2"+
		"\u010f\u0110\7\61\2\2\u0110\u0114\3\2\2\2\u0111\u0113\n\t\2\2\u0112\u0111"+
		"\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115"+
		"\u0117\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118\b\'\2\2\u0118N\3\2\2\2"+
		"\13\2\u00d2\u00d7\u00ec\u00f1\u00f7\u00fc\u0106\u0114\3\2\3\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}