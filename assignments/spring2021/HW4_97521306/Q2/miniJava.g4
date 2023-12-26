grammar miniJava;

program:	        mainClass ( classDeclaration )* EOF;

mainClass:	        'class' identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier ')' '{' statement '}' '}';

classDeclaration:	'class' identifier ( 'extends' identifier )? '{' ( varDeclaration )* ( methodDeclaration )* '}';

varDeclaration: 	type identifier ';';

methodDeclaration:	'public' type identifier '(' ( type identifier ( ',' type identifier )* )? ')' '{' ( varDeclaration )* ( statement )* 'return' expression ';' '}';

type:               'int' '[' ']'
                |	'boolean'
                |	'int'
                |	identifier;

statement:	        '{' ( statement )* '}'
                |	'if' '(' expression ')' statement 'else' statement
                |	'while' '(' expression ')' statement
                |	'System.out.println' '(' expression ')' ';'
                |	identifier '=' expression ';'
                |	identifier '[' expression ']' '=' expression ';';

expression:         (INTEGER_LITERAL|'true'|'false'|identifier|'this'|'new' 'int' '[' expression ']'|'new' identifier '(' ')'|'!' expression|'(' expression ')')
                    ((( '&&' | '<' | '+' | '-' | '*' ) expression)|'[' expression ']'|'.' 'length'|'.' identifier '(' ( expression ( ',' expression )* )? ')')*;

identifier:        	IDENTIFIER ;

/* lexical rules */
INTEGER_LITERAL :
                    DIGIT+;

IDENTIFIER:         LETTER(LETTER | '_' | DIGIT)*;

fragment LETTER:             [a-zA-Z];

fragment DIGIT:              [0-9];

Whitespace:         ('\t' | ' ')+ -> skip;

BlockComment:       '/*' .*? '*/' -> skip;

LineComment:        '//' ~ ('\r' | '\n')* -> skip;

Newline:           ('\r' '\n'? | '\n') -> skip;
