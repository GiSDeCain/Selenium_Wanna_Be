from config.cfg import Config


def test_check_page_title(app):
    app.open_home_page()
    app.common.get_page_title()
    assert app.wd.title == Config.mainPageTitle


__author__ = 'GiSDeCain'
