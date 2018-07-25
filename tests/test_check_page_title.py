from fixture.methods import *


def test_check_page_title():
    wd = driver()
    open_main_page(wd)
    get_page_title(wd)
    assert wd.title == config.mainPageTitle
    close_browser(wd)


__author__ = 'GiSDeCain'
