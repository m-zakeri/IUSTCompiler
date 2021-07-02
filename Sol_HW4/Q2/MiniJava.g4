grammar MiniJava;

program:
    mainClass (classDeclaration)* EOF;

mainClass:
    'class' ID '{' PUBLIC STATIC VOID MAIN '(' STRING '[' ']' ID ')' '{' statement '}' '}';

classDeclaration:
    'class' ID (EXTENDS ID)? '{' (varDeclaration)* (methodDeclaration)* '}';

varDeclaration:
    type_t ID ';';

methodDeclaration:
    PUBLIC type_t ID '(' (type_t ID (',' type_t ID)*)? ')' '{' (varDeclaration)* (statement)* RETURN expression ';' '}';

type_t:
    INT '[' ']'
    | BOOLEAN
    | INT
    | ID
    ;

statement: '{' (statement)* '}'
         | IF '(' expression ')' statement ELSE statement
         | WHILE '(' expression ')' statement
         | 'System.out.println' '(' expression ')' ';'
         | ID '=' expression ';'
         | ID '[' expression ']' '=' expression ';'
         ;
expression : expression '&&' expression
        | expression '<' expression
        | expression ('+' | '-') expression
        | expression '*' expression
        | expression '[' expression ']'
        | expression '.' LENGTH
        | expression '.' ID '(' (expression (',' expression)*)? ')'
        | INT_VALUE
        | TRUE
        | FALSE
        | ID
        | THIS
        | NEW INT '[' expression ']'
        | NEW ID '(' ')'
        | '!' expression
        | '(' expression ')'
        ;



BOOLEAN : 'boolean';
CLASS : 'class';
ELSE : 'else';
EXTENDS : 'extends';
FALSE : 'false';
IF : 'if';
INT : 'int';
LENGTH : 'length';
MAIN : 'main';
NEW : 'new';
PUBLIC : 'public';
RETURN : 'return';
STATIC : 'static';
STRING : 'String';
THIS : 'this';
TRUE : 'true';
VOID : 'void';
WHILE : 'while';

ASSIGN : '=';
GREAT : '>';
LITTLE : '<';
GREAT_EQUAL : '>=';
LITTLE_EQUAL : '<=';
PLUS : '+';
MINUS : '-';
TIMES : '*';
BANG : '!';
AND : '&&';
OR : '||';


LEFT_PARANTEZ : '(';
RIGHT_PARANTEZ : ')';
LEFT_BRACKET : '[';
RIGHT_BRACKET : ']';
LEFT_BRACE : '{';
RIGHT_BRACE : '}';
COMMA : ',';
DOT : '.';
SEMICOLEM : ';';


ID : LETTER (LETTER | NUMS)*;
INT_VALUE : ('0' | [1-9] NUMS*);
fragment
LETTER : [a-zA-Z_];
fragment
NUMS : [0-9];



WS : [ \t\r\n]+ -> skip ;
COMMENT : '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;