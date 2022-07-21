from .entity.disbursements import DisbursementEntity, DisbursementList, DisbursementTask
from xfers_sdk._api_requestor import _APIRequestor
from xfers_sdk._extract_params import _extract_params
from xfers_sdk.xfers_error import XfersError
from xfers_sdk._post_attributes import _post_attributes
from xfers_sdk.models._to_model import _to_model
from urllib import parse


class Disbursements:
    """Disbursements class (API Reference: Disbursements)

    Related Classes:
      - DisbursementsEntity

    Static Methods:
      - Disbursements.create (API Reference: /Create Disbursement)
    """
    @staticmethod
    def create(
        *,
        amount,
        reference_id,
        bank_shortcode,
        bank_account_no,
        bank_account_holder_name,
        description="",
        **kwargs
    ) -> DisbursementEntity:
        url = "/disbursements"
        headers, body = _extract_params(
            locals(),
            func_object=Disbursements.create,
        )

        kwargs["headers"] = headers
        body = _post_attributes(body)
        disbursement_method = {
            "type": "bank_transfer",
            "bankShortCode": bank_shortcode,
            "bankAccountNo": bank_account_no,
            "bankAccountHolderName": bank_account_holder_name
        }
        body["data"]["attributes"].update({
            "amount": amount,
            "referenceId": reference_id,
            "description": description,
            "disbursementMethod": disbursement_method
        })

        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if 200 <= resp.status_code < 300:
            return _to_model(model=DisbursementEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def get(
        *,
        disbursement_id,
        **kwargs
    ) -> DisbursementEntity:
        url = f"/disbursements/{disbursement_id}"
        resp = _APIRequestor.get(url, **kwargs)
        if 200 <= resp.status_code < 300:
            return _to_model(model=DisbursementEntity, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def list(
        *,
        created_before="",
        created_after="",
        reference_id="",
        status="",
        **kwargs
    ) -> DisbursementList:
        query = {
            "createdBefore": created_before,
            "createdAfter": created_after,
            "referenceId": reference_id,
            "status": status
        }
        str_query = parse.urlencode(query)
        url = f"/disbursements?{str_query}"
        resp = _APIRequestor.get(url, **kwargs)
        if 200 <= resp.status_code < 300:
            return _to_model(model=DisbursementList, data=resp.body)
        else:
            raise XfersError(resp)

    @staticmethod
    def action(
        *,
        disbursement_id,
        action_name,
        **kwargs
    ):
        if action_name not in ["complete", "fail"]:
            raise Exception("Type not supported")

        url = f"/disbursements/{disbursement_id}/tasks"
        kwargs["body"] = _post_attributes({
            "action": action_name
        })
        resp = _APIRequestor.post(url, **kwargs)

        if 200 <= resp.status_code < 300:
            return _to_model(model=DisbursementTask, data=resp.body)
        else:
            raise XfersError(resp)
