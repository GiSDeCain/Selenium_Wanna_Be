from methods import *
import pytest

def test_Login():
    wd = driver()
    open_main_page(wd)
    login_user(wd)
    close_browser(wd)


test_Login()


__author__ = 'GiSDeCain'
