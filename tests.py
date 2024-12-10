from ParseTable import ParseTable
from Lexer import Lexer
from Parser2 import LL1
import Rules


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
}


def test_parser_1():
    success_counter = 0
    results = []
    parse_table = ParseTable(Rules.productions, Rules.FIRST, Rules.FOLLOW)
    parsing_table = parse_table.get_parsing_table()
    for test_name, value in TESTING.items():
        try:
            source_code = value["source_code"]
            should_pass = value["should_pass"]
            create_source_code_file(source_code)
            code = Lexer.read_code("source_code.txt")
            tokens = Lexer(code).tokenize()
            result = LL1(tokens, parsing_table).parse()

            if result != should_pass:
                results.append(f"Test {test_name} failed.")
            else:
                results.append(f"Test {test_name} successed.")
                success_counter += 1

            delete_source_code_file()
        except Exception as e:
            delete_source_code_file ()
            results.append(f"Test {test_name} failed.")

    print("-" * 90)
    print("Testing Results:")
    for result in results:
        print(result)

    print(f"Successed {success_counter}/{len(TESTING)}")


if __name__ == "__main__":
    print("Running all tests...")
    test_parser_1()
