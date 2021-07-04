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
    '{' ( statement )* '}' #st1
    |'if' '(' expression ')' statement 'else' statement #if_st
    |'while' '(' expression ')' statement #while_st
    |'System.out.println' '(' expression ')' ';' #print_st
    |identifier '=' expression ';' #assign_st
    |identifier '[' expression ']' '=' expression ';' #id_st
    ;
expression:
    expression ( '&&' | '<' | '+' | '-' | '*' ) expression #exp1
    |expression '[' expression ']' #exp2
    |expression '.' 'length' #exp3
    |expression '.' identifier '(' ( expression ( ',' expression )* )? ')' #exp4
    |Integer #exp5
    |'true' #exp6
    |'false' #exp7
    |identifier #exp8
    |'this' #exp9
    |'new' 'int' '[' expression ']' #exp10
    |'new' identifier '(' ')' #exp11
    |'!' expression #exp12
    |'(' expression ')' #exp13
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