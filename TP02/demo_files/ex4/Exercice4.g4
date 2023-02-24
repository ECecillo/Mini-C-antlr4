grammar Exercice4;
/*
Need to respect the following properties :
  - If it start with a parenthesis it needs to end with a parenthesis.
  - If it start with a parenthesis it needs to end with a parenthesis.
  - Repeat the pattern and accept every other input.
*/

// Define our main rule to accept well-formed parentheses
full_expr: ( '(' full_expr ')' | '[' full_expr ']')* EOF;

// Skip les [] et ().
CHARS: ~[()[\]] -> skip;
