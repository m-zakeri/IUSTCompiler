// Generated from C:/git/compiler/HW4/Q2\MiniJava.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MiniJavaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, BOOLEAN=2, CLASS=3, ELSE=4, EXTENDS=5, FALSE=6, IF=7, INT=8, LENGTH=9, 
		MAIN=10, NEW=11, PUBLIC=12, RETURN=13, STATIC=14, STRING=15, THIS=16, 
		TRUE=17, VOID=18, WHILE=19, ASSIGN=20, GT=21, LT=22, GE=23, LE=24, PLUS=25, 
		MINUS=26, TIMES=27, BANG=28, AND=29, OR=30, L_PAREN=31, R_PAREN=32, L_BRACK=33, 
		R_BRACK=34, L_BRACE=35, R_BRACE=36, COMMA=37, DOT=38, SEMI=39, ID=40, 
		INT_VAL=41, WS=42, COMMENT=43, LINE_COMMENT=44;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "BOOLEAN", "CLASS", "ELSE", "EXTENDS", "FALSE", "IF", "INT", 
			"LENGTH", "MAIN", "NEW", "PUBLIC", "RETURN", "STATIC", "STRING", "THIS", 
			"TRUE", "VOID", "WHILE", "ASSIGN", "GT", "LT", "GE", "LE", "PLUS", "MINUS", 
			"TIMES", "BANG", "AND", "OR", "L_PAREN", "R_PAREN", "L_BRACK", "R_BRACK", 
			"L_BRACE", "R_BRACE", "COMMA", "DOT", "SEMI", "ID", "INT_VAL", "LETTER", 
			"DIGIT", "WS", "COMMENT", "LINE_COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'System.out.println'", "'boolean'", "'class'", "'else'", "'extends'", 
			"'false'", "'if'", "'int'", "'length'", "'main'", "'new'", "'public'", 
			"'return'", "'static'", "'String'", "'this'", "'true'", "'void'", "'while'", 
			"'='", "'>'", "'<'", "'>='", "'<='", "'+'", "'-'", "'*'", "'!'", "'&&'", 
			"'||'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'.'", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "BOOLEAN", "CLASS", "ELSE", "EXTENDS", "FALSE", "IF", "INT", 
			"LENGTH", "MAIN", "NEW", "PUBLIC", "RETURN", "STATIC", "STRING", "THIS", 
			"TRUE", "VOID", "WHILE", "ASSIGN", "GT", "LT", "GE", "LE", "PLUS", "MINUS", 
			"TIMES", "BANG", "AND", "OR", "L_PAREN", "R_PAREN", "L_BRACK", "R_BRACK", 
			"L_BRACE", "R_BRACE", "COMMA", "DOT", "SEMI", "ID", "INT_VAL", "WS", 
			"COMMENT", "LINE_COMMENT"
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


	public MiniJavaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MiniJava.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2.\u013d\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22"+
		"\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32"+
		"\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3"+
		" \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\7)\u010b"+
		"\n)\f)\16)\u010e\13)\3*\3*\3*\7*\u0113\n*\f*\16*\u0116\13*\5*\u0118\n"+
		"*\3+\3+\3,\3,\3-\6-\u011f\n-\r-\16-\u0120\3-\3-\3.\3.\3.\3.\7.\u0129\n"+
		".\f.\16.\u012c\13.\3.\3.\3.\3.\3.\3/\3/\3/\3/\7/\u0137\n/\f/\16/\u013a"+
		"\13/\3/\3/\3\u012a\2\60\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f"+
		"\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63"+
		"\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U\2W\2Y,[-].\3\2\7\3"+
		"\2\63;\5\2C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\4\2\f\f\17\17\2\u0141\2\3"+
		"\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2"+
		"\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31"+
		"\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2"+
		"\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2"+
		"\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2"+
		"\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2"+
		"I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2Y\3"+
		"\2\2\2\2[\3\2\2\2\2]\3\2\2\2\3_\3\2\2\2\5r\3\2\2\2\7z\3\2\2\2\t\u0080"+
		"\3\2\2\2\13\u0085\3\2\2\2\r\u008d\3\2\2\2\17\u0093\3\2\2\2\21\u0096\3"+
		"\2\2\2\23\u009a\3\2\2\2\25\u00a1\3\2\2\2\27\u00a6\3\2\2\2\31\u00aa\3\2"+
		"\2\2\33\u00b1\3\2\2\2\35\u00b8\3\2\2\2\37\u00bf\3\2\2\2!\u00c6\3\2\2\2"+
		"#\u00cb\3\2\2\2%\u00d0\3\2\2\2\'\u00d5\3\2\2\2)\u00db\3\2\2\2+\u00dd\3"+
		"\2\2\2-\u00df\3\2\2\2/\u00e1\3\2\2\2\61\u00e4\3\2\2\2\63\u00e7\3\2\2\2"+
		"\65\u00e9\3\2\2\2\67\u00eb\3\2\2\29\u00ed\3\2\2\2;\u00ef\3\2\2\2=\u00f2"+
		"\3\2\2\2?\u00f5\3\2\2\2A\u00f7\3\2\2\2C\u00f9\3\2\2\2E\u00fb\3\2\2\2G"+
		"\u00fd\3\2\2\2I\u00ff\3\2\2\2K\u0101\3\2\2\2M\u0103\3\2\2\2O\u0105\3\2"+
		"\2\2Q\u0107\3\2\2\2S\u0117\3\2\2\2U\u0119\3\2\2\2W\u011b\3\2\2\2Y\u011e"+
		"\3\2\2\2[\u0124\3\2\2\2]\u0132\3\2\2\2_`\7U\2\2`a\7{\2\2ab\7u\2\2bc\7"+
		"v\2\2cd\7g\2\2de\7o\2\2ef\7\60\2\2fg\7q\2\2gh\7w\2\2hi\7v\2\2ij\7\60\2"+
		"\2jk\7r\2\2kl\7t\2\2lm\7k\2\2mn\7p\2\2no\7v\2\2op\7n\2\2pq\7p\2\2q\4\3"+
		"\2\2\2rs\7d\2\2st\7q\2\2tu\7q\2\2uv\7n\2\2vw\7g\2\2wx\7c\2\2xy\7p\2\2"+
		"y\6\3\2\2\2z{\7e\2\2{|\7n\2\2|}\7c\2\2}~\7u\2\2~\177\7u\2\2\177\b\3\2"+
		"\2\2\u0080\u0081\7g\2\2\u0081\u0082\7n\2\2\u0082\u0083\7u\2\2\u0083\u0084"+
		"\7g\2\2\u0084\n\3\2\2\2\u0085\u0086\7g\2\2\u0086\u0087\7z\2\2\u0087\u0088"+
		"\7v\2\2\u0088\u0089\7g\2\2\u0089\u008a\7p\2\2\u008a\u008b\7f\2\2\u008b"+
		"\u008c\7u\2\2\u008c\f\3\2\2\2\u008d\u008e\7h\2\2\u008e\u008f\7c\2\2\u008f"+
		"\u0090\7n\2\2\u0090\u0091\7u\2\2\u0091\u0092\7g\2\2\u0092\16\3\2\2\2\u0093"+
		"\u0094\7k\2\2\u0094\u0095\7h\2\2\u0095\20\3\2\2\2\u0096\u0097\7k\2\2\u0097"+
		"\u0098\7p\2\2\u0098\u0099\7v\2\2\u0099\22\3\2\2\2\u009a\u009b\7n\2\2\u009b"+
		"\u009c\7g\2\2\u009c\u009d\7p\2\2\u009d\u009e\7i\2\2\u009e\u009f\7v\2\2"+
		"\u009f\u00a0\7j\2\2\u00a0\24\3\2\2\2\u00a1\u00a2\7o\2\2\u00a2\u00a3\7"+
		"c\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7p\2\2\u00a5\26\3\2\2\2\u00a6\u00a7"+
		"\7p\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7y\2\2\u00a9\30\3\2\2\2\u00aa\u00ab"+
		"\7r\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7d\2\2\u00ad\u00ae\7n\2\2\u00ae"+
		"\u00af\7k\2\2\u00af\u00b0\7e\2\2\u00b0\32\3\2\2\2\u00b1\u00b2\7t\2\2\u00b2"+
		"\u00b3\7g\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7w\2\2\u00b5\u00b6\7t\2\2"+
		"\u00b6\u00b7\7p\2\2\u00b7\34\3\2\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba\7"+
		"v\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be"+
		"\7e\2\2\u00be\36\3\2\2\2\u00bf\u00c0\7U\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2"+
		"\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7i\2\2\u00c5"+
		" \3\2\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7j\2\2\u00c8\u00c9\7k\2\2\u00c9"+
		"\u00ca\7u\2\2\u00ca\"\3\2\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7t\2\2\u00cd"+
		"\u00ce\7w\2\2\u00ce\u00cf\7g\2\2\u00cf$\3\2\2\2\u00d0\u00d1\7x\2\2\u00d1"+
		"\u00d2\7q\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7f\2\2\u00d4&\3\2\2\2\u00d5"+
		"\u00d6\7y\2\2\u00d6\u00d7\7j\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9\7n\2\2"+
		"\u00d9\u00da\7g\2\2\u00da(\3\2\2\2\u00db\u00dc\7?\2\2\u00dc*\3\2\2\2\u00dd"+
		"\u00de\7@\2\2\u00de,\3\2\2\2\u00df\u00e0\7>\2\2\u00e0.\3\2\2\2\u00e1\u00e2"+
		"\7@\2\2\u00e2\u00e3\7?\2\2\u00e3\60\3\2\2\2\u00e4\u00e5\7>\2\2\u00e5\u00e6"+
		"\7?\2\2\u00e6\62\3\2\2\2\u00e7\u00e8\7-\2\2\u00e8\64\3\2\2\2\u00e9\u00ea"+
		"\7/\2\2\u00ea\66\3\2\2\2\u00eb\u00ec\7,\2\2\u00ec8\3\2\2\2\u00ed\u00ee"+
		"\7#\2\2\u00ee:\3\2\2\2\u00ef\u00f0\7(\2\2\u00f0\u00f1\7(\2\2\u00f1<\3"+
		"\2\2\2\u00f2\u00f3\7~\2\2\u00f3\u00f4\7~\2\2\u00f4>\3\2\2\2\u00f5\u00f6"+
		"\7*\2\2\u00f6@\3\2\2\2\u00f7\u00f8\7+\2\2\u00f8B\3\2\2\2\u00f9\u00fa\7"+
		"]\2\2\u00faD\3\2\2\2\u00fb\u00fc\7_\2\2\u00fcF\3\2\2\2\u00fd\u00fe\7}"+
		"\2\2\u00feH\3\2\2\2\u00ff\u0100\7\177\2\2\u0100J\3\2\2\2\u0101\u0102\7"+
		".\2\2\u0102L\3\2\2\2\u0103\u0104\7\60\2\2\u0104N\3\2\2\2\u0105\u0106\7"+
		"=\2\2\u0106P\3\2\2\2\u0107\u010c\5U+\2\u0108\u010b\5U+\2\u0109\u010b\5"+
		"W,\2\u010a\u0108\3\2\2\2\u010a\u0109\3\2\2\2\u010b\u010e\3\2\2\2\u010c"+
		"\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010dR\3\2\2\2\u010e\u010c\3\2\2\2"+
		"\u010f\u0118\7\62\2\2\u0110\u0114\t\2\2\2\u0111\u0113\5W,\2\u0112\u0111"+
		"\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115"+
		"\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u010f\3\2\2\2\u0117\u0110\3\2"+
		"\2\2\u0118T\3\2\2\2\u0119\u011a\t\3\2\2\u011aV\3\2\2\2\u011b\u011c\t\4"+
		"\2\2\u011cX\3\2\2\2\u011d\u011f\t\5\2\2\u011e\u011d\3\2\2\2\u011f\u0120"+
		"\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\3\2\2\2\u0122"+
		"\u0123\b-\2\2\u0123Z\3\2\2\2\u0124\u0125\7\61\2\2\u0125\u0126\7,\2\2\u0126"+
		"\u012a\3\2\2\2\u0127\u0129\13\2\2\2\u0128\u0127\3\2\2\2\u0129\u012c\3"+
		"\2\2\2\u012a\u012b\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012d\3\2\2\2\u012c"+
		"\u012a\3\2\2\2\u012d\u012e\7,\2\2\u012e\u012f\7\61\2\2\u012f\u0130\3\2"+
		"\2\2\u0130\u0131\b.\2\2\u0131\\\3\2\2\2\u0132\u0133\7\61\2\2\u0133\u0134"+
		"\7\61\2\2\u0134\u0138\3\2\2\2\u0135\u0137\n\6\2\2\u0136\u0135\3\2\2\2"+
		"\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b"+
		"\3\2\2\2\u013a\u0138\3\2\2\2\u013b\u013c\b/\2\2\u013c^\3\2\2\2\n\2\u010a"+
		"\u010c\u0114\u0117\u0120\u012a\u0138\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}