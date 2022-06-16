from dataclasses import dataclass
from typing import Optional

@dataclass
class PaymentIntructions:
    bank_short_code: Optional[str]
    account_no: Optional[str]
    display_name: Optional[str]
    image_url: Optional[str]
    retail_outlet_name: Optional[str]
    payment_code: Optional[str]

@dataclass
class PaymentMethod:
    type: str
    reference_id: str
    instructions: PaymentIntructions

@dataclass
class PaymentAttributes:
    status: str
    amount: str
    created_at: str
    description: Optional[str]
    expired_at: str
    reference_id: str
    fees: str
    payment_method: PaymentMethod

@dataclass
class PaymentData:
    id: str
    type: str
    attributes: PaymentAttributes

@dataclass
class PaymentEntity:
    data: PaymentData
