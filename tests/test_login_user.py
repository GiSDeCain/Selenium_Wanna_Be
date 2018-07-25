from fixture.methods import *


def test_login():
    wd = driver()
    open_main_page(wd)
    login_user(wd)
    assert get_logged_username(wd) == config.userName
    close_browser(wd)


__author__ = 'GiSDeCain'
