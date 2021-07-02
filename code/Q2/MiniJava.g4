grammar MiniJava;

program:
    mainClass ( classDecleration )* EOF ;

mainClass:
    Class Identifier
        LBrace
            Public Static Void Main LPran StringType LBrack RBrack Identifier RPran
            LBrace
                statement
            RBrace
        RBrace ;

classDecleration:
    Class Identifier (Extends Identifier)?
    LBrace
        varDecleration* methodDecleration*
    RBrace;

varDecleration:
    type Identifier SemiColon;

methodDecleration:
    Public type Identifier LPran (type Identifier (Comma type Identifier)*)? RPran
    LBrace
        varDecleration* statement* Return exp SemiColon
    RBrace;

type:
      IntType LBrack RBrack
    | BoolType
    | IntType
    | Identifier;

statement:
      LBrace
        statement*
      RBrace
    | If LPran exp RPran statement Else statement
    | While LPran exp RPran statement
    | 'System.out.println' LPran exp RPran SemiColon
    | Identifier Equals exp SemiColon
    | Identifier LBrack exp RBrack Equals exp SemiColon;

exp:
      exp ( BinaryOperator ) exp
    | exp LBrack exp RBrack
    | exp Dot 'length'
    | exp Dot Identifier LPran ( exp ( Comma exp )* )? RPran
    | Integer
    | True
    | False
    | Identifier
    | This
    | New IntType LBrack exp RBrack
    | New Identifier LPran RPran
    | Not exp
    | LPran exp RPran;


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
True: 'true';
False: 'false';
This: 'this';
New: 'new';
IntType: 'int';
StringType: 'String';
BoolType: 'bool';
Not: '!';
BinaryOperator: '&&'|'<'|'+'|'-'|'*';
Extends: 'extends';
Return: 'return';

Integer:
    '0'
    | N_Digit Digit*;

N_Digit :
    [1-9];

Digit :
    [0-9];

Identifier:
    Letter (Letter | Digit)*;

Letter:
    [a-zA-Z$_];