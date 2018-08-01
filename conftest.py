import pytest
from fixture.app import Application


@pytest.fixture
def app(request):
    fixture = Application()
    fixture.open_home_page()
    request.addfinalizer(fixture.destroy)
    return fixture


__author__ = 'GiSDeCain'
