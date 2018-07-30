from fixture.methods import *


def test_login(app):
    app.methods.login_user()
    assert app.get_logged_username() == config.userName


__author__ = 'GiSDeCain'
