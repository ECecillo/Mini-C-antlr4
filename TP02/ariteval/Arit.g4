grammar Arit;

// MIF08, simple arit evaluator with semantic actions
// Reminder: lower-case for parser rules, UPPER-CASE for lexer rules.

prog: statement+ EOF
    ;

statement: expr SCOL    {print($expr.text+" = "+str($expr.val))} // print the value
         ;

expr returns [int val]
    // MULT is * (matched before PLUS if possible)
    : e1=expr MULT  e2=expr {$val = $e1.val * $e2.val}
    | e1=expr PLUS  e2=expr {$val = $e1.val + $e2.val} // PLUS is +
    | e1 = expr MINUS e2 = expr {$val = $e1.val - $e2.val} // PLUS is +
    | a= atom {$val = $a.val} // just copy the value
    ;

atom returns [int val]
    : INT               {$val = int($INT.text)} // get the value from the lexer
    | '(' expr ')'      {$val=$expr.val} // just copy the value
    | '-' expr {$val=-$expr.val} // just copy the value
    ;


SCOL :      ';';
PLUS :      '+';
MINUS :     '-';
MULT :      '*';
DIV :       '/';

INT:        [0-9]+;

COMMENT
 : '//' ~[\r\n]* -> skip
 ;


NEWLINE:    '\r'? '\n' -> skip;
WS  :       (' '|'\t')+  -> skip;
