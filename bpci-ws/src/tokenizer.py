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
        if self.ptr >= len(self.code):
            return Token(TokenType.EOF)  # end of file

        char = self.code[self.ptr]
        self.ptr += 1

        if char in "0123456789":
            return Token(TokenType.INT, int(char))
        elif token := CHARS_AS_TOKENS.get(char):
            return token


if __name__ == "__main__":
    tok = Tokenizer("3 + 5")
    print(tok.next_token())
    print(tok.next_token())
    print(tok.next_token())
    print(tok.next_token())
