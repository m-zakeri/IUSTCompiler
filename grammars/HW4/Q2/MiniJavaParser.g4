parser grammar MiniJavaParser;


options { tokenVocab=MiniJavaLexer; }


program
    : mainClass ( classDeclaration )* EOF
    ;

mainClass
    : 'class' identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier ')' '{' s=statement '}' '}'
    ;

classDeclaration
    : 'class' identifier ( 'extends' identifier )? '{' ( varDeclaration )* ( methodDeclaration )* '}'
    ;

varDeclaration
    : t=type_ i=identifier ';'
    ;

methodDeclaration
    : 'public' type_ identifier '(' ( type_ identifier ( ',' type_ identifier )* )? ')' '{' ( varDeclaration )* ( s=statement )* 'return' expression ';' '}'
    ;

type_
    : 'int' '[' ']'
    | 'boolean'
    | 'int'
    | i=identifier
    ;


statement
    :   '{' ( s=statement )* '}'
    |  'if' '(' e=expression ')' s1=statement 'else' s2=statement
    | 'while' '(' e=expression ')' s=statement
    | 'System.out.println' '(' expression ')' ';'
    | i=identifier '=' e=expression ';'
    | i=identifier '[' e1=expression ']' '=' e2=expression ';'
    ;

expression
    : '(' e=expression ')'
    | e1=expression '&&' e2=expression
    | e1=expression '*' e2=expression
    | e1=expression '<' e2=expression
    | e1=expression '+' e2=expression
    | e1=expression '-' e2=expression
    | e1=expression '[' e2=expression ']'
    | e=expression '.' 'length'
    | expression '.' identifier '(' ( expression ( ',' expression )* )? ')'
    | INTEGER_LITERAL
    | 'true'
    | 'false'
    | i=identifier
    | 'this'
    | 'new' 'int' '[' expression ']'
    | 'new' identifier '(' ')'
    | '!' e=expression
    ;

identifier
    : IDENTIFIER
    ;