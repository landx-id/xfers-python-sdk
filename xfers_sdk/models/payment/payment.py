import datetime
from xfers_sdk._api_requestor import _APIRequestor
from xfers_sdk._extract_params import _extract_params
from xfers_sdk.models.payment_methods.entity.manage_payment_method import ManagePaymentMethodEntity
from .entity.payment import PaymentEntity
from xfers_sdk.xfers_error import XfersError
from xfers_sdk._post_attributes import _post_attributes
from xfers_sdk.models._to_model import _to_model
from humps import camelize

class Payment:
    @staticmethod
    def create(
        *,
        type:str,
        amount:float,
        reference_id:str,
        expired_at,
        description:str=None,
        display_name:str,
        # Virtual Account
        bank_short_code:str=None,
        suffix_no:str=None,
        # Retail Outlet
        retail_outlet_name:str=None,
        # E-Wallet
        provider_code:str=None,
        after_settlement_return_url:str=None,
        **kwargs,
    ) -> PaymentEntity:
        if type not in ["virtual_bank_account", "qris", "retail_outlet", "e-wallet"]:
            raise Exception("Type not sypported")

        url = f"/payments"
        ignore_params = [
            "type",
            "bank_short_code",
            "suffix_no",
            "retail_outlet_name",
            "provider_code",
            "after_settlement_return_url",
            "expired_at"
        ]

        headers, body = _extract_params(
            locals(),
            func_object=Payment.create,
            ignore_params=ignore_params
        )
        kwargs["headers"] = headers
        body = _post_attributes(body)

        if type == "virtual_bank_account":
            payment_method_option = {
                "bankShortCode": bank_short_code,
                "displayName": display_name,
                "suffixNo": suffix_no
            }
        elif type == "retail_outlet":
            payment_method_option = {
                "retailOutletName": retail_outlet_name,
                "displayName": display_name,
            }
        elif type == "e-wallet":
            payment_method_option = {
                "provider_code": provider_code,
                "afterSettlementReturnUrl": after_settlement_return_url,
            }
        else:
            payment_method_option = {
                "displayName": display_name,
            }

        body["data"]["attributes"].update({
            "paymentMethodType": type,
            "paymentMethodOptions": payment_method_option,
            "expiredAt": expired_at.isoformat() if isinstance(expired_at, datetime.date) else expired_at
        })

        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=PaymentEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def get(
        *,
        payment_id,
        **kwargs,
    ) -> PaymentEntity:
        """Send GET Request to retrieve Payment (API Reference: Payment/Retrieve a Payment)

        Args:
          - payment_id (str)

        Returns:
          PaymentEntity

        Raises:
          XfersError

        """

        url = f"/payments/{payment_id}"

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=PaymentEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def list(
        *,
        created_before=None,
        created_after=None,
        reference_id=None,
        status=None,
        **kwargs,
    ) -> PaymentEntity:
        """Send GET Request to List All Payments (API Reference: Payment Methods/List Payment Method's Payments)

        Args:
          - **created_before,
          - **created_after,
          - **reference_id,
          - **status,

        Returns:
          PaymentMethodsEntity

        Raises:
          XfersError

        """

        url = f"/payments"

        headers, body = _extract_params(
            locals(),
            func_object=Payment.list,
        )
        kwargs["params"] = camelize(body)

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=PaymentEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def manage(
        *,
        payment_id,
        action,
        **kwargs,
    ) -> ManagePaymentMethodEntity:
        """Manage Payment (API Reference: Payment Methods/Managing Payment Methods)

        Args:
          - payment_id (str)
          - action (str)

        Returns:
          PaymentMethodsEntity

        Raises:
          XfersError

        """

        if action not in ["cancel", "receive_payment", "settle"]:
            raise Exception("Action not supported!")

        url = f"/payments/{payment_id}/tasks"

        kwargs["body"] = _post_attributes({
            "action": action
        })

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=ManagePaymentMethodEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def receive_payment(
        *,
        payment_id,
        **kwargs,
    ) -> ManagePaymentMethodEntity:
        """Simulates a payment received from the customer for a given payment. Status will be changed to 'paid'. (API Reference: Payment/Managing Payments)

        Args:
          - payment_id (str)

        Returns:
          PaymentMethodsEntity

        Raises:
          XfersError

        """

        return Payment.manage(payment_id=payment_id, action="receive_payment")

    @staticmethod
    def cancel(
        *,
        payment_id,
        **kwargs,
    ) -> ManagePaymentMethodEntity:
        """Cancel a payment when it is still in pending state. Status will be changed to 'cancelled'. (API Reference: Payment/Managing Payments)

        Args:
          - payment_id (str)

        Returns:
          PaymentMethodsEntity

        Raises:
          XfersError

        """

        return Payment.manage(payment_id=payment_id, action="cancel")

    @staticmethod
    def settle(
        *,
        payment_id,
        **kwargs,
    ) -> ManagePaymentMethodEntity:
        """Simulates funds for a payment being made available for transfer or withdrawal. Status will be changed to 'completed'. (API Reference: Payment/Managing Payments)

        Args:
          - payment_id (str)

        Returns:
          PaymentMethodsEntity

        Raises:
          XfersError

        """

        return Payment.manage(payment_id=payment_id, action="settle")
