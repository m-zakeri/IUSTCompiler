grammar MiniJava;

program               :   mainClass classDeclaration* EOF;

mainClass           :   'class' Identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' Identifier ')' '{' statement '}' '}';
classDeclaration    :   'class' Identifier ( 'extends' Identifier )? '{' varDeclaration* methodDeclaration* '}';
varDeclaration      :   type Identifier ';';
methodDeclaration   :   'public' type Identifier '(' (parameter (',' parameter)*)? ')' '{' varDeclaration* statement* 'return' expression ';' '}';

type                :    'int'
                    |    'int' '[' ']'
                    |    'boolean'
                    |    Identifier;

statement           :    '{' statement* '}'
                    |    'if' '(' expression ')' statement 'else' statement
                    |    'while' '(' expression ')' statement
                    |    'System.out.println' '(' expression ')' ';'
                    |    Identifier '=' expression ';'
                    |    Identifier '[' expression ']' '=' expression ';';

expression          :    expression BinaryOperator expression
                    |    expression '[' expression ']'
                    |    expression '.length'
                    |    expression '.' Identifier '(' ( expression ( ',' expression )* )? ')'
                    |    IntegerLiteral
                    |    'true'
                    |    'false'
                    |    Identifier
                    |    'this'
                    |    'new' 'int' '[' expression ']'
                    |    'new' Identifier '(' ')'
                    |    '!' expression
                    |    '(' expression ')';

parameter           :   type Identifier;

Identifier          :   [a-zA-Z_][0-9a-zA-Z_]*;
BinaryOperator      :   '&&' | '<' | '+' | '-' | '*';
IntegerLiteral      :   '0' | [1-9][0-9]*;

WhiteSpace          :   [ \r\t\n]+ -> skip;
MULTILINE_COMMENT   :   '/*' .*? '*/' -> skip;
LINE_COMMENT        :   '//' .*? '\n' -> skip;
