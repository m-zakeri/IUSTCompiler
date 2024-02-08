grammar MiniJava;

program returns[value_attr = str(), type_attr = str()]:
    mainClass (classDeclaration)* EOF;

mainClass returns[value_attr = str(), type_attr = str()]:
    CLASS identifier LBRACE PUBLIC STATIC VOID MAIN LPAREN STRING LBRACK RBRACK identifier RPAREN LBRACE statement RBRACE RBRACE;

classDeclaration returns[value_attr = str(), type_attr = str()]:
    CLASS identifier (EXTENDS identifier)? LBRACE (varDeclaration)* (methodDeclaration)* RBRACE;

varDeclaration returns[value_attr = str(), type_attr = str()]:
    type_t identifier SEMI;

methodDeclaration returns[value_attr = str(), type_attr = str()]:
    PUBLIC type_t identifier LPAREN (type_t identifier (COMMA type_t identifier)*)? RPAREN LBRACE (varDeclaration)* (statement)* RETURN expression SEMI RBRACE;

type_t returns[value_attr = str(), type_attr = str()]:
    INT LBRACK RBRACK
    | BOOLEAN
    | INT
    | identifier
    ;

statement returns[value_attr = str(), type_attr = str()]:
           LBRACE (statement)* RBRACE                            #bracket_statmetn
         | IF LPAREN expression RPAREN statement ELSE statement  #if_statment
         | WHILE LPAREN expression RPAREN statement              #while_statment
         | 'System.out.println' LPAREN expression RPAREN SEMI    #output_statment
         | identifier EQ expression SEMI                         #equal_statment
         | identifier LBRACK expression RBRACK EQ expression SEMI #equal_array_statment
         ;
expression returns[value_attr = str(), type_attr = str()]:
          expression AND expression                             #and_exp
        | expression LT expression                              #lt_exp
        | expression (PLUS | MINUS) expression                  #plus_minus_exp
        | expression MUL expression                             #mul_exp
        | expression LBRACK expression RBRACK                   #bracket_exp
        | expression DOT LENGTH                                 #len_exp
        | expression DOT identifier LPAREN (expression (COMMA expression)*)? RPAREN  #dot_par_expression
        | INT_VAL                                               #num_exp
        | TRUE                                                  #true_exp
        | FALSE                                                 #false_exp
        | identifier                                            #identifier_exp
        | THIS                                                  #this_exp
        | NEW INT LBRACK expression RBRACK                      #new_array_exp
        | NEW identifier LPAREN RPAREN                          #new_identifier
        | NOT expression                                        #not_exp
        | LPAREN expression RPAREN                              #in_par_expression
        ;

identifier returns[value_attr = str(), type_attr = str()]:
    Identifier;

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
EQ      : '=';
LT      : '<';
PLUS    : '+';
MINUS   : '-';
MUL     : '*';
NOT     : '!';
AND     : '&&';
LPAREN  : '(';
RPAREN  : ')';
LBRACK  : '[';
RBRACK  : ']';
LBRACE  : '{';
RBRACE  : '}';
COMMA   : ',';
DOT     : '.';
SEMI    : ';';
Identifier : LETTER (LETTER | DIGIT)*;
INT_VAL : ('0' | N_DIGIT DIGIT*);

fragment LETTER  :
    [a-zA-Z_];

fragment DIGIT   :
    [0-9];

fragment N_DIGIT  :
    [1-9];

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;