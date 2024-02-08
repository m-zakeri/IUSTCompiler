grammar T4Q2;

prog :  mainClass classDecl*
       ;
mainClass
  :   'class' ID '{' 'public' 'static' 'void' 'main'
                '(' 'String' '[' ']' ID ')' '{' varDecl* statement* '}' '}'
  ;
classDecl
  :   'class' ID '{' varDecl* methodDecl* '}'
        ;
varDecl : type ID ';'
        ;
methodDecl
  :   'public' type ID '(' (formalList (',' formalList+)*)? ')'
                '{' varDecl* statement* 'return' expr ';' '}'
        ;
formalList
  :   type ID
        ;
type  :   'int'
  |   'int' '[' ']'
  |   'boolean'
  |   ID
        ;
statement
  :   '{' statement* '}'
  |   'System.out.println' '(' expr ')' ';'
  |   ID '=' expr ';'
  |   ID '[' (INT | ID) ']' '=' expr ';'
  |   'while' '(' condExpr ')' statement
  |   'if' '(' condExpr ')' statement 'else' statement
  ;
condExpr
  :   '(' condExpr ')'
  |   '!' condExpr
  |   condExpr '<' condExpr
  |   condExpr '&&' condExpr
  |   expr
  ;
expr
  :   atom ( '+' atom | '-' atom | '*' atom )*
  |   ('+' | '-') atom
  |   atom '[' expr ']'
  |   atom '.' 'length'
  |   atom '.' ID '(' ( expr ( ',' expr )* )? ')'
  ;
atom : ( INT
  | (ID | 'this') ('.' ID '(' expr ')')?
  | 'new' ID '(' ')'
  | 'this'
  | 'new' 'int' '[' expr ']'
  | '(' expr ')')
  ;

ID        :   [a-zA-Z_][a-zA-Z0-9_]*;
INT       :   '0'..'9'+ ;
BOOLEAN   :   ('true' | 'false') ;
WS        :   [ \t\r\n]+ -> skip ;
COMMENT   : '/*' .*? '*/' -> skip ;
LINE_COMMENT
          : '//' .*? '\r'? '\n' -> skip;