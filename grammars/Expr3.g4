/*
grammar Expr3
Test grammar (version 2) for demo and education porpuse.
Version 3 for explaining attributed grammar with actions in ANTLR.

Written by: Morteza Zakeri
*/
grammar Expr3;

@parser::members{
parser_member1 = None
parser_member0 = str()
temp_counter = 0

def create_temp(self, temp_counter):
    self.temp_counter +=1
    return temp_counter
}

start:
    Id '=' expr EOF
    ;

expr returns [code=int(), attr=1] locals [attr2=2]:
    e2=expr '+' t1=term  {$code = self.create_temp(self.temp_counter)
print($code, '=', $e2.code, '+', $t1.code)} #expr1
    | expr '-' term  #expr2
    | term #expr3
    ;

term returns [code, attr]:
    term '*' fact #term1
    | term '/' fact #term2
    | fact #term3
    ;

fact returns [code]:
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



