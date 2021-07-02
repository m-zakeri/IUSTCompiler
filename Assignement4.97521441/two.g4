grammar two;

program :
    mainClass ( classDeclare )* EOF
    ;

mainClass: 'class' mainClassDeclare ;

mainClassDeclare:
    identifier '{' mainMethodDecl '}'
    ;

mainMethodDecl:
     Public Static Void Main '(' String '[' ']' identifier ')' mainMethodBody
    ;

mainMethodBody:
    '{'
        statement
    '}'
    ;

classDeclare:
    'class' identifier ('extend' identifier)?
    '{'
        varDeclation* methodDecl*
    '}'
    ;

varDeclation:
    type identifier ';'
    ;

methodDecl:
    'public' type identifier '(' (type identifier (',' type Identifier)*)? ')' methodBody
    ;

methodBody:
    '{'
        varDeclation* statement* 'return' exp ';'
    '}'
    ;

type:
    identifier
    |IntType '[' ']'
    | BoolType
    | IntType

    ;
statement:
    '{' statement* '}'                                #statement_lb
    | 'while' '(' exp ')' statement                   #statement_while
    | 'if' '(' exp ')' statement 'else' statement     #statement_if
    | 'System.out.println' '(' exp ')' ';'            #statement_system
    | identifier '[' exp ']' '=' exp ';'              #statement_equalwithbra
    | identifier '=' exp ';'                          #statement_equal
    ;

exp:
      exp ( binOperator ) exp                               #exp_binaryop
    | exp '+' exp                                           #exp_sum
    | exp '-' exp                                           #exp_minus
    | exp '*' exp                                           #exp_multi
    |exp '<'  exp                                           #exp_gt
    |exp  '&&' exp                                          #exp_and
    | exp '[' exp ']'                                       #exp_lb
    | exp '.' 'length'                                      #exp_Dot
    | exp '.' identifier '(' ( exp ( ',' exp )* )? ')'      #exp_di
    | identifier                                            #exp_id
    | Integer                                               #exp_in
    | 'true'                                                #exp_tru
    | 'false'                                               #exp_false
    | 'this'                                                #exp_this
    | New IntType '[' exp ']'                               #exp_exp
    | New identifier '(' ')'                                #exp_ide
    | '!' exp                                               #exp_exclamation
    | '(' exp ')'                                           #exp_pran
    ;
binOperator: BinaryOperator;

identifier: Identifier;

Public: 'public';
Static: 'static';
Void: 'void';
Main: 'main';
Else: 'else';
This: 'this';
New: 'new';
IntType: 'int';
String: 'String';
BoolType: 'bool';
BinaryOperator: '&&'|'<'|'+'|'-'|'*';
Integer: [0-9]+;


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

LINE_COMMENT:       '//' ~[\r\n]*    -> channel(HIDDEN);
WS:                 [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT:            '/*' .*? '*/'    -> channel(HIDDEN);
