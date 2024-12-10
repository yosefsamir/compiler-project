class ParseTable:
    def __init__(self, productions, FIRST, FOLLOW):
        self.productions = productions
        self.FIRST = FIRST
        self.FOLLOW = FOLLOW
        self.terminals = set()
        self.non_terminals = productions.keys()
        self.parsing_table = {non_terminal: {t: None for t in self.terminals} for non_terminal in self.non_terminals}
        self._compute_terminals()
        self._fill_parsing_table()

    def _compute_terminals(self):
        for key, values in self.FIRST.items():
            self.terminals.update(values)
        self.terminals.add("$") 

    def _compute_first_set(self, rule):
        first_set = set()
        for symbol in rule.split():
            if symbol in self.FIRST:
                first_set.update(self.FIRST[symbol] - {"ε"})
                if "ε" not in self.FIRST[symbol]:
                    break
            else:
                first_set.add(symbol)
                break
        else:
            first_set.add("ε")
        return first_set

    def _fill_parsing_table(self):
        for non_terminal, rules in self.productions.items():
            for rule in rules:
                first_set = self._compute_first_set(rule)
                for terminal in first_set:
                    if terminal != "ε":
                        self.parsing_table[non_terminal][terminal] = rule
                if "ε" in first_set:
                    for terminal in self.FOLLOW[non_terminal]:
                        self.parsing_table[non_terminal][terminal] = rule

    def get_parsing_table(self):
        return self.parsing_table

    def write_to_file(self, file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Parsing Table:\n\n")
            for non_terminal, row in self.parsing_table.items():
                f.write(f"{non_terminal}:\n")
                for terminal, rule in row.items():
                    if rule is not None:
                        f.write(f"  {terminal}: {rule}\n")
                f.write("\n")
        print(f"Parsing table has been written to {file_path}")
