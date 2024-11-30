import re
class Lexer:
    def __init__(self, code):
        self.code = code.replace('\n', ' ')
        self.tokens = []
        self.length = len(self.code)

    def length_of_str(self, word):
        return len(word)

    def compare_str(self, word1, word2):
        return word1 == word2

    def substring(self, word, left, right):
        return word[left:right]

    def is_operator(self, word):
        operators = ['+=', '-=', '*=', '/=', '==', '!=', '>=', '<=', '&&', '||', '+', '-', '*', '/', '>', '<', '=', '!']
        return word in operators

    def is_delimiter(self, word):
        delimiters = [' ', '(', ')', '[', ']', '{', '}', ',', ';', '+', '-', '*', '/', '=']
        return word in delimiters

    def is_valid_identifier(self, word):
        if word[0].isalpha() or word[0] == '_':
            for i in range(1, len(word)):
                if not (word[i].isalpha() or word[i].isdigit() or word[i] == '_'):
                    return False
            return True
        return False

    def is_keyword(self, word):
        keywords = ['int', 'float', 'double', 'char', 'string', 'signed', 'unsigned', 'do', 'if', 'else', 'while',
                    'for', 'return', 'break', 'continue', 'void', 'main', 'function', 'class', 'public', 'private',
                    'protected', 'static', 'go', 'stop', 'true', 'false', 'null', 'print']
        return word in keywords

    def is_integer(self, word):
        return bool(re.fullmatch(r'\d+', word))

    def is_scientific_number(self, word):
        return bool(re.fullmatch(r'[-+]?\d+(\.\d+)?[eE][-+]?\d+', word))

    def is_real_number(self, word):
        return bool(re.fullmatch(r'[-+]?\d*\.\d+', word))

    def tokenize(self):
        left = 0
        right = 0

        while self.length > right >= left:
            if not self.is_delimiter(self.code[right]):
                right += 1

            if self.is_delimiter(self.code[right]) and left == right:
                if self.is_operator(self.code[right]):
                    self.tokens.append({'token class': 'operator', 'lexeme': self.code[right]})

                elif self.is_delimiter(self.code[right]) and self.code[right] != ' ':
                    self.tokens.append({'token class': 'delimiter', 'lexeme': self.code[right]})

                right += 1
                left = right

            elif self.is_delimiter(self.code[right]) and left != right or (right == self.length and left != right):
                word = self.substring(self.code, left, right)
                if self.is_keyword(word):
                    self.tokens.append({'token class': 'keyword', 'lexeme': word})
                elif self.is_valid_identifier(word):
                    self.tokens.append({'token class': 'identifier', 'lexeme': word})
                elif self.is_integer(word):
                    self.tokens.append({'token class': 'integer', 'lexeme': word})
                elif self.is_scientific_number(word):
                    self.tokens.append({'token class': 'Scientific number', 'lexeme': word})
                elif self.is_real_number(word):
                    self.tokens.append({'token class': 'real number', 'lexeme': word})
                elif self.is_operator(word):
                    self.tokens.append({'token class': 'operator', 'lexeme': word})
                else:
                    self.tokens.append({'token class': 'invalid', 'lexeme': word})
                left = right

        return self.tokens

    @staticmethod
    def read_code(file):
        with open(file, 'r') as file:
            return file.read()
