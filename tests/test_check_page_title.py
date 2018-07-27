from fixture.methods import *


def test_check_page_title():
    get_page_title(wd)
    assert wd.title == config.mainPageTitle


__author__ = 'GiSDeCain'
