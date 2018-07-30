from fixture.methods import *


def test_login(app):
    app.methodsHelper.login_user()
    assert app.get_logged_username() == config.userName


__author__ = 'GiSDeCain'
