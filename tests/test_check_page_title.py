from config.cfg import Config


def test_check_page_title(app):
    assert app.wd.title == Config.mainPageTitle


__author__ = 'GiSDeCain'
