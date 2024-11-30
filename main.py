from Lexer import *
from parser import *

code = Lexer.read_code('code.j')
lexer = Lexer(code)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
