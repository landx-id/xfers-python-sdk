from dataclasses import dataclass
from typing import List, Optional
from .payment_method import PaymentMethodIntructions

@dataclass
class PaymentMethod:
    type: str
    reference_id: str
    instructions: PaymentMethodIntructions

@dataclass
class PaymentMethodAttributes:
    status: str
    amount: str
    created_at: str
    description: Optional[str]
    expired_at: Optional[str]
    reference_id: str
    fees: str
    payment_method: PaymentMethod

@dataclass
class PaymentMethodData:
    id: str
    type: str
    attributes: PaymentMethodAttributes



@dataclass
class PaymentMethodsEntity:
    data: List[PaymentMethodData]
