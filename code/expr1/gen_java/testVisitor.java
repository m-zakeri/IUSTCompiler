// Generated from D:/AnacondaProjects/iust_start/grammars\test.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link testParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface testVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link testParser#start}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStart(testParser.StartContext ctx);
	/**
	 * Visit a parse tree produced by the {@code rule_minus}
	 * labeled alternative in {@link testParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRule_minus(testParser.Rule_minusContext ctx);
	/**
	 * Visit a parse tree produced by the {@code rule_plus}
	 * labeled alternative in {@link testParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRule_plus(testParser.Rule_plusContext ctx);
	/**
	 * Visit a parse tree produced by the {@code rule3}
	 * labeled alternative in {@link testParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRule3(testParser.Rule3Context ctx);
	/**
	 * Visit a parse tree produced by {@link testParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm(testParser.TermContext ctx);
	/**
	 * Visit a parse tree produced by {@link testParser#fact}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFact(testParser.FactContext ctx);
}