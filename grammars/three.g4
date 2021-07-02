grammar three;

@parser::members {
from io import StringIO
import operator
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '&&': operator.and_,
    '<' : operator.lt,
    '>' : operator.gt
}

conversion = {
    'float': float,
    'int': int,
}

temp_counter = label_counter = 0
declare_dict = {}
function_stack_size = 0
param_count = 0
method_text = None

def create_method_text(self):
    if self.method_text is not None:
        self.method_text.close()

    self.method_text = StringIO()

def create_temp(self):
    self.function_stack_size += 4
    self.temp_counter += 1
    return f"T{self.temp_counter}"

def get_temp(self):
    return f"T{self.temp_counter}"

def create_label(self):
    self.label_counter += 1
    return f"L{self.label_counter}"

def get_label(self):
    return f"L{self.label_counter}"

def is_temp(self, tmp: str):
    return tmp[0] == 'T'

def remove_temp(self):
    self.temp_counter -= 1

def declare(self, type, name):
    if name in self.declare_dict:
        self.declare_dict[name] = type
        return
    self.declare_dict[name] = type

def clear_declare_dict(self):
    self.declare_dict.clear()

def get_type(self, name):
    if name in self.declare_dict:
        return self.declare_dict[name]
    return None
}

program:
    mainClass ( classDecl )* EOF
    ;

mainClass: Class mainClassDecl ;

mainClassDecl:
    identifier LBrace mainMethodDecl RBrace
    ;

mainMethodDecl:
{
print("main:")
self.create_method_text()
self.function_stack_size = 0
}
     Public Static Void Main LPran StringType LBrack RBrack identifier RPran mainMethodBody
    ;

mainMethodBody:
    LBrace
        st=statement
    RBrace
{
print(f"\tbeginFunc {self.function_stack_size}\n{self.method_text.getvalue()}\tret")
}
    ;

classDecl:
    Class identifier (Extends identifier)?
    LBrace
        varDecl* methodDecl*
    RBrace
    ;

varDecl returns []:
    t=type id=identifier SemiColon
{
self.declare($t.text, $id.text)
self.function_stack_size += 4
}
    ;

methodDecl:
{
self.create_method_text()
self.function_stack_size = 0
}
    methodDeclName LPran (methodParam (Comma methodParam)*)? RPran methodBody
    ;

methodDeclName:
    Public type id=identifier
{
print(f"{$id.text}:")
}
    ;

methodParam:
    t=type id=identifier
{
self.declare($t.text, $id.text)
}
    ;

methodBody:
    LBrace
        varDecl* statement* Return exp SemiColon
    RBrace
{
print(f"\tbeginFunc {self.function_stack_size}\n{self.method_text.getvalue()}\tret {$exp.value_attr}")
}
    ;

type returns [size_attr = int()]:
      IntType LBrack RBrack
    | BoolType
{
$size_attr = 1
}
    | IntType
{
$size_attr = 4
}
    | id=identifier
    ;
statement returns [value_attr = str(), type_attr = str(), is_var = bool()]:
      LBrace statement* RBrace
    | If ifCondition st1=statement Else elseSt
{
if_label = self.get_label()
end = self.create_label()
print(f"\tgoto {end}", file=self.method_text)
print(f"{if_label}:", file=self.method_text)
print(f"\t{$st1.value_attr}", file=self.method_text)
print(f"{end}:", file=self.method_text)
}
    | While c=whileCondition whileSt
{
before = $c.before
after = $c.after
print(f"\tgoto {before}", file=self.method_text)
print(f"\tgoto {after}", file=self.method_text)
print(f"{after}:", file=self.method_text)

}
    | 'System.out.println' LPran exp RPran SemiColon
{
print(f"\tpush {$exp.value_attr}", file=self.method_text)
print("\tcall System.out.println", file=self.method_text)
print(f"\tpopParams {4}", file=self.method_text)
self.param_count = 0;
}
    | id=identifier Equals e=exp SemiColon
{
t = self.create_temp()
if $e.type_attr == "str":
    $value_attr = f"{t} = {$e.value_attr}\n\t{$id.text} = {t}"
else:
   $value_attr = f"{$id.text} = {$e.value_attr}"
print(f"\t{$value_attr}", file=self.method_text)

}
    | id=identifier LBrack e=exp RBrack Equals e2=exp SemiColon
{
t = self.create_temp()
addr = self.create_temp()
print(f"\t{t} = {$e.value_attr} * 4", file=self.method_text)
print(f"\t{addr} = {t} + {$id.text}", file=self.method_text)
if not self.is_temp($e2.value_attr):
    value = self.create_temp()
    print(f"\t{value} = {$e2.value_attr}", file=self.method_text)
    print(f"\t*({addr}) = {value}", file=self.method_text)
else:
    print(f"\t*({addr}) = {$e2.value_attr}", file=self.method_text)
};

whileCondition returns[before = str(), after = str()]: LPran e=exp RPran
{
$before = self.create_label()
$after = self.create_label()
t = self.create_temp()
print(f"{$before}:", file=self.method_text)
print(f"\t{t} = {$e.value_attr}", file=self.method_text)
print(f"\tifz {t} goto {$after}", file=self.method_text)
};

whileSt: st=statement;

ifCondition: LPran e=exp RPran
{
if_label = self.create_label()
t = self.create_temp()
print(f"\t{t} = {$e.value_attr}", file=self.method_text)
print(f"\tifz {t} goto {if_label}", file=self.method_text)
}
    ;
elseSt: st=statement
{
print(f"\t{$st.value_attr}", file=self.method_text)
}
    ;
exp returns [value_attr = str(), type_attr = str(), is_var = bool(), is_complete = bool()]:
    e1=exp ( op=binOp ) e2=exp
{
#if $e1.type_attr != $e2.type_attr:
#    print('Semantic error4 in "+" operator: Inconsistent types!', $e1.type_attr, $e1.value_attr ,$e2.type_attr, $e2.value_attr)
#else:
$value_attr = f"{$e1.value_attr} {$op.text} {$e2.value_attr}"
$type_attr = "str"
$is_complete = True
}
    | e1=exp LBrack e2=exp RBrack
{
t = self.create_temp()
ptr = self.create_temp()
value = self.create_temp()
print(f"\t{t} = {$e2.value_attr} * 4", file=self.method_text)
print(f"\t{ptr} = {$e1.value_attr} + {t}", file=self.method_text)
print(f"\t{value} = *({ptr})", file=self.method_text)
$value_attr = value
}
    | exp Dot 'length'
{
# print("hey there")
}
    | exp Dot id=identifier LPran ( methodInvocParams ( Comma methodInvocParams )* )? RPran
{
t = self.create_temp()
$value_attr = t
$type_attr = "ret_var"
$is_var = True
print(f"\t{t} = call {$id.text}", file=self.method_text)
print(f"\tpopParams {self.param_count * 4}", file=self.method_text)
self.param_count = 0;
}
    | Integer
{
$value_attr=$Integer.text
$type_attr="int"
}
    | TRUE
{
$value_attr=$TRUE.text
$type_attr="boolean"
}
    | FALSE
{
$value_attr=$FALSE.text
$type_attr="boolean"
}
    | id=identifier
{
name = $id.text
type = self.get_type(name)
if type is None:
    print(f"this shouldn't happen: {name}")
    return
$is_var = True
$value_attr= name
$type_attr= type
}
    | This
    | New IntType LBrack exp RBrack
{
self.function_stack_size += 4
}
    | New identifier LPran RPran
    | Exclamation exp
{
t = self.create_temp()
if $exp.type_attr == "str":
    print(f"\t{t} = {$exp.value_attr}", file=self.method_text)
    print(f"\t{t} = !{t}", file=self.method_text)
else:
    t = self.create_temp()
    print(f"\t{t} = !{$exp.value_attr}", file=self.method_text)
$value_attr = t
$type_attr = "int"
}
    | LPran exp RPran
{
$value_attr = $exp.value_attr
$type_attr = $exp.type_attr
$is_var = $exp.is_var
}
    ;


methodInvocParams:
    e1=exp
{
self.param_count += 1

if $e1.type_attr == "str":
    t = self.create_temp()
    print(f"\t{t} = {$e1.value_attr}", file=self.method_text)
    print(f"\tpush {t}", file=self.method_text)
else:
    print(f"\tpush {$e1.value_attr}", file=self.method_text)
}
    ;

binOp:
    BinaryOperator
    ;

identifier: Identifier;


Class: 'class';
Public: 'public';
Static: 'static';
Void: 'void';
Main: 'main';
LBrace: '{';
RBrace: '}';
LPran: '(';
RPran: ')';
LBrack: '[';
RBrack: ']';
If: 'if';
Else: 'else';
While: 'while';
SemiColon: ';';
Equals: '=';
Dot: '.';
Comma: ',';
TRUE: 'true';
FALSE: 'false';
This: 'this';
New: 'new';
IntType: 'int';
StringType: 'String';
BoolType: 'bool';
Exclamation: '!';
BinaryOperator: '&&'|'<'|'+'|'-'|'*';
Integer: [0-9]+;
Extends: 'extends';
Return: 'return';

Identifier: Letter LetterOrDigit*;

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;
fragment Letter
    : [a-zA-Z$_] // these are the "java letters" below 0x7F
    | ~[\u0000-\u007F\uD800-\uDBFF] // covers all characters above 0x7F which are not a surrogate
    | [\uD800-\uDBFF] [\uDC00-\uDFFF] // covers UTF-16 surrogate pairs encodings for U+10000 to U+10FFFF
    ;


WS:                 [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT:            '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*    -> channel(HIDDEN);