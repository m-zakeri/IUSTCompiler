grammar Assignment4q4;


//parsing rules
program returns [value_attr = str(), type_attr = str()]:
    mainClass ( classDeclaration )* EOF;


mainClass returns [value_attr = str(), type_attr = str()]:
    'class' i1=identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' i2=identifier ')' '{' s1=statement '}' '}';


classDeclaration returns [value_attr = str(), type_attr = str()]:
    'class' i1=identifier ( 'extends' i2=identifier )? '{' ( v1=varDeclaration )* ( m1=methodDeclaration )* '}';


varDeclaration returns [value_attr = str(), type_attr = str()]:
    t1=type i1=identifier ';';


methodDeclaration returns [value_attr = str(), type_attr = str()]:
    'public' t1=type identifier '(' ( t2=type i1=identifier ( ',' type identifier )* )?
     ')' '{' ( varDeclaration )* ( statement )* 'return' e1=expression ';' '}';


type returns [value_attr = str(), type_attr = str()]:
    'int' '[' ']'  #typeint0
|	'boolean'      #boolean
|	'int'          #typeint
|	i1=identifier  #typeid
;


statement returns [value_attr = str(), type_attr = str()]:
    '{' ( statement )* '}'                                                                #st0
|	'if' '(' e1=expression ')' s1=statement 'else' s2=statement                           #st1
|	'while' '(' e1=expression ')' s1=statement                                            #st2
|	'System.out.println' '(' e1=expression ')' ';'                                        #st3
|	i1=identifier '=' e1=expression ';'                                                   #st4
|	i1=identifier '[' e1=expression ']' '=' e2=expression ';'                             #st5
;
expression returns [value_attr = str(), type_attr = str()]:
    e1=expression ( '&&' | '<' | '+' | '-' | '*' ) e2=expression                          #exp0
|	e1=expression '[' e2=expression ']'                                                   #exp1
|	e1=expression '.' 'length'                                                            #exp2
|	e1=expression '.' i1=identifier '(' ( e2=expression ( ',' e3=expression )* )? ')'     #exp3
|	INTEGER_LITERAL                                                                       #exp4
|	'true'                                                                                #exp5
|	'false'                                                                               #exp6
|	i1=identifier                                                                         #exp7
|	'this'                                                                                #exp8
|	'new' 'int' '[' e1=expression ']'                                                     #exp9
|	'new' i1=identifier '(' ')'                                                           #exp10
|	'!' e1=expression                                                                     #exp11
|	'(' e1=expression ')'                                                                 #exp12
;

identifier returns [value_attr = str(), type_attr = str()]:
    IDENTIFIER {};


//lexical rules
IDENTIFIER:
    [a-zA-Z][_0-9a-zA-Z]*;

INTEGER_LITERAL:
    [0-9]+;

WS:
    [ \n\t\r]+ -> skip;

LINE_COMMENT:
    '//' ~[\r\n]* -> skip;