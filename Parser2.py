from tokens import *

class LL1:
    def __init__(self, tokens, Parsing_table):
        self.tokens = tokens
        self.Parsing_table = Parsing_table
        self.stack = []
        self.stack.append('$')
        self.stack.append('Program')
        self.trace = []

    def parse(self):
        stack_input_rule_list = []
        input_pointer = 0
        print("Parsing...")
        if len(self.tokens) == 0:
            return True, stack_input_rule_list
        current_token = self.tokens[input_pointer].lexeme
        if isinstance(self.tokens[input_pointer], IntegerToken) or isinstance(self.tokens[input_pointer], FloatToken):
            current_token = 'num'
        elif isinstance(self.tokens[input_pointer], StringToken) or isinstance(self.tokens[input_pointer], CharacterToken):
            current_token = 'str'
        elif isinstance(self.tokens[input_pointer], IdentifierToken):
            current_token = 'id'
        result = False
        while self.stack:
            top = self.stack[-1]

            self.trace.append({
                "stack": list(self.stack),
                "input": [token.lexeme for token in self.tokens[input_pointer:]] + ["$"],
                "rule": ""
            })

            if top == '$' and current_token == '$':
                self.trace[-1]["rule"] = "Parsing complete"
                result = True
                break
            elif top == current_token:
                self.stack.pop()
                self.trace[-1]["rule"] = f"Match: {top}"
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
                    self.stack.pop()
                    self.trace[-1]["rule"] = f"{top} → {rule}"

                    for symbol in reversed(rule.split()):
                        if symbol != "ε":
                            self.stack.append(symbol)
                elif "ε" in self.Parsing_table[top]:
                    self.stack.pop()
                    self.trace[-1]["rule"] = f"{top} → ε"
                else:
                    self.trace[-1]["rule"] = f"Error: No rule for {top} with {current_token}"
                    break
            else:
                self.trace[-1]["rule"] = f"Error: Unexpected token {current_token}"
                break

        # Write to file
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(f"{'Stack':<150} {'Input':<120} {'Rule'}\n")
            file.write("-" * 300 + "\n")
            for step in self.trace:
                stack_str = " ".join(step["stack"])
                input_str = " ".join(step["input"])
                rule_str = step["rule"]
                # TODO: Remove print statements
                # print("Stack:", stack_str)
                # print("Input:", input_str)
                # print("Rule:", rule_str)
                stack_input_rule_list.append({"stack": stack_str, "input": input_str, "rule": rule_str})
                file.write(f"{stack_str:<150} {input_str:<120} {rule_str}\n")

        print("Parsing trace has been written to output.txt")
        return result, stack_input_rule_list
