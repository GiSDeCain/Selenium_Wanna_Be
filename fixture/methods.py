from config.cfg import config


class Methods:

    def __init__(self, app):
        self.app = app

    def close_browser(self):
        wd = self.app.wd
        wd.close()
        wd.quit()

    def login_user(self):
        wd = self.app.wd
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(config.userName)
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(config.passwd)
        wd.find_element_by_name("login").click()

    def get_logged_username(self):
        wd = self.app.wd
        return wd.find_element_by_id("username_logged_in").text

    def get_page_title(self):
        wd = self.app.wd
        return wd.find_element_by_tag_name("title")


__author__ = 'GiSDeCain'
