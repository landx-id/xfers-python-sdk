from xfers_sdk._api_requestor import _APIRequestor
from .entity.balance import BalanceEntity
from xfers_sdk.xfers_error import XfersError
from xfers_sdk.models._to_model import _to_model

class Balance:
    @staticmethod
    def get(**kwargs) -> BalanceEntity:
        """Send GET Request to check for your account balance (API Reference: Account Balance)

        Returns:
          BalanceEntity

        Raises:
          XfersError

        """

        url = f"/overviews/balance_overview"

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return _to_model(model=BalanceEntity, data=resp.body)
        else:
            raise XfersError(resp)
