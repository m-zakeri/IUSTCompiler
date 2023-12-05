grammar MiniJava;

program: mainClass (classDeclaration)* EOF ;
mainClass:	'class' IDENTIFIER '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' IDENTIFIER ')' '{' statement '}' '}' ;
classDeclaration:	'class' IDENTIFIER ( 'extends' IDENTIFIER )? '{' ( varDeclaration )* ( methodDeclaration )* '}' ;
varDeclaration:	type1 IDENTIFIER ';' ;
methodDeclaration:	'public' type1 IDENTIFIER '(' ( type1 IDENTIFIER ( ',' type1 IDENTIFIER )* )? ')' '{' ( varDeclaration )* ( statement )* 'return' expression ';' '}' ;
type1:	'int' '[' ']'
|	'boolean'
|	'int'
|	IDENTIFIER
;
statement:	'{' ( statement )* '}'
|	'if' '(' expression ')' statement 'else' statement
|	'while' '(' expression ')' statement
|	'System.out.println' '(' expression ')' ';'
|	IDENTIFIER '=' expression ';'
|	IDENTIFIER '[' expression ']' '=' expression ';'
;
expression:	expression ( '&&' | '<' | '+' | '-' | '*' ) expression
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
|	'(' expression ')'
;
IDENTIFIER:	[a-zA-Z_][a-zA-Z0-9_]* ;
INTEGER_LITERAL: '0'..'9'+ ;
WS        :   [ \t\r\n]+ -> skip ;
COMMENT   : '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' .*? '\r'? '\n' -> skip;