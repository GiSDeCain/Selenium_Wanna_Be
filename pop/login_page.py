from config.cfg import Config


class LoginPage:

    def __init__(self, app):
        self.app = app

    def login_user(self):
        wd = self.app.wd
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(Config.userName)
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(Config.passwd)
        wd.find_element_by_name("login").click()


__author__ = 'GiSDeCain'
