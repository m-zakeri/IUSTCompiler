/*
Hello world grammar in ANTLR

*/


// Define a grammar called Hello
grammar HelloWorld;
s  : 'hello' ID ;         // match keyword hello followed by an identifier
ID : [a-zA-Z]+ ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
