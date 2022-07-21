import os
from xfers_sdk.xfers import Xfers

API_KEY = os.getenv('XFERS_API_KEY')
SECRET_KEY = os.environ.get('XFERS_SECRET_KEY')
x = Xfers(api_key=API_KEY, secret_key=SECRET_KEY, production=False)

class VirtualAccount:
    @staticmethod
    def create():
        payment_method = x.PaymentMethod
        return payment_method.create(
            type="virtual_bank_accounts",
            reference_id="12345678",
            bank_short_code="SAHABAT_SAMPOERNA",
            display_name="Coba coba",
            # suffix_no="082325001300"
        )

    @staticmethod
    def get(payment_method_id):
        payment_method = x.PaymentMethod
        return payment_method.get(
            type="virtual_bank_accounts",
            payment_method_id=payment_method_id
        )

    @staticmethod
    def list(payment_method_id):
        payment_method = x.PaymentMethod
        return payment_method.list(
            payment_method_id=payment_method_id
        )

    @staticmethod
    def receive_payment(payment_method_id, amount):
        payment_method = x.PaymentMethod
        return payment_method.receive_payment(
            payment_method_id=payment_method_id,
            amount=amount
        )

create = VirtualAccount.create()
print("-- create --")
print(create.data)

# print("-- get from create --")
# get = VirtualAccount.get(payment_method_id=create.data.id)
# print(get.data)

# print("-- list --")
# list = VirtualAccount.list(payment_method_id="va_0fa99769f0ff1ba3c6cbb1dd65b5aece")
# print(list.data)

# print("-- receive payment --")
# receive_payment = VirtualAccount.receive_payment(payment_method_id="va_0fa99769f0ff1ba3c6cbb1dd65b5aece", amount=90000)
# print(receive_payment)
