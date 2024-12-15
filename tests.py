from ParseTable import ParseTable
from Lexer import Lexer
from Parser2 import LL1
import Rules
import sys

def create_source_code_file(source_code):
    try:
        with open("source_code.txt", "w", encoding="utf-8") as f:
            f.write(source_code)
    except Exception as e:
        print(e)


def delete_source_code_file():
    try:
        import os

        os.remove("source_code.txt")
    except Exception as e:
        print(e)

FAILING_TESTS = {
    "test_while_loop": {
        "source_code": """
        int i = 0;
        while (i < 10) {
            print(i);
            i = i + 1;
        }
        """,
        "should_pass": True,
    },
    "test_print_statement": {
        "source_code": """
        print("Hello World");
        """,
        "should_pass": True,
    },
}

TESTING = {
    "test_for_loop": {
        "source_code": """
        for (int i = 0 ; i < 10; i = i + 1;){
            print(i);
        }
        """,
        "should_pass": True,
    },
    "test_function": {
        "source_code": """
        string s = "ahmed";
        function display(string data)
        {
            print(data);
        }
        display(s);
        """,
        "should_pass": True,
    },
    "test_invalid_code": {
        "source_code": """
        string string = "ahmed";
        """,
        "should_pass": False,
    },
    # FAILING TESTS
    "test_while_loop": {
        "source_code": """
        int i = 0;
        while (i < 10) {
            print(i);
            i = i + 1;
        }
        """,
        "should_pass": True,
    },
    "test_if_statement": {
        "source_code": """
        int i = 0;
        if (i < 10){
            print(i);
        }
        """,
        "should_pass": True,
    },
    "test_invalid_if_statement": {
        "source_code": """
        if (i <== 10){
            print(i);
        }
        """,
        "should_pass": False,
    },
    "test_invalid_define_variable": {
        "source_code": """
        int int = 10;
        """,
        "should_pass": False,
    },
    "test_invalid_define_function": {
        "source_code": """
        function function(){
            print("Hello, World!");
        }
        """,
        "should_pass": False,
    },
    "test_invalid_function": {
        "source_code": """
        function gg(){
            if
            print("Hello, World!");
        }
        """,
        "should_pass": False,
    },
    "test_invalid_function_parameter": {
        "source_code": """
        function gg(int int){
        }
        """,
        "should_pass": False,
    },
    "test_empty_source_code": {
        "source_code": """
        """,
        "should_pass": True,
    },
    "test_double_declare": {
        "source_code": """
        double xxx = 32;
        """,
        "should_pass": True,
    },
    
    "test_invalid_declare": {
        "source_code": """
        int 123abc = 45;
        """,
        "should_pass": False,
    },
    "test_array_declare": {
        "source_code": """
        int arr[5] = {1, 2, 3, 4, 5};
        """,
        "should_pass": True,
    },
    "test_function_definition": {
        "source_code": """
        function myFunc(int a, double b) {
            return a + b;
        }
        """,
        "should_pass": True,
    },
    # might fail
    "test_function_call": {
        "source_code": """
        myFunc(5, 3.14);
        """,
        "should_pass": True,
    },
    "test_missing_semicolon": {
        "source_code": """
        int a = 10
        """,
        "should_pass": False,
    },
    "test_nested_if_else": {
        "source_code": """
        if (a > b) {
            if (c < d) {
                print(c);
            } else {
                print(d);
            }
        }
        """,
        "should_pass": True,
    },
    "test_invalid_operator": {
        "source_code": """
        int x = 5 ** 2;
        """,
        "should_pass": False,
    },
    "test_array_missing_braces": {
        "source_code": """
        int arr[5] = 1, 2, 3, 4, 5;
        """,
        "should_pass": False,
    },
    # might fail
    "test_nested_function_calls": {
        "source_code": """
        print(sum(add(1, 2), 3));
        """,
        "should_pass": True,
    },
    "test_invalid_if_syntax": {
        "source_code": """
        if a > b {
            print(a);
        }
        """,
        "should_pass": False,
    },
    "test_return_statement": {
        "source_code": """
        return a * b + c;
        """,
        "should_pass": True,
    },
    # might fail
    "test_empty_function": {
        "source_code": """
        function empty() {
        }
        """,
        "should_pass": True,
    },
    "test_missing_function_body": {
        "source_code": """
        function invalid();
        """,
        "should_pass": False,
    },
    
    "test_int_declare": {
        "source_code": """
        int a = 10;
        """,
        "should_pass": True,
    },
    "test_float_declare": {
        "source_code": """
        float x = 3.14;
        """,
        "should_pass": True,
    },
    "test_char_declare": {
        "source_code": """
        char c = 'a';
        """,
        "should_pass": True,
    },
    "test_string_declare": {
        "source_code": """
        string name = "John";
        """,
        "should_pass": True,
    },
    "test_bool_declare": {
        "source_code": """
        bool isActive = true;
        """,
        "should_pass": True,
    },
    # test failed
    "test_big_int_declare": {
        "source_code": """
        big int largeNumber = 123456789012345;
        """,
        "should_pass": True,
    },
    # test failed
    "test_small_int_declare": {
        "source_code": """
        small int smallNum = 5;
        """,
        "should_pass": True,
    },
    "test_variable_declaration_no_value": {
        "source_code": """
        int age;
        """,
        "should_pass": True,
    },
    "test_array_assignment": {
        "source_code": """
        int arr[3] = {1, 2, 3};
        """,
        "should_pass": True,
    },
    "test_function_definition_with_parameters": {
        "source_code": """
        function add(int x, int y) {
            return x + y;
        }
        """,
        "should_pass": True,
    },
    # test failed
    "test_function_with_no_parameters": {
        "source_code": """
        function printMessage() {
            print("Hello");
        }
        """,
        "should_pass": True,
    },
    # test failed
    "test_function_with_return": {
        "source_code": """
        function getValue() {
            return 42;
        }
        """,
        "should_pass": True,
    },
    "test_invalid_function_declaration": {
        "source_code": """
        function int add(x, y) {
            return x + y;
        }
        """,
        "should_pass": False,
    },
    # test failed
    "test_function_call_with_no_arguments": {
        "source_code": """
        printMessage();
        """,
        "should_pass": True,
    },
    "test_function_call_with_arguments": {
        "source_code": """
        add(5, 7);
        """,
        "should_pass": True,
    },
    "test_missing_function_parameter_type": {
        "source_code": """
        function add(x, y) {
            return x + y;
        }
        """,
        "should_pass": False,
    },
    "test_assignment_with_expression": {
        "source_code": """
        int b = a + 10;
        """,
        "should_pass": True,
    },
    "test_if_statement_without_else": {
        "source_code": """
        if (x < y) {
            print(x);
        }
        """,
        "should_pass": True,
    },
    "test_nested_if_statements": {
        "source_code": """
        if (a > b) {
            if (c < d) {
                print(c);
            }
        }
        """,
        "should_pass": True,
    },
    "test_elseif_statements": {
        "source_code": """
        if (a > b) {
            print(a);
        } elseif (a == b) {
            print("Equal");
        } else {
            print(b);
        }
        """,
        "should_pass": True,
    },
    # test failed
    "test_while_loop_basic": {
        "source_code": """
        while (a < 10) {
            a = a + 1;
        }
        """,
        "should_pass": True,
    },
    "test_invalid_while_syntax": {
        "source_code": """
        while a < 10 {
            a = a + 1;
        }
        """,
        "should_pass": False,
    },
    "test_invalid_for_syntax": {
        "source_code": """
        for int i = 0 i < 10 i = i + 1 {
            print(i);
        }
        """,
        "should_pass": False,
    },
    "test_for_loop_missing_semicolon": {
        "source_code": """
        for (int i = 0 i < 10; i = i + 1) {
            print(i);
        }
        """,
        "should_pass": False,
    },
    "test_return_statement_with_expression": {
        "source_code": """
        return a * 10;
        """,
        "should_pass": True,
    },
    # test failed
    "test_print_statement": {
        "source_code": """
        print(aa);
        """,
        "should_pass": True,
    },
    "test_print_with_expression": {
        "source_code": """
        print(a + b);
        """,
        "should_pass": True,
    },
    "test_invalid_print_syntax": {
        "source_code": """
        print Hello World;
        """,
        "should_pass": False,
    },
    "test_nested_for_loops": {
        "source_code": """
        for (int i = 0; i < 10; i = i + 1;) {
            for (int j = 0; j < 5; j = j + 1;) {
                print(i * j);
            }
        }
        """,
        "should_pass": True,
    },
    "test_multiple_statements": {
        "source_code": """
        int x = 5;
        int y = 10;
        print(x + y);
        """,
        "should_pass": True,
    },
    "test_invalid_condition_in_if": {
        "source_code": """
        if a > b {
            print(a);
        }
        """,
        "should_pass": False,
    },
    "test_expression_with_multiple_terms": {
        "source_code": """
        int z = x + y * 2 - 3;
        """,
        "should_pass": True,
    },
    "test_invalid_operator_in_expression": {
        "source_code": """
        int z = x % 2;
        """,
        "should_pass": False,
    },
    # test failed
    "test_function_with_array_return_type": {
        "source_code": """
        function getArray() {
            int arr[3] = {1, 2, 3};
            return arr;
        }
        """,
        "should_pass": True,
    },
    "test_invalid_array_declaration": {
        "source_code": """
        int arr[] = {1, 2, 3};
        """,
        "should_pass": False,
    },
    "test_condition_with_relational_operator": {
        "source_code": """
        if (x == y) {
            print("Equal");
        }
        """,
        "should_pass": True,
    },
    "test_invalid_relational_operator": {
        "source_code": """
        if (x <=> y) {
            print("Invalid");
        }
        """,
        "should_pass": False,
    },
    # test failed
    "test_empty_program": {
        "source_code": """
        """,
        "should_pass": True,
    },
    "test_invalid_comment_syntax": {
        "source_code": """
        /* This is an invalid comment
        int x = 10;
        """,
        "should_pass": False,
    },
}

tests = None
args = sys.argv
if len(args) > 1 and args[1] == "all":
    tests = TESTING
elif len(args) > 1 and args[1] == "f":
    tests = FAILING_TESTS
else:
    tests = TESTING
def test_parser_1():
    success_counter = 0
    results = []
    parse_table = ParseTable(Rules.productions, Rules.FIRST, Rules.FOLLOW)
    parsing_table = parse_table.get_parsing_table()
    
    for test_name, value in tests.items():
        try:
            source_code = value["source_code"]
            should_pass = value["should_pass"]
            create_source_code_file(source_code)
            code = Lexer.read_code("source_code.txt")
            tokens = Lexer(code).tokenize()
            result, li = LL1(tokens, parsing_table).parse()

            if result != should_pass:
                results.append(f"Test {test_name} failed.")
            else:
                results.append(f"Test {test_name} successed.")
                success_counter += 1

        except Exception as e:
            print(e)
            results.append(f"Test {test_name} failed.")
    delete_source_code_file()

    print("-" * 90)
    print("Testing Results:")
    for result in results:
        # input("Press Enter to continue...")
        print(result)

    print(f"Successed {success_counter}/{len(tests)}")


if __name__ == "__main__":
    print("Running all tests...")
    test_parser_1()
