grammar Threecode;

@parser::members{
temp_counter = 0
label_counter = 0
def create_temp(self):
    self.temp_counter += 1
    return 'T' + str(self.temp_counter)

def remove_temp(self):
    self.temp_counter -= 1

def create_label(self):
    self.label_counter += 1
    return 'L' + str(self.label_counter)

def get_temp(self):
    return 'T' + str(self.temp_counter)

def is_temp(self, var:str):
    if var[0] == 'T':
        return True
    return False
}

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

    |'{' s=statement* '}' {$value_attr = $s.value_attr
$value_attr = $s.value_attr}                      #statement_lb
    | 'while' '(' exp ')' statement                   #statement_while
    | 'System.out.println' '(' exp ')' ';'            #statement_system
    | identifier '[' exp ']' '=' exp ';'              #statement_equalwithbra
    | identifier '=' exp ';'                          #statement_equal
    ;
ifst returns [value_attr = str(), type_attr = str()] : 'if' '(' exp ')' statement 'else' statement
;
exp returns [value_attr = str(), type_attr = str()]:
    exp '<'  exp
    |exp ( binOperator ) exp
    |e=exp '+' ex=exp  {
if $e.type_attr != $ex.type_attr:
    print('Semantic error4 in "OP" operator: Inconsistent types!')
else:
    $type_attr = $ex.type_attr
    if $ex.type_attr=='float':
        $value_attr = str(float($e.value_attr) + float($ex.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' + ', $ex.value_attr)
    elif $ex.type_attr=='int':
        $value_attr = str(int($e.value_attr) + int($ex.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' + ', $ex.value_attr)
    elif $ex.type_attr=='str':
        if self.is_temp($e.value_attr):
            $value_attr = $e.value_attr
            if self.is_temp($ex.value_attr):
                self.remove_temp()
        elif self.is_temp($ex.value_attr):
            $value_attr = $ex.value_attr
        else:
            $value_attr = self.create_temp()
        print($value_attr, ' = ', $e.value_attr, ' + ', $ex.value_attr)
              }

        |e=exp '-' ex=exp     {
if $e.type_attr != $ex.type_attr:
    print('Semantic error3 in "-" operator: Inconsistent types!')
else:
    $type_attr = $ex.type_attr
    if $ex.type_attr=='float':
        $value_attr = str(float($e.value_attr) - float($ex.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' - ', $ex.value_attr)
    elif $ex.type_attr == 'int':
        $value_attr = str(int($e.value_attr) - int($ex.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' - ', $ex.value_attr)
    elif $ex.type_attr=='str':
        if self.is_temp($e.value_attr):
            $value_attr = $e.value_attr
            if self.is_temp($ex.value_attr):
                self.remove_temp()
        elif self.is_temp($ex.value_attr):
            $value_attr = $ex.value_attr
        else:
             $value_attr = self.create_temp()
        print($value_attr, ' = ', $e.value_attr, ' - ', $ex.value_attr)
}
         |e=exp '*' ex=exp     {
if $e.type_attr != $ex.type_attr:
    print('Semantic error2 in "*" operator: Inconsistent types!')
else:
    $type_attr = $ex.type_attr
    if $ex.type_attr=='float':
        $value_attr = str(float($e.value_attr) * float($ex.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' * ', $ex.value_attr)
    elif $ex.type_attr == 'int':
        $value_attr = str(int($e.value_attr) * int($ex.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' * ', $ex.value_attr)
    elif $ex.type_attr=='str':
        if self.is_temp($e.value_attr):
            $value_attr = $e.value_attr
            if self.is_temp($ex.value_attr):
                self.remove_temp()
        elif self.is_temp($ex.value_attr):
            $value_attr = $ex.value_attr
        else:
             $value_attr = self.create_temp()
        print($value_attr, ' = ', $e.value_attr, ' * ', $ex.value_attr)
}
    |e=exp '&&' ex=exp     {
if $e.type_attr != $ex.type_attr:
    print('Semantic error3 in "&&" operator: Inconsistent types!')
else:
    $type_attr = $ex.type_attr
    if $ex.type_attr=='float':
        $value_attr = str(float($e.value_attr) & float($ex.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' && ', $ex.value_attr)
    elif $ex.type_attr == 'int':
        $value_attr = str(int($e.value_attr) & int($ex.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' && ', $ex.value_attr)
    elif $ex.type_attr=='str':
        if self.is_temp($e.value_attr):
            $value_attr = $e.value_attr
            if self.is_temp($ex.value_attr):
                self.remove_temp()
        elif self.is_temp($ex.value_attr):
            $value_attr = $ex.value_attr
        else:
             $value_attr = self.create_temp()
        print($value_attr, ' = ', $e.value_attr, ' && ', $ex.value_attr)
}

    | exp '[' exp ']'
    | exp '.' 'length'
    | exp '.' identifier '(' ( exp ( ',' exp )* )? ')'
    | identifier
    | Integer
    | 'true'
    | 'false'
    | 'this'
    | New IntType '[' exp ']'
    | New identifier '(' ')'
    | '!' exp
    | '(' exp ')'
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