
grammar Q3;

@parser :: members {

temp_counter = 0
label_counter = 0
is_equality = False

def create_temp(self):
    self.temp_counter += 1
    return 'T' + str(self.temp_counter)

def remove_temp(self) :
    self.temp_counter -= 1

def is_temp(self, var:str):
    if var[0] == 'T':
        return True
    return False

def create_label(self):
    self.label_counter += 1
    return 'L' + str(self.label_counter)
}


program returns [value_attr = str(), type_attr = str()]	:	m = mainClass ( c = classDeclaration )* EOF
{print('Parsing was done!')}
;
mainClass returns [value_attr = str(), type_attr = str()]	:	'class' IDENTIFIER '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' IDENTIFIER ')' '{' statement '}' '}' ;
classDeclaration returns [value_attr = str(), type_attr = str()]	:	'class' IDENTIFIER ( 'extends' IDENTIFIER )? '{' ( varDeclaration )* ( methodDeclaration )* '}' ;
varDeclaration returns [value_attr = str(), type_attr = str()]	:	t=type IDENTIFIER ';' ;
methodDeclaration returns [value_attr = str(), type_attr = str()]	:	'public' type IDENTIFIER '(' ( type IDENTIFIER ( ',' type IDENTIFIER )* )? ')' '{' ( varDeclaration )* ( statement )* 'return' expression ';' '}'
 {print('-----------------------')}
 ;
type returns [value_attr = str(), type_attr = str()]
:	'int' '[' ']'
|	'boolean'
|	'int'
|	IDENTIFIER
;
statement returns [value_attr = str(), type_attr = str()]	:	'{' ( statement )* '}'
|	'if' '(' cond=expression ')' e1 = job1 'else' e2 = job2
    {print('if ' , $cond.value_attr,  ': goto' , self.create_label()  )}
    {print('goto ' , self.create_label() )}
{self.is_equality = False}
|	'while' '(' expression ')' statement
{self.is_equality = False}
|	'System.out.println' '(' expression ')' ';'
{self.is_equality = False}
|	IDENTIFIER '=' e = expression ';'
        {$value_attr = $IDENTIFIER.text}
        {self.is_equality = True}
        {if(len(str($e.value_attr)) > 0 ):}
        {   print( $IDENTIFIER.text, ' = ' , str($e.value_attr))}
|	IDENTIFIER '[' expression ']' '=' expression ';'
{self.is_equality = False}
;

job1
    :statement job1
    |statement {}
    ;

job2
    :statement job1
    |statement {}
    ;



expression returns [value_attr = str(), type_attr = str()] :	expression ( '&&' | '<' ) expression
|	array = expression '[' index =  expression ']'
    {$value_attr = str($array.value_attr) + '[' + str($index.value_attr) + ']' }
|	expression '.' 'length'
|	expression '.' IDENTIFIER '(' ( expression ( ',' expression )* )? ')'

|	n = number {$type_attr = $n.type_attr}
           {$value_attr = $n.value_attr}
|	'true' {$value_attr = 'true'}
|	'false' {$value_attr = 'false'}
|	IDENTIFIER {$type_attr = 'str'}
{$value_attr = $IDENTIFIER.text}
|	'this'
|	'new' 'int' '[' expression ']'
|	'new' IDENTIFIER '(' ')'
|	'!' expression
|	'(' expression ')'
|   t = expression '-' f=  expression
    {$value_attr = str($t.value_attr) + ' - ' + str($f.value_attr)}
    {if(self.is_equality == False):}
    {   $value_attr = self.create_temp()}
    {   print($value_attr , '=' , str($t.value_attr) , '-' , str($f.value_attr) )}
|   t = expression '+'  f = expression
    {$value_attr = str($t.value_attr) + ' + ' + str($f.value_attr)}
    {if(self.is_equality == False):}
    {   $value_attr = self.create_temp()}
    {   print($value_attr , '=' , str($t.value_attr) , '+' , str($f.value_attr) )}
|   expression ' * '  expression
    {$value_attr = str($t.value_attr) + ' * ' + str($f.value_attr)}
    {if(self.is_equality == False):}
    {   $value_attr = self.create_temp()}
    {   print($value_attr , '=' , str($t.value_attr) , '*' , str($f.value_attr) )}
|    expression ' / '  expression
    {$value_attr = str($t.value_attr) + ' / ' + str($f.value_attr)}
    {if(self.is_equality == False):}
    {   $value_attr = self.create_temp()}
    {   print($value_attr , '=' , str($t.value_attr) , '-' , str($f.value_attr) )}
;
//        -------------------------------------




factor returns [value_attr = str(), type_attr = str()]:
    '(' e=expression ')'        {$type_attr = $e.type_attr}
{$value_attr = $e.value_attr}

    | ID        {$type_attr = 'str'}
{$value_attr = $ID.text}

    | n=number        {$type_attr = $n.type_attr}
{$value_attr = $n.value_attr}
    ;


number returns [value_attr = str(), type_attr = str()]:
    INT     {$value_attr = $INT.text}
{$type_attr = 'int'}
    |FLOAT      {$value_attr = $FLOAT.text}
{$type_attr = 'float'}
    ;

INT: DIGIT+ ;

FLOAT:
    DIGIT+ '.' DIGIT*
    | '.' DIGIT+
    ;



String:
    '"' (ESC|.)*? '"'
    ;


//ID:
//    LETTER(LETTER|DIGIT)* ;


RELOP: '<=' | '<' ;


fragment
        DIGIT: [0-9] ;
fragment
        LETTER: [a-zA-Z] ;
fragment
        ESC: '\\"' | '\\\\' ;


WS: [ \t\r\n]+ -> skip ;
NEWLINE: '\n';

//-----------------------------------------


CLASS : 'class' ;
New : 'new' ;
StartStatement : '{' ;
EndtStatement : '}' ;
Semicolon : ';' ;
Public : 'public' ;
Static : 'static' ;
Void : 'void' ;

//Number
//    : [0-9]Number
//    | '.' Number
//    | [0-9]
//    ;
//    :LETTER(LETTER|DIGIT)* ;
IDENTIFIER:	[a-zA-Z_][a-zA-Z0-9_]* ;
COMMENT   : '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' .*? '\r'? '\n' -> skip;