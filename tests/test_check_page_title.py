from fixture.methods import *


def test_check_page_title(app):
    app.methods.get_page_title()
    assert app.wd.title == config.mainPageTitle


__author__ = 'GiSDeCain'
