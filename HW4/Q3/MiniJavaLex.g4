lexer grammar MiniJavaLex;

fragment Digit
    : [0-9]
    ;

fragment Letter
    : [a-zA-Z_]
    ;

fragment LetterOrDigit
    : Letter
    | Digit
    ;

RETURN:             'return';
INT:                'int';
BOOLEAN:            'boolean';
IF:                 'if';
ELSE:               'else';
WHILE:              'while';
SOUT:               'System.out.println';
ASSIGN:             '=';
ADD:                '+';
SUB:                '-';
MUL:                '*';
LT:                 '<';
ANDAND:             '&&';
LEN:                'length';
NOT:                '!';
NEW:                'new';
THIS:               'this';
CLASS:              'class';
LPAREN:             '(';
RPAREN:             ')';
LBRACE:             '{';
RBRACE:             '}';
LBRACK:             '[';
RBRACK:             ']';
SEMI:               ';';
COMMA:              ',';
DOT:                '.';
TRUE:               'true';
FALSE:              'false';
PUBLIC:             'public';
STATIC:             'static';
VOID:               'void';
MAIN:               'main';
STRING:             'String';
EXTENDS:            'extends';
