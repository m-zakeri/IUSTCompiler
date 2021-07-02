// Generated from /home/loop/Desktop/Ass/Compiler/HW4/ast.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link astParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface astVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link astParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(astParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#mainClass}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMainClass(astParser.MainClassContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#mainClassDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMainClassDecl(astParser.MainClassDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#mainMethodDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMainMethodDecl(astParser.MainMethodDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#mainMethodBody}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMainMethodBody(astParser.MainMethodBodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#classDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClassDecl(astParser.ClassDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#varDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarDecl(astParser.VarDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#methodDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethodDecl(astParser.MethodDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#methodBody}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethodBody(astParser.MethodBodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(astParser.TypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(astParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp(astParser.ExpContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#binOp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinOp(astParser.BinOpContext ctx);
	/**
	 * Visit a parse tree produced by {@link astParser#identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdentifier(astParser.IdentifierContext ctx);
}