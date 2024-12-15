from flask import Flask, render_template, request, jsonify, redirect, url_for
from Lexer import Lexer
from tokens import KeywordToken, TypeToken, IdentifierToken, OperatorToken, RelationalOperatorToken, DelimiterToken, IntegerToken, FloatToken, ScientificNumberToken, StringToken, CharacterToken, InvalidToken
from Parser2 import LL1
import Rules
from ParseTable import ParseTable
import webview

app = Flask(__name__)
window = webview.create_window("Parser GUI", app, width=1500, height=1000)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/parse", methods=["POST"])
def parse():
    if request.method == "POST":
        body = request.get_json()
        code = body["code"]
        try:
            tokens = Lexer(code).tokenize()
            tokens_list = []
            for token in tokens:
                if isinstance(token, KeywordToken):
                    type = "Keyword"
                elif isinstance(token, TypeToken):
                    type = "Type"
                elif isinstance(token, IdentifierToken):
                    type = "Identifier"
                elif isinstance(token, OperatorToken):
                    type = "Operator"
                elif isinstance(token, RelationalOperatorToken):
                    type = "Relational Operator"
                elif isinstance(token, DelimiterToken):
                    type = "Delimiter"
                elif isinstance(token, IntegerToken):
                    type = "Integer"
                elif isinstance(token, FloatToken):
                    type = "Float"
                elif isinstance(token, ScientificNumberToken):
                    type = "Scientific Number"
                elif isinstance(token, StringToken):
                    type = "String"
                elif isinstance(token, CharacterToken):
                    type = "Character"
                elif isinstance(token, InvalidToken):
                    type = "Invalid"
                tokens_list.append({"value": token.lexeme, "type": type})
                # tokens_list.append({"value": token.value, "type": token.type})
            # print(tokens_list)

            parse_table = ParseTable(Rules.productions, Rules.FIRST, Rules.FOLLOW)
            parsing_table = parse_table.get_parsing_table()

            result, stack_input_rule_list = LL1(tokens, parsing_table).parse()
            # print(stack_input_rule_list)
            data = {
                "lexer": tokens_list,
                "parser": stack_input_rule_list
            }
            return jsonify(data)
        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 400
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
    # webview.start()
