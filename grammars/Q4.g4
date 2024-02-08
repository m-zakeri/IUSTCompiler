
grammar Q2;

@parser :: members {

temp_counter = 0

def create_temp(self):
    self.temp_counter += 1
    return 'T' + str(self.temp_counter)

def remove_temp(self) :
    self.temp_counter -= 1

def is_temp(self, var:str):
    if var[0] == 'T':
        return True
    return False

def create_label(self):
    slef.label_counter += 1
    return 'L' + str(self.tmp_counter)
}

program
        :
        mainClass ( classDeclaration ) *EOF
        ;

mainClass
        :
         Class IDENTIFIER StartStatement Public Static Void 'main' '(' 'String' '[' ']' IDENTIFIER ')' StartStatement Statement EndtStatement EndtStatement
         ;

classDeclaration
        : Class IDENTIFIER ( 'extends' IDENTIFIER )? StartStatement ( varDeclaration )* ( methodDeclaration )* EndtStatement
        ;

varDeclaration
        :	Type IDENTIFIER Semicolon
        ;

methodDeclaration
        :	Public Type IDENTIFIER '(' ( Type IDENTIFIER ( ',' Type IDENTIFIER )* )? ')' StartStatement ( VarDeclaration )* ( Statement )* 'return' expression Semicolon EndtStatement
        ;

Type	:	'int' '[' ']'
        |	'boolean'
        |	'int'
        |	IDENTIFIER
        ;

statement
	    :  StartStatement ( statement )* EndtStatement
        |	'if' '(' expression ')' statement 'else' statement
        |	'while' '(' expression ')' statement
        |	'System.out.println' '(' expression ')' Semicolon
        |	IDENTIFIER '=' expression Semicolon
        |	IDENTIFIER '[' expression ']' '=' expression Semicolon
        ;

expression
        :	expression ( '&&' | '<' | '+' | '-' | '*' ) expression
        |	expression '[' expression ']'
        |	expression '.' 'length'
        |	expression '.' IDENTIFIER '(' ( expression ( ',' expression )* )? ')'
//        |	INTEGER_LITERAL
        |	'true'
        |	'false'
        |	IDENTIFIER
        |	'this'
        |	New 'int' '[' expression ']'
        |	New IDENTIFIER '(' ')'
        |	'!' expression
        |	'(' expression ')'
        ;
//        three address code generator


//        AST generator

Class : 'class' ;
New : 'new' ;
StartStatement : '{' ;
EndtStatement : '}' ;
Semicolon : ';' ;
Public : 'public' ;
Static : 'static' ;
Void : 'void' ;

Number
    : [0-9]Number
    | '.' Number
    | [0-9]
    ;

IDENTIFIER
    : [a-zA-Z_] IDENTIFIER
    | [a-zA-Z_]
    | Number
    ;