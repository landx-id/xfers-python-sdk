import os
from datetime import datetime, timedelta
from xfers_sdk.xfers import Xfers

API_KEY = os.getenv('XFERS_API_KEY')
SECRET_KEY = os.environ.get('XFERS_SECRET_KEY')
x = Xfers(api_key=API_KEY, secret_key=SECRET_KEY, production=False)

class VirtualAccount:
    @staticmethod
    def create():
        payment = x.Payment
        return payment.create(
            type="virtual_bank_account",
            amount=10000,
            expired_at=datetime.now() + timedelta(days=1),
            reference_id="va_12345678",
            bank_short_code="SAHABAT_SAMPOERNA",
            display_name="Coba coba",
            description="Ini coba"
            # suffix_no="12345678"
        )

    @staticmethod
    def get(payment_id):
        payment = x.Payment
        return payment.get(
            payment_id=payment_id
        )

    @staticmethod
    def list(payment_id):
        payment = x.Payment
        return payment.list(
            payment_id=payment_id
        )

    @staticmethod
    def receive_payment(payment_id):
        payment = x.Payment
        return payment.receive_payment(
            payment_id=payment_id,
        )

create = VirtualAccount.create()
print("-- create --")
print(create.data)

# print("-- get from create --")
# get = VirtualAccount.get(payment_id=create.data.id)
# print(get.data)

# print("-- list --")
# list = VirtualAccount.list(payment_id="va_0fa99769f0ff1ba3c6cbb1dd65b5aece")
# print(list.data)

# print("-- receive payment --")
# receive_payment = VirtualAccount.receive_payment(payment_id="va_0fa99769f0ff1ba3c6cbb1dd65b5aece", amount=90000)
# print(receive_payment)
