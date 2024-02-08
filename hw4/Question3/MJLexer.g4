lexer grammar MJLexer;

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


fragment Digit:
    [0-9];
fragment LetterOrDigit:
    [a-zA-Z_]
    | Digit;
IDENTIFIER:
    [a-zA-Z_] LetterOrDigit*;

INTEGER_LITERAL:
    ( '0' | [1-9] Digit* );


WS:                 [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT:            '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*    -> channel(HIDDEN);