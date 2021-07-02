grammar MiniJava;

goal                :   mainClass classDeclaration* EOF;

Identifier          :   [a-zA-Z_][0-9a-zA-Z_]*;

mainClass           :   'class' Identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' Identifier ')' '{' statement '}' '}';
classDeclaration    :   'class' Identifier ( 'extends' Identifier )? '{' varDeclaration* methodDeclaration* '}';
methodDeclaration   :   'public' type Identifier '(' parameterList? ')' '{' varDeclaration* statement* 'return' expression ';' '}';

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

expression          :    expression '.length'
                    |    expression '[' expression ']'
                    |    expression '.' Identifier '(' ( expression ( ',' expression )* )? ')'
                    |    expression Relation expression
                    |    'this'
                    |    'new' 'int' '[' expression ']'
                    |    'new' Identifier '(' ')'
                    |    '!' expression
                    |    '(' expression ')'
                    |    IntegerLiteral
                    |    Decimal
                    |    Boolean
                    |    Identifier;

parameter           :   type Identifier;
varDeclaration      :   type Identifier ';';
parameterList       :   parameter (',' parameter)*;

Boolean             :   'true' | 'false';
Relation            :   '**' | '*' | '/' | '+' | '-' | '>' | '<' | '=' | '&&' | '||';
IntegerLiteral      :   '0' | [1-9][0-9]*;
Decimal             :   IntegerLiteral? '.' [0-9]*;
WhiteSpace          :   [ \r\t\n]+ -> skip;
MULTILINE_COMMENT   :   '/*' .*? '*/' -> skip;
LINE_COMMENT        :   '//' .*? '\n' -> skip;