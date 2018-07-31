from pages.login_page import *


def test_login(app):
    app.open_home_page()
    app.login_page.login_user()
    assert app.main_page.get_logged_username() == Config.userName


__author__ = 'GiSDeCain'
