// Generated from /home/loop/Desktop/Ass/Compiler/HW4/ast.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link astParser}.
 */
public interface astListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link astParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(astParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(astParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#mainClass}.
	 * @param ctx the parse tree
	 */
	void enterMainClass(astParser.MainClassContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#mainClass}.
	 * @param ctx the parse tree
	 */
	void exitMainClass(astParser.MainClassContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#mainClassDecl}.
	 * @param ctx the parse tree
	 */
	void enterMainClassDecl(astParser.MainClassDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#mainClassDecl}.
	 * @param ctx the parse tree
	 */
	void exitMainClassDecl(astParser.MainClassDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#mainMethodDecl}.
	 * @param ctx the parse tree
	 */
	void enterMainMethodDecl(astParser.MainMethodDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#mainMethodDecl}.
	 * @param ctx the parse tree
	 */
	void exitMainMethodDecl(astParser.MainMethodDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#mainMethodBody}.
	 * @param ctx the parse tree
	 */
	void enterMainMethodBody(astParser.MainMethodBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#mainMethodBody}.
	 * @param ctx the parse tree
	 */
	void exitMainMethodBody(astParser.MainMethodBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void enterClassDecl(astParser.ClassDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void exitClassDecl(astParser.ClassDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(astParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(astParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#methodDecl}.
	 * @param ctx the parse tree
	 */
	void enterMethodDecl(astParser.MethodDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#methodDecl}.
	 * @param ctx the parse tree
	 */
	void exitMethodDecl(astParser.MethodDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#methodBody}.
	 * @param ctx the parse tree
	 */
	void enterMethodBody(astParser.MethodBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#methodBody}.
	 * @param ctx the parse tree
	 */
	void exitMethodBody(astParser.MethodBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(astParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(astParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(astParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(astParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(astParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(astParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#binOp}.
	 * @param ctx the parse tree
	 */
	void enterBinOp(astParser.BinOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#binOp}.
	 * @param ctx the parse tree
	 */
	void exitBinOp(astParser.BinOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link astParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(astParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link astParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(astParser.IdentifierContext ctx);
}