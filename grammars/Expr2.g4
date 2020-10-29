/*
grammar Expr2
Test grammar (version 2) for demo and education porpuse.
Version 2 for explaining attributed grammar in ANTLR.

Written by: Morteza Zakeri
Only for teaching porpuses
*/


grammar Expr2;
start:
    Id '=' expr EOF
    ;

expr returns [code=str()]:
    e2=expr '+' t1=term  #expr1
    | expr '-' term  #expr2
    | term #expr3
    ;

term returns [code=str()]:
    term '*' fact  #term1
    | term '/' fact #term2
    | fact #term3
    ;

fact returns [code=str()]:
    Id #fact1
    | Number #fact2
    | '('expr')' #fact3
    ;


/* Lexical rules*/
Plus: '+';
MINUS: '-';
MUL: '*';
DIVIDE: '/';
ASSIGN: '=';

Id: IDENTIFIER;
Number: NUMBER;

fragment IDENTIFIER: [a-zA-Z]+;
fragment NUMBER: [0-9]+;

Whitespace: [ \t]+ -> channel(HIDDEN);
Newline: '\n' -> skip;



