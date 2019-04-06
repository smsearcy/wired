import pytest

from wired import ServiceRegistry


@pytest.fixture
def registry():
    from factory.app import setup
    r: ServiceRegistry = setup()
    return r

def test_greet_a_customer(registry):
    from factory.app import greet_a_customer
    actual = greet_a_customer(registry)
    assert 'Hello !!' == actual
