grammar Assignment4q3;

@parser::members{
label_counter = 0
temp_counter = 0
def create_temp(self):
    self.temp_counter += 1
    return 'T' + str(self.temp_counter)
def remove_temp(self):
    self.temp_counter -= 1
def get_temp(self):
    return 'T' + str(self.temp_counter)
def create_label(self):
    self.label_counter += 1
    return 'L' + str(self.label_counter)
}


//parsing rules
program returns [value_attr = str(), type_attr = str()]:
    m=mainClass{$value_attr = $m.value_attr} ( c=classDeclaration {$value_attr = $value_attr + $c.value_attr})* EOF
{
print($value_attr)
};


mainClass returns [value_attr = str(), type_attr = str()]:
    'class' i1=identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' i2=identifier ')' '{' st=statement '}' '}'
{$value_attr = $st.value_attr
};


classDeclaration returns [value_attr = str(), type_attr = str()]:
    'class' i1=identifier ( 'extends' i2=identifier )? '{' ( v1=varDeclaration )*
     ( m1=methodDeclaration {$value_attr = $value_attr + $m1.value_attr})* '}';


varDeclaration returns [value_attr = str(), type_attr = str()]:
    t1=type i1=identifier ';';


methodDeclaration returns [value_attr = str(), type_attr = str()]:
    'public' t1=type identifier '(' ( t2=type i1=identifier ( ',' type identifier )* )?
     ')' '{' ( varDeclaration )* ( st=statement {$value_attr = $value_attr + $st.value_attr})* 'return' e1=expression
      {$value_attr = $value_attr + '\n' + 'push ' + $e1.value_attr + '\n' + 'RET' + '\n'} ';' '}';


type returns [value_attr = str(), type_attr = str()]:
    'int' '[' ']'
|	'boolean'
|	'int'
|	i1=identifier;


statement returns [value_attr = str(), type_attr = str()]:
    '{' ( st=statement {$value_attr = $value_attr + $st.value_attr})* '}'
|	'if' '(' e1=expression ')' s1=statement 'else' s2=statement
{l_true = self.create_label()
l_after = self.create_label()
code = 'if ' + $e1.value_attr + 'goto ' + l_true + '\n'
code += $s2.value_attr + '\n'
code += 'goto ' + l_after + '\n'
code += l_true + $s1.value_attr + '\n'
code += l_after + ': '
$value_attr = code + '\n'
}
|	'while' '(' e1=expression ')' s1=statement
{l_while = self.create_label()
l_st = self.create_label()
l_after = self.create_label()
code = l_while + ' : if ' + $e1.value_attr + ' goto ' + l_st + '\n'
code += 'goto ' + l_after + '\n'
code += l_st + ':' + $s1.value_attr + '\n'
code += 'goto ' + l_while + '\n'
code += l_after + ': '
$value_attr = code + '\n'
}
|	'System.out.println' '(' e1=expression ')' ';'
{t = self.create_temp()
$value_attr = t + ' = ' + $e1.value_attr + '\n'
$value_attr += 'print(' + t + ')' + '\n'
}
|	i1=identifier '=' e1=expression ';'
{t = self.create_temp()
$value_attr = t + ' = ' + $e1.value_attr + '\n'
$value_attr += $i1.value_attr + ' = ' + t + '\n'
}
|	i1=identifier '[' e1=expression ']' '=' e2=expression ';'
{t1 = self.create_temp()
$value_attr = t1 + ' = ' + $e1.value_attr + '\n'
t2 = self.create_temp()
$value_attr += t2 + ' = ' + $e1.value_attr + '\n'
$value_attr += $i1.value_attr + '[' + t1 + ']' + ' = ' + t2 + '\n'
};

expression returns [value_attr = str(), type_attr = str(), amount_attr = str()]:
|   e1=expression ('&&') e2=expression {$value_attr = $e1.value_attr +'&&' + $e2.value_attr + '\n'}
|   e1=expression ('<') e2=expression {$value_attr = $e1.value_attr + '<' + $e2.value_attr + '\n'}
|   e1=expression ('+') e2=expression {$value_attr = $e1.value_attr + '+' + $e2.value_attr + '\n'}
|   e1=expression ('-') e2=expression {$value_attr = $e1.value_attr + '-' + $e2.value_attr + '\n'}
|   e1=expression ('*') e2=expression {$value_attr = $e1.value_attr + '*' + $e2.value_attr + '\n'}
|	e1=expression '[' e2=expression ']'
{$value_attr = $e1.value_attr + '[' + $e2.value_attr + ']' + '\n'
}
|	e1=expression '.' 'length'
{$value_attr = 'len ' + '(' + $e1.value_attr + ')' + '\n'
}
|	e1=expression '.' i1=identifier '(' ( e2=expression {$value_attr = 'push ' + $e2.value_attr + '\n'} ( ',' e3=expression
{$value_attr = $value_attr + 'push ' + $e3.value_attr + '\n'} )* )? ')'
{code = 'call ' + $e1.value_attr + $i1.value_attr + '\n'}
{code += 'pop params' + '\n'}
{$value_attr = $value_attr + code + '\n'}
|	INTEGER_LITERAL
{$value_attr = $INTEGER_LITERAL.text
}
|	'true'
{$value_attr = 'true'
}
|	'false'
{$value_attr = 'false'
}
|	i1=identifier
{$value_attr = $i1.value_attr
}
|	'this'
{$value_attr = 'this'
}
|	'new' 'int' '[' e1=expression ']'
{$value_attr = $e1.value_attr
}
|	'new' i1=identifier '(' ')'
{$value_attr = $i1.value_attr
}
|	'!' e1=expression
{$value_attr = 'not ' + $e1.value_attr
}
|	'(' e1=expression ')'
{$value_attr = $e1.value_attr
};


identifier returns [value_attr = str(), type_attr = str()]:
    IDENTIFIER {$value_attr = $IDENTIFIER.text};


//lexical rules
IDENTIFIER:
    [a-zA-Z][_0-9a-zA-Z]*;

INTEGER_LITERAL:
    [0-9]+;

WS:
    [ \t\r\n]+ -> skip;

LINE_COMMENT:
    '//' ~[\r\n]* -> skip;