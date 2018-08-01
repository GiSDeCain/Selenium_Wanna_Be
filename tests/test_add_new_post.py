from config.cfg import Config


def test_add_post(app):
    app.login_page.login_user(Config.userName, Config.passwd)
    app.main_page.open_subforum()
    #tu będzie reszta testu

__author__ = 'GiSDeCain'
