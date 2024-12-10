from Lexer import *
from Parser2 import *
import Rules
from ParseTable import ParseTable

code = Lexer.read_code('code.j')
tokens = Lexer(code).tokenize()
parse_table = ParseTable(Rules.productions, Rules.FIRST, Rules.FOLLOW)
parsing_table = parse_table.get_parsing_table()
LL1(tokens, parsing_table).parse()

