from config.cfg import Config


def test_enter_subforum(app):
    app.login_page.login_user(Config.userName, Config.passwd)
    app.main_page.open_subforum()


__author__ = 'GiSDeCain'
