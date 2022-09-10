/*
grammer AssignmentStatement1 (version 1)

@author: Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)
@date: 20201025

- Compiler generator:   ANTRL4.x
- Target language(s):     Python3.x,


-Changelog:
-- v1
---

- Reference: Compiler book by Dr. Saeed Parsa (http://parsa.iust.ac.ir/)
- Course website:   http://parsa.iust.ac.ir/courses/compilers/
- Laboratory website:   http://reverse.iust.ac.ir/

*/

grammar AssignmentStatement1;

start: prog EOF;



prog: prog assign | assign;

assign: Id ':=' expr (NEWLINE | EOF);

expr:	expr '+' term
    |	expr '-' term
    |	term
    ;

term:	term '*' factor
    |	term '/' factor
    |	factor
    ;

factor:
    '(' expr ')'
    | Id
    | number
    | String
    ;

number  : INT | FLOAT;



/* Lexical Rules */
Id      : LETTER(LETTER|DIGIT)*;   /*    */

INT     : DIGIT+;

FLOAT:
    DIGIT+ '.' DIGIT*
    | '.' DIGIT+ ;

String  :
        '"' (ESC|.)*?;

fragment
        DIGIT: [0-9];
fragment
        LETTER: [a-zA-Z];
fragment
        ESC : '\\"' | '\\\\' ;

WS: [ \t\r]+ -> skip ;
NEWLINE: '\n' ;
RELOP: '<=' | '<' ;
