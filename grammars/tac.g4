grammar tac;

@parser::members{
label_counter = 0
temp_counter = 0
def create_temp(self):
    self.temp_counter += 1
    return '_t' + str(self.temp_counter)

def remove_temp(self):
    self.temp_counter -= 1

def get_temp(self):
    return f'_t{self.temp_counter}'

def create_label(self):
    self.label_counter += 1
    return '_L{self.label_counter}'
}

program:
    main=mainClass ( cls=classDecleration )* EOF
{
f = open('result.txt', 'w')
tac = $main.tac + $cls.tac
f.write(tac)
f.close()
}
    ;
mainClass returns [tac = str()]:
    'class' identifier  '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier ')' '{' st=statement '}' '}'
{
$tac = $st.tac
}
    ;
classDecleration returns [tac = str()]:
    'class' identifier ( 'extends' identifier )? '{' ( varDeclaration )* ( method=methodDeclaration {
$tac += $method.tac
    } )* '}'
    ;
varDeclaration:
    typeId identifier ';'
    ;
methodDeclaration returns [tac = str()]:
    'public' typeId identifier '(' ( typeId identifier ( ',' typeId identifier )* )? ')'
    '{' ( varDeclaration )* ( st=statement {$tac += $st.tac} )* 'return' exp=expression {
$tac += f"\n PushParam {$exp.tac} \n ret \n"
    } ';' '}'
    ;
typeId:
    'int' '[' ']'
    |'boolean'
    |'int'
    |identifier
    ;
statement returns [tac = str()]:
    '{' ( st=statement {
$tac += $st.tac
    })* '}'
    |'if' '(' exp=expression ')' st1=statement 'else' st2=statement
{
l_true = self.create_label()
l_after = self.create_label()
tac = f"If {$exp.tac} GoTo {l_true}\n"
tac += f"{$st2.tac}\n"
tac += f"Goto {l_after}\n"
tac += f"{l_true} {$st1.tac}\n"
tac += f"{l_after}:\n"
$tac = tac
}
    |'while' '(' exp=expression ')' st=statement
{
l_while = self.create_label()
l_st = self.create_label()
l_after = self.create_label()
$tac = f"{l_while}: if {$exp.tac} Goto {l_st}\n"
$tac += f"Goto {l_after}\n"
$tac += f"{l_st}: {$st.tac}\n"
$tac += f"Goto {l_while}\n"
$tac += f"{l_after}:\n"
}
    |'System.out.println' '(' exp=expression ')' ';'
{
t = self.create_temp()
$tac = f"{t} = {$exp.tac} \n"
}
    |id1=identifier '=' exp=expression ';'
{
t = self.create_temp()
$tac = f"{t} = {$exp.tac} \n"
$tac += $id1.text + ' = ' + t + '\n'
}
    |id1=identifier '[' exp1=expression ']' '=' exp2=expression ';'
{
t1 = self.create_temp()
$tac = t1 + ' = ' + $exp1.tac + '\n'
t2 = self.create_temp()
$tac += f"{t2} = {$exp2.tac} \n"
$tac += f"{$id1.text} [{t1}] = {t2} \n"
}
    ;
expression returns [tac = str()]:
    exp1=expression opt=( '&&' | '<' | '+' | '-' | '*' ) exp2=expression
{
$tac =$exp1.tac + $opt.text + $exp2.tac
}
    |exp1=expression '[' exp2=expression ']'
{
$tac = $exp1.tac + '[' + $exp2.tac + ']' + '\n'
}
    |exp1=expression '.' 'length'
{
$tac = 'len ' + '(' + $exp1.tac + ')' + '\n'
}
    |exp1=expression '.' id1=identifier '(' ( exp2=expression {$tac = 'PushParam ' + $exp2.tac + '\n'} 
    ( ',' exp3=expression {$tac += 'PushParam ' + $exp3.tac + '\n'})* )? ')'
{
$tac = f"Call {$exp1.tac} {$id1.tac}\n"
$tac += "PopParams"
}
    | Integer
{
$tac = $Integer.text
}
    |'true'
{
$tac = "true"
}
    |'false'
{
$tac = "false"
}
    |id1=identifier
{
$tac = $id1.text
}
    |'this'
{
$tac = "this"
}
    |'new' 'int' '[' exp1=expression ']'
{
$tac = $exp1.tac
}
    |'new' id1=identifier '(' ')'
{
$tac = $id1.tac
}
    |'!' exp1=expression
{
$tac = "~"+$exp1.tac
}
    |'(' exp1=expression ')'
{
$tac = $exp1.tac
}
;
identifier returns [tac = str()]:
    Identifier {$tac = $Identifier.text}
    ;

Identifier: Letter LetterOrDigit*;

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
    [0-9]+
    ;
WS:
    [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT:
    '/*' .*? '*/' -> channel(HIDDEN)
    ;
LINE_COMMENT:
    '//' ~[\r\n]* -> channel(HIDDEN)
    ;