import datetime
from xfers_sdk._api_requestor import _APIRequestor
from xfers_sdk.models.payment_methods.entity.manage_payment_method import ManagePaymentMethodEntity
from .entity.payment_link import PaymentLinkEntity
from xfers_sdk.xfers_error import XfersError
from xfers_sdk.models._to_model import _to_model
from xfers_sdk._extract_params import _extract_params
from xfers_sdk._post_attributes import _post_attributes

class PaymentLink:
    @staticmethod
    def create(
        *,
        amount:float,
        reference_id:str,
        customer_name:str,
        customer_email:str,
        customer_phone_number:str,
        description:str=None,
        expired_at=None,
        display_name=None,
        **kwargs
    ) -> PaymentLinkEntity:
        """Creates a Payment Link object that will allow you to receive payments from your customer. (API Reference: Payment Link/Create Payment Link)

        Returns:
          PaymentLinkEntity

        Raises:
          XfersError

        """

        url = f"/payment_links"

        headers, body = _extract_params(
            locals(),
            func_object=PaymentLink.create,
            ignore_params=["expired_at", "display_name"]
        )
        kwargs["headers"] = headers

        body.update({
            "expired_at": expired_at.isoformat() if isinstance(expired_at, datetime.date) else expired_at,
            "payment_method_options": {
                "display_name": display_name,
            }
        })

        body = _post_attributes(body)
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=PaymentLinkEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def get(
        *,
        payment_link_id,
        **kwargs,
    ) -> PaymentLinkEntity:
        """Retrieves a Payment Link object that was previously requested. (API Reference: Payment Link/Retrieve a Payment Link)

        Args:
          - payment_link_id (str)

        Returns:
          PaymentLinkEntity

        Raises:
          XfersError

        """

        url = f"/payment_links/{payment_link_id}"

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=PaymentLinkEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def manage(
        *,
        payment_link_id,
        action,
        **kwargs,
    ) -> ManagePaymentMethodEntity:
        """Manage Payment Link (API Reference: Payment Link/Managing Payment Link)

        Args:
          - payment_link_id (str)
          - action (str)

        Returns:
          PaymentMethodsEntity

        Raises:
          XfersError

        """

        if action not in ["cancel", "receive_payment", "settle"]:
            raise Exception("Action not supported!")

        url = f"/payment_links/{payment_link_id}/tasks"

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
        payment_link_id,
        **kwargs,
    ) -> ManagePaymentMethodEntity:
        """Simulates a payment received from the customer for a given payment. Status will be changed to 'paid'. (API Reference: Payment/Managing Payments)

        Args:
          - payment_link_id (str)

        Returns:
          PaymentMethodsEntity

        Raises:
          XfersError

        """

        return PaymentLink.manage(payment_link_id=payment_link_id, action="receive_payment")

    @staticmethod
    def cancel(
        *,
        payment_link_id,
        **kwargs,
    ) -> ManagePaymentMethodEntity:
        """Cancel a payment when it is still in pending state. Status will be changed to 'cancelled'. (API Reference: Payment/Managing Payments)

        Args:
          - payment_link_id (str)

        Returns:
          PaymentMethodsEntity

        Raises:
          XfersError

        """

        return PaymentLink.manage(payment_link_id=payment_link_id, action="cancel")

    @staticmethod
    def settle(
        *,
        payment_link_id,
        **kwargs,
    ) -> ManagePaymentMethodEntity:
        """Simulates funds for a payment being made available for transfer or withdrawal. Status will be changed to 'completed'. (API Reference: Payment/Managing Payments)

        Args:
          - payment_link_id (str)

        Returns:
          PaymentMethodsEntity

        Raises:
          XfersError

        """

        return PaymentLink.manage(payment_link_id=payment_link_id, action="settle")
