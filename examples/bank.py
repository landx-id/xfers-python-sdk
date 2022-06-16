import os
from landx_xfers_sdk.xfers import Xfers

API_KEY = os.getenv('XFERS_API_KEY')
SECRET_KEY = os.environ.get('XFERS_SECRET_KEY')
x = Xfers(api_key=API_KEY, secret_key=SECRET_KEY, production=False)

bank = x.Bank
# Bank Account Validation
print(bank.account_validation(account_no="123456", bank_short_code="BNI"))
