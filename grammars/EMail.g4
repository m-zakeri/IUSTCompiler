/*
grammer EMail1 (version 1)

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

grammar EMail;

start: LocalPart'@'Domain;
LocalPart: LocalPartRule+;
Domain: LETTER(LETTER|DIGIT|'-')*'.'ListOfDomain;

LocalPartRule: LETTER|DIGIT|PrintableCharacters|'.';
LETTER: [A-Za-z];
PrintableCharacters: '!'|'#'|'$'|'%'|'&'|'\''|'*'|'+'|'-'|'/'|'='|'?'|'^'|'_'|'`'|'{'|'}'|'~';
DIGIT: [0-9];
ListOfDomain: 'com'|'org'|'net'|'ir'|'info'|'gov';
