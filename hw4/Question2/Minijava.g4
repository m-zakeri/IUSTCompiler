grammar Minijava;

start returns [value_attr = str(), type_attr = str()]:   mainClass classDeclaration* EOF;

mainClass returns [value_attr = str(), type_attr = str()]:
   'class' identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier ')' '{' statement '}' '}';
classDeclaration  returns [value_attr = str(), type_attr = str()]:
   'class' identifier ( 'extends' identifier )? '{' varDeclaration* methodDeclaration* '}';
varDeclaration  returns [value_attr = str(), type_attr = str()]:
   typ identifier ';';
methodDeclaration  returns [value_attr = str(), type_attr = str()]:
   'public' typ identifier '(' (param (',' param)*)? ')' '{' varDeclaration* statement* 'return' expression ';' '}';

typ returns [value_attr = str(), type_attr = str()]:
    'int'
|    'int' '[' ']'
|    'boolean'
|    identifier;

statement returns [value_attr = str(), type_attr = str()]:    '{' statement* '}'
|    'if' '(' expression ')' statement 'else' statement
|    'while' '(' expression ')' statement
|    'System.out.println' '(' expression ')' ';'
|    identifier '=' expression ';'
|    identifier '[' expression ']' '=' expression ';';

expression returns [value_attr = str(), type_attr = str()]:
    expression binaryOperator expression
|    expression '[' expression ']'
|    expression '.length'
|    expression '.' identifier '(' ( expression ( ',' expression )* )? ')'
|    IntegerLiteral
|    'true'
|    'false'
|    identifier
|    'this'
|    'new' 'int' '[' expression ']'
|    'new' identifier '(' ')'
|    '!' expression
|    '(' expression ')';

param  returns [value_attr = str(), type_attr = str()]:  typ identifier;
binaryOperator  returns [value_attr = str(), type_attr = str()]:   '&&' | '<' | '+' | '-' | '*';

identifier         returns [value_attr = str(), type_attr = str()]:   Letter;
Letter :  [a-zA-Z_][0-9a-zA-Z_]*;
IntegerLiteral      :   '0' | [1-9][0-9]*;

WhiteSpace          :   [ \r\t\n]+ -> skip;
MULTILINE_COMMENT   :   '/*' .*? '*/' -> skip;
LINE_COMMENT        :   '//' .*? '\n' -> skip;
