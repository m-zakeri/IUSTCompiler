grammar mjava;

program:
    mainClass ( classDecl )* EOF
    ;

mainClass: Class mainClassDecl ;

mainClassDecl:
    identifier LBrace mainMethodDecl RBrace
    ;

mainMethodDecl:
     Public Static Void Main LPran StringType LBrack RBrack identifier RPran mainMethodBody
    ;

mainMethodBody:
    LBrace
        statement
    RBrace
    ;

classDecl:
    Class identifier (Extends identifier)?
    LBrace
        varDecl* methodDecl*
    RBrace
    ;

varDecl:
    type identifier SemiColon
    ;

methodDecl:
    Public type identifier LPran (type identifier (Comma type Identifier)*)? RPran methodBody
    ;

methodBody:
    LBrace
        varDecl* statement* Return exp SemiColon
    RBrace
    ;

type:
      IntType LBrack RBrack
    | BoolType
    | IntType
    | identifier
    ;
statement:
      LBrace statement* RBrace
    | If LPran exp RPran statement Else statement
    | While LPran exp RPran statement
    | 'System.out.println' LPran exp RPran SemiColon
    | identifier Equals exp SemiColon
    | identifier LBrack exp RBrack Equals exp SemiColon
    ;

exp:
      exp ( binOp ) exp
    | exp LBrack exp RBrack
    | exp Dot 'length'
    | exp Dot identifier LPran ( exp ( Comma exp )* )? RPran
    | Integer
    | True
    | False
    | identifier
    | This
    | New IntType LBrack exp RBrack
    | New identifier LPran RPran
    | Exclamation exp
    | LPran exp RPran
    ;
binOp: BinaryOperator;

identifier: Identifier;


Class: 'class';
Public: 'public';
Static: 'static';
Void: 'void';
Main: 'main';
LBrace: '{';
RBrace: '}';
LPran: '(';
RPran: ')';
LBrack: '[';
RBrack: ']';
If: 'if';
Else: 'else';
While: 'while';
SemiColon: ';';
Equals: '=';
Dot: '.';
Comma: ',';
True: 'true';
False: 'false';
This: 'this';
New: 'new';
IntType: 'int';
StringType: 'String';
BoolType: 'bool';
Exclamation: '!';
BinaryOperator: '&&'|'<'|'+'|'-'|'*';
Integer: [0-9]+;
Extends: 'extends';
Return: 'return';

Identifier: Letter LetterOrDigit*;

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;
fragment Letter
    : [a-zA-Z$_] // these are the "java letters" below 0x7F
    | ~[\u0000-\u007F\uD800-\uDBFF] // covers all characters above 0x7F which are not a surrogate
    | [\uD800-\uDBFF] [\uDC00-\uDFFF] // covers UTF-16 surrogate pairs encodings for U+10000 to U+10FFFF
    ;


WS:                 [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT:            '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*    -> channel(HIDDEN);