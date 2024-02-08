parser grammar MiniJavaParser;

options { tokenVocab=MiniJavaLex; }

@parser::members {
temp_counter = 0
goto_counter = 0
def create_goto(self):
    self.goto_counter += 1
    return 'L' + str(self.goto_counter)
def create_temp(self):
    self.temp_counter += 1
    return 'T' + str(self.temp_counter)
def remove_temp(self):
    self.temp_counter -= 1
def get_temp(self):
    return 'T' + str(self.temp_counter)
}

program
    : {print('3 Code Address:')} mainClass ( classDeclaration )* EOF
    ;

mainClass
    : 'class' identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier ')' '{' s=statement '}' '}'
    {print($s.value_attr)}
    ;

classDeclaration
    : 'class' identifier ( 'extends' identifier )? '{' ( varDeclaration )* ( methodDeclaration )* '}'
    ;

varDeclaration
    : t=type_ i=identifier ';'
    ;

methodDeclaration
    : 'public' type_ identifier '(' ( type_ identifier ( ',' type_ identifier )* )? ')' '{' ( varDeclaration )* ( s=statement {print($s.value_attr)} )* 'return' expression ';' '}'
    ;

type_
    : 'int' '[' ']'
    | 'boolean'
    | 'int'
    | i=identifier
    ;