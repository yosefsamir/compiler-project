productions = {
    "Program": {"Declaration Program_Tail", "Statement Program_Tail"},
    "Program_Tail": {"Program", "ε"},
    "Declaration": {"Variable_Declaration", "Function_Definition"},
    "Variable_Declaration": {"Type Identifier Variable_Declaration_Tail"},
    "Variable_Declaration_Tail": {
        "End_Line",
        "= Expression End_Line",
        "[ Number ] Variable_Array_Tail",
    },
    "Variable_Array_Tail": {"End_Line", "= { Array_Values } End_Line"},
    "Type": {
        "int",
        "float",
        "char",
        "string",
        "bool",
        "big int",
        "double",
        "small int",
    },
    "Array_Values": {"Expression Array_Values_Tail"},
    "Array_Values_Tail": {", Expression Array_Values_Tail", "ε"},
    "Function_Definition": {"function Identifier ( Parameters ) { Program }"},
    "Parameters": {"Parameter Parameters_Tail"},
    "Parameters_Tail": {", Parameter Parameters_Tail", "ε"},
    "Parameter": {"Type Identifier Parameter_Tail"},
    "Parameter_Tail": {"{ }", "= Expression", "ε"},
    "Statement": {
        "Assignment",
        "If_Statement",
        "While_Statement",
        "For_Statement",
        "Return_Statement",
        "Function_Call",
        "Print",
    },
    "Assignment": {"Identifier = Expression End_Line"},
    "If_Statement": {"if ( Conditions ) { Program } If_Statement_Tail"},
    "If_Statement_Tail": {"Else_If_Statements Optional_Else"},
    "Else_If_Statements": {"Else_If_Statement Else_If_Statements", "ε"},
    "Else_If_Statement": {"elseif ( Conditions ) { Program }"},
    "Optional_Else": {"Else_Statement", "ε"},
    "Else_Statement": {"else { Program }"},
    "While_Statement": {"while ( Conditions ) { Program }"},
    "For_Statement": {"for ( Parameters ; Conditions ; Assignment ) { Program }"},
    "Return_Statement": {"return Expression End_Line"},
    "Function_Call": {"Identifier ( Arguments ) End_Line"},
    "Arguments": {"Arguments_Tail"},
    "Arguments_Tail": {", Expression Arguments_Tail", "ε"},
    "Expression": {"Term Expression_Tail"},
    "Expression_Tail": {"+ Term Expression_Tail", "- Term Expression_Tail", "ε"},
    "Term": {"Factor Term_Tail"},
    "Term_Tail": {"* Factor Term_Tail", "/ Factor Term_Tail", "ε"},
    "Factor": {"Identifier", "Number", "string_literal", "( Expression )"},
    "Conditions": {"Condition Conditions_Tail"},
    "Conditions_Tail": {
        "&& Condition Conditions_Tail",
        "|| Condition Conditions_Tail",
        "ε",
    },
    "Condition": {"Expression Relational_Operator Expression"},
    "Relational_Operator": {"==", "!=", "<", "<=", ">", ">="},
    "Print": {"print ( Expression ) End_Line"},
    "End_Line": {";"},
    "Identifier": {"id"},
    "string_literal": {"str"},
    "Number": {"num"},
}


def call_first(s, productions):
    first = set()
    for production in productions[s]:

        for symbol in production.split():
            if symbol not in productions:
                first.add(symbol)
                break
            else:
                non_terminal_first = call_first(symbol, productions)
                first.update(non_terminal_first - {"ε"})
                if "ε" not in non_terminal_first:
                    break
                elif symbol == production.split()[-1]:
                    first.add("ε")

    return first


def call_follow(s, productions, first, follow):
    if s not in follow:
        follow[s] = set()
    if s == list(productions.keys())[0]:
        follow[s].add("$")

    for lhs, rhs_list in productions.items():
        for rhs in rhs_list:
            if s in rhs.split():
                idx = rhs.split().index(s)
                if idx == len(rhs.split()) - 1:
                    if lhs != s:
                        follow[s].update(follow[lhs])
                else:
                    next_symbol = rhs.split()[idx + 1]
                    if next_symbol not in productions:
                        follow[s].add(next_symbol)
                    else:
                        next_first = first[next_symbol]
                        follow[s].update(next_first - {"ε"})
                        if "ε" in next_first:
                            if lhs != s:
                                follow[s].update(follow[lhs])

    return follow


FIRST = {}
for non_terminal in productions:
    FIRST[non_terminal] = call_first(non_terminal, productions)


FOLLOW = {}
for non_terminal in productions:
    FOLLOW[non_terminal] = set()

for non_terminal in productions:
    FOLLOW = call_follow(non_terminal, productions, FIRST, FOLLOW)
