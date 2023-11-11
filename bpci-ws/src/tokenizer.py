from dataclasses import dataclass
from typing import Any


@dataclass
class Token:
    type: TokenType
    value: Any
