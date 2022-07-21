from dataclasses import dataclass
from typing import Optional, List


@dataclass
class DisbursementMethod:
    type: str
    bank_account_no: str
    bank_short_code: str
    bank_name: str
    bank_account_holder_name: Optional[str]
    server_bank_account_holder_name: str


@dataclass
class DisbursementAttributes:
    reference_id: str
    description: Optional[str]
    amount: str
    status: str
    created_at: str
    fees: str
    failure_reason: Optional[str]
    disbursement_method: DisbursementMethod


@dataclass
class DisbursementData:
    id: str
    type: str
    attributes: DisbursementAttributes


@dataclass
class DisbursementEntity:
    data: DisbursementData


@dataclass
class DisbursementList:
    data: List[DisbursementData]


@dataclass
class DisbursementTaskAttribute:
    target_id: str
    target_type: str
    action: str


@dataclass
class DisbursementTaskData:
    type: str
    attributes: DisbursementTaskAttribute


@dataclass
class DisbursementTask:
    data: DisbursementTaskData
