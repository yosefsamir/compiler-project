from tokens import *
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.token = self.tokens[self.index]

    def move(self):
        self.index += 1
        if self.index < len(self.tokens):
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
        elif isinstance(self.token , IdentifierToken):
            left_node = self.variable()
            if self.token.lexeme == "=":
                operation = self.token.lexeme
                self.move()
                right_node = self.expression()
                return [left_node, operation, right_node]
        elif isinstance(self.token, (IntegerToken, FloatToken, IdentifierToken)): 
            return self.expression()
        elif isinstance(self.token, KeywordToken) and self.token.lexeme == "if":
            return self.if_statement()
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


    def if_statement(self):
        if self.token.lexeme == "if":
            self.move()
            if self.token.lexeme == "(":
                self.move()
                conditions = self.conditions()
                if self.token.lexeme == ")":
                    self.move()
                    if self.token.lexeme == "{":
                        self.move()
                        program = self.program()
                        if self.token.lexeme == "}":
                            self.move()
                            else_if_statement = None
                            else_statement = None
                            if self.token.lexeme == "else":
                                else_statement = self.else_statement()
                            elif self.token.lexeme == "elseif":
                                else_if_statement = self.else_if_statement()
                            return {"type": "if", "conditions": conditions, "program": program, 
                                    "else_if": else_if_statement, "else": else_statement}
        raise SyntaxError(f"Expected 'if' statement, but found {self.token.lexeme}")

    def else_if_statement(self):
        else_if_nodes = []
        while self.token.lexeme == "elseif":
            self.move()  # Skip 'elseif'
            if self.token.lexeme == "(":
                self.move()
                conditions = self.conditions()
                if self.token.lexeme == ")":
                    self.move()
                    if self.token.lexeme == "{":
                        self.move()
                        program = self.program()
                        if self.token.lexeme == "}":
                            self.move()
                            else_if_nodes.append({"conditions": conditions, "program": program})
                        else:
                            raise SyntaxError(f"Expected '}}', but found {self.token.lexeme}")
        return else_if_nodes

    def else_statement(self):
        if self.token.lexeme == "else":
            self.move()
            if self.token.lexeme == "{":
                self.move()
                program = self.program()
                if self.token.lexeme == "}":
                    self.move()
                    return program
        raise SyntaxError(f"Expected 'else' statement, but found {self.token.lexeme}")

    def conditions(self):
        condition_node = self.condition()
        tail_node = self.conditions_tail()
        return {"condition": condition_node, "tail": tail_node}

    def conditions_tail(self):
        if self.token.lexeme in ["&&", "||"]:
            operator = self.token.lexeme
            self.move()
            condition_node = self.condition()
            tail_node = self.conditions_tail()
            return {"operator": operator, "condition": condition_node, "tail": tail_node}
        return None  # ε (empty)

    def condition(self):
        left_expr = self.expression()
        relational_operator = self.relational_operator()
        right_expr = self.expression()
        return {"left": left_expr, "operator": relational_operator, "right": right_expr}

    def relational_operator(self):
        if self.token.lexeme in ["==", "!=", "<", "<=", ">", ">="]:
            operator = self.token.lexeme
            self.move()
            return operator
        raise SyntaxError(f"Expected relational operator, but found {self.token.lexeme}")

    def program(self):
        program_statements = []
        while self.token.lexeme != "}":
            statement = self.statement()
            program_statements.append(statement)
            if self.token.lexeme == ";":
                self.move()
        return program_statements

    def peek(self, n):
        if self.index + n < len(self.tokens):
            return self.tokens[self.index + n]
        return None
