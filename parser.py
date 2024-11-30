class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse_program(self):
        functions = []
        while self.current < len(self.tokens):
            functions.append(self.parse_function())
        return functions

    def parse_function(self):
        # Match 'Type Identifier ( ParameterList ) { Statement* }'
        func_type = self.consume('type')
        identifier = self.consume('identifier')
        self.consume('(')
        parameters = self.parse_parameter_list()
        self.consume(')')
        self.consume('{')
        statements = self.parse_statements()
        self.consume('}')
        return {'type': func_type, 'name': identifier, 'parameters': parameters, 'statements': statements}

    def parse_parameter_list(self):
        parameters = []
        while self.current < len(self.tokens) and self.tokens[self.current]['token class'] != ')':
            parameters.append(self.parse_parameter())
            if self.tokens[self.current]['lexeme'] == ',':
                self.consume(',')
        return parameters

    def parse_parameter(self):
        param_type = self.consume('type')
        param_name = self.consume('identifier')
        return {'type': param_type, 'name': param_name}

    def parse_statements(self):
        statements = []
        while self.current < len(self.tokens) and self.tokens[self.current]['lexeme'] != '}':
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        # This would match an 'if' statement, assignment, etc.
        if self.tokens[self.current]['lexeme'] == 'if':
            return self.parse_if_statement()
        elif self.tokens[self.current]['lexeme'] == 'return':
            return self.parse_return_statement()
        # Add other statements like assignments, loops, etc.

    def consume(self, expected_class):
        token = self.tokens[self.current]
        if token['token class'] == expected_class:
            self.current += 1
            return token['lexeme']
        else:
            raise SyntaxError(f"Expected {expected_class}, but found {token['token class']}")

