#from pages.login_page import *
from config.cfg import Config


def test_login(app):
    app.login_page.login_user(Config.userName, Config.passwd)
    assert app.common.get_logged_username() == Config.userName


__author__ = 'GiSDeCain'
