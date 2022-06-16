from dataclasses import dataclass

@dataclass
class PaymentLinkAttributes:
    status: str
    amount: str
    reference_id: str
    created_at: str
    description: str
    expired_at: str
    payment_link_url: str
    customer_name: str
    customer_email: str
    customer_phone_number: str
    display_name: str

@dataclass
class PaymentLinkData:
    attributes: PaymentLinkAttributes

@dataclass
class PaymentLinkEntity:
    data: PaymentLinkData
