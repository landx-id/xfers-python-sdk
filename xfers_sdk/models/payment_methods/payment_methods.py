from .entity.manage_payment_method import ManagePaymentMethodEntity
from .entity.payment_methods import PaymentMethodsEntity
from .entity.payment_method import PaymentMethodEntity
from xfers_sdk._api_requestor import _APIRequestor
from xfers_sdk._extract_params import _extract_params
from xfers_sdk.xfers_error import XfersError
from xfers_sdk._post_attributes import _post_attributes
from xfers_sdk.models._to_model import _to_model
from humps import camelize

class PaymentMethods:
    """Payment Methods class (API Reference: Payment Methods)

    Related Classes:
      - PaymentMethodEntity

    Static Methods:
      - PaymentMethods.create (API Reference: /Create Payment Methods)
      - PaymentMethods.get (API Reference: /Retrieve Payment Method)
      - PaymentMethods.list (API Reference: /List Payment Method's Payments)
      - PaymentMethods.manage (API Reference: /Managing Payment Methods)
    """

    @staticmethod
    def create(
        *,
        type,
        reference_id,
        display_name,
        bank_short_code=None,
        suffix_no=None,
        **kwargs,
    ) -> PaymentMethodEntity:
        """Send POST Request to create Payment Methods (API Reference: Payment Methods/Create Payment Method)

        Args:
          - type (str)
          - reference_id (str)
          - display_name (str)
          - **bank_short_code (string)
          - **suffix_no

        Returns:
          PaymentMethodEntity

        Raises:
          XfersError

        """
        if type not in ["virtual_bank_accounts", "qris"]:
            raise Exception("Type not sypported")

        url = f"/payment_methods/{type}"
        ignore_params = ["type"] if type == "virtual_bank_accounts" else ["type", "bank_short_code", "suffix_no"]
        headers, body = _extract_params(
            locals(),
            func_object=PaymentMethods.create,
            ignore_params=ignore_params
        )
        kwargs["headers"] = headers
        kwargs["body"] = _post_attributes(body)

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=PaymentMethodEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def get(
        *,
        type,
        payment_method_id,
        **kwargs,
    ) -> PaymentMethodEntity:
        """Send GET Request to retrieve Payment Methods (API Reference: Payment Methods/Retrieve Payment Method)

        Args:
          - type (str)
          - payment_method_id (str)

        Returns:
          PaymentMethodEntity

        Raises:
          XfersError

        """
        if type not in ["virtual_bank_accounts", "qris"]:
            raise Exception("Type not sypported")

        url = f"/payment_methods/{type}/{payment_method_id}"

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=PaymentMethodEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def list(
        *,
        payment_method_id,
        created_before=None,
        created_after=None,
        reference_id=None,
        status=None,
        **kwargs,
    ) -> PaymentMethodsEntity:
        """Send GET Request to retrieve Payment Methods (API Reference: Payment Methods/List Payment Method's Payments)

        Args:
          - payment_method_id (str)
          - **created_before,
          - **created_after,
          - **reference_id,
          - **status,

        Returns:
          PaymentMethodsEntity

        Raises:
          XfersError

        """

        url = f"/payment_methods/virtual_bank_accounts/{payment_method_id}/payments"

        headers, body = _extract_params(
            locals(),
            func_object=PaymentMethods.list,
            ignore_params=["payment_method_id"]
        )
        kwargs["params"] = camelize(body)

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=PaymentMethodsEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def receive_payment(
        *,
        payment_method_id,
        amount:float,
        **kwargs,
    ) -> ManagePaymentMethodEntity:
        """Simulates a payment received from the customer for a given payment. Status will be changed to 'paid'. (API Reference: Payment Methods/Managing Payment Methods)

        Args:
          - payment_method_id (str)
          - amount (float)

        Returns:
          PaymentMethodsEntity

        Raises:
          XfersError

        """

        url = f"/payment_methods/virtual_bank_accounts/{payment_method_id}/tasks"

        kwargs["body"] = _post_attributes({
            "action": "receive_payment",
            "options": {
                "amount": amount
            }
        })

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=ManagePaymentMethodEntity, data=resp.body)
        else:
            raise XfersError(resp)
