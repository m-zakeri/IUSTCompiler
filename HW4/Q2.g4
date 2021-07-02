grammar Q2;

program:
    mainClass (classDeclaration)* EOF;

mainClass :
    CLASS Identifier L_BRACE PUBLIC STATIC VOID  MAIN L_PAREN STRING L_BRACK R_BRACK Identifier R_PAREN L_BRACE statement R_BRACE R_BRACE;

classDeclaration :
    CLASS Identifier (EXTENDS Identifier)? L_BRACE (varDeclaration)* (methodDeclaration)* R_BRACE;

varDeclaration :
    type_t Identifier SEMI;

methodDeclaration :
    PUBLIC type_t Identifier L_PAREN (type_t Identifier (COMMA type_t Identifier)*)? R_PAREN L_BRACE (varDeclaration)* (statement)* RETURN expression SEMI R_BRACE;

type_t :
    INT L_BRACK R_BRACK
    | BOOLEAN
    | INT
    | Identifier
    ;

statement :
         L_BRACE (statement)* R_BRACE
         | IF L_PAREN expression R_PAREN statement ELSE statement
         | WHILE L_PAREN expression R_PAREN statement
         | 'System.out.println' L_PAREN expression R_PAREN SEMI
         | Identifier ASSIGN expression SEMI
         | Identifier L_BRACK expression R_BRACK ASSIGN expression SEMI
         ;
expression
        : expression AND expression
        | expression LT expression
        | expression (PLUS | MINUS) expression
        | expression TIMES expression
        | expression L_BRACK expression R_BRACK
        | expression DOT LENGTH
        | expression DOT Identifier L_PAREN (expression (COMMA expression)*)? R_PAREN
        | INT_VAL
        | TRUE
        | FALSE
        | Identifier
        | THIS
        | NEW INT L_BRACK expression R_BRACK
        | NEW Identifier L_PAREN R_PAREN
        | BANG expression
        | L_PAREN expression R_PAREN
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

// Identifierentifier
Identifier      : LETTER (LETTER | DIGIT)*;
INT_VAL : ('0' | [1-9] DIGIT*);
fragment
LETTER  : [a-zA-Z_];
fragment
DIGIT   : [0-9];

// whitespaces and comments
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;