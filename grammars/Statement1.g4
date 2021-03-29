/*
grammer AssignmentStatement3 (version 3)

@author: Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)
@date: 20201028

- Compiler generator:   ANTRL4.x
- Target language(s):     Python3.x,


-Changelog:
-- v3.0
--- Add semantic rules to perform type checking
--- Add semantic routines to generate intermediate representation (three addresses codes)
-- v2.0

- Reference: Compiler book by Dr. Saeed Parsa (http://parsa.iust.ac.ir/)
- Course website:   http://parsa.iust.ac.ir/courses/compilers/
- Laboratory website:   http://reverse.iust.ac.ir/

*/


grammar Statement1;


start :st;

sts : st |  sts st
;

st : assign | forst | compondst;

compondst : '{' sts '}';

assign: ID ':=' expr;

forst:  '[' ID ':=' expr ':' 'for' e1=expr 'in' 'range' '(' expr ':' expr ')' ']' ;

expr:
    expr '+' term
    |expr RELOP term
    | expr '-' term
    | expr RELOP term
    | term
;


term :
    term '*'factor
    | term '/' factor
    | factor
    ;


factor:
    '(' e=expr ')'
    | ID
    | n=number
    ;

number:
    |FLOAT
    ;



/* Lexical Rules */
INT: DIGIT+ ;

FLOAT:
    DIGIT+ '.' DIGIT*
    | '.' DIGIT+
    ;



String:
    '"' (ESC|.)*? '"'
    ;


ID:
    LETTER(LETTER|DIGIT)* ;


RELOP: '<=' | '<' ;


fragment
        DIGIT: [0-9] ;
fragment
        LETTER: [a-zA-Z] ;
fragment
        ESC: '\\"' | '\\\\' ;


WS: [ \t\r]+ -> skip ;
NEWLINE: '\n';
