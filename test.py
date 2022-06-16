from cgi import test
from landx_xfers_sdk import __version__, Hello


def test_version():
    assert __version__ == '0.1.0'


def test_hello():
    res = Hello()
    assert res == "test"

print("version", __version__)
print(Hello())
