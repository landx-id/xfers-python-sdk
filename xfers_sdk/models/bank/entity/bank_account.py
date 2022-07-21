from dataclasses import dataclass

@dataclass
class BankAccountAttributes:
    account_no: str
    bank_short_code: str

@dataclass
class BankAccountData:
    attributes: BankAccountAttributes

@dataclass
class BankAccountEntity:
    data: BankAccountData
