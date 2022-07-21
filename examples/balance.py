import os
from xfers_sdk.xfers import Xfers

API_KEY = os.getenv('XFERS_API_KEY')
SECRET_KEY = os.environ.get('XFERS_SECRET_KEY')
x = Xfers(api_key=API_KEY, secret_key=SECRET_KEY, production=False)

balance = x.Balance
print(balance.get())
