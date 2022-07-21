# Xfers Python Library

This library is the abstraction of Xfers API for access from applications written with Python.

## Table of Contents

- [API Documentation](#api-documentation)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [API Key](#api-key)
  - [Using Custom HTTP Client](#using-custom-http-client)
  - [Balance](#balance)
    - [Get Balance](#get-balance)
  - [Bank](#bank)
    - [Bank Account Validation](#bank-account-validation)
    - [List Disbursement Banks](#list-disbursement-bank)
  - [Payment](#payment)
    - [Virtual Account](#virtual-account)
    - [QRIS](#qris)
    - [Retail Outlet](#retail-outlet)
    - [E-Wallet](#e-wallet)
  - [Retrieve a Payment](#retrieve-a-payment)
  - [Managing Payments](#managing-payments)
  - [Disbursements](#disbursements)

    
## API Documentation
Please check [Xfers API Reference](https://docs.xfers.com/reference).

## Requirements

Python 3.7 or later

## Installation

To use the package, run ```pip install xfers-sdk```

## Usage

### API Key

```python
from landx_xfers_sdk import Xfers
xfers = Xfers(api_key="test-key123", secret_key="12345678")

# Then access each class from x attribute
balance = xfers.Balance
balance.get()
```


### Balance

#### Get Balance

```python
balance = xfers.Balance
balance.get()
```

Usage example:

```python
from landx_xfers_sdk import Xfers
xfers = Xfers(api_key="test-key123", secret_key="12345678", production=False)

# Then access each class from x attribute
balance = xfers.Balance
print(balance.get())
``` 

Reference: https://docs.xfers.com/reference/account-balance

### Bank Service

#### Bank Account Validation

```python
bank = xfers.Bank
bank.account_validation(account_no="123456", bank_short_code="BNI")
```

Reference: https://docs.xfers.com/reference/bank-account-validation

#### List Disbursement Banks
```python
bank = xfers.Bank
bank.list()
```

Reference: https://docs.xfers.com/reference/list-disbursement-banks

### Payment

There are 2 main ways to accept payments with Xfers.

-  One time payment
  Use `xfers.Payment` instance
- Persistent payment method linked to one of your customers
  Use `xfers.PaymentMethod` instance

Reference: https://docs.xfers.com/docs/accepting-payments



#### Virtual Account


##### Create One Time Payment

```python
payment = xfers.Payment
payment.create(
  type="virtual_bank_account",
  amount=10000,
  expired_at=datetime.now() +  timedelta(days=1), # One Day
  reference_id="va_12345678",
  bank_short_code="SAHABAT_SAMPOERNA",
  display_name="Your preferred name",
  description="Payment Description"
  # suffix_no="12345678"
)
```

API Reference: https://docs.xfers.com/reference/create-payment

##### Create Persistent Payment

```python
payment_method = xfers.PaymentMethod
payment_method.create(
  type="virtual_bank_accounts",
  reference_id="12345678",
  bank_short_code="SAHABAT_SAMPOERNA",
  display_name="Your preferred name",
  # suffix_no="12345678"
)
```

API Reference: https://docs.xfers.com/reference/create-payment-method



#### QRIS

##### Create One Time Payment

```python
payment = xfers.Payment
payment.create(
  type="qris",
  amount=10000,
  expired_at=datetime.now() +  timedelta(days=1), # One Day
  reference_id="qris_12345678",
  display_name="Your preferred name",
  description="Payment Description"
)
```

API Reference: https://docs.xfers.com/reference/create-payment

##### Create Persistent Payment

```python
payment_method = xfers.PaymentMethod
payment_method.create(
  type="qris",
  reference_id="12345678",
  display_name="Your preferred name"
)
```

API Reference: https://docs.xfers.com/reference/create-payment-method



#### Retail Outlet

##### Create Payment

```python
payment = xfers.Payment
payment.create(
  type="retail_outlet",
  amount=10000,
  expired_at=datetime.now() +  timedelta(days=1), # One Day
  reference_id="qris_12345678",
  retail_outlet_name="ALFAMART",
  display_name="Your preferred name",
  description="Payment Description"
)
```
Available Outlets: https://docs.xfers.com/docs/retail-store#available-outlets

API Reference: https://docs.xfers.com/reference/create-payment



####  E-Wallet

##### Create Payment

```python
payment = xfers.Payment
payment.create(
  type="e-wallet",
  amount=10000,
  expired_at=datetime.now() +  timedelta(days=1), # One Day
  reference_id="qris_12345678",
  provider_code="SHOPEEPAY",
  after_settlement_return_url="https://pay.examplessee.co.id/return-pay-here?0340450",
  display_name="Your preferred name",
  description="Payment Description"
)
```
List of E-Wallet: https://docs.xfers.com/docs/e-wallet#list-of-e-wallet

API Reference: https://docs.xfers.com/reference/create-payment

#### Retrieve a Payment

Retrieves a Payment object that was previously requested.

###### One time payment

```python
payment = xfers.Payment
payment.get(payment_id="va_1234567")
```

API Reference: https://docs.xfers.com/reference/retrieve-payment

###### Persistent payment

type = The type of payment method. Currently support "virtual_bank_accounts" and "qris".

```python
payment_method = xfers.PaymentMethod
payment_method.get(type="virtual_bank_accounts", payment_id="va_1234567")
```

API Reference: https://docs.xfers.com/reference/retrieve-payment-method



### Managing Payments

#### Persistent Payment (PaymentMethod)

##### Receive Payment

Simulates a payment received from the customer for a given payment. Status will be changed to 'paid'.

```python
payment_method = xfers.PaymentMethod
payment_method.receive_payment(
  payment_method_id="va_123456789",
  amount=90000
)
```

#### One Time Payment (Payment)

##### Receive Payment [Sandbox Mode]

Simulates a payment received from the customer for a given payment. Status will be changed to 'paid'.

```python
payment = xfers.Payment
payment.receive_payment(
  payment_method_id="va_123456789",
)
```

##### Receive Payment [Sandbox Mode]

Simulates a payment received from the customer for a given payment. Status will be changed to 'paid'.

```python
payment = xfers.Payment
payment.receive_payment(
  payment_method_id="va_123456789",
)
```

##### Cancel Payment

Cancel a payment when it is still in pending state. Status will be changed to 'cancelled'.
(This is only available for One-off Virtual Account at the moment.)


```python
payment = xfers.Payment
payment.cancel(
  payment_method_id="va_123456789",
)
```

##### Settle Payment [Sandbox Mode]

Simulates funds for a payment being made available for transfer or withdrawal. Status will be changed to 'completed'.


```python
payment = xfers.Payment
payment.settle(
  payment_method_id="va_123456789",
)
```

### Disbursements

#### Create Disbursements
Creates a Disbursement object that will send funds from your Xfers account to an intended recipient.

```python
xfers.Disbursements.create(amount="10000",
                      reference_id="123",
                      bank_shortcode="BCA",
                      bank_account_no="0123123123",
                      bank_account_holder_name="john doe")
```

### Retrieve a Disbursement
Retrieves a Disbursement object that was previously requested.

```python
xfers.Disbursements.get(disbursement_id="id")
```

### List All Disbursement
Returns a list of Disbursements.

```python
xfers.Disbursements.list(created_after="2022-04-15")
```
