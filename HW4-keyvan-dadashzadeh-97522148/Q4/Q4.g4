grammar Q4;

program:	        mainClass ( classDeclaration )* EOF;

mainClass:
                    'class' identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier ')' '{' statement '}' '}'
                    ;

classDeclaration:	'class' id1=identifier ( 'extends' identifier )? '{' ( varDeclaration )* ( methodDeclaration )* '}';

varDeclaration: 	type identifier ';';

methodDeclaration:
	                'public' type id1=identifier '(' ( type id2=identifier ( ',' type id3=identifier )* )? ')' '{' ( varDeclaration )* ( statement )* 'return' expression ';' '}'
	                ;

type:
                'int' '[' ']'
            |	'boolean'
            |	'int'
            |	identifier;

statement returns [value_attr=str(), type_attr = str()]:
                'if' '(' expression ')' st1=statement 'else' st2=statement                          #state_if
            |   '{' ( statement )* '}'                                                              #state_brace
            |	'while' '(' expression ')' st1=statement                                            #state_while
            |	'System.out.println' '(' expression ')' ';'                                         #state_println
            |	identifier '=' expression ';'                                                       #state_equal_assign
            |	identifier '[' first=expression ']' '=' second=expression ';'                       #state_access_array_assign
            ;


expression	returns [value_attr=str(), type_attr = str()]
            :
            	id=identifier                                                                        #expr_term_id
            |   first=expression '&&' second=expression                                              #expr_term_and
            |	'!' expression                                                                       #expr_term_not
            |	INTEGER_LITERAL                                                                      #expr_term_int
            |   first=expression '<'  second=expression                                              #expr_term_less
            |   first=expression '+'  second=expression                                              #expr_term_plus
            |	'true'                                                                               #expr_term_true
            |   first=expression '-'  second=expression                                              #expr_term_minus
            |	'false'                                                                              #expr_term_false
            |	'(' expression ')'                                                                   #expr_term_paran
            |   first=expression '*'  second=expression                                              #expr_term_multiply
            |	first=expression '.' id=identifier '(' ( second=expression ( ',' expression )* )? ')'#expr_term_call_function
            |	'this'                                                                               #expr_term_useless_1
            |	'new' 'int' '[' expression ']'                                                       #expr_term_useless_2
            |	'new' identifier '(' ')'                                                             #expr_term_useless_3
            |	first=expression '[' second=expression ']'                                           #expr_term_useless_4
            |	expression '.' 'length'                                                              #expr_term_useless_5
            ;


identifier returns [value_attr=str(), type_attr = str()]:
        	        IDENTIFIER
        	        ;

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