from config.cfg import Config


def test_enter_subforum(app):
    app.login_page.login_user(Config.userName, Config.passwd)
    if app.main_page.open_subforum() != 0:
        assert app.sub_page.check_if_in_good_subforum() == Config.subforumName
    else:
        print("Test not done")


__author__ = 'GiSDeCain'
