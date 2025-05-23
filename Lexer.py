import re
from tokens import RelationalOperatorToken, OperatorToken, DelimiterToken, KeywordToken, TypeToken, IdentifierToken, IntegerToken, ScientificNumberToken, FloatToken, StringToken, CharacterToken, InvalidToken


class Lexer:
    def __init__(self, code):
        self.code = code.replace('\n', ' ')
        self.tokens = []
        self.length = len(self.code)

    def length_of_str(self, word):
        return len(word)

    def substring(self, word, left, right):
        return word[left:right]

    def is_operator(self, word):
        operators = ['+', '-', '*', '/', '%']
        return word in operators

    def is_relational_operator(self, word):
        operators = ['==', '!=', '>=', '<=', '>', '<', '&&', '||']
        return word in operators

    def is_delimiter(self, word):
        delimiters = [' ', '(', ')', '[', ']', '{', '}', ',', ';', '+', '-', '*', '/', '=', '<', '>', '&', '|','%']
        return word in delimiters

    def is_valid_identifier(self, word):
        if word[0].isalpha() or word[0] == '_':
            for i in range(1, self.length_of_str(word)):
                if not word[i].isalnum() and word[i] != '_':
                    return False
            return True
        return False

    def is_type(self, word):
        types = ['int', 'float', 'double', 'char', 'string', 'bool', 'big int', 'small int']
        return word in types

    def is_keyword(self, word):
        keywords = ["function", "if", "while", "for", "elseif", "else", "return", "print", "main"]
        return word in keywords

    def is_integer(self, word):
        return bool(re.fullmatch(r'\d+', word))

    def is_scientific_number(self, word):
        return bool(re.fullmatch(r'[-+]?\d+(\.\d+)?[eE][-+]?\d+', word))

    def is_real_number(self, word):
        return bool(re.fullmatch(r'[-+]?\d*\.\d+', word))

    def is_string_literal(self, word):
        return bool(re.fullmatch(r'"[^"]*"', word))

    def is_character_literal(self, word):
        return bool(re.fullmatch(r"'.'", word))

    def tokenize(self):
        left = 0
        right = 0

        while self.length > right >= left:
            if self.code[right:right + 2] in ['>=', '<=', '==', '!=', '&&', '||']:
                self.tokens.append(RelationalOperatorToken(self.code[right:right + 2]))
                right += 2
                left = right
                continue

            if not self.is_delimiter(self.code[right]):
                right += 1

            if self.is_delimiter(self.code[right]) and left == right:
                if self.is_operator(self.code[right]):
                    self.tokens.append(OperatorToken(self.code[right]))
                elif self.is_relational_operator(self.code[right]):
                    self.tokens.append(RelationalOperatorToken(self.code[right]))
                elif self.is_delimiter(self.code[right]) and self.code[right] != ' ':
                    self.tokens.append(DelimiterToken(self.code[right]))
                right += 1
                left = right

            elif self.is_delimiter(self.code[right]) and left != right or (right == self.length and left != right):
                word = self.substring(self.code, left, right)
                if self.is_keyword(word):
                    self.tokens.append(KeywordToken(word))
                elif self.is_type(word):
                    self.tokens.append(TypeToken(word))
                elif self.is_valid_identifier(word):
                    self.tokens.append(IdentifierToken(word))
                elif self.is_integer(word):
                    self.tokens.append(IntegerToken(word))
                elif self.is_scientific_number(word):
                    self.tokens.append(ScientificNumberToken(word))
                elif self.is_real_number(word):
                    self.tokens.append(FloatToken(word))
                elif self.is_string_literal(word):
                    self.tokens.append(StringToken(word))
                elif self.is_character_literal(word):
                    self.tokens.append(CharacterToken(word))
                else:
                    self.tokens.append(InvalidToken(word))
                left = right

        return self.tokens

    @staticmethod
    def read_code(file):
        with open(file, 'r') as file:
            return file.read()
