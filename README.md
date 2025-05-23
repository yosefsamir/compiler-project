# Compiler Project - Lexical Analyzer and Parser Implementation

This project implements a lexical analyzer and parser for a custom programming language. It uses LL(1) parsing technique to validate the syntax of the input code.

## Project Structure

The project consists of several key components:

### Core Components

1. **Lexer (`Lexer.py`)**
   - Implements lexical analysis
   - Tokenizes input code into meaningful tokens
   - Supports various token types including keywords, identifiers, operators, and literals

2. **Parser (`Parser2.py`)**
   - Implements LL(1) parsing algorithm
   - Uses a parsing table to validate syntax
   - Generates detailed parsing trace
   - Outputs parsing results to `output.txt`

3. **Token Definitions (`tokens.py`)**
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

4. **Grammar Rules (`rules2.py`)**
   - Defines the grammar productions
   - Implements FIRST and FOLLOW set computations
   - Contains grammar rules for:
     - Program structure
     - Variable declarations
     - Function definitions
     - Control structures (if, while, for)
     - Expressions and conditions

5. **Parse Table Generator (`ParseTable.py`)**
   - Generates LL(1) parsing table
   - Computes terminals and non-terminals
   - Writes parsing table to `parseTable.txt`

### Main Entry Point

- `main.py`: Orchestrates the compilation process:
  1. Reads input code from `code.j`
  2. Tokenizes the code
  3. Generates parsing table
  4. Performs syntax analysis
  5. Outputs results

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

## Note

The project uses a custom file extension `.j` for source code files. Make sure your input code follows the grammar rules defined in `rules2.py`.

## Unused Files

Based on the current implementation, there might be some files that are not being used:
- `Rules.py` (referenced in main.py but not shown in the codebase)
- Any backup or old versions of files (if they exist)

## Future Improvements

1. Add semantic analysis
2. Implement code generation
3. Add error recovery mechanisms
4. Include more comprehensive error messages
5. Add support for more language features
6. Implement optimization passes
7. Add unit tests
8. Include documentation for the language syntax