from Lexer import Lexer
from Parser2 import LL1
import Rules
from ParseTable import ParseTable

code = Lexer.read_code('code.j')
tokens = Lexer(code).tokenize()
parse_table = ParseTable(Rules.productions, Rules.FIRST, Rules.FOLLOW)
parsing_table = parse_table.get_parsing_table()

result, stack_input_rule_list = LL1(tokens, parsing_table).parse()
print(result)
