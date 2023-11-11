from dataclasses import dataclass
from enum import Enum
from typing import Any


class TokenType(Enum):
    INT = "INT"
    PLUS = "PLUS"


@dataclass
class Token:
    type: TokenType
    value: Any
