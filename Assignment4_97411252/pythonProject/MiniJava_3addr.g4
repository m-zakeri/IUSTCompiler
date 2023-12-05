grammar MiniJava_3addr;

@parser::members{
temp_counter = 0
label_counter = 0

def create_temp(self):
    self.temp_counter += 1
    return 'T' + str(self.temp_counter)

def is_temp(self, value:str):
    if value is None:
        return False
    return value[0] == 'T'

def remove_temp(self):
    self.temp_counter -= 1

def reset_temp(self):
    self.temp_counter = 0

def get_temp(self, *args):
    val = ''
    value_is_set = False
    for t in args:
        if self.is_temp(t):
            if value_is_set is True:
                self.remove_temp()
            else:
                val = t
                value_is_set = True
    if value_is_set is False:
        val = self.create_temp()
    return val

def create_label(self):
    self.label_counter += 1
    return '<L' + str(self.label_counter) + '>'
}

program
:   mainClass (classDeclaration)* EOF
;
mainClass
:   'class' IDENTIFIER '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' IDENTIFIER ')' '{' s1=statement '}' '}'
{print('main:\nBeginFunc\n' + $s1.prnt + 'EndFunc\n')}
{self.reset_temp()}
;
classDeclaration
:   'class' IDENTIFIER ( 'extends' IDENTIFIER )? '{' ( varDeclaration )* ( methodDeclaration )* '}'
;
varDeclaration
:   type1 IDENTIFIER ';'
;
methodDeclaration
:   'public' type1 IDENTIFIER '(' ( type1 IDENTIFIER ( ',' type1 IDENTIFIER )* )? ')' '{' ( varDeclaration )* 'return' expression ';' '}'
|   'public' type1 n=IDENTIFIER '(' ( type1 IDENTIFIER ( ',' type1 IDENTIFIER )* )? ')' '{' ( varDeclaration )* ss1=statements 'return' expression ';' '}'
{print($n.text + ':\nBeginFunc\n' + $ss1.prnt + 'EndFunc\n')}
{self.reset_temp()}
;
type1
:	'int' '[' ']'
|	'boolean'
|	'int'
|	IDENTIFIER
;
statements returns[prnt=str()]
:   s1=statement ss1=statements {$prnt = $s1.prnt + $ss1.prnt}
|   s1=statement                {$prnt = $s1.prnt}
;
statement returns[prnt=str()]
:   '{' '}'
|   '{' ss1=statements '}'  {$prnt = $ss1.prnt}
|	'if' '(' e1=expression ')' s1=statement 'else' s2=statement
{
label1 = self.create_label()
label2 = self.create_label()
$prnt = $e1.prnt + 'if(' + $e1.val + ') goto ' + label1 + '\n' + $s2.prnt + 'goto ' + label2 + '\n' + label1 + ':\n' + $s1.prnt + label2 + ':\n'
}
|	'while' '(' e1=expression ')' s1=statement
{
label1 = self.create_label()
label2 = self.create_label()
$prnt = 'goto ' + label1 + '\n' + label2 + ':\n' + $s1.prnt + label1 + ':\n' + $e1.prnt + 'if(' + $e1.val + ') goto ' + label2 + '\n'
}
|	'System.out.println' '(' e1=expression ')' ';'{$prnt = $e1.prnt + 'Push ' + $e1.val + '\nCall System.out.println,1\n'}
|	IDENTIFIER '=' e1=expression ';'    {$prnt = $e1.prnt + $IDENTIFIER.text + ' = ' + $e1.val + ';\n'}
|	IDENTIFIER '[' e1=expression ']' '=' e2=expression ';'  {$prnt = $e1.prnt + $e2.prnt + $IDENTIFIER.text + '[' + $e1.val + '] = ' + $e2.val + ';\n'}
;
exps returns[val=str(), prnt=str()]
:   e1=expression ',' es1=exps
{$val = 'Push ' + $e1.val + '\n' + $es1.val}
{$prnt = $e1.prnt + $es1.prnt}
|   e1=expression
{$val = 'Push ' + $e1.val + '\n'}
{$prnt = $e1.prnt}
;
expression returns[val=str(), prnt=str()]
:   e1=expression op=( '&&' | '<' | '+' | '-' | '*' ) e2=expression
{$val = self.get_temp($e1.val, $e2.val)}
{prev_prnt = $e1.prnt + $e2.prnt}
{$prnt = prev_prnt + $val + ' = ' + $e1.val + ' ' + $op.text + ' ' + $e2.val + '\n'}
|	e1=expression '[' e2=expression ']'
{$val = self.get_temp($e1.val, $e2.val)}
{prev_prnt = $e1.prnt + $e2.prnt}
{$prnt = prev_prnt + $val + ' = ' + $e1.val + '[' + $e2.val + ']\n'}
|	e1=expression '.' 'length'
{$val = self.get_temp($e1.val)}
{$prnt = $e1.prnt + $val + ' = ' + $e1.val + '.length\n'}
|   e1=expression '.' IDENTIFIER '(' ')'
{$val = self.get_temp($e1.val)}
{$prnt = $e1.prnt + 'Call ' + $e1.val + '.' + $IDENTIFIER.text + ',0\nPop ' + $val + '\n'}
|	e1=expression '.' IDENTIFIER '(' es1=exps ')'
{$val = self.get_temp($e1.val)}
{prev_prnt = $e1.prnt + $es1.prnt}
{$prnt = prev_prnt + $es1.val + 'Call ' + $e1.val + '.' + $IDENTIFIER.text + ',' + str($es1.val.count('\n')) + '\nPop ' + $val + '\n'}
|	INTEGER_LITERAL {$val = $INTEGER_LITERAL.text}
|	'true'          {$val = 'true'}
|	'false'         {$val = 'false'}
|	IDENTIFIER      {$val = $IDENTIFIER.text}
|	'this'          {$val = 'this'}
|	'new' 'int' '[' e1=expression ']'
{$val = self.get_temp($e1.val)}
{$prnt = $e1.prnt + $val + ' = new int[' +  $e1.val + ']\n'}
|	'new' IDENTIFIER '(' ')'
{$val = self.create_temp()}
{$prnt = 'Call ' + $IDENTIFIER.text + ',0\nPop ' + $val + '\n'}
|	'!' e1=expression
{$val = self.get_temp($e1.val)}
{$prnt = $e1.prnt + $val + ' = !' + $e1.val + '\n'}
|	'(' e1=expression ')'
{$val = $e1.val}
{$prnt = $e1.prnt}
;
IDENTIFIER:	[a-zA-Z_][a-zA-Z0-9_]* ;
INTEGER_LITERAL: '0'..'9'+ ;
WS        :   [ \t\r\n]+ -> skip ;
COMMENT   : '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' .*? '\r'? '\n' -> skip;
