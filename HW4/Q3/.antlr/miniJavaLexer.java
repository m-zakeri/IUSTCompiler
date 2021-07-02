// Generated from c:\Users\Sajjad\Documents\University\Semester 8\Compiler\HW4\HW4\test\miniJavaThreeCode.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class miniJavaLexer extends Lexer {
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
		HEX_LITERAL=38, OCT_LITERAL=39, BINARY_LITERAL=40;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "T__19", "T__20", "T__21", "T__22", "T__23", "T__24", 
			"T__25", "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", "T__32", 
			"T__33", "T__34", "IDENTIFIER", "DECIMAL_LITERAL", "HEX_LITERAL", "OCT_LITERAL", 
			"BINARY_LITERAL", "Digits", "LetterOrDigit", "Letter"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'{'", "'public'", "'static'", "'void'", "'main'", "'('", 
			"'String'", "'['", "']'", "')'", "'}'", "'extends'", "';'", "','", "'return'", 
			"'int'", "'boolean'", "'if'", "'else'", "'while'", "'System.out.println'", 
			"'='", "'&&'", "'<'", "'+'", "'-'", "'*'", "'.'", "'length'", "'true'", 
			"'false'", "'this'", "'new'", "'!'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"IDENTIFIER", "DECIMAL_LITERAL", "HEX_LITERAL", "OCT_LITERAL", "BINARY_LITERAL"
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


	public miniJavaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "miniJavaThreeCode.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*\u0155\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3"+
		"\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3"+
		"\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3"+
		"\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3"+
		"\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3"+
		"\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3"+
		"\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3"+
		"$\3$\3%\3%\7%\u00f9\n%\f%\16%\u00fc\13%\3&\3&\3&\5&\u0101\n&\3&\6&\u0104"+
		"\n&\r&\16&\u0105\3&\5&\u0109\n&\5&\u010b\n&\3&\5&\u010e\n&\3\'\3\'\3\'"+
		"\3\'\7\'\u0114\n\'\f\'\16\'\u0117\13\'\3\'\5\'\u011a\n\'\3\'\5\'\u011d"+
		"\n\'\3(\3(\7(\u0121\n(\f(\16(\u0124\13(\3(\3(\7(\u0128\n(\f(\16(\u012b"+
		"\13(\3(\5(\u012e\n(\3(\5(\u0131\n(\3)\3)\3)\3)\7)\u0137\n)\f)\16)\u013a"+
		"\13)\3)\5)\u013d\n)\3)\5)\u0140\n)\3*\3*\7*\u0144\n*\f*\16*\u0147\13*"+
		"\3*\5*\u014a\n*\3+\3+\5+\u014e\n+\3,\3,\3,\3,\5,\u0154\n,\2\2-\3\3\5\4"+
		"\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22"+
		"#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C"+
		"#E$G%I&K\'M(O)Q*S\2U\2W\2\3\2\22\3\2\63;\4\2NNnn\4\2ZZzz\5\2\62;CHch\6"+
		"\2\62;CHaach\3\2\629\4\2\629aa\4\2DDdd\3\2\62\63\4\2\62\63aa\3\2\62;\4"+
		"\2\62;aa\6\2&&C\\aac|\4\2\2\u0081\ud802\udc01\3\2\ud802\udc01\3\2\udc02"+
		"\ue001\2\u0166\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3"+
		"\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2"+
		"\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3"+
		"\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2"+
		"\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2"+
		"9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3"+
		"\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2"+
		"\2\3Y\3\2\2\2\5_\3\2\2\2\7a\3\2\2\2\th\3\2\2\2\13o\3\2\2\2\rt\3\2\2\2"+
		"\17y\3\2\2\2\21{\3\2\2\2\23\u0082\3\2\2\2\25\u0084\3\2\2\2\27\u0086\3"+
		"\2\2\2\31\u0088\3\2\2\2\33\u008a\3\2\2\2\35\u0092\3\2\2\2\37\u0094\3\2"+
		"\2\2!\u0096\3\2\2\2#\u009d\3\2\2\2%\u00a1\3\2\2\2\'\u00a9\3\2\2\2)\u00ac"+
		"\3\2\2\2+\u00b1\3\2\2\2-\u00b7\3\2\2\2/\u00ca\3\2\2\2\61\u00cc\3\2\2\2"+
		"\63\u00cf\3\2\2\2\65\u00d1\3\2\2\2\67\u00d3\3\2\2\29\u00d5\3\2\2\2;\u00d7"+
		"\3\2\2\2=\u00d9\3\2\2\2?\u00e0\3\2\2\2A\u00e5\3\2\2\2C\u00eb\3\2\2\2E"+
		"\u00f0\3\2\2\2G\u00f4\3\2\2\2I\u00f6\3\2\2\2K\u010a\3\2\2\2M\u010f\3\2"+
		"\2\2O\u011e\3\2\2\2Q\u0132\3\2\2\2S\u0141\3\2\2\2U\u014d\3\2\2\2W\u0153"+
		"\3\2\2\2YZ\7e\2\2Z[\7n\2\2[\\\7c\2\2\\]\7u\2\2]^\7u\2\2^\4\3\2\2\2_`\7"+
		"}\2\2`\6\3\2\2\2ab\7r\2\2bc\7w\2\2cd\7d\2\2de\7n\2\2ef\7k\2\2fg\7e\2\2"+
		"g\b\3\2\2\2hi\7u\2\2ij\7v\2\2jk\7c\2\2kl\7v\2\2lm\7k\2\2mn\7e\2\2n\n\3"+
		"\2\2\2op\7x\2\2pq\7q\2\2qr\7k\2\2rs\7f\2\2s\f\3\2\2\2tu\7o\2\2uv\7c\2"+
		"\2vw\7k\2\2wx\7p\2\2x\16\3\2\2\2yz\7*\2\2z\20\3\2\2\2{|\7U\2\2|}\7v\2"+
		"\2}~\7t\2\2~\177\7k\2\2\177\u0080\7p\2\2\u0080\u0081\7i\2\2\u0081\22\3"+
		"\2\2\2\u0082\u0083\7]\2\2\u0083\24\3\2\2\2\u0084\u0085\7_\2\2\u0085\26"+
		"\3\2\2\2\u0086\u0087\7+\2\2\u0087\30\3\2\2\2\u0088\u0089\7\177\2\2\u0089"+
		"\32\3\2\2\2\u008a\u008b\7g\2\2\u008b\u008c\7z\2\2\u008c\u008d\7v\2\2\u008d"+
		"\u008e\7g\2\2\u008e\u008f\7p\2\2\u008f\u0090\7f\2\2\u0090\u0091\7u\2\2"+
		"\u0091\34\3\2\2\2\u0092\u0093\7=\2\2\u0093\36\3\2\2\2\u0094\u0095\7.\2"+
		"\2\u0095 \3\2\2\2\u0096\u0097\7t\2\2\u0097\u0098\7g\2\2\u0098\u0099\7"+
		"v\2\2\u0099\u009a\7w\2\2\u009a\u009b\7t\2\2\u009b\u009c\7p\2\2\u009c\""+
		"\3\2\2\2\u009d\u009e\7k\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7v\2\2\u00a0"+
		"$\3\2\2\2\u00a1\u00a2\7d\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4\7q\2\2\u00a4"+
		"\u00a5\7n\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7p\2\2"+
		"\u00a8&\3\2\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7h\2\2\u00ab(\3\2\2\2\u00ac"+
		"\u00ad\7g\2\2\u00ad\u00ae\7n\2\2\u00ae\u00af\7u\2\2\u00af\u00b0\7g\2\2"+
		"\u00b0*\3\2\2\2\u00b1\u00b2\7y\2\2\u00b2\u00b3\7j\2\2\u00b3\u00b4\7k\2"+
		"\2\u00b4\u00b5\7n\2\2\u00b5\u00b6\7g\2\2\u00b6,\3\2\2\2\u00b7\u00b8\7"+
		"U\2\2\u00b8\u00b9\7{\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc"+
		"\7g\2\2\u00bc\u00bd\7o\2\2\u00bd\u00be\7\60\2\2\u00be\u00bf\7q\2\2\u00bf"+
		"\u00c0\7w\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7\60\2\2\u00c2\u00c3\7r\2"+
		"\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7"+
		"\7v\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9\7p\2\2\u00c9.\3\2\2\2\u00ca\u00cb"+
		"\7?\2\2\u00cb\60\3\2\2\2\u00cc\u00cd\7(\2\2\u00cd\u00ce\7(\2\2\u00ce\62"+
		"\3\2\2\2\u00cf\u00d0\7>\2\2\u00d0\64\3\2\2\2\u00d1\u00d2\7-\2\2\u00d2"+
		"\66\3\2\2\2\u00d3\u00d4\7/\2\2\u00d48\3\2\2\2\u00d5\u00d6\7,\2\2\u00d6"+
		":\3\2\2\2\u00d7\u00d8\7\60\2\2\u00d8<\3\2\2\2\u00d9\u00da\7n\2\2\u00da"+
		"\u00db\7g\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7i\2\2\u00dd\u00de\7v\2\2"+
		"\u00de\u00df\7j\2\2\u00df>\3\2\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2\7t\2"+
		"\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7g\2\2\u00e4@\3\2\2\2\u00e5\u00e6\7"+
		"h\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea"+
		"\7g\2\2\u00eaB\3\2\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7j\2\2\u00ed\u00ee"+
		"\7k\2\2\u00ee\u00ef\7u\2\2\u00efD\3\2\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2"+
		"\7g\2\2\u00f2\u00f3\7y\2\2\u00f3F\3\2\2\2\u00f4\u00f5\7#\2\2\u00f5H\3"+
		"\2\2\2\u00f6\u00fa\5W,\2\u00f7\u00f9\5U+\2\u00f8\u00f7\3\2\2\2\u00f9\u00fc"+
		"\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fbJ\3\2\2\2\u00fc"+
		"\u00fa\3\2\2\2\u00fd\u010b\7\62\2\2\u00fe\u0108\t\2\2\2\u00ff\u0101\5"+
		"S*\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0109\3\2\2\2\u0102"+
		"\u0104\7a\2\2\u0103\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0103\3\2"+
		"\2\2\u0105\u0106\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0109\5S*\2\u0108\u0100"+
		"\3\2\2\2\u0108\u0103\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u00fd\3\2\2\2\u010a"+
		"\u00fe\3\2\2\2\u010b\u010d\3\2\2\2\u010c\u010e\t\3\2\2\u010d\u010c\3\2"+
		"\2\2\u010d\u010e\3\2\2\2\u010eL\3\2\2\2\u010f\u0110\7\62\2\2\u0110\u0111"+
		"\t\4\2\2\u0111\u0119\t\5\2\2\u0112\u0114\t\6\2\2\u0113\u0112\3\2\2\2\u0114"+
		"\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0118\3\2"+
		"\2\2\u0117\u0115\3\2\2\2\u0118\u011a\t\5\2\2\u0119\u0115\3\2\2\2\u0119"+
		"\u011a\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u011d\t\3\2\2\u011c\u011b\3\2"+
		"\2\2\u011c\u011d\3\2\2\2\u011dN\3\2\2\2\u011e\u0122\7\62\2\2\u011f\u0121"+
		"\7a\2\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0122"+
		"\u0123\3\2\2\2\u0123\u0125\3\2\2\2\u0124\u0122\3\2\2\2\u0125\u012d\t\7"+
		"\2\2\u0126\u0128\t\b\2\2\u0127\u0126\3\2\2\2\u0128\u012b\3\2\2\2\u0129"+
		"\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012c\3\2\2\2\u012b\u0129\3\2"+
		"\2\2\u012c\u012e\t\7\2\2\u012d\u0129\3\2\2\2\u012d\u012e\3\2\2\2\u012e"+
		"\u0130\3\2\2\2\u012f\u0131\t\3\2\2\u0130\u012f\3\2\2\2\u0130\u0131\3\2"+
		"\2\2\u0131P\3\2\2\2\u0132\u0133\7\62\2\2\u0133\u0134\t\t\2\2\u0134\u013c"+
		"\t\n\2\2\u0135\u0137\t\13\2\2\u0136\u0135\3\2\2\2\u0137\u013a\3\2\2\2"+
		"\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\3\2\2\2\u013a\u0138"+
		"\3\2\2\2\u013b\u013d\t\n\2\2\u013c\u0138\3\2\2\2\u013c\u013d\3\2\2\2\u013d"+
		"\u013f\3\2\2\2\u013e\u0140\t\3\2\2\u013f\u013e\3\2\2\2\u013f\u0140\3\2"+
		"\2\2\u0140R\3\2\2\2\u0141\u0149\t\f\2\2\u0142\u0144\t\r\2\2\u0143\u0142"+
		"\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146"+
		"\u0148\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u014a\t\f\2\2\u0149\u0145\3\2"+
		"\2\2\u0149\u014a\3\2\2\2\u014aT\3\2\2\2\u014b\u014e\5W,\2\u014c\u014e"+
		"\t\f\2\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2\u014eV\3\2\2\2\u014f"+
		"\u0154\t\16\2\2\u0150\u0154\n\17\2\2\u0151\u0152\t\20\2\2\u0152\u0154"+
		"\t\21\2\2\u0153\u014f\3\2\2\2\u0153\u0150\3\2\2\2\u0153\u0151\3\2\2\2"+
		"\u0154X\3\2\2\2\27\2\u00fa\u0100\u0105\u0108\u010a\u010d\u0115\u0119\u011c"+
		"\u0122\u0129\u012d\u0130\u0138\u013c\u013f\u0145\u0149\u014d\u0153\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}