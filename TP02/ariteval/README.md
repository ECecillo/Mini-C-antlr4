# LAB2, arithmetic expressions interpreter
MIF08, 2020-2021, Laure Gonnord & Matthieu Moy

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

Given the following grammar of non-empty lists of arithmetic expressions


$$ S → Z+ $$
$$ Z → E; $$
$$ E → E +E $$
$$ E → E ∗E $$
$$ E → F $$
$$ F → i nt $$
$$ F → (E) $$




# Known bugs

N/A
