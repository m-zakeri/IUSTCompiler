grammar AssignmentStAss4;

program returns [value_attr = str(), type_attr = str()]:
    mainClass ( classDeclare )* EOF
    ;

mainClass returns [value_attr = str(), type_attr = str()]: 'class' mainClassDeclare ;

mainClassDeclare returns [value_attr = str(), type_attr = str()]:
    identifier '{' mainMethodDecl '}'
    ;

mainMethodDecl returns [value_attr = str(), type_attr = str()]:
     Public Static Void Main '(' String '[' ']' identifier ')' mainMethodBody
    ;

mainMethodBody returns [value_attr = str(), type_attr = str()]:
    '{'
        statement
    '}'
    ;

classDeclare returns [value_attr = str(), type_attr = str()]:
    'class' identifier ('extend' identifier)?
    '{'
        varDeclation* methodDecl*
    '}'
    ;

varDeclation returns [value_attr = str(), type_attr = str()]:
    type identifier ';'
    ;

methodDecl returns [value_attr = str(), type_attr = str()]:
    'public' type identifier '(' (type identifier (',' type Identifier)*)? ')' methodBody
    ;

methodBody returns [value_attr = str(), type_attr = str()]:
    '{'
        varDeclation* statement* 'return' exp ';'
    '}'
    ;

type returns [value_attr = str(), type_attr = str()]:
    identifier
    |IntType '[' ']'
    | BoolType
    | IntType

    ;
statement returns [value_attr = str(), type_attr = str()]:
    ifst                                              #statement_if

    |'{' statement* '}'                                #statement_lb
    | 'while' '(' exp ')' statement                   #statement_while
    | 'System.out.println' '(' exp ')' ';'            #statement_system
    | identifier '[' exp ']' '=' exp ';'              #statement_equalwithbra
    | identifier '=' exp ';'                          #statement_equal
    ;
ifst returns [value_attr = str(), type_attr = str()] : 'if' '(' exp ')' statement 'else' statement
;
exp returns [value_attr = str(), type_attr = str()]:
    exp '<'  exp                                           #exp_gt
    |exp ( binOperator ) exp                               #exp_binaryop
    | exp '+' exp                                           #exp_sum
    | exp '-' exp                                           #exp_minus
    | exp '*' exp                                           #exp_multi
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
identifier returns [value_attr = str(), type_attr = str()]: Identifier;

binOperator returns [value_attr = str(), type_attr = str()]: BinaryOperator;


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
    | [\uD800-\uDBFF] [\uDC00-\uDFFF]
    | ~[\u0000-\u007F\uD800-\uDBFF]
    ;


WS:                 [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT:            '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*    -> channel(HIDDEN);