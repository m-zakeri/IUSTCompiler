parser grammar MiniJavaParser;


options { tokenVocab=MiniJavaLexer; }

@parser::members
{
    from AST import AST
    self.ast = AST()
}

program returns [node=None]
    : {$node = self.ast.make_node('program',None,None)}
    m=mainClass ( c=classDeclaration )* EOF
    {self.ast.add_child($node,$m.node)}
    {self.ast.add_child($node,$c.node)}
    {self.ast.print_tree($node)}
    ;

mainClass returns [node=None]
    : 'class' i1=identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' i2=identifier ')' '{' s=statement '}' '}'
    {self.ast.add_brother($i1.node,$i2.node)}
    {self.ast.add_brother($i2.node,$s.node)}
    {$node = self.ast.make_node('main-class',$i1.node,None)}
    ;

classDeclaration returns [node=None]
    : {$node = self.ast.make_node('class-declaration',None,None)}
    'class' i1=identifier{self.ast.add_child($node,$i1.node)} ( 'extends' i2=identifier{self.ast.add_child($node,$i2.node)} )? '{' ( v=varDeclaration{self.ast.add_child($node,$v.node)} )* ( m=methodDeclaration{self.ast.add_child($node,$m.node)} )* '}'
    ;

varDeclaration returns [node=None]
    : t=type_ i=identifier ';'
    {self.ast.add_brother($t.node,$i.node)}
    {$node = self.ast.make_node('variable-declaration',$t.node,None)}
    ;

methodDeclaration returns [node=None]
    : {$node = self.ast.make_node('method-declaration',None,None)}
     'public' t1=type_ {self.ast.add_child($node,$t1.node)} i1=identifier{self.ast.add_child($node,$i1.node)} '(' ( t2=type_{self.ast.add_child($node,$t2.node)} i2=identifier{self.ast.add_child($node,$i2.node)} ( ',' t3=type_{self.ast.add_child($node,$t3.node)} i3=identifier{self.ast.add_child($node,$i3.node)} )* )? ')' '{' ( v=varDeclaration{self.ast.add_child($node,$v.node)} )* ( s=statement{self.ast.add_child($node,$s.node)} )* 'return' e=expression{self.ast.add_child($node,$e.node)} ';' '}'
    ;

type_ returns [node=None]
    : 'int' '[' ']' {$node = self.ast.make_node('int-array',None,None)}
    | 'boolean' {$node = self.ast.make_node('bool',None,None)}
    | 'int' {$node = self.ast.make_node('int',None,None)}
    | i=identifier {$node = self.ast.make_node('object',$i.node,None)}
    ;


statement returns [node=None]
    : {$node = self.ast.make_node('block',None,None)}  '{' ( s=statement{self.ast.add_child($node,$s.node)} )* '}'
    |  'if' '(' e=expression ')' s1=statement 'else' s2=statement
    {self.ast.add_brother($e.node,$s1.node)}
    {self.ast.add_brother($s1.node,$s2.node)}
    {$node = self.ast.make_node('if',$e.node,None)}
    | 'while' '(' e=expression ')' s=statement
    {self.ast.add_brother($e.node,$s.node)}
    {$node = self.ast.make_node('while',$e.node,None)}
    | 'System.out.println' '(' e=expression ')' ';'
    {$node = self.ast.make_node('print',$e.node,None)}
    | i=identifier '=' e=expression ';'
    {self.ast.add_brother($i.node,$e.node)}
    {$node = self.ast.make_node('assign',$i.node,None)}
    | i=identifier '[' e1=expression ']' '=' e2=expression ';'
    {self.ast.add_brother($i.node,$e1.node)}
    {self.ast.add_brother($e1.node,$e2.node)}
    {$node = self.ast.make_node('assign-array-index',$i.node,None)}
    ;

expression returns [node=None]
    : e1=expression '<' e2=expression
    {self.ast.add_brother($e1.node,$e2.node)}
    {$node = self.ast.make_node('<',$e1.node,None)}
    | e1=expression '&&' e2=expression
    {self.ast.add_brother($e1.node,$e2.node)}
    {$node = self.ast.make_node('&&',$e1.node,None)}
    | e1=expression '*' e2=expression
    {self.ast.add_brother($e1.node,$e2.node)}
    {$node = self.ast.make_node('*',$e1.node,None)}
    | e1=expression '+' e2=expression
    {self.ast.add_brother($e1.node,$e2.node)}
    {$node = self.ast.make_node('+',$e1.node,None)}
    | e1=expression '-' e2=expression
    {self.ast.add_brother($e1.node,$e2.node)}
    {$node = self.ast.make_node('-',$e1.node,None)}
    | e1=expression '[' e2=expression ']'
    {self.ast.add_brother($e1.node,$e2.node)}
    {$node = self.ast.make_node('array-index',$e1.node,None)}
    | e=expression '.' 'length'
    {$node = self.ast.make_node('length',$e.node,None)}
    | e1=expression '.' i=identifier '(' ( e2=expression{self.ast.add_brother($i.node,$e2.node)} ( ',' e3=expression{self.ast.add_brother($e2.node,$e3.node)} )* )? ')'
//    {self.ast.add_brother($e1.node,$i.node)}
    {$node = self.ast.make_node('function-call',$i.node,None)}
    |'(' e=expression ')' {$node=$e.node}
    | INTEGER_LITERAL {$node=self.ast.make_node($INTEGER_LITERAL.text,None,None)}
    | 'true' {$node = self.ast.make_node('true',None,None)}
    | 'false' {$node = self.ast.make_node('false',None,None)}
    | i=identifier {$node=$i.node}
    |'this'
    {$node = self.ast.make_node('this','None','None')}
    | 'new' 'int' '[' e=expression ']' {$node = self.ast.make_node('array-initialkization',$e.node,None)}
    | 'new' i=identifier '(' ')' {$node = self.ast.make_node('object-initialization',$i.node,None)}
    | '!' e=expression {$node = self.ast.make_node('not',$e.node,None)}
    ;

identifier returns [node=None]
    : IDENTIFIER
    {$node = self.ast.make_node($IDENTIFIER.text,None,None)}
    ;