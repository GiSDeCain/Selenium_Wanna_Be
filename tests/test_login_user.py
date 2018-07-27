from fixture.methods import *


def test_login():
    login_user(wd)
    assert get_logged_username(wd) == config.userName


__author__ = 'GiSDeCain'
