/*
grammer AssignmentStatement4 (version 4)

@author: Morteza Zakeri, (http://webpages.iust.ac.ir/morteza_zakeri/)
@date: 20201029

- Compiler generator:   ANTLR4.x
- Target language(s):     Python3.x,


-Changelog:
-- v4.0
--- Generate intermediate representation (three addresses codes) with minimum number of 'temp' variables
-- v3.0
--- Add semantic rules to perform type checking
--- Add semantic routines to generate intermediate representation (three addresses codes)

- Reference: Compiler book by Dr. Saeed Parsa (http://parsa.iust.ac.ir/)
- Course website:   http://parsa.iust.ac.ir/courses/compilers/
- Laboratory website:   http://reverse.iust.ac.ir/

*/

grammar AssignmentStatement4;

@parser::members{
temp_counter = 0

def create_temp(self):
    self.temp_counter += 1
    return 'T' + str(self.temp_counter)

def remove_temp(self):
    self.temp_counter -= 1

def get_temp(self):
    return 'T' + str(self.temp_counter)

def is_temp(self, var:str):
    if var[0] == 'T':
        return True
    return False
}


start returns [value_attr = str(), type_attr = str()]: p=prog EOF  {$value_attr=$p.value_attr
$type_attr = $p.type_attr
print('Parsing was done!')
};

prog returns [value_attr = str(), type_attr = str()]: prog a=assign | a=assign       {$value_attr=$a.value_attr
$type_attr = $a.type_attr
print('----------')
};

assign returns [value_attr = str(), type_attr = str()]: ID ':=' e=expr (NEWLINE | EOF)      {$value_attr=$e.value_attr
$type_attr = $e.type_attr
print('Assignment value:', $ID.text, '=', $e.value_attr)
print('Assignment type:', $e.type_attr)
};

expr returns [value_attr = str(), type_attr = str()]:
    e=expr '+' t=term       {
if $e.type_attr != $t.type_attr:
    print('Semantic error4 in "+" operator: Inconsistent types!')
else:
    $type_attr = $t.type_attr
    if $t.type_attr=='float':
        $value_attr = str(float($e.value_attr) + float($t.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' + ', $t.value_attr)
    elif $t.type_attr=='int':
        $value_attr = str(int($e.value_attr) + int($t.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' + ', $t.value_attr)
    elif $t.type_attr=='str':
        if self.is_temp($e.value_attr):
            $value_attr = $e.value_attr
            if self.is_temp($t.value_attr):
                self.remove_temp()
        elif self.is_temp($t.value_attr):
            $value_attr = $t.value_attr
        else:
            $value_attr = self.create_temp()
        print($value_attr, ' = ', $e.value_attr, ' + ', $t.value_attr)
}

    | e=expr '-' t=term     {
if $e.type_attr != $t.type_attr:
    print('Semantic error3 in "-" operator: Inconsistent types!')
else:
    $type_attr = $t.type_attr
    if $t.type_attr=='float':
        $value_attr = str(float($e.value_attr) - float($t.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' - ', $t.value_attr)
    elif $t.type_attr == 'int':
        $value_attr = str(int($e.value_attr) - int($t.value_attr))
        print($value_attr, ' = ', $e.value_attr, ' - ', $t.value_attr)
    elif $t.type_attr=='str':
        if self.is_temp($e.value_attr):
            $value_attr = $e.value_attr
            if self.is_temp($t.value_attr):
                self.remove_temp()
        elif self.is_temp($t.value_attr):
            $value_attr = $t.value_attr
        else:
             $value_attr = self.create_temp()
        print($value_attr, ' = ', $e.value_attr, ' - ', $t.value_attr)
}

    | expr RELOP term

    | t=term        {$type_attr = $t.type_attr
$value_attr = $t.value_attr
};



term returns [value_attr = str(), type_attr = str()]:
    t=term '*' f=factor     {
if $t.type_attr != $f.type_attr:
    print('Semantic error2 in "*" operator: Inconsistent types!')
else:
    $type_attr = $f.type_attr
    if $f.type_attr=='float':
        $value_attr = str(float($t.value_attr) * float($f.value_attr))
        print($value_attr, ' = ', $t.value_attr, ' * ', $f.value_attr)
    elif $f.type_attr=='int':
        $value_attr = str(int($t.value_attr) * int($f.value_attr))
        print($value_attr, ' = ', $t.value_attr, ' * ', $f.value_attr)
    elif $f.type_attr=='str':
        if self.is_temp($t.value_attr):
            $value_attr = $t.value_attr
            if self.is_temp($f.value_attr):
                self.remove_temp()
        elif self.is_temp($f.value_attr):
            $value_attr = $f.value_attr
        else:
             $value_attr = self.create_temp()
        print($value_attr, ' = ', $t.value_attr, ' * ', $f.value_attr)
}

    | t=term '/' f=factor       {
if $t.type_attr != $f.type_attr:
    print('Semantic error1 in "/" operator: Inconsistent types!')
else:
    $type_attr = $f.type_attr
    if $f.type_attr=='float':
        $value_attr = str(float($t.value_attr) / float($f.value_attr))
        print($value_attr, ' = ', $t.value_attr, ' / ', $f.value_attr)
    elif $f.type_attr=='int':
        $value_attr = str(int(int($t.value_attr) / int($f.value_attr)))
        print($value_attr, ' = ', $t.value_attr, ' / ', $f.value_attr)
    elif $f.type_attr=='str':
        if self.is_temp($t.value_attr):
            $value_attr = $t.value_attr
            if self.is_temp($f.value_attr):
                self.remove_temp()
        elif self.is_temp($f.value_attr):
            $value_attr = $f.value_attr
        else:
            $value_attr = self.create_temp()
        print($value_attr, ' = ', $t.value_attr, ' / ', $f.value_attr)
}

    | f=factor      {$type_attr = $f.type_attr
$value_attr = $f.value_attr
}
    ;


factor returns [value_attr = str(), type_attr = str()]:
    '(' e=expr ')'        {$type_attr = $e.type_attr
$value_attr = $e.value_attr
}

    | ID        {$type_attr = 'str'
$value_attr = $ID.text
}

    | n=number        {$type_attr = $n.type_attr
$value_attr = $n.value_attr
    }
    ;


number returns [value_attr = str(), type_attr = str()]:
    INT     {$value_attr = $INT.text
$type_attr = 'int'
}
    |FLOAT      {$value_attr = $FLOAT.text
$type_attr = 'float'
}
    ;



/* Lexical Rules */
INT: DIGIT+ ;

FLOAT:
    DIGIT+ '.' DIGIT*
    | '.' DIGIT+
    ;



String:
    '"' (ESC|.)*? '"'
    ;


ID:
    LETTER(LETTER|DIGIT)* ;


RELOP: '<=' | '<' ;


fragment
        DIGIT: [0-9] ;
fragment
        LETTER: [a-zA-Z] ;
fragment
        ESC: '\\"' | '\\\\' ;


WS: [ \t\r]+ -> skip ;
NEWLINE: '\n';
