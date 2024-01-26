grammar Q3;


@parser::members { 
var_dict = {}
temp_counter = 0
label_counter = 0
params = 0
current_function_params = 0


method_body = ""

def define_variable(self, type, name):
    if name not in self.var_dict:
        self.var_dict[name] = type

def create_temp(self):
    new_temp = f"_t{self.temp_counter}"
    self.temp_counter += 1
    self.current_function_params += 1
    return new_temp

def create_label(self):
    new_label = f"L{self.label_counter}"
    self.label_counter += 1
    return new_label

def add_to_method_body(self, text):
    self.method_body += text + "\n"

def get_method_body(self):
    return self.method_body

def clear_method_body(self):
    self.method_body = ""
}

program:	        
    mainClass ( classDeclaration )* EOF
    ;

mainClass:	        
{
print("main:")
self.params = 0
self.current_function_params = 0
}    
    ClassSmt identifier LBrace PublicSmt StaticSmt VoidType MainSmt LPran StringType LBrack RBrack identifier RPran mainDefinition
    ;

mainDefinition:
    LBrace statement RBrace RBrace
{
print(f"\tBeginFunc {self.current_function_params * 4}")
print(self.get_method_body())
self.clear_method_body()
}
    ;

classDeclaration:	
    ClassSmt identifier ( ExtendsSmt identifier )? LBrace ( varDeclaration )* ( methodDeclaration )* RBrace
    ;

methodDeclaration:	
{
self.params = 0
self.current_function_params = 0
}
    methodName LPran ( methodParam ( Comma methodParam )* )? RPran methodDefinition
    ;

methodName:
    PublicSmt methodType=type methodID=identifier
{
print(f"{$methodID.text}:")
}
    ;

methodDefinition
    :
    LBrace ( varDeclaration )* ( statement )* ReturnSmt first=expression SemiColon RBrace
{
print(f"\tBeginFunc {self.current_function_params * 4}")
print(self.get_method_body())
print(f"\tretrun {$first.value_attr}")
self.clear_method_body()
}
    ;

varDeclaration: 	
    varType=type varID=identifier SemiColon
{
self.define_variable($varType.text, $varID.text)
self.current_function_params += 1
}
    ;

methodParam:
    paramType=type paramID=identifier
{
self.define_variable($paramType.text, $paramID.text)
}
    ;


type:
        IntegerType LBrack RBrack
    |	BooleanType
    |	IntegerType
    |	identifier;

statement returns [value_attr=str(), type_attr = str()]:
	                LBrace ( statement )* RBrace
                |	
                
                
                
                
                
                IfSmt LPran first=expression RPran 
{
else_label = self.create_label()
temp = self.create_temp()
self.add_to_method_body(f"\t{temp} = {$first.value_attr}")
self.add_to_method_body(f"\tifZ {temp} goto {else_label}")
}                
                
                first_s=statement 
{
end_label = self.create_label()    
self.add_to_method_body(f"\t{$first_s.value_attr}")
self.add_to_method_body(f"\tgoto {end_label}")
}                
                
                ElseSmt second_s=statement
{
self.add_to_method_body(f"{else_label}:")
self.add_to_method_body(f"\t{$second_s.value_attr}")
self.add_to_method_body(f"{end_label}:")
}




                |
{
while_label = self.create_label()
self.add_to_method_body(f"{while_label}:")  
}	
                WhileSmt LPran first=expression RPran 
{
after_while_label = self.create_label()
temp = self.create_temp()
self.add_to_method_body(f"\t{temp} = {$first.value_attr}")
self.add_to_method_body(f"\tifZ {temp} goto {after_while_label}")
}                
                first_s=statement
{
self.add_to_method_body(f"\t{$first_s.value_attr}")
self.add_to_method_body(f"\tgoto {while_label}")
self.add_to_method_body(f"{after_while_label}:")
}




                |	'System.out.println' LPran first=expression RPran SemiColon
{
self.add_to_method_body(f"\tpush {$first.value_attr}")
self.add_to_method_body(f"\tSystem.out.println")
self.add_to_method_body(f"\tPopParams 4")
}


                |	varID=identifier Equals varEXP=expression SemiColon
{
#self.add_to_method_body($varID.text)
#self.add_to_method_body($varEXP.value_attr)
if $varEXP.type_attr == "str": #right side is math exper
    temp = self.create_temp()
    $value_attr = f"{temp} = {$varEXP.value_attr}\n{$varID.text} = {temp}"
    self.add_to_method_body(f"\t{temp} = {$varEXP.value_attr}")
    self.add_to_method_body(f"\t{$varID.text} = {temp}")
elif $varEXP.type_attr == "arr":
    pass
else:
    $value_attr = f"{$varID.text} = {$varEXP.value_attr}"
    self.add_to_method_body('\t' + $value_attr)
}



                |	varID=identifier LBrack varEXP=expression RBrack Equals eqEXP=expression SemiColon
{
$value_attr = f"{$varID.text}[{$varEXP.value_attr}] = {$eqEXP.value_attr}"
self.add_to_method_body('\t' + $value_attr)
}
                ;





expression	returns [value_attr = str(), type_attr = str(), is_var = bool(), is_complete = bool()]:
                first=expression ( oper=Operations ) second=expression
{
#self.add_to_method_body($first.type_attr)
#self.add_to_method_body($second.type_attr)
#self.add_to_method_body($oper.text)
#if $first.type_attr != $second.type_attr:
#    self.add_to_method_body('i think we messd up')
#else:
$value_attr = f"{$first.value_attr} {$oper.text} {$second.value_attr}"
$type_attr = "str"
$is_complete = True
}
            |	first=expression LBrack second=expression RBrack
{
temp = self.create_temp()
self.add_to_method_body(f"\t{temp} = {$first.value_attr}[{$second.value_attr}]")
$value_attr = temp
}
            |	first=expression Dot 'length'
{
}
            |	first=expression Dot iden=identifier LPran ( functionParams ( Comma functionParams )* )? RPran
{
$value_attr = self.create_temp()
self.add_to_method_body(f"\t_LCall {$iden.text}")
self.add_to_method_body(f"\tPopParams {$value_attr}")
self.params = 0
$type_attr = "ret_var"
}
            |	intt=INTEGER_LITERAL
{
$value_attr = $intt.text
$type_attr = "int"
}
            |	tr=TRUE
{
$value_attr = $tr.text
$type_attr = "boolean"
}
            |	fa=FALSE
{
$value_attr = $fa.text
$type_attr = "boolean"
}
            |	iden=identifier
{
$value_attr = $iden.text
$is_var = True
$type_attr = self.var_dict[$iden.text]
}
            |	This
{
}
            |	New IntegerType LBrack first=expression RBrack
{
$type_attr = "arr"
self.current_function_params += 1
}
            |	New identifier LPran RPran
{
}
            |	Exclamation first=expression
{
self.add_to_method_body(f"\t{self.create_temp()} = !{$first.value_attr}")
}
            |	LPran first=expression RPran
{
$value_attr = $first.value_attr
$type_attr = $first.type_attr
$is_var = $first.is_var
}
            ;


functionParams:
    paramss=expression
{
self.params += 1
self.add_to_method_body(f"\tpush {$paramss.value_attr}")
}
    ;

identifier returns [value_attr=str(), type_attr = str()]:
        	        IDENTIFIER ;

/* lexical rules */
INTEGER_LITERAL :
                    DIGIT+;

LBrace: '{';
RBrace: '}';
LPran:  '(';
RPran:  ')';
LBrack: '[';
RBrack: ']';

BooleanType:'boolean';
IntegerType:'int';
StringType: 'String';
VoidType:   'void';

ClassSmt:  'class';
ExtendsSmt:'extends';
MainSmt:   'main';
PublicSmt: 'public';
StaticSmt: 'static';
ReturnSmt: 'return';

WhileSmt: 'while';
IfSmt:    'if';
ElseSmt:  'else';

Equals: '=';
Operations: '&&'|'<'|'+'|'-'|'*';
Exclamation: '!';


SemiColon: ';';
Dot: '.';
Comma: ',';

TRUE: 'true';
FALSE:'false';
This: 'this';
New:  'new';

IDENTIFIER:         LETTER(LETTER | '_' | DIGIT)*;

fragment LETTER:             [a-zA-Z];

fragment DIGIT:              [0-9];

Whitespace:         ('\t' | ' ')+ -> skip;

BlockComment:       '/*' .*? '*/' -> skip;

LineComment:        '//' ~ ('\r' | '\n')* -> skip;

Newline:           ('\r' '\n'? | '\n') -> skip;