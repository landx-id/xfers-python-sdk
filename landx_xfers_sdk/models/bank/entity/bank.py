from dataclasses import dataclass
from typing import List

@dataclass
class BankAttributes:
    name: str
    short_code: str

@dataclass
class BankData:
    id: str
    type: str
    attributes: BankAttributes

@dataclass
class BankEntity:
    data: List[BankData]
