from inspect import signature

from .models import PaymentMethods, Payment, Balance, Bank, PaymentLink, Disbursements


class _XfersParamInjector:
    """Builder class to inject parameters (api_key, base_url, http_client) to feature class"""

    def __init__(self, params):
        self.params = params

    def instantiate_payment_methods(self) -> PaymentMethods:
        return self.instantiate(PaymentMethods)

    def instantiate_payment(self) -> Payment:
        return self.instantiate(Payment)

    def instantiate_balance(self) -> Balance:
        return self.instantiate(Balance)

    def instantiate_bank(self) -> Bank:
        return self.instantiate(Bank)

    def instantiate_payment_link(self) -> PaymentLink:
        return self.instantiate(PaymentLink)

    def instantiate_disbursements(self)->Disbursements:
        return self.instantiate(Disbursements)

    def instantiate(self, injected_class):
        """Inject every static method in `injected_class` with provided parameters.

        Args:
          - injected_class (class): Class that will be injected

        Return:
          injected_class
        """
        params = self.params

        injected_class = type(
            injected_class.__name__,
            injected_class.__bases__,
            dict(injected_class.__dict__),
        )
        for keys, value in vars(injected_class).items():
            if type(value) == staticmethod and not keys.startswith("_"):
                _XfersParamInjector._inject_function(
                    injected_class, params, keys, value
                )
        return injected_class

    @staticmethod
    def _inject_function(injected_class, params, func_name, func_value):
        """Inject `func_name` function with params"""
        api_key, secret_key, production, http_client = params
        attr = func_value.__func__

        def inject_func_with_api_key(*args, **kwargs):
            kwargs["api_key"] = api_key
            kwargs["secret_key"] = secret_key
            kwargs["production"] = production
            kwargs["http_client"] = http_client
            result = attr(*args, **kwargs)
            return result

        inject_func_with_api_key.__signature__ = signature(attr)
        setattr(injected_class, func_name, staticmethod(inject_func_with_api_key))
