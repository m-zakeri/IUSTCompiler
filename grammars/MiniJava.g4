/*
Program	::=	MainClass ( ClassDeclaration )* <EOF>
MainClass	::=	"class" Identifier "{" "public" "static" "void" "main" "(" "String" "[" "]" Identifier ")" "{" Statement "}" "}"
ClassDeclaration	::=	"class" Identifier ( "extends" Identifier )? "{" ( VarDeclaration )* ( MethodDeclaration )* "}"
VarDeclaration	::=	Type Identifier ";"
MethodDeclaration	::=	"public" Type Identifier "(" ( Type Identifier ( "," Type Identifier )* )? ")" "{" ( VarDeclaration )* ( Statement )* "return" Expression ";" "}"
Type	::=	"int" "[" "]"
|	"boolean"
|	"int"
|	Identifier
Statement	::=	"{" ( Statement )* "}"
|	"if" "(" Expression ")" Statement "else" Statement
|	"while" "(" Expression ")" Statement
|	"System.out.println" "(" Expression ")" ";"
|	Identifier "=" Expression ";"
|	Identifier "[" Expression "]" "=" Expression ";"
Expression	::=	Expression ( "&&" | "<" | "+" | "-" | "*" ) Expression
|	Expression "[" Expression "]"
|	Expression "." "length"
|	Expression "." Identifier "(" ( Expression ( "," Expression )* )? ")"
|	<INTEGER_LITERAL>
|	"true"
|	"false"
|	Identifier
|	"this"
|	"new" "int" "[" Expression "]"
|	"new" Identifier "(" ")"
|	"!" Expression
|	"(" Expression ")"
Identifier	::=	<IDENTIFIER>
*/

grammar MiniJava;

program:
    mainClass ( classDeclaration )* EOF;

mainClass:
    'class' IDENTIFIER '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' IDENTIFIER ')' '{' statement '}' '}';


classDeclaration:
    'class' IDENTIFIER ( 'extends' IDENTIFIER )? '{' ( varDeclaration )* ( methodDeclaration )* '}';


varDeclaration:
    type IDENTIFIER ';';


methodDeclaration:
    'public' type IDENTIFIER '(' ( type IDENTIFIER ( ',' type IDENTIFIER )* )?
     ')' '{' ( varDeclaration )* ( statement )* 'return' expression ';' '}';


type:
    'int' '[' ']'
|	'boolean'
|	'int'
|	identifier;


statement:
    '{' ( statement )* '}'
|	'if' '(' expression ')' statement 'else' statement
|	'while' '(' expression ')' statement
|	'System.out.println' '(' expression ')' ';'
|	IDENTIFIER '=' expression ';'
|	IDENTIFIER '[' expression ']' '=' expression ';';


expression:
    expression ( '&&' | '<' | '+' | '-' | '*' ) expression
|	expression '[' expression ']'
|	expression '.' 'length'
|	expression '.' IDENTIFIER '(' ( expression ( ',' expression )* )? ')'
|	INTEGER_LITERAL
|	'true'
|	'false'
|	IDENTIFIER
|	'this'
|	'new' 'int' '[' expression ']'
|	'new' IDENTIFIER '(' ')'
|	'!' expression
|	'(' expression ')';

IDENTIFIER:
    [a-zA-Z][_0-9a-zA-Z]*;

INTEGER_LITERAL:
    [0-9]+;

WS:
    [\n \t\r]+ -> skip;

LINE_COMMENT:
    '//' ~[\r\n]* -> skip;
