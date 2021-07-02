grammar MiniJava;

program:
    mainClass (classDeclaration)* EOF;

// parser rules
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
expression    : expression '&&' expression
        | expression '<' expression
        | expression ('+' | '-') expression
        | expression '*' expression
        | expression '[' expression ']'
        | expression '.' LENGTH
        | expression '.' ID '(' (expression (',' expression)*)? ')'
        | INT_VAL
        | TRUE
        | FALSE
        | ID
        | THIS
        | NEW INT '[' expression ']'
        | NEW ID '(' ')'
        | '!' expression
        | '(' expression ')'
        ;

// Keywords
BOOLEAN : 'boolean';
CLASS   : 'class';
ELSE    : 'else';
EXTENDS : 'extends';
FALSE   : 'false';
IF      : 'if';
INT     : 'int';
LENGTH  : 'length';
MAIN    : 'main';
NEW     : 'new';
PUBLIC  : 'public';
RETURN  : 'return';
STATIC  : 'static';
STRING  : 'String';
THIS    : 'this';
TRUE    : 'true';
VOID    : 'void';
WHILE   : 'while';

// Operators
ASSIGN  : '=';
GT      : '>';
LT      : '<';
GE      : '>=';
LE      : '<=';
PLUS    : '+';
MINUS   : '-';
TIMES   : '*';
BANG    : '!';
AND     : '&&';
OR      : '||';

// Separators
L_PAREN : '(';
R_PAREN : ')';
L_BRACK : '[';
R_BRACK : ']';
L_BRACE : '{';
R_BRACE : '}';
COMMA   : ',';
DOT     : '.';
SEMI    : ';';

// Identifier
ID      : LETTER (LETTER | DIGIT)*;
INT_VAL : ('0' | [1-9] DIGIT*);
fragment
LETTER  : [a-zA-Z_];
fragment
DIGIT   : [0-9];

// whitespaces and comments
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;