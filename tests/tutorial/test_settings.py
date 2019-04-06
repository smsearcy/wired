import pytest

from wired import ServiceRegistry


@pytest.fixture
def settings():
    from settings.app import Settings

    settings = Settings(punctuation='!!')
    return settings


@pytest.fixture
def registry(settings):
    from settings.app import setup

    r: ServiceRegistry = setup(settings)
    return r


def test_greet_a_customer(registry):
    from settings.app import greet_a_customer

    actual = greet_a_customer(registry)
    assert 'Hello !!' == actual
