from tokens import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.token = self.tokens[self.index]

    def factor(self):
        if isinstance(self.token, (IntegerToken, FloatToken)): 
            value = self.token.lexeme
            self.move()
            return value
        elif isinstance(self.token, IdentifierToken):  
            var_name = self.token.lexeme
            self.move()
            return var_name
        elif self.token.lexeme == '(': 
            self.move()
            expr = self.expression()
            if self.token.lexeme != ')':
                raise SyntaxError(f"Expected ')', but found {self.token.lexeme}")
            self.move()
            return expr
        raise SyntaxError(f"Unexpected token: {self.token.lexeme}")

    def term(self):
        left_node = self.factor()
        while self.token.lexeme in ['*', '/']: 
            operation = self.token.lexeme
            self.move()
            right_node = self.factor()
            left_node = [left_node, operation, right_node]
        return left_node

    def expression(self):
        left_node = self.term()
        while self.token.lexeme in ['+', '-']: 
            operation = self.token.lexeme
            self.move()
            right_node = self.term()
            left_node = [left_node, operation, right_node]
        return left_node

    def variable(self):
        if isinstance(self.token, IdentifierToken):
            var_name = self.token.lexeme
            self.move()
            return var_name
        raise SyntaxError(f"Expected an identifier, but found {self.token.lexeme}")

    def statement(self):
        if isinstance(self.token, TypeToken):  
            self.move()
            left_node = self.variable()
            if self.token.lexeme == "=":
                operation = self.token.lexeme
                self.move()
                right_node = self.expression()
                return [left_node, operation, right_node]
        elif isinstance(self.token, (IntegerToken, FloatToken, IdentifierToken)): 
            return self.expression()
        raise SyntaxError(f"Invalid statement starting with {self.token.lexeme}")

    def parse(self):
        statements = []
        while self.index < len(self.tokens):
            statement = self.statement()
            if self.token.lexeme != ";":
                raise SyntaxError(f"Expected ';' at the end of the statement, but found {self.token.lexeme}")
            self.move()  
            statements.append(statement)
        return statements

    def move(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.token = self.tokens[self.index]
