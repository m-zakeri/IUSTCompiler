grammar mini_java;

program:
    mainClass ( classDecleration )* EOF
    ;
mainClass:
    'class' identifier  '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier ')' '{' statement '}' '}'
    ;
classDecleration:
    'class' identifier ( 'extends' identifier )? '{' ( varDeclaration )* ( methodDeclaration )* '}'
    ;
varDeclaration:
    type identifier ';'
    ;
methodDeclaration:
    'public' type identifier '(' ( type identifier ( ',' type identifier )* )? ')' '{' ( varDeclaration )* ( statement )* 'return' expression ';' '}'
    ;
type:
    'int' '[' ']'
    |'boolean'
    |'int'
    |identifier
    ;
statement:
    '{' ( statement )* '}'
    |'if' '(' expression ')' statement 'else' statement
    |'while' '(' expression ')' statement
    |'System.out.println' '(' expression ')' ';'
    |identifier '=' expression ';'
    |identifier '[' expression ']' '=' expression ';'
    ;
expression:
    expression ( '&&' | '<' | '+' | '-' | '*' ) expression
    |expression '[' expression ']'
    |expression '.' 'length'
    |expression '.' identifier '(' ( expression ( ',' expression )* )? ')'
    |Integer
    |'true'
    |'false'
    |identifier
    |'this'
    |'new' 'int' '[' expression ']'
    |'new' identifier '(' ')'
    |'!' expression
    |'(' expression ')'
    ;
identifier:
    Identifier;

Identifier: Letter LetterOrDigit*;

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;
fragment Letter
    : [a-zA-Z$_]
    | ~[\u0000-\u007F\uD800-\uDBFF]
    | [\uD800-\uDBFF] [\uDC00-\uDFFF]
    ;
Integer:
    [0-9]+
    ;
WS:
    [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT:
    '/*' .*? '*/' -> channel(HIDDEN)
    ;
LINE_COMMENT:
    '//' ~[\r\n]* -> channel(HIDDEN)
    ;