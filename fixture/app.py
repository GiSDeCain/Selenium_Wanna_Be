from selenium.webdriver.chrome.webdriver import WebDriver
from pop.common import Common
from pop.login_page import LoginPage
from pop.forum_main_page import MainPage
from pop.forum_sub_page import SubPage


class Application:

    def __init__(self, base_url="http://forum.attnauka.webd.pro"):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.base_url = base_url
        self.common = Common(self)
        self.login_page = LoginPage(self)
        self.main_page = MainPage(self)
        self.sub_page = SubPage(self)

    def destroy(self):
        self.wd.close()
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


__author__ = 'GiSDeCain'
