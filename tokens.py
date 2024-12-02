class Token:
    def __init__(self, lexeme):
        self.lexeme = lexeme

    def __repr__(self):
        return f"{self.__class__.__name__}(lexeme='{self.lexeme}')"


class KeywordToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)


class TypeToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)


class IdentifierToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)


class OperatorToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)


class RelationalOperatorToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)


class DelimiterToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)


class IntegerToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)


class FloatToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)


class ScientificNumberToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)


class StringToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)


class CharacterToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)


class InvalidToken(Token):
    def __init__(self, lexeme):
        super().__init__(lexeme)
