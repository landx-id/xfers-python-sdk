from dataclasses import dataclass
from typing import Optional

@dataclass
class PaymentMethodIntructions:
    """Payment Method Instruction class (API Reference: Payment Methods)
    Attributes:
      - **bank_short_code (str)
      - **account_no (string)
      - **display_name (string)
      - **image_url (string)
    """
    bank_short_code: Optional[str]
    account_no: Optional[str]
    display_name: Optional[str]
    image_url: Optional[str]

@dataclass
class PaymentMethodAttributes:
    """Payment Method Data class (API Reference: Payment Methods)
    Attributes:
      - reference_id (str)
      - instructions: (PaymentMethodIntructions)
    """
    reference_id: str
    instructions: PaymentMethodIntructions

@dataclass
class PaymentMethodData:
    """Payment Method Data class (API Reference: Payment Methods)
    Attributes:
      - id (str)
      - type (str)
      - attributes (PaymentMethodAttributes)
    """
    id: str
    type: str
    attributes: PaymentMethodAttributes

@dataclass
class PaymentMethodEntity:
    """Payment Method class (API Reference: Payment Methods)
    Attributes:
      - data (PaymentMethodData)
    """

    data: PaymentMethodData
