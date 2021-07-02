// Generated from C:/Users/asus/Desktop\q2.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class q2Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MainClass=1, ClassDeclaration=2, VarDeclaration=3, Type=4, MethodDeclaration=5, 
		Statement=6, Expression=7, Expression_prim=8, Identifier=9, COMMENT=10, 
		LINE_COMMENT=11, IDENTIFIER=12, INTEGER_LITERAL=13;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MainClass", "ClassDeclaration", "VarDeclaration", "Type", "MethodDeclaration", 
			"Statement", "Expression", "Expression_prim", "Identifier", "COMMENT", 
			"LINE_COMMENT", "IDENTIFIER", "INTEGER_LITERAL"
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


	public q2Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "q2.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17\u0185\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\5\3_\n\3\3\3\3\3\7\3c\n\3\f\3\16\3f\13\3\3\3\7\3i\n\3\f"+
		"\3\16\3l\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0085\n\5\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u0097\n\6\f\6\16\6\u009a"+
		"\13\6\5\6\u009c\n\6\3\6\3\6\3\6\7\6\u00a1\n\6\f\6\16\6\u00a4\13\6\3\6"+
		"\7\6\u00a7\n\6\f\6\16\6\u00aa\13\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\7\3\7\7\7\u00b8\n\7\f\7\16\7\u00bb\13\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0102\n\7\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\5\b\u013d\n\b\3\t\3\t\3\t\5\t\u0142\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u0156\n\t\f\t\16\t"+
		"\u0159\13\t\5\t\u015b\n\t\3\t\3\t\3\t\5\t\u0160\n\t\3\n\3\n\3\13\3\13"+
		"\3\13\3\13\7\13\u0168\n\13\f\13\16\13\u016b\13\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\f\3\f\3\f\3\f\7\f\u0176\n\f\f\f\16\f\u0179\13\f\3\f\3\f\3\r\3"+
		"\r\3\r\3\16\7\16\u0181\n\16\f\16\16\16\u0184\13\16\3\u0169\2\17\3\3\5"+
		"\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3\2\7\5\2,-"+
		"//>>\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\2\u01a7\2\3\3\2\2"+
		"\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3"+
		"\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2"+
		"\2\2\33\3\2\2\2\3\35\3\2\2\2\5N\3\2\2\2\7o\3\2\2\2\t\u0084\3\2\2\2\13"+
		"\u0086\3\2\2\2\r\u0101\3\2\2\2\17\u013c\3\2\2\2\21\u015f\3\2\2\2\23\u0161"+
		"\3\2\2\2\25\u0163\3\2\2\2\27\u0171\3\2\2\2\31\u017c\3\2\2\2\33\u0182\3"+
		"\2\2\2\35\36\7e\2\2\36\37\7n\2\2\37 \7c\2\2 !\7u\2\2!\"\7u\2\2\"#\3\2"+
		"\2\2#$\5\23\n\2$%\7}\2\2%&\7r\2\2&\'\7w\2\2\'(\7d\2\2()\7n\2\2)*\7k\2"+
		"\2*+\7e\2\2+,\3\2\2\2,-\7u\2\2-.\7v\2\2./\7c\2\2/\60\7v\2\2\60\61\7k\2"+
		"\2\61\62\7e\2\2\62\63\3\2\2\2\63\64\7x\2\2\64\65\7q\2\2\65\66\7k\2\2\66"+
		"\67\7f\2\2\678\3\2\2\289\7o\2\29:\7c\2\2:;\7k\2\2;<\7p\2\2<=\3\2\2\2="+
		">\7*\2\2>?\7U\2\2?@\7v\2\2@A\7t\2\2AB\7k\2\2BC\7p\2\2CD\7i\2\2DE\3\2\2"+
		"\2EF\7]\2\2FG\7_\2\2GH\5\23\n\2HI\7+\2\2IJ\7}\2\2JK\5\r\7\2KL\7\177\2"+
		"\2LM\7\177\2\2M\4\3\2\2\2NO\7e\2\2OP\7n\2\2PQ\7c\2\2QR\7u\2\2RS\7u\2\2"+
		"ST\3\2\2\2T^\5\23\n\2UV\7g\2\2VW\7z\2\2WX\7v\2\2XY\7g\2\2YZ\7p\2\2Z[\7"+
		"f\2\2[\\\7u\2\2\\]\3\2\2\2]_\5\23\n\2^U\3\2\2\2^_\3\2\2\2_`\3\2\2\2`d"+
		"\7}\2\2ac\5\7\4\2ba\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2ej\3\2\2\2fd"+
		"\3\2\2\2gi\5\13\6\2hg\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2km\3\2\2\2"+
		"lj\3\2\2\2mn\7\177\2\2n\6\3\2\2\2op\5\t\5\2pq\5\23\n\2qr\7=\2\2r\b\3\2"+
		"\2\2st\7k\2\2tu\7p\2\2uv\7v\2\2vw\3\2\2\2wx\7]\2\2x\u0085\7_\2\2yz\7d"+
		"\2\2z{\7q\2\2{|\7q\2\2|}\7n\2\2}~\7g\2\2~\177\7c\2\2\177\u0085\7p\2\2"+
		"\u0080\u0081\7k\2\2\u0081\u0082\7p\2\2\u0082\u0085\7v\2\2\u0083\u0085"+
		"\5\23\n\2\u0084s\3\2\2\2\u0084y\3\2\2\2\u0084\u0080\3\2\2\2\u0084\u0083"+
		"\3\2\2\2\u0085\n\3\2\2\2\u0086\u0087\7r\2\2\u0087\u0088\7w\2\2\u0088\u0089"+
		"\7d\2\2\u0089\u008a\7n\2\2\u008a\u008b\7k\2\2\u008b\u008c\7e\2\2\u008c"+
		"\u008d\3\2\2\2\u008d\u008e\5\t\5\2\u008e\u008f\5\23\n\2\u008f\u009b\7"+
		"*\2\2\u0090\u0091\5\t\5\2\u0091\u0098\5\23\n\2\u0092\u0093\7.\2\2\u0093"+
		"\u0094\5\t\5\2\u0094\u0095\5\23\n\2\u0095\u0097\3\2\2\2\u0096\u0092\3"+
		"\2\2\2\u0097\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099"+
		"\u009c\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u0090\3\2\2\2\u009b\u009c\3\2"+
		"\2\2\u009c\u009d\3\2\2\2\u009d\u009e\7+\2\2\u009e\u00a2\7}\2\2\u009f\u00a1"+
		"\5\7\4\2\u00a0\u009f\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2"+
		"\u00a3\3\2\2\2\u00a3\u00a8\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a7\5\r"+
		"\7\2\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8"+
		"\u00a9\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ac\7t"+
		"\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7w\2\2\u00af\u00b0"+
		"\7t\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\5\17\b\2\u00b3"+
		"\u00b4\7\177\2\2\u00b4\f\3\2\2\2\u00b5\u00b9\7}\2\2\u00b6\u00b8\5\r\7"+
		"\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba"+
		"\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u0102\7\177\2\2"+
		"\u00bd\u00be\7y\2\2\u00be\u00bf\7j\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1"+
		"\7n\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\7*\2\2\u00c4"+
		"\u00c5\5\17\b\2\u00c5\u00c6\7+\2\2\u00c6\u00c7\7}\2\2\u00c7\u00c8\5\r"+
		"\7\2\u00c8\u00c9\7\177\2\2\u00c9\u0102\3\2\2\2\u00ca\u00cb\7k\2\2\u00cb"+
		"\u00cc\7h\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\7*\2\2\u00ce\u00cf\5\17"+
		"\b\2\u00cf\u00d0\7+\2\2\u00d0\u00d1\7}\2\2\u00d1\u00d2\5\r\7\2\u00d2\u00d3"+
		"\7\177\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6\7u\2\2\u00d6"+
		"\u00d7\7g\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\7}\2\2\u00d9\u00da\5\r\7"+
		"\2\u00da\u00db\7\177\2\2\u00db\u0102\3\2\2\2\u00dc\u00dd\7U\2\2\u00dd"+
		"\u00de\7{\2\2\u00de\u00df\7u\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1\7g\2\2"+
		"\u00e1\u00e2\7o\2\2\u00e2\u00e3\7\60\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5"+
		"\7w\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7\60\2\2\u00e7\u00e8\7r\2\2\u00e8"+
		"\u00e9\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7v\2\2"+
		"\u00ec\u00ed\7n\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0"+
		"\7*\2\2\u00f0\u00f1\5\17\b\2\u00f1\u00f2\7+\2\2\u00f2\u00f3\7=\2\2\u00f3"+
		"\u0102\3\2\2\2\u00f4\u00f5\5\23\n\2\u00f5\u00f6\7?\2\2\u00f6\u00f7\5\17"+
		"\b\2\u00f7\u00f8\7=\2\2\u00f8\u0102\3\2\2\2\u00f9\u00fa\5\23\n\2\u00fa"+
		"\u00fb\7]\2\2\u00fb\u00fc\5\17\b\2\u00fc\u00fd\7_\2\2\u00fd\u00fe\7?\2"+
		"\2\u00fe\u00ff\5\17\b\2\u00ff\u0100\7=\2\2\u0100\u0102\3\2\2\2\u0101\u00b5"+
		"\3\2\2\2\u0101\u00bd\3\2\2\2\u0101\u00ca\3\2\2\2\u0101\u00dc\3\2\2\2\u0101"+
		"\u00f4\3\2\2\2\u0101\u00f9\3\2\2\2\u0102\16\3\2\2\2\u0103\u013d\3\2\2"+
		"\2\u0104\u0105\5\33\16\2\u0105\u0106\5\21\t\2\u0106\u013d\3\2\2\2\u0107"+
		"\u0108\7v\2\2\u0108\u0109\7t\2\2\u0109\u010a\7w\2\2\u010a\u010b\7g\2\2"+
		"\u010b\u010c\3\2\2\2\u010c\u013d\5\21\t\2\u010d\u010e\7h\2\2\u010e\u010f"+
		"\7c\2\2\u010f\u0110\7n\2\2\u0110\u0111\7u\2\2\u0111\u0112\7g\2\2\u0112"+
		"\u0113\3\2\2\2\u0113\u013d\5\21\t\2\u0114\u0115\5\23\n\2\u0115\u0116\5"+
		"\21\t\2\u0116\u013d\3\2\2\2\u0117\u0118\7v\2\2\u0118\u0119\7j\2\2\u0119"+
		"\u011a\7k\2\2\u011a\u011b\7u\2\2\u011b\u011c\3\2\2\2\u011c\u013d\5\21"+
		"\t\2\u011d\u011e\7p\2\2\u011e\u011f\7g\2\2\u011f\u0120\7y\2\2\u0120\u0121"+
		"\3\2\2\2\u0121\u0122\7k\2\2\u0122\u0123\7p\2\2\u0123\u0124\7v\2\2\u0124"+
		"\u0125\3\2\2\2\u0125\u0126\7]\2\2\u0126\u0127\5\17\b\2\u0127\u0128\7_"+
		"\2\2\u0128\u0129\5\21\t\2\u0129\u013d\3\2\2\2\u012a\u012b\7p\2\2\u012b"+
		"\u012c\7g\2\2\u012c\u012d\7y\2\2\u012d\u012e\3\2\2\2\u012e\u012f\5\23"+
		"\n\2\u012f\u0130\7*\2\2\u0130\u0131\7+\2\2\u0131\u0132\5\21\t\2\u0132"+
		"\u013d\3\2\2\2\u0133\u0134\7#\2\2\u0134\u0135\5\17\b\2\u0135\u0136\5\21"+
		"\t\2\u0136\u013d\3\2\2\2\u0137\u0138\7*\2\2\u0138\u0139\5\17\b\2\u0139"+
		"\u013a\7+\2\2\u013a\u013b\5\21\t\2\u013b\u013d\3\2\2\2\u013c\u0103\3\2"+
		"\2\2\u013c\u0104\3\2\2\2\u013c\u0107\3\2\2\2\u013c\u010d\3\2\2\2\u013c"+
		"\u0114\3\2\2\2\u013c\u0117\3\2\2\2\u013c\u011d\3\2\2\2\u013c\u012a\3\2"+
		"\2\2\u013c\u0133\3\2\2\2\u013c\u0137\3\2\2\2\u013d\20\3\2\2\2\u013e\u013f"+
		"\7(\2\2\u013f\u0142\7(\2\2\u0140\u0142\t\2\2\2\u0141\u013e\3\2\2\2\u0141"+
		"\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0160\5\17\b\2\u0144\u0145\7"+
		"]\2\2\u0145\u0146\5\17\b\2\u0146\u0147\7_\2\2\u0147\u0160\3\2\2\2\u0148"+
		"\u0149\7\60\2\2\u0149\u014a\7n\2\2\u014a\u014b\7g\2\2\u014b\u014c\7p\2"+
		"\2\u014c\u014d\7i\2\2\u014d\u014e\7v\2\2\u014e\u0160\7j\2\2\u014f\u0150"+
		"\7\60\2\2\u0150\u0151\5\23\n\2\u0151\u015a\7*\2\2\u0152\u0157\5\17\b\2"+
		"\u0153\u0154\7.\2\2\u0154\u0156\5\17\b\2\u0155\u0153\3\2\2\2\u0156\u0159"+
		"\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u015b\3\2\2\2\u0159"+
		"\u0157\3\2\2\2\u015a\u0152\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015c\3\2"+
		"\2\2\u015c\u015d\7+\2\2\u015d\u0160\3\2\2\2\u015e\u0160\3\2\2\2\u015f"+
		"\u0141\3\2\2\2\u015f\u0144\3\2\2\2\u015f\u0148\3\2\2\2\u015f\u014f\3\2"+
		"\2\2\u015f\u015e\3\2\2\2\u0160\22\3\2\2\2\u0161\u0162\5\31\r\2\u0162\24"+
		"\3\2\2\2\u0163\u0164\7\61\2\2\u0164\u0165\7,\2\2\u0165\u0169\3\2\2\2\u0166"+
		"\u0168\13\2\2\2\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u016a\3"+
		"\2\2\2\u0169\u0167\3\2\2\2\u016a\u016c\3\2\2\2\u016b\u0169\3\2\2\2\u016c"+
		"\u016d\7,\2\2\u016d\u016e\7\61\2\2\u016e\u016f\3\2\2\2\u016f\u0170\b\13"+
		"\2\2\u0170\26\3\2\2\2\u0171\u0172\7\61\2\2\u0172\u0173\7\61\2\2\u0173"+
		"\u0177\3\2\2\2\u0174\u0176\n\3\2\2\u0175\u0174\3\2\2\2\u0176\u0179\3\2"+
		"\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017a\3\2\2\2\u0179"+
		"\u0177\3\2\2\2\u017a\u017b\b\f\2\2\u017b\30\3\2\2\2\u017c\u017d\t\4\2"+
		"\2\u017d\u017e\t\5\2\2\u017e\32\3\2\2\2\u017f\u0181\t\6\2\2\u0180\u017f"+
		"\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183"+
		"\34\3\2\2\2\u0184\u0182\3\2\2\2\25\2^dj\u0084\u0098\u009b\u00a2\u00a8"+
		"\u00b9\u0101\u013c\u0141\u0157\u015a\u015f\u0169\u0177\u0182\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}