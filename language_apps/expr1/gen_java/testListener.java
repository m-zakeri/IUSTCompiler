// Generated from D:/AnacondaProjects/iust_start/grammars\test.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link testParser}.
 */
public interface testListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link testParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(testParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link testParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(testParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by the {@code rule_minus}
	 * labeled alternative in {@link testParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterRule_minus(testParser.Rule_minusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code rule_minus}
	 * labeled alternative in {@link testParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitRule_minus(testParser.Rule_minusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code rule_plus}
	 * labeled alternative in {@link testParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterRule_plus(testParser.Rule_plusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code rule_plus}
	 * labeled alternative in {@link testParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitRule_plus(testParser.Rule_plusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code rule3}
	 * labeled alternative in {@link testParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterRule3(testParser.Rule3Context ctx);
	/**
	 * Exit a parse tree produced by the {@code rule3}
	 * labeled alternative in {@link testParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitRule3(testParser.Rule3Context ctx);
	/**
	 * Enter a parse tree produced by {@link testParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(testParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link testParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(testParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link testParser#fact}.
	 * @param ctx the parse tree
	 */
	void enterFact(testParser.FactContext ctx);
	/**
	 * Exit a parse tree produced by {@link testParser#fact}.
	 * @param ctx the parse tree
	 */
	void exitFact(testParser.FactContext ctx);
}