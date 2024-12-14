from flask import Flask, render_template, request, jsonify, redirect, url_for
from Lexer import *
from Parser2 import *
import Rules
from ParseTable import ParseTable

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/parse", methods=["POST"])
def parse():
    if request.method == "POST":
        body = request.get_json()
        print(body)
        code = body["code"]
        try:
            tokens = Lexer(code).tokenize()
            parse_table = ParseTable(Rules.productions, Rules.FIRST, Rules.FOLLOW)
            parsing_table = parse_table.get_parsing_table()

            result, stack_input_rule_list = LL1(tokens, parsing_table).parse()
            return jsonify(stack_input_rule_list)
        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 400
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
