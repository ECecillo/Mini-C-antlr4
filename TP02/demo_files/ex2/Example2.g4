grammar Example2;

/* Parsing rules */

full_expr: expr ';' EOF;

expr: expr OP expr | ID {print('oh an id : '+$ID.text)} | INT;

/* Lexing rules */

OP: '+' | '*' | '-' | '/';

INT: '0' ..'9'+;
ID: ('a' ..'z' | 'A' ..'Z')+;
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
