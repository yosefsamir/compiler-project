# Compiler Project - Lexical Analyzer and Parser Implementation

This project implements a lexical analyzer and parser for a custom programming language. It uses LL(1) parsing technique to validate the syntax of the input code.

## Project Structure

The project consists of the following core components:

### Source Files

1. **Main Entry Point (`main.py`)**
   - Orchestrates the compilation process
   - Reads input code
   - Coordinates tokenization and parsing
   - Generates output files

2. **Lexical Analyzer (`Lexer.py`)**
   - Implements lexical analysis
   - Tokenizes input code into meaningful tokens
   - Supports various token types including keywords, identifiers, operators, and literals

3. **Parser (`Parser.py`)**
   - Implements LL(1) parsing algorithm
   - Uses a parsing table to validate syntax
   - Generates detailed parsing trace
   - Outputs parsing results to `output.txt`

4. **Token Definitions (`tokens.py`)**
   - Defines various token classes:
     - `Token` (base class)
     - `KeywordToken`
     - `TypeToken`
     - `IdentifierToken`
     - `OperatorToken`
     - `RelationalOperatorToken`
     - `DelimiterToken`
     - `IntegerToken`
     - `FloatToken`
     - `ScientificNumberToken`
     - `StringToken`
     - `CharacterToken`
     - `InvalidToken`

5. **Grammar Rules (`Rules.py`)**
   - Defines the grammar productions
   - Implements FIRST and FOLLOW set computations
   - Contains grammar rules for:
     - Program structure
     - Variable declarations
     - Function definitions
     - Control structures (if, while, for)
     - Expressions and conditions

6. **Parse Table Generator (`ParseTable.py`)**
   - Generates LL(1) parsing table
   - Computes terminals and non-terminals
   - Writes parsing table to `parseTable.txt`

### Generated Files

1. `parseTable.txt`: Contains the LL(1) parsing table
2. `output.txt`: Contains the parsing trace and results

### Example Files

1. `code.j`: Example source code file demonstrating the language syntax

## Usage

1. Place your source code in a file named `code.j`
2. Run the compiler:
   ```bash
   python main.py
   ```
3. Check the output files:
   - `parseTable.txt`: Contains the LL(1) parsing table
   - `output.txt`: Contains the parsing trace

## Language Features

The language supports:
- Variable declarations with types (int, float, char, string, bool, etc.)
- Array declarations and initializations
- Function definitions with parameters
- Control structures (if-else, while, for loops)
- Arithmetic and relational expressions
- Function calls
- Print statements

## Output Files

1. `parseTable.txt`: Contains the LL(1) parsing table showing the grammar rules for each non-terminal and terminal combination
2. `output.txt`: Contains the detailed parsing trace showing:
   - Stack contents
   - Remaining input
   - Applied rules
   - Any parsing errors

## Dependencies

- Python 3.x
- No external dependencies required

## Development Setup

1. Clone the repository
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Run the compiler:
   ```bash
   python main.py
   ```

## Future Improvements

1. Add semantic analysis
2. Implement code generation
3. Add error recovery mechanisms
4. Include more comprehensive error messages
5. Add support for more language features
6. Implement optimization passes
7. Add unit tests
8. Include documentation for the language syntax

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.