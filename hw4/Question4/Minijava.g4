grammar Minijava;

start returns [value_attr = str(), type_attr = str()]:   mainClass classDeclaration* EOF;

mainClass returns [value_attr = str(), type_attr = str()]:
   'class' identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier ')' '{' statement '}' '}';
classDeclaration  returns [value_attr = str(), type_attr = str()]:
   'class' identifier ( 'extends' identifier )? '{' varDeclaration* methodDeclaration* '}';
varDeclaration  returns [value_attr = str(), type_attr = str()]:
   typ identifier ';';
methodDeclaration  returns [value_attr = str(), type_attr = str()]:
   'public' typ identifier '(' (param (',' param)*)? ')' '{' varDeclaration* statement* 'return' expression ';' '}';

typ returns [value_attr = str(), type_attr = str()]:
    'int'                   #typ_int
|    'int' '[' ']'          #typ_int_array
|    'boolean'              #typ_boolean
|    identifier            #typ_identifier
;

statement returns [value_attr = str(), type_attr = str()]:
'{' statement* '}'                                                  #statement_1
|    'if' '(' expression ')' statement 'else' statement             #statement_2
|    'while' '(' expression ')' statement                           #statement_3
|    'System.out.println' '(' expression ')' ';'                    #statement_4
|    identifier '=' expression ';'                                  #statement_5
|    identifier '[' expression ']' '=' expression ';'               #statement_6
;

expression returns [value_attr = str(), type_attr = str()]:
    expression binaryOperator expression                                            #expression_1
|    expression '[' expression ']'                                                  #expression_2
|    expression '.length'                                                           #expression_3
|    expression '.' identifier '(' ( expression ( ',' expression )* )? ')'          #expression_4
|    IntegerLiteral                                                                 #expression_5
|    'true'                                                                         #expression_6
|    'false'                                                                        #expression_7
|    identifier                                                                     #expression_8
|    'this'                                                                         #expression_9
|    'new' 'int' '[' expression ']'                                                 #expression_10
|    'new' identifier '(' ')'                                                       #expression_11
|    '!' expression                                                                 #expression_12
|    '(' expression ')'                                                             #expression_13
;

param  returns [value_attr = str(), type_attr = str()]:  typ identifier;
binaryOperator  returns [value_attr = str(), type_attr = str()]:
'&&'        #binaryOperator_and
| '<'       #binaryOperator_smaller
| '+'       #binaryOperator_plus
| '-'       #binaryOperator_minus
| '*'       #binaryOperator_multiple
;

identifier         returns [value_attr = str(), type_attr = str()]:   Letter;
Letter :  [a-zA-Z_][0-9a-zA-Z_]*;
IntegerLiteral      :   '0' | [1-9][0-9]*;

WhiteSpace          :   [ \r\t\n]+ -> skip;
MULTILINE_COMMENT   :   '/*' .*? '*/' -> skip;
LINE_COMMENT        :   '//' .*? '\n' -> skip;
