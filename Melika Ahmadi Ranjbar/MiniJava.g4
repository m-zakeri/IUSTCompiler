// Parser section
grammar MiniJava;

program returns[value_attr = str(), type_attr = str()]:
    mainClass (classDeclaration)* EOF;

mainClass returns[value_attr = str(), type_attr = str()]:
    Class mainClassEnter;

mainClassEnter returns[value_attr = str(), type_attr = str()]:
    identifier BraketOpen mainClassBody BraketClose;

mainClassBody returns[value_attr = str(), type_attr = str()]:
    Public Static Void Main ParOpen String '[' ']' identifier ParClose BraketOpen statement BraketClose;

classDeclaration returns[value_attr = str(), type_attr = str()]:
    Class identifier ('extends' identifier) ? BraketOpen (varDeclaration)* (methodDeclaration)* BraketClose;

varDeclaration returns[value_attr = str(), type_attr = str()]:
    kind identifier ';';

methodDeclaration returns[value_attr = str(), type_attr = str()]:
    Public kind identifier ParOpen ( kind identifier ( ',' kind identifier )* ) ? ParClose BraketOpen (varDeclaration)* (statement)* Return expression ';' BraketClose;

kind returns[value_attr = str(), type_attr = str()]:
    Int '[' ']' #array_int
    | Boolean   #bool
    | Int       #int
    | identifier #id
    ;

statement returns[value_attr = str(), type_attr = str()]:
    BraketOpen (statement)* BraketClose                         #braket_statement
    | If ParOpen expression ParClose statement Else statement   #if_statement
    | While ParOpen expression ParClose statement               #while_statement
    | 'System.out.println' ParOpen expression ParClose ';'      #print
    | identifier '=' expression ';'                             #equal_statement
    | identifier '[' expression ']' '=' expression ';'          #equal_array_statement
    ;

expression returns[value_attr = str(), type_attr = str()]:
    expression ( operations ) expression                                   #operations_expression
    | expression '[' expression ']'                                                     #array_expression
    | expression Dot 'length'                                                           #length_expression
    | expression Dot identifier ParOpen ( expression ( ',' expression )* ) ? ParClose   #dot_par_expression
    | IntegerLiteral                                                                    #number
    | KeyWords                                                                          #keywords
    | identifier                                                                        #word
    | New Int '[' expression ']'                                                        #new_array_expression
    | New identifier ParOpen ParClose                                                   #new_identifier
    | '!' expression                                                                    #not_expression
    | ParOpen expression ParClose                                                       #in_par_expression
    ;

identifier returns[value_attr = str(), type_attr = str()]:
    Identifier;

operations:
    Operations;

// Lexical section

Class: 'class';
Public: 'public';
Static: 'static';
Void: 'void';
Main: 'main';
String: 'String';
BraketOpen: '{';
BraketClose: '}';
ParOpen: '(';
ParClose: ')';
Int: 'int';
New: 'new';
Return: 'return';
If: 'if';
Boolean: 'boolean';
While: 'while';
Else: 'else';
Dot: '.';

Identifier: Letter LetterOrDigit*;

KeyWords:
    'true'
    | 'false'
    | 'this';

Operations:
    '&&' | '<' | '+' | '-' | '*';

IntegerLiteral:
    [0-9] [0-9_]*;

fragment Letter
    : [a-zA-Z$_]
    | ~[\u0000-\u007F\uD800-\uDBFF]
    | [\uD800-\uDBFF] [\uDC00-\uDFFF]
    ;

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;

COMMENT:            '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*    -> channel(HIDDEN);
WS:                 [ \t\r\n\u000C]+ -> channel(HIDDEN);