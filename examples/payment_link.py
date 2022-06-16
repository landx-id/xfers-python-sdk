import os
from landx_xfers_sdk.xfers import Xfers
from datetime import datetime, timedelta

API_KEY = os.getenv('XFERS_API_KEY')
SECRET_KEY = os.environ.get('XFERS_SECRET_KEY')
x = Xfers(api_key=API_KEY, secret_key=SECRET_KEY, production=False)

payment_link = x.PaymentLink
create = payment_link.create(
    amount=90000,
    reference_id="test_134556789",
    customer_name="Pringgo Radianto",
    customer_email="pringgo@gmx.com",
    customer_phone_number="082325001300",
    description="Judul Pembayaran",
    expired_at=datetime.now() + timedelta(days=1),
    display_name="Coba Pembayaran",
)

print(create.data.id)

payment_link.get(payment_link_id=create.data.id)
