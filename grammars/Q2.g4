grammar Q2 ;

@parser :: members {

temp_counter = 0

def create_temp(self):
    self.temp_counter += 1
    return 'T' + str(self.temp_counter)

def remove_temp(self) :
    self.temp_counter -= 1

def is_temp(self, var:str):
    if var[0] == 'T':
        return True
    return False

def create_label(self):
    slef.label_counter += 1
    return 'L' + str(self.tmp_counter)
}


program	:	mainClass ( classDeclaration )* EOF ;
mainClass	:	'class' IDENTIFIER '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' IDENTIFIER ')' '{' statement '}' '}' ;
classDeclaration	:	'class' IDENTIFIER ( 'extends' IDENTIFIER )? '{' ( varDeclaration )* ( methodDeclaration )* '}' ;
varDeclaration	:	type IDENTIFIER ';' ;
methodDeclaration	:	'public' type IDENTIFIER '(' ( type IDENTIFIER ( ',' type IDENTIFIER )* )? ')' '{' ( varDeclaration )* ( statement )* 'return' expression ';' '}' ;
type	:	'int' '[' ']'
|	'boolean'
|	'int'
|	IDENTIFIER
;
statement	:	'{' ( statement )* '}'
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