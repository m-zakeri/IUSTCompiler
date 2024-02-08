grammar q2;

program: MainClass (ClassDeclaration)* EOF;


/* classes */

MainClass:
          'class' Identifier '{'
              'public' 'static' 'void' 'main' '(' 'String' '[' ']' Identifier ')' '{'
                      Statement
              '}'
            '}'
          ;

ClassDeclaration:
        'class' Identifier ('extends' Identifier)? '{' (VarDeclaration)* (MethodDeclaration)* '}'
        ;

/*variaveis e tipos */
VarDeclaration:
		Type Identifier ';'
		;
Type:
		'int' '[' ']'
		|'boolean'
		|'int'
		|Identifier
		;
/*metodos*/

MethodDeclaration:
        'public' Type Identifier '(' (Type Identifier (',' Type Identifier)* )? ')' '{' (VarDeclaration)* (Statement)* 'return' Expression '}'
        ;


/*statements*/

Statement:
		'{' ( Statement )* '}'
		| 'while' '(' Expression ')' '{' Statement '}'
        | 'if' '(' Expression ')' '{' Statement '}' 'else' '{' Statement '}'
        | 'System.out.println' '(' Expression ')' ';'
        | Identifier '=' Expression ';'
        | Identifier '[' Expression ']' '=' Expression ';'
        ;


/* Expressoes */
Expression:
		| INTEGER_LITERAL Expression_prim
		| 'true' Expression_prim
		| 'false' Expression_prim
		| Identifier Expression_prim
		| 'this' Expression_prim
		| 'new' 'int' '[' Expression ']' Expression_prim
		| 'new' Identifier '(' ')' Expression_prim
		| '!' Expression Expression_prim
		| '(' Expression ')' Expression_prim
		;
Expression_prim:
		( '&&' | '<' | '+' | '-' | '*' ) Expression
		| '[' Expression ']'
		| '.' 'length'
		| '.' Identifier '(' ( Expression ( ',' Expression )* )? ')'
		|
		;


Identifier: IDENTIFIER;

/* CTES */
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
IDENTIFIER: [_a-zA-Z][_a-zA-Z0-9];
INTEGER_LITERAL: [0-9]*;