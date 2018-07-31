from config.cfg import Config


def test_check_page_title(app):
    app.open_home_page()
    assert app.wd.title == Config.mainPageTitle


__author__ = 'GiSDeCain'
