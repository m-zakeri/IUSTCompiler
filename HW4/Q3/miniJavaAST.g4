grammar miniJavaAST;




program returns [v='program'] :  main_class ( class_declaration )* EOF ;

main_class returns [v='main_class']: 'class' identifier_r '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier_r ')' '{' s=statement '}' '}';

class_declaration returns [v='class_declaration']: 'class' identifier_r ( 'extends' identifier_r)? '{' (var_declaration)* (method_declaration)* '}';
var_declaration returns [v='var_dec']: type_r identifier_r ';';

method_declaration returns [v='method']: 'public' type_r identifier_r '(' (type_r identifier_r (',' type_r identifier_r)*)? ')' '{' (var_declaration)* (statement )* 'return' expression ';' '}';

type_r returns [v='type']: 'int' '[' ']' | 'boolean' | 'int' | identifier_r ;

statement returns [v='statement']: 
        '{' (statement )* '}' | 
        'if' '(' expression ')' statement 'else' statement 
        | 
        'while' '(' expression ')' statement 
        |
        'System.out.println' '(' expression ')' ';' 
        |identifier_r '=' expression ';' 
        | identifier_r '[' expression ']' '=' expression ';' 
        ;

expression returns [v='expression']: expression ('+' | '-' | '*'|'&&'|'<') expression 
    | expression '[' expression ']'
    | expression '.' 'length'
    |expression '.' identifier_r '(' (expression ( ',' expression)*)? ')' 
    | DECIMAL_LITERAL 
    | 'true'| 'false' | identifier_r |'this' 
    | 'new' 'int' '[' expression ']' 
    | 'new' identifier_r '(' ')' 
    | '!' expression 
    | '(' expression ')'
    ;
identifier_r returns [v=str()]: IDENTIFIER {$v=$IDENTIFIER.text};

IDENTIFIER :  Letter LetterOrDigit*;


DECIMAL_LITERAL:    ('0' | [1-9] (Digits? | '_'+ Digits)) [lL]?;
HEX_LITERAL:        '0' [xX] [0-9a-fA-F] ([0-9a-fA-F_]* [0-9a-fA-F])? [lL]?;
OCT_LITERAL:        '0' '_'* [0-7] ([0-7_]* [0-7])? [lL]?;
BINARY_LITERAL:     '0' [bB] [01] ([01_]* [01])? [lL]?;


fragment Digits
    : [0-9] ([0-9_]* [0-9])?
    ;

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;


fragment Letter
    : [a-zA-Z$_] // these are the "java letters" below 0x7F
    | ~[\u0000-\u007F\uD800-\uDBFF] // covers all characters above 0x7F which are not a surrogate
    | [\uD800-\uDBFF] [\uDC00-\uDFFF] // covers UTF-16 surrogate pairs encodings for U+10000 to U+10FFFF
    ;

WS:                 [ \t\r\n\u000C]+    -> channel(HIDDEN);
COMMENT:            '/*' .*? '*/'       -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*       -> channel(HIDDEN);