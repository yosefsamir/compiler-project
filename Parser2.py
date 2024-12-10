from tokens import *
class LL1:
    def __init__(self , tokens , Parsing_table):
        self.tokens = tokens
        self.Parsing_table = Parsing_table
        self.stack = []
        self.stack.append('$')
        self.stack.append('Program') 

    def parse(self):
        input_pointer = 0
        current_token = self.tokens[input_pointer].lexeme
        if isinstance(self.tokens[input_pointer], IntegerToken) or isinstance(self.tokens[input_pointer], FloatToken):
            current_token = 'num'
        elif isinstance(self.tokens[input_pointer], StringToken) or isinstance(self.tokens[input_pointer], CharacterToken):
            current_token = 'str'
        elif isinstance(self.tokens[input_pointer], IdentifierToken):
            current_token = 'id'

        print("Starting LL(1) Parsing")
        print(f"Initial Stack: {self.stack}")
        print(f"Initial Tokens: {[token.lexeme for token in self.tokens]}")

        while self.stack:
            top = self.stack[-1]
            print("\n--- Parsing Step ---")
            print(f"Stack: {self.stack} --> top")
            print(f"Current Token: {current_token}")
            print(f"top: {top}")


            if top == '$' and current_token == '$':
                print("Parsing complete. Input is valid.")
                return
            elif top == current_token:
                print(f"Match found: {top}, popping stack and moving to next token.")
                self.stack.pop()
                input_pointer += 1
                if input_pointer < len(self.tokens):
                    current_token = self.tokens[input_pointer].lexeme
                    if isinstance(self.tokens[input_pointer], IntegerToken) or isinstance(self.tokens[input_pointer], FloatToken):
                        current_token = 'num'
                    elif isinstance(self.tokens[input_pointer], StringToken) or isinstance(self.tokens[input_pointer], CharacterToken):
                        current_token = 'str'
                    elif isinstance(self.tokens[input_pointer], IdentifierToken):
                        current_token = 'id'
                else:
                    current_token = '$'
            elif top in self.Parsing_table:
                rule = self.Parsing_table[top].get(current_token)
                if rule:
                    print(f"Applying rule: {top} → {rule}")
                    self.stack.pop()

                    for symbol in reversed(rule.split()):
                        if symbol != "ε":
                            self.stack.append(symbol)
                elif "ε" in self.Parsing_table[top]:
                    print(f"Applying rule: {top} → ε")
                    self.stack.pop() 
                else:
                    print(f"Error: No rule found for top: {top} and current_token: {current_token}")
                    return
            else:
                print(f"Error: Unexpected token {current_token} while parsing {top}")
                return

                    
                


