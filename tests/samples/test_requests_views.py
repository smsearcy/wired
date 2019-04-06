import pytest

from wired import ServiceRegistry


@pytest.fixture
def settings():
    from wired.samples.requests_views import Settings
    settings = Settings(punctuation='!!')
    return settings


@pytest.fixture
def registry(settings):
    from wired.samples.requests_views import app_bootstrap
    r: ServiceRegistry = app_bootstrap(settings)
    return r


def test_sample_interactions(registry):
    # Integration-style test

    from wired.samples.requests_views import sample_interactions
    greetings = sample_interactions(registry)
    assert 'Hello Mary !!' == greetings[0]
    assert 'Bonjour Henri !!' == greetings[1]
