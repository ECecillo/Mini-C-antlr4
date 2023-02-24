/*
 Lexer Grammar
 */

// Défini le nom de la grammaire que l'on utilise et que l'on défini seulement des règles de lexing.
lexer grammar Example1;

// Dans un grammaire on commence à lire ici en premier.

// Défini les signes suivants comme des opérations.
OP: '+' | '*' | '-' | '/';

// Indique à ANTLR que les parenthèses peuvent être prises en compte comme des tokens.
PARENTHESES: '(' | ')';

// On indique que les caractères qui sont des chiffres seront traités comme des tokens.
DIGIT: [0-9];

// On indique que les caractères qui sont des lettres peuvent former un token.
LETTER: [A-Za-z];

// Invoke les fragments définies ci-dessus, autorise la récursivité des patterns à droites, peut être soit un fragment LETTER ou DIGIT.
ID: LETTER (LETTER | DIGIT)*; // match idents
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
