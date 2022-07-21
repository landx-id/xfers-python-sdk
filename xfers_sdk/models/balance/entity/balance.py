from dataclasses import dataclass

@dataclass
class BalanceAttributes:
    total_balance: str
    available_balance: str
    pending_balance: str

@dataclass
class BalanceData:
    attributes: BalanceAttributes

@dataclass
class BalanceEntity:
    data: BalanceData
