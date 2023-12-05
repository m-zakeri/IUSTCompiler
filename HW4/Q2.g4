grammar Q2;

program returns[value_attr = str(), type_attr = str()]:
    mainClass (classDeclaration)* EOF;

mainClass returns[value_attr = str(), type_attr = str()]:
    CLASS Identifier L_BRACE PUBLIC STATIC VOID  MAIN L_PAREN STRING L_BRACK R_BRACK Identifier R_PAREN L_BRACE statement R_BRACE R_BRACE;

classDeclaration returns[value_attr = str(), type_attr = str()] :
    CLASS Identifier (EXTENDS Identifier)? L_BRACE (varDeclaration)* (methodDeclaration)* R_BRACE;

varDeclaration returns[value_attr = str(), type_attr = str()]:
    type_t Identifier SEMI;

methodDeclaration returns[value_attr = str(), type_attr = str()] :
    PUBLIC type_t Identifier L_PAREN (type_t Identifier (COMMA type_t Identifier)*)? R_PAREN L_BRACE (varDeclaration)* (statement)* RETURN expression SEMI R_BRACE;

type_t returns[value_attr = str(), type_attr = str()] :
    INT L_BRACK R_BRACK     #array_int
    | BOOLEAN               #bool
    | INT                   #int
    | Identifier            #id
    ;

statement returns[value_attr = str(), type_attr = str()] :
         L_BRACE (statement)* R_BRACE                                   #braket_statement
         | IF L_PAREN expression R_PAREN statement ELSE statement       #if_statement
         | Identifier ASSIGN expression SEMI                            #equal_statement
         | WHILE L_PAREN expression R_PAREN statement                   #while_statement
         | 'System.out.println' L_PAREN expression R_PAREN SEMI         #print
         | Identifier L_BRACK expression R_BRACK ASSIGN expression SEMI #equal_array_statement
         ;
expression returns[value_attr = str(), type_attr = str()] :
          expression L_BRACK expression R_BRACK                                         #array_expression
        | expression DOT LENGTH                                                         #length_expression
        | expression DOT Identifier L_PAREN (expression (COMMA expression)*)? R_PAREN   #dot_par_expression
        | INT_VAL                                                                       #number
        | BANG expression                                                               #not_expression
        | BOOL                                                                          #keywords
        | Identifier                                                                    #word
        | NEW INT L_BRACK expression R_BRACK                                            #new_array_expression
        | NEW Identifier L_PAREN R_PAREN                                                #new_identifier
        | L_PAREN expression R_PAREN                                                    #in_par_expression
        | expression OP expression                                                      #operations_expression
        ;

BOOL    :TRUE | FALSE | THIS;
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
//LT      : '<';
OP      : '&&' | '<' | '+' | '-' | '*';
GE      : '>=';
LE      : '<=';
//PLUS    : '+';
//MINUS   : '-';
//TIMES   : '*';
BANG    : '!';
//AND     : '&&';
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