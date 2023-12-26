grammar MiniJava_AST;

@parser::members{
class TreeNode:
    def __init__(self, value, child, brother):
        self.value = value
        self.child = child
        self.brother = brother


def add_child(self, node, new_child):
    if node.child is None:
        node.child = new_child
    else:
        current = node.child
        while current.brother is not None:
            current = current.brother
        current.brother = new_child

def add_brother(self, node, new_brother):
    if node.brother is None:
        node.brother = new_brother
    else:
        current = node.brother
        while current.brother is not None:
            current = current.brother
        current.brother = new_brother
}

program
:   mainClass (classDeclaration)* EOF
;
mainClass returns[val=str()]
:   'class' IDENTIFIER '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' IDENTIFIER ')' '{' s1=statement '}' '}'
{$val = $s1.val}
;
classDeclaration
:   'class' IDENTIFIER ( 'extends' IDENTIFIER )? '{' ( varDeclaration )* ( methodDeclaration )* '}'
;
varDeclaration
:   type1 IDENTIFIER ';'
;
methodDeclaration returns[val=str()]
:   'public' type1 IDENTIFIER '(' ( type1 IDENTIFIER ( ',' type1 IDENTIFIER )* )? ')' '{' ( varDeclaration )* 'return' expression ';' '}'
|   'public' type1 n=IDENTIFIER '(' ( type1 IDENTIFIER ( ',' type1 IDENTIFIER )* )? ')' '{' ( varDeclaration )* ss1=statements 'return' expression ';' '}'
{$val = $ss1.val}
;
type1
:	'int' '[' ']'
|	'boolean'
|	'int'
|	IDENTIFIER
;
statements returns[val=str()]
:   s1=statement ss1=statements
{self.add_brother($s1.val, $ss1.val)}
{$val = $s1.val}
|   s1=statement                {$val = $s1.val}
;
statement returns[val=str()]
:   '{' '}'
|   '{' ss1=statements '}'  {$val = $ss1.val}
|	'if' '(' e1=expression ')' s1=statement 'else' s2=statement
{ptr = self.TreeNode('block', $s2.val, None)}
{ptr = self.TreeNode('block', $s1.val, ptr)}
{self.add_brother($e1.val, ptr)}
{$val = self.TreeNode('if', $e1.val, None)}
|	'while' '(' e1=expression ')' s1=statement
{ptr = self.TreeNode('block', $s1.val, None)}
{self.add_brother($e1.val, ptr)}
{$val = self.TreeNode('while', $e1.val, None)}
|	'System.out.println' '(' e1=expression ')' ';'
{ptr1 = self.TreeNode('out', None, None)}
{ptr1 = self.TreeNode('System', None, ptr1)}
{ptr2 = self.TreeNode('println', $e1.val, None)}
{ptr1 = self.TreeNode('.', ptr1, ptr2)}
{$val = self.TreeNode('.', ptr1, None)}
|	IDENTIFIER '=' e1=expression ';'
{ptr = self.TreeNode($IDENTIFIER.text, None, $e1.val)}
{$val = self.TreeNode('=', ptr, None)}
|	IDENTIFIER '[' e1=expression ']' '=' e2=expression ';'
{ptr = self.TreeNode($IDENTIFIER.text, $e1.val, $e2.val)}
{$val = self.TreeNode('=', ptr, None)}
;
exps returns[val=str(), prnt=str()]
:   e1=expression ',' es1=exps
{self.add_brother($e1.val, $es1.val)}
{$val = $e1.val}
|   e1=expression
{$val = $e1.val}
;
expression returns[val=str(), prnt=str()]
:   e1=expression op=( '&&' | '<' | '+' | '-' | '*' ) e2=expression
{self.add_brother($e1.val, $e2.val)}
{$val = self.TreeNode($op.text, $e1.val, None)}
|	e1=expression '[' e2=expression ']'
{self.add_child($e1.val, $e2.val)}
{$val = $e1.val}
|	e1=expression '.' 'length'
{ptr = self.TreeNode('length', None, None)}
{self.add_brother($e1.val, ptr)}
{$val = self.TreeNode('.', $e1.val, None)}
|   e1=expression '.' IDENTIFIER '(' ')'
{ptr = self.TreeNode($IDENTIFIER.text, None, None)}
{self.add_brother($e1.val, ptr)}
{$val = self.TreeNode('.', $e1.val, None)}
|	e1=expression '.' IDENTIFIER '(' es1=exps ')'
{ptr = self.TreeNode($IDENTIFIER.text, $es1.val, None)}
{self.add_brother($e1.val, ptr)}
{$val = self.TreeNode('.', $e1.val, None)}
|	INTEGER_LITERAL {$val = self.TreeNode($INTEGER_LITERAL.text, None, None)}
|	'true'          {$val = self.TreeNode('true', None, None)}
|	'false'         {$val = self.TreeNode('false', None, None)}
|	IDENTIFIER      {$val = self.TreeNode($IDENTIFIER.text, None, None)}
|	'this'          {$val = self.TreeNode('this', None, None)}
|	'new' 'int' '[' e1=expression ']'
{ptr = self.TreeNode('int', $e1.val, None)}
{$val = self.TreeNode('new', ptr, None)}
|	'new' IDENTIFIER '(' ')'
{ptr = self.TreeNode($IDENTIFIER.text, None, None)}
{$val = self.TreeNode('new', ptr, None)}
|	'!' e1=expression
{$val = self.TreeNode('!', $e1.val, None)}
|	'(' e1=expression ')'
{$val = $e1.val}
;
IDENTIFIER:	[a-zA-Z_][a-zA-Z0-9_]* ;
INTEGER_LITERAL: '0'..'9'+ ;
WS        :   [ \t\r\n]+ -> skip ;
COMMENT   : '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' .*? '\r'? '\n' -> skip;
