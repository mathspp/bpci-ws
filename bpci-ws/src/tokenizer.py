from dataclasses import dataclass
from enum import Enum
from typing import Any


class TokenType(Enum):
    INT = "INT"
    PLUS = "PLUS"
    EOF = "EOF"


@dataclass
class Token:
    type: TokenType
    value: Any = None


class Tokenizer:
    def __init__(self, code):
        self.code = code
        self.ptr = 0

    def next_token(self):
        if self.ptr >= len(self.code):
            return Token(TokenType.EOF)

        char = self.code[self.ptr]
        self.ptr += 1

        if char in "0123456789":
            return Token(TokenType.INT, int(char))
        elif char == "+":
            return Token(TokenType.PLUS)
