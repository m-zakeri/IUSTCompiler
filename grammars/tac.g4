grammar tac;

@parser::members {

conversion = {
    'float': float,
    'int': int,
}

tmp_cnt = name_cnt = 0
declare_dict = {}
function_stack_size = 0
param_count = 0
method_text = None


def create_temp(self):
    self.function_stack_size += 4
    self.tmp_cnt += 1
    return f"T{self.tmp_cnt}"

def get_temp(self):
    return f"T{self.tmp_cnt}"

def generate_name(self):
    self.name_cnt += 1
    return f"L{self.name_cnt}"

def get_label(self):
    return f"L{self.name_cnt}"

def is_temp(self, tmp: str):
    return tmp[0] == 'T'

def remove_temp(self):
    self.tmp_cnt -= 1

def declare(self, type, name):
    if name in self.declare_dict:
        self.declare_dict[name] = type
        return
    self.declare_dict[name] = type

def clear_declare_dict(self):
    self.declare_dict.clear()

def create_method_text(self):
    if self.method_text is not None:
        self.method_text.close()

def get_type(self, name):
    if name in self.declare_dict:
        return self.declare_dict[name]
    return None
}



program:
    mainClass ( classDecl )* EOF
    ;

mainClass: 'class' identifier '{' mainMethodDeclaration '}' ;


mainMethodDeclaration:
{
print("main:")
self.create_method_text()
self.function_stack_size = 0
}
     'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier ')''{'st=statement'}'
{
print(f"\tbeginFunc {self.function_stack_size}\n{self.method_text.getvalue()}\tret")
}
    ;

classDecl:
    'class' identifier ('extends' identifier)?
    '{'
        varDeclaration* methodDecl*
    '}'
    ;


methodDecl:
{
self.create_method_text()
self.function_stack_size = 0
}
    methodDeclName '(' (methodParam (',' methodParam)*)? ')'
    ;

varDeclaration returns []:
    tp=type id=identifier ';'
    {
    self.declare($tp.text, $id.text)
    self.function_stack_size += 4
    }
    ;


methodDeclName:
    'public' type id=identifier
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


type returns [size_attr = int()]:
      'int' '[' ']'
    | 'bool'
{
$size_attr = 1
}
    | 'int'
{
$size_attr = 4
}
;


binOp:
    '&&'|'<'|'+'|'-'|'*'
    ;

identifier: Identifier;


Identifier:
    Letter LetterOrDigit*
    ;

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;
fragment Letter
    : [a-zA-Z$_]
    | ~[\u0000-\u007F\uD800-\uDBFF]
    | [\uD800-\uDBFF] [\uDC00-\uDFFF]
    ;

Integer:
    [0-9]+;

WS:
    [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT:
    '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT:
    '//' ~[\r\n]*    -> channel(HIDDEN);