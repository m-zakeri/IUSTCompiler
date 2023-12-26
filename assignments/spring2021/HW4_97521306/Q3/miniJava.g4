grammar miniJava;

@parser::members{
temp_counter = label_counter = 0
declare_dict = {}
function_stack_size = 0
param_count = 0
method_text = None


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
        print("wtf are you doing dude")
        return
    self.declare_dict[name] = type

def clear_declare_dict(self):
    self.declare_dict.clear()

def get_type(self, name):
    if name in self.declare_dict:
        return self.declare_dict[name]
    return None
}


program:	        mainClass ( classDeclaration )* EOF;

mainClass:
                    {
                        print("main:")
                        self.function_stack_size = 0
                    }
                    'class' identifier '{' 'public' 'static' 'void' 'main' '(' 'String' '[' ']' identifier ')' '{' statement '}' '}'

                    ;

classDeclaration:	'class' id1=identifier
                    {
                        print(f"{$id1.text}:")
                    }
                    ( 'extends' identifier )? '{' ( varDeclaration )* ( methodDeclaration )* '}';

varDeclaration: 	type identifier ';';

methodDeclaration:
	                'public' type id1=identifier
	                {
                        self.function_stack_size = 0
                        print(f"{$id1.text}:")
                    }
	                '(' ( type id2=identifier
	                                    {
	                                        print("pop",$id2.value_attr)
	                                    }
	                                    ( ',' type id3=identifier
	                                    {
	                                        print("pop",$id3.value_attr)
	                                    }
	                                    )* )? ')' '{' ( varDeclaration )* ( statement )* 'return' expression ';' '}'
                    {
                        print("push",$expression.value_attr)
                        print("return")
                    }
	                ;

type:
                    'int' '[' ']'
                |	'boolean'
                |	'int'
                |	identifier;

statement returns [value_attr=str(), type_attr = str()]:
	                '{' ( statement )* '}'
                |	'if' '(' expression ')'
                    {
                        else_label = self.create_label()
                        end_label = self.create_label()
                        print('if', 'not', $expression.value_attr, 'goto',else_label)
                    }
                    st1=statement
                    {
                        print(f"{$st1.value_attr}")
                        print(f"goto {end_label}")
                    }
                    'else' st2=statement
                    {
                        print(f"{else_label}:")
                        print(f"{$st2.value_attr}")
                        print(f"goto {end_label}")
                        print(f"{end_label}:")
                    }
                |
                    {
                        while_label = self.create_label()
                        end_label = self.create_label()
                        print(f"{while_label}:")
                    }
                    'while' '(' expression ')'
                    {
                        print('if', 'not', $expression.value_attr, 'goto',end_label)
                    }
                    st1=statement
                    {
                        print(f"{$st1.value_attr}")
                        print("goto", while_label)
                        print(f"{end_label}:")
                    }
                |	'System.out.println' '(' expression ')' ';'
                    {
                        print(f"push {$expression.value_attr}")
                        print("call System.out.println , 0")
                        print(f"pop {$expression.value_attr}")
                        self.param_count = 0
                    }
                |	identifier '=' expression ';'
                    {
                        print(f"{$identifier.value_attr} = {$expression.value_attr}")
                        $value_attr=f"{$identifier.value_attr} = {$expression.value_attr}"
                    }
                |	identifier '[' expression ']' '=' expression ';'
                    {
                        print(f"{$identifier.value_attr} [{$expression.value_attr}]= {$expression.value_attr}")
                    }
                ;


expression	returns [value_attr=str(), type_attr = str()]:
                e1=expression '&&' e2=expression
                {
                    tmp=self.create_temp()
                    print(tmp,"=",$e1.value_attr,"&&",$e2.value_attr)
                    $value_attr= tmp
                }
            |   e1=expression '<'  e2=expression
                {
                    tmp=self.create_temp()
                    print(tmp,"=",$e1.value_attr,"<",$e2.value_attr)
                    $value_attr= tmp
                }
            |   e1=expression '+'  e2=expression
                {
                    tmp=self.create_temp()
                    print(tmp,"=",$e1.value_attr,"+",$e2.value_attr)
                    $value_attr= tmp
                }
            |   e1=expression '-'  e2=expression
                {
                    tmp=self.create_temp()
                    print(tmp,"=",$e1.value_attr,"-",$e2.value_attr)
                    $value_attr= tmp
                }
            |   e1=expression '*'  e2=expression
                {
                    tmp=self.create_temp()
                    print(tmp,"=",$e1.value_attr,"*",$e2.value_attr)
                    $value_attr= tmp
                }
            |	e1=expression '[' e2=expression ']'
                {
                    tmp = self.create_temp()
                    print(tmp,"=",$e1.value_attr,'[',$e2.value_attr,']')
                    $value_attr = tmp
                }
            |	expression '.' 'length'
            |	expression '.' id=identifier '(' ( e2=expression
                                                    {
                                                        self.param_count+=1
                                                        print("push",$e2.value_attr)
                                                    } ( ',' e3=expression
                                                            {
                                                                self.param_count+=1
                                                                print("push",$e3.value_attr)
                                                            }
                                                            )* )? ')'
                {
                    tmp = self.create_temp()
                    $value_attr = tmp
                    print(f"call {$id.text} , {self.param_count}")
                    print(f"pop {tmp}")
                    self.param_count = 0;
                }
            |	INTEGER_LITERAL
                {
                    tmp = self.create_temp()
                    print(tmp,'=',$INTEGER_LITERAL.text)
                    $value_attr=tmp
                }
            |	'true'
                {
                    tmp = self.create_temp()
                    print(tmp,'=', 'true')
                    $value_attr=tmp
                    $type_attr="boolean"
                }
            |	'false'
                {
                    tmp = self.create_temp()
                    print(tmp,'=', 'false')
                    $value_attr=tmp
                    $type_attr="boolean"
                }
            |	id=identifier
                {
                    tmp = self.create_temp()
                    print(tmp,'=', $id.text)
                    $value_attr=tmp
                }
            |	'this'
            |	'new' 'int' '[' expression ']'
                {
                    self.function_stack_size += 4
                }
            |	'new' identifier '(' ')'
            |	'!' expression
                {
                    tmp= self.create_temp()
                    print(tmp, '=','not',$expression.value_attr)
                    $value_attr= tmp
                }
            |	'(' expression ')'
                {
                    tmp=self.create_temp()
                    print(tmp, '=',$expression.value_attr)
                    $value_attr= tmp
                }
            ;


identifier returns [value_attr=str(), type_attr = str()]:
        	        IDENTIFIER
        	        {
        	            $value_attr = $IDENTIFIER.text
        	        }
        	        ;

/* lexical rules */
INTEGER_LITERAL :
                    DIGIT+;

IDENTIFIER:         LETTER(LETTER | '_' | DIGIT)*;

fragment LETTER:             [a-zA-Z];

fragment DIGIT:              [0-9];

Whitespace:         ('\t' | ' ')+ -> skip;

BlockComment:       '/*' .*? '*/' -> skip;

LineComment:        '//' ~ ('\r' | '\n')* -> skip;

Newline:           ('\r' '\n'? | '\n') -> skip;
