grammar Exercice5;

full_expr: asequence bsequence EOF;

asequence: 'a'*;
bsequence: 'bb'*;

WS: [ \t\r\n]+ -> skip;
