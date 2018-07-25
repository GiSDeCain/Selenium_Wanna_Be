from methods import *


def test_login():
    wd = driver()
    open_main_page(wd)
    login_user(wd)
    assert_is_correct_user_logged(wd)
    close_browser(wd)


__author__ = 'GiSDeCain'
