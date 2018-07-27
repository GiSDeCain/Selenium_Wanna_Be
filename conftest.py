import pytest
from fixture.app import App


@pytest.fixture()
def app(request):
    fixture = App("http://forum.attnauka.webd.pro""")
    request.addfinalizer(fixture.destroy)
    return fixture


def open_main_page(app):
    app.open_main_page()


__author__ = 'GiSDeCain'
