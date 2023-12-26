grammar miniJava;

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
	                '{' ( statement )* '}'                                          #statement_statement
                |	'if' '(' expression ')' st1=statement 'else' st2=statement      #statement_if
                |	'while' '(' expression ')' st1=statement                        #statement_while
                |	'System.out.println' '(' expression ')' ';'                     #statement_println
                |	identifier '=' expression ';'                                   #statement_value_assignment
                |	identifier '[' e1=expression ']' '=' e2=expression ';'                #statement_array_cell_assignment
                ;


expression	returns [value_attr=str(), type_attr = str()]:
                e1=expression '&&' e2=expression        #expression_and_expression
            |   e1=expression '<'  e2=expression        #expression_lessthan_expression
            |   e1=expression '+'  e2=expression        #expression_plus_expression
            |   e1=expression '-'  e2=expression        #expression_minus_expression
            |   e1=expression '*'  e2=expression        #expression_multiply_expression
            |	e1=expression '[' e2=expression ']'     #expression_array
            |	expression '.' 'length'                 #expression_array_length
            |	e1=expression '.' id=identifier '(' ( e2=expression ( ',' expression )* )? ')'      #expression_function_call
            |	INTEGER_LITERAL                         #expression_integer_literal
            |	'true'                                  #expression_true
            |	'false'                                 #expression_false
            |	id=identifier                           #expression_identifier
            |	'this'                                  #expression_this
            |	'new' 'int' '[' expression ']'          #expression_array_declaration
            |	'new' identifier '(' ')'                #expression_class_declaration
            |	'!' expression                          #expression_not
            |	'(' expression ')'                      #expression_paranthesis_expression
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
