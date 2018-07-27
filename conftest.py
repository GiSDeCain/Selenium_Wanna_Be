import pytest
from fixture.app import Application


@pytest.fixture
def app(request):
    fixture = Application()
    #request.addfinlizer(fixture.destroy)
    return fixture

# @pytest.fixture
# def appp(request):
#     fixture = Application("http://google.pl")
#     request.addfinalizer(fixture.destroy)
#     return fixture


def open_home_page(app):
    app.open_home_page()

# def open_google_page(appp):
#     app.open_home_page()


__author__ = 'GiSDeCain'
