from dataclasses import dataclass
from enum import Enum
from typing import Any


class TokenType(Enum):
    INT = "INT"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MUL = "MUL"
    DIV = "DIV"
    EOF = "EOF"


@dataclass
class Token:
    type: TokenType
    value: Any = None


CHARS_AS_TOKENS = {
    "+": Token(TokenType.PLUS),
    "-": Token(TokenType.MINUS),
    "*": Token(TokenType.MUL),
    "/": Token(TokenType.DIV),
}


class Tokenizer:
    def __init__(self, code):
        self.code = code
        self.ptr = 0

    def next_token(self):
        # ignore spaces
        while self.ptr < len(self.code) and self.code[self.ptr] == " ":
            self.ptr += 1

        # check for end of file
        if self.ptr >= len(self.code):
            return Token(TokenType.EOF)

        # create a token
        char = self.code[self.ptr]
        self.ptr += 1

        if char in "0123456789":
            return Token(TokenType.INT, int(char))
        elif token := CHARS_AS_TOKENS.get(char):
            return token

    def all_tokens(self):
        tokens = []
        while (tok := self.next_token()).type != TokenType.EOF:
            tokens.append(tok)
        tokens.append(tok)
        return tokens


class TreeNode:
    pass


@dataclass
class Int:
    value: int


@dataclass
class BinOp:
    op: str
    left: Int
    right: Int


class Parser:
    """
    program := computation EOF

    computation := number PLUS number
    number := INT
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.ptr = 0

    def parse(self):
        comp = self.parse_computation()
        self.eat(TokenType.EOF)
        return comp

    def eat(self, expected_token_type):
        token = self.tokens[self.ptr]
        if token.type != expected_token_type:
            raise RuntimeError("1 / 0")
        return token


if __name__ == "__main__":
    tok = Tokenizer("3 + + + + + 5")
    print(tok.all_tokens())
