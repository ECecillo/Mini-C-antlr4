# LAB2, arithmetic expressions interpreter

MIF08, 2022-2023, Laure Gonnord & Matthieu Moy

# Content

This directory contains an interpreter for simple arithmetic
expressions like 5+3, for instance. The intepreter evaluates the
arithmetic expressions and prints their value on the standard
output.

# Usage

* `make` to generate AritLexer.py and AritParser.py (once)

* `python3 arit1.py <path/and/test/name>` to test a given file, for
 instance:
 `python3 arit1.py tests/test01.txt`  should print `1+2 = 3`

* `make test` to test on all tests files of the `testfile` directory

# Syntax of our language/restrictions

The syntax is the one textually given in the Lab2 sheet.
Restriction : we did not implement minus nor unary minus.

# Design choices

## Binary and Unary minus

Given the following grammar of non-empty lists of arithmetic expressions:

$$ S → Z+ $$
$$ Z → E; $$
$$ E → E +E $$
$$ E → E ∗E $$
$$ E → F $$
$$ F → i nt $$
$$ F → (E) $$

We want to handle in our grammar, binary and unary minus we need to cover the following cases:

$$ -1 = -1 $$
$$ 1 - 1 = 0 $$
$$ -1-1 = -2 $$
$$ -1 + 1 = 0 $$
$$ -1 + (-1) = -2 $$
$$ --1 = 1 $$

The minus operation can be easily define with the following rule :

$$ E → E - E $$

However, this won't cover all of the above cases, so we can agree that the following rules should cover the last remaining cases:

$$ E → -F $$

Which can be repeated n times.

Now we also need to define a rule that handles $$ -1-1 $$ and so we added the following :

$$ E → - E - E $$

Finally to handle recursive `-` symbol and the fact that we could have `-+` we can define the following:

$$ F → -F $$
$$ F → +F $$

We coded all of the above into our ANTLR grammar and all of the test seems to be passing.

# Known bugs

N/A
