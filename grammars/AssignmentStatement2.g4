/*
grammer AssignmentStatement2 (version 2)

@author: Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)
@date: 20201029

- Compiler generator:   ANTRL4.x
- Target language(s):     Python3.x,


-Changelog:
-- v2
---

- Reference: Compiler book by Dr. Saeed Parsa (http://parsa.iust.ac.ir/)
- Course website:   http://parsa.iust.ac.ir/courses/compilers/
- Laboratory website:   http://reverse.iust.ac.ir/

*/

grammar AssignmentStatement2;

start returns [n = str()]: prog EOF ;

prog returns [n = str()]: prog assign | assign ;

assign returns [n = str()]: ID ':=' e=expr (NEWLINE | EOF) {n = $e.text};

expr returns [n = str()] :
    e=expr '+' t=term   { if $t.ctx.type == FLOAT:
                                    n = str(float($e.text) + float($t.text))
                                 else :
                                    n = str(int($e.text) + int($t.text))}

    | e=expr '-' t=term   { if $t.ctx.type == FLOAT:
                                    n = str(float($e.text) - float($t.text))
                                 else :
                                    n = str(int($e.text) - int($t.text))}

    | expr RELOP term
    | t=term              {n=$t.text};
term returns [n = str() ]:
    t=term '*' f = factor      { if $t.ctx.type == FLOAT:
                                    n = str(float($t.text) * float($f.text))
                                 else :
                                    n = str(int($t.text) * int($f.text))}

    | t=term '/' f=factor      { if $t.ctx.type == FLOAT:
                                    n = str(float($t.text) / float($f.text))
                                 else :
                                    n = str(int($t.text) / int($f.text))}
    | f=factor                 {n= $f.text }
    ;
factor returns [n = str()]:
    '(' expr ')'
    | ID                 {n = ($ID.text)}
    | number             {n = ($number.text)}
    ;
number :
    FLOAT
    | INT
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