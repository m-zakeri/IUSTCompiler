/*
grammer AssignmentStatement2 (version 2)

@author: Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)
@date: 20201029

- Compiler generator:   ANTRL4.x
- Target language(s):   Python3.x,


-Changelog:
-- v2.0
--- add atribute for holding rule tyep and rule intermediate representations (AST and Three-addresses codes)
---

- Reference: Compiler book by Dr. Saeed Parsa (http://parsa.iust.ac.ir/)
- Course website:   http://parsa.iust.ac.ir/courses/compilers/
- Laboratory website:   http://reverse.iust.ac.ir/

*/

grammar AssignmentStatement2;

start returns [value_attr = str(), type_attr = str()]: prog EOF ;

prog returns [value_attr = str(), type_attr = str()]: prog assign | assign ;

assign returns [value_attr = str(), type_attr = str()]: ID ':=' expr (NEWLINE | EOF) ;

expr returns [value_attr = str(), type_attr = str()]:
    expr '+' term #expr_term_plus
    | expr '-' term  #expr_term_minus
    | expr RELOP term #expr_term_relop
    | term #term4
    ;

term returns [value_attr = str(), type_attr = str()]:
    term '*' factor #term_fact_mutiply
    | term '/' factor #term_fact_divide
    | factor #factor3
    ;

factor returns [value_attr = str(), type_attr = str()]:
    '(' expr ')' #fact_expr
    | ID #fact_id
    | number #fact_number
    ;

number returns [value_attr = str(), type_attr = str()]:
    FLOAT #number_float
    | INT #number_int
    ;

/* Lexical Rules */
INT     : DIGIT+ ;

FLOAT:
    DIGIT+ '.' DIGIT*
    | '.' DIGIT+ ;

String:
        '"' (ESC|.)*? '"' ;
ID:
    LETTER(LETTER|DIGIT)* ;


fragment
        DIGIT: [0-9] ;
fragment
        LETTER: [a-zA-Z] ;
fragment
        ESC: '\\"' | '\\\\' ;


WS: [ \t\r]+ -> skip ;
NEWLINE: '\n';
RELOP: '<=' | '<' ;