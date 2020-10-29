// Define a grammar called Hello
// The same Hello world grammar inside grammars directory
grammar Hello;
s  : 'hello' ID ;         // match keyword hello followed by an identifier
ID : [a-zA-Z]+ ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines