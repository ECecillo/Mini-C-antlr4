from antlr4 import InputStream
from antlr4 import CommonTokenStream

# include to use the generated lexer and parser
from Exercice5Lexer import Exercice5Lexer
from Exercice5Parser import Exercice5Parser

import sys


def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = Exercice5Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Exercice5Parser(stream)
    parser.full_expr()  # We want to recognize full_expr in the grammar Example2
    print("Finished")


# warns pb if py file is included in others
if __name__ == '__main__':
    main()
