from dataclasses import dataclass

@dataclass
class ManagePaymentOptions:
    amount: str

@dataclass
class ManagePaymentAttributes:
    target_id: str
    target_type: str
    options: ManagePaymentOptions

@dataclass
class ManagePaymentData:
    type: str
    attributes: ManagePaymentAttributes


@dataclass
class ManagePaymentMethodEntity:
    data: ManagePaymentData
