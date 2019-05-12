from app import make_registry
from configure import register
from request import process_request


def test_greeter():
    registry = make_registry()
    register(registry)
    result = process_request(registry)
    assert 'Hello Larry my name is Mary' == result
