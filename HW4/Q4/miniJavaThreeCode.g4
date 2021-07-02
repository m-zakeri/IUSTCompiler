grammar miniJavaThreeCode;

@header{
    from AddressCodeConverter import *
}

@parser::members{
child_ptrs={}
tmp_counter=0
label_counter=0

def new_label(self):
    self.label_counter+=1
    return 'Label_{}'.format(str(self.label_counter))
def new_tmp(self):
    self.tmp_counter+=1
    return 'T_{}'.format(str(self.tmp_counter))

def current_tmp(self):
    return 'T_{}'.format(str(self.tmp_counter))

}


program : {print("BEGINS:")} main_class ( class_declaration )* EOF ;

main_class : 'class' identifier_r '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier_r ')' '{' s=statement '}' '}'
    {print($s.v)};

class_declaration : 'class' identifier_r ( 'extends' identifier_r)? '{' (var_declaration)* (method_declaration)* '}';
var_declaration : type_a=type_r identifier=identifier_r ';';

method_declaration : 'public' type_r identifier_r '(' (type_r identifier_r (',' type_r identifier_r)*)? ')' '{' (var_declaration)* (s=statement {print($s.v)})* 'return' expression ';' '}';

type_r : 'int' '[' ']' | 'boolean' | 'int' | identifier=identifier_r ;

statement returns [v = str() , type_a = str() , prev_v = str()] : 
        '{' {$v=''} (s=statement {$v+=$s.v+'\n'})* '}' | 
        'if' '(' exp=expression ')' ifs=statement 'else' es=statement 
        {if_go = self.new_label()}
        {else_go = self.new_label()}
        {$v += '\n'.join([item for item in $exp.tmps])+'\n'}
        {$v+='\t\t if ({}) goto {}\n'.format($exp.v , if_go)}
        {$v+=$es.v}
        {$v+='\t\t goto {}\n'.format(else_go)}
        {$v+='{}:{}'.format(if_go,$ifs.v)}
        {$v+='{}:{}'.format(else_go,'\t\t')}
        | 
        'while' '(' exp=expression ')' s=statement 
        {go_while=self.new_label()}
        {inner_while=self.new_label()}
        {$v+='\t\t goto {}\n'.format(go_while)}
        {$v+='{}:{}'.format(inner_while,$s.v)}
        {$v+=go_while + '\n'.join([item for item in $exp.tmps])+'\n'}
        {$v+='\t\t if({}) goto {}\n'.format($exp.v,inner_while)}        
        |
        'System.out.println' '(' expression ')' ';' 
        |identifier=identifier_r '=' exp=expression ';' 
        {$v='\n'.join([item for item in $exp.tmps])+'\n'}
        {$v+='\t\t {} = {}'.format($identifier.v , $exp.v)}
        | identifier=identifier_r '[' exp1=expression ']' '=' exp2=expression ';' 
        {$v='\n'.join([item for item in $exp1.tmps])+'\n'}
        {$v+='\n'.join([item for item in $exp2.tmps])+'\n'}
        {tmp=self.new_tmp()}
        {$v+=AddressCodeConverter.array_initializer($identifier_r.v , $exp1.v , $exp2.v , tmp)}
        ;

expression returns [v = str(), type_a=str(), prev_v=str(), tmps=[] ]: 
    expl = expression op=('+' | '-' | '*') expr=expression 
    {tmps = $expl.tmps}
    {$type_a = 'INT'}
    {temp , $tmps , $expl.v = (self.new_tmp() , $tmps + ['\t\t {} = {}'.format(self.current_tmp(),$expl.prev_v)] , self.current_tmp() ) if $expl.prev_v is not None else (None , $tmps , $expl.v)}
    {$tmps += $expr.tmps}
    {temp , $tmps , $expr.v = (self.new_tmp() , $tmps + ['\t\t {} = {}'.format(self.current_tmp(),$expr.prev_v)] , self.current_tmp() ) if $expr.prev_v is not None else (None , $tmps , $expr.v)}
    {$prev_v= $v = $expl.v + $op.text + $expr.v}
    | expl = expression op=('&&' | '<') expr=expression
    {tmps = $expl.tmps}
    {$type_a = 'BOOL'}
    {temp , $tmps , $expl.v = (self.new_tmp() , $tmps + ['\t\t {} = {}'.format(self.current_tmp(),$expl.prev_v)] , self.current_tmp()) if $expl.prev_v is not None else (None , $tmps , $expl.v) }
    {$tmps += $expr.tmps}
    {temp , $tmps , $expr.v = (self.new_tmp() , $tmps + ['\t\t {} = {}'.format(self.current_tmp(),$expr.prev_v)] , self.current_tmp()) if $expr.prev_v is not None else (None , $tmps , $expr.v)}
    {$prev_v= $v = $expl.v + $op.text + $expr.v}
    | exp1=expression '[' exp2=expression ']'
    {$tmps , $type_a = $exp1.tmps + $exp2.tmps , 'INT'}
    {temp , $tmps , $exp2.v = (self.new_tmp() ,$tmps + ['\t\t {} = {}'.format(self.current_tmp(),$exp2.prev_v)] , self.current_tmp()) if $exp2.prev_v is not None else (None , $tmps , $exp2.v)}
    {temp = self.new_tmp()}
    {$tmps += AddressCodeConverter.tmp_array(temp , $exp1.v , $exp2.v)}
    {$prev_v=$v='*'+temp}
    | exp=expression '.' 'length'
    {$tmps=$exp.tmps}
    {$type_a='INT'}
    {temp , $tmps , $exp.v = (self.new_tmp() ,$tmps + ['\t\t {} = {}'.format(self.current_tmp(),$exp.prev_v)] , self.current_tmp()) if $exp.prev_v is not None else (None , $tmps , $exp.v)}    
    {$prev_v = $v = $exp.v + '.length'}
    |expression '.' identifier_r '(' (expression ( ',' expression)*)? ')' 
    | integerLiteral 
    {$type_a,$v,$prev_v='INT' , $integerLiteral.text,None}
    | 'true'
    {$type_a,$v,$prev_v='BOOL', 'true',None}
    | 'false' 
    {$type_a,$v,$prev_v='BOOL', 'false',None}
    | identifier=identifier_r
    {$type_a,$v,$prev_v= ($identifier.type_a, $identifier.v , None) if $identifier.type_a=='NOTDEFIENED' else ($type_a, $v,$prev_v)}
    |'this' 
    | 'new' 'int' '[' expression ']' 
    | 'new' identifier_r '(' ')' 
    | '!' exp=expression 
    {$tmps=$exp.tmps}
    {$type_a='BOOL'}
    {temp , $tmps , $exp.v = (self.new_tmp() ,$tmps + ['\t\t {} = {}'.format(self.current_tmp(),$exp.prev_v)] , self.current_tmp()) if $exp.prev_v is not None else (None , $tmps , $exp.v)}    
    {$prev_v = $v = '!' + $exp.v}
    | '(' exp=expression ')'
    {$type_a=$exp.type_a}
    {$v = $exp.v}
    {$prev_v=$exp.prev_v}
    {$tmps=$exp.tmps};

identifier_r returns [v=str(), type_a=str()]: IDENTIFIER
{$v , $type_a = $IDENTIFIER.text , 'NOTDEFIENED'}
;

IDENTIFIER:  Letter LetterOrDigit*;


integerLiteral
    : DECIMAL_LITERAL
    | HEX_LITERAL
    | OCT_LITERAL
    | BINARY_LITERAL
    ;

DECIMAL_LITERAL:    ('0' | [1-9] (Digits? | '_'+ Digits)) [lL]?;
HEX_LITERAL:        '0' [xX] [0-9a-fA-F] ([0-9a-fA-F_]* [0-9a-fA-F])? [lL]?;
OCT_LITERAL:        '0' '_'* [0-7] ([0-7_]* [0-7])? [lL]?;
BINARY_LITERAL:     '0' [bB] [01] ([01_]* [01])? [lL]?;


fragment Digits
    : [0-9] ([0-9_]* [0-9])?
    ;

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;


fragment Letter
    : [a-zA-Z$_] // these are the "java letters" below 0x7F
    | ~[\u0000-\u007F\uD800-\uDBFF] // covers all characters above 0x7F which are not a surrogate
    | [\uD800-\uDBFF] [\uDC00-\uDFFF] // covers UTF-16 surrogate pairs encodings for U+10000 to U+10FFFF
    ;

WS:                 [ \t\r\n\u000C]+    -> channel(HIDDEN);
COMMENT:            '/*' .*? '*/'       -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*       -> channel(HIDDEN);