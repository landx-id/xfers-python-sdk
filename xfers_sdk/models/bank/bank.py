from xfers_sdk._api_requestor import _APIRequestor
from .entity.bank import BankEntity
from .entity.bank_account import BankAccountEntity
from xfers_sdk.xfers_error import XfersError
from xfers_sdk.models._to_model import _to_model
from xfers_sdk._extract_params import _extract_params
from xfers_sdk._post_attributes import _post_attributes


class Bank:
    @staticmethod
    def account_validation(
        *,
        account_no: str,
        bank_short_code: str,
        **kwargs
    ) -> BankAccountEntity:
        """Bank Account Validation (API Reference: Bank Account Validation)

        Args:
          - account_no (str)
          - bank_short_code (str)

        Returns:
          BankAccountEntity

        Raises:
          XfersError

        """

        url = f"/validation_services/bank_account_validation"

        headers, body = _extract_params(
            locals(),
            func_object=Bank.account_validation,
        )
        kwargs["body"] = _post_attributes(body)

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=BankAccountEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def list(
        **kwargs,
    ) -> BankEntity:
        """Send GET Request to List All Bank (API Reference: List Disbursement Banks)

        Returns:
          BankEntity

        Raises:
          XfersError

        """

        url = f"/banks"

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=BankEntity, data=resp.body)
        else:
            raise XfersError(resp)
