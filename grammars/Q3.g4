
grammar Q3;

@parser :: members {

temp_counter = 0

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
    return 'L' + str(self.tmp_counter)
}


program returns [value_attr = str(), type_attr = str()]	:	m = mainClass ( c = classDeclaration )* EOF
{print('Parsing was done!')}
;
mainClass returns [value_attr = str(), type_attr = str()]	:	'class' IDENTIFIER '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' IDENTIFIER ')' '{' statement '}' '}' ;
classDeclaration returns [value_attr = str(), type_attr = str()]	:	'class' IDENTIFIER ( 'extends' IDENTIFIER )? '{' ( varDeclaration )* ( methodDeclaration )* '}' ;
varDeclaration returns [value_attr = str(), type_attr = str()]	:	type IDENTIFIER ';' ;
methodDeclaration returns [value_attr = str(), type_attr = str()]	:	'public' type IDENTIFIER '(' ( type IDENTIFIER ( ',' type IDENTIFIER )* )? ')' '{' ( varDeclaration )* ( statement )* 'return' expression ';' '}' ;
type returns [value_attr = str(), type_attr = str()]	:	'int' '[' ']'
|	'boolean'
|	'int'
|	IDENTIFIER
;
statement returns [value_attr = str(), type_attr = str()]	:	'{' ( statement )* '}'
|	'if' '(' expression ')' statement 'else' statement
|	'while' '(' expression ')' statement
|	'System.out.println' '(' expression ')' ';'
|	IDENTIFIER '=' expression ';'
|	IDENTIFIER '[' expression ']' '=' expression ';'
|   expr
;
expression returns [value_attr = str(), type_attr = str()] :	expression ( '&&' | '<'  ) expression
|	expression '[' expression ']'
|	expression '.' 'length'
|	expression '.' IDENTIFIER '(' ( expression ( ',' expression )* )? ')'
|	INTEGER_LITERAL
|	'true'
|	'false'
|	IDENTIFIER
|	'this'
|	'new' 'int' '[' expression ']'
|	'new' IDENTIFIER '(' ')'
|	'!' expression
|	'(' expression ')'
|   expr
;
//        -------------------------------------

expr returns [value_attr = str(), type_attr = str()]:
    e=expr ' + ' t=term
    {if $e.type_attr != $t.type_attr:}
    {   print('Semantic error4 in "+" operator: Inconsistent types!')}
    {else:}
//    {   print("biatchchchch)}
    {   $type_attr = $t.type_attr}
    {   if $t.type_attr=='float':}
    {       $value_attr = str(float($e.value_attr) + float($t.value_attr))}
    {       print($value_attr, ' = ', $e.value_attr, ' + ', $t.value_attr)}
    {   elif $t.type_attr=='int':}
    {       $value_attr = str(int($e.value_attr) + int($t.value_attr))}
    {       print($value_attr, ' = ', $e.value_attr, ' + ', $t.value_attr)}
    {   elif $t.type_attr=='str':}
    {       if self.is_temp($e.value_attr):}
    {           $value_attr = $e.value_attr}
    {           if self.is_temp($t.value_attr):}
    {               self.remove_temp()}
    {       elif self.is_temp($t.value_attr):}
    {           $value_attr = $t.value_attr}
    {       else:}
    {           $value_attr = self.create_temp()}
    {       print($value_attr, ' = ', $e.value_attr, ' + ', $t.value_attr)}
    | e=expr ' - ' t=term
    {if $e.type_attr != $t.type_attr:}
    {   print('Semantic error3 in "-" operator: Inconsistent types!')}
    {else:}
    {   $type_attr = $t.type_attr}
    {   if $t.type_attr=='float':}
    {       $value_attr = str(float($e.value_attr) - float($t.value_attr))}
    {       print($value_attr, ' = ', $e.value_attr, ' - ', $t.value_attr)}
    {   elif $t.type_attr == 'int':}
    {       $value_attr = str(int($e.value_attr) - int($t.value_attr))}
    {       print($value_attr, ' = ', $e.value_attr, ' - ', $t.value_attr)}
    {   elif $t.type_attr=='str':}
    {       if self.is_temp($e.value_attr):}
    {           $value_attr = $e.value_attr}
    {           if self.is_temp($t.value_attr):}
    {               self.remove_temp()}
    {       elif self.is_temp($t.value_attr):}
    {           $value_attr = $t.value_attr}
    {       else:}
    {           $value_attr = self.create_temp()}
    {       print($value_attr, ' = ', $e.value_attr, ' - ', $t.value_attr)}

    | expr RELOP term

    | t=term        {$type_attr = $t.type_attr}
{$value_attr = $t.value_attr}
;



term returns [value_attr = str(), type_attr = str()]:
    t=term ' * ' f=factor
    {if $t.type_attr != $f.type_attr:}
    {   print('Semantic error2 in "*" operator: Inconsistent types!')}
    {else:}
    {   $type_attr = $f.type_attr}
    {   if $f.type_attr=='float':}
    {       $value_attr = str(float($t.value_attr) * float($f.value_attr))}
    {       print($value_attr, ' = ', $t.value_attr, ' * ', $f.value_attr)}
    {   elif $f.type_attr=='int':}
    {       $value_attr = str(int($t.value_attr) * int($f.value_attr))}
    {       print($value_attr, ' = ', $t.value_attr, ' * ', $f.value_attr)}
    {   elif $f.type_attr=='str':}
    {       if self.is_temp($t.value_attr):}
    {           $value_attr = $t.value_attr}
    {           if self.is_temp($f.value_attr):}
    {               self.remove_temp()}
    {       elif self.is_temp($f.value_attr):}
    {           $value_attr = $f.value_attr}
    {       else:}
    {           $value_attr = self.create_temp()}
    {       print($value_attr, ' = ', $t.value_attr, ' * ', $f.value_attr)}

    | t=term ' / ' f=factor
    {if $t.type_attr != $f.type_attr:}
    {   print('Semantic error2 in "/" operator: Inconsistent types!')}
    {else:}
    {   $type_attr = $f.type_attr}
    {   if $f.type_attr=='float':}
    {       $value_attr = str(float($t.value_attr) * float($f.value_attr))}
    {       print($value_attr, ' = ', $t.value_attr, ' / ', $f.value_attr)}
    {   elif $f.type_attr=='int':}
    {       $value_attr = str(int($t.value_attr) * int($f.value_attr))}
    {       print($value_attr, ' = ', $t.value_attr, ' / ', $f.value_attr)}
    {   elif $f.type_attr=='str':}
    {       if self.is_temp($t.value_attr):}
    {           $value_attr = $t.value_attr}
    {           if self.is_temp($f.value_attr):}
    {               self.remove_temp()}
    {       elif self.is_temp($f.value_attr):}
    {           $value_attr = $f.value_attr}
    {       else:}
    {           $value_attr = self.create_temp()}
    {       print($value_attr, ' = ', $t.value_attr, ' * ', $f.value_attr)}

    | f=factor      {$type_attr = $f.type_attr}
{$value_attr = $f.value_attr}
    ;


factor returns [value_attr = str(), type_attr = str()]:
    '(' e=expr ')'        {$type_attr = $e.type_attr}
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

INTEGER_LITERAL:    INT
               |    FLOAT
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

Number
    : [0-9]Number
    | '.' Number
    | [0-9]
    ;
//    :LETTER(LETTER|DIGIT)* ;
IDENTIFIER:	[a-zA-Z_][a-zA-Z0-9_]* ;
COMMENT   : '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' .*? '\r'? '\n' -> skip;