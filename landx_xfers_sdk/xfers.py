import requests

from ._xfers_param_injector import _XfersParamInjector

from .network import HTTPClientInterface


class Xfers:
    """Xfers instance. Initialize this with your API Key and Secret Key."""

    def __init__(
        self,
        api_key,
        secret_key,
        production=False,
        http_client: HTTPClientInterface = requests,
    ):
        injected_params = (api_key, secret_key, production, http_client)
        param_injector = _XfersParamInjector(injected_params)

        self.PaymentMethod = param_injector.instantiate_payment_methods()
        self.Payment = param_injector.instantiate_payment()
        self.Balance = param_injector.instantiate_balance()
        self.Bank = param_injector.instantiate_bank()
        self.PaymentLink = param_injector.instantiate_payment_link()
        self.Disbursements = param_injector.instantiate_disbursements()
