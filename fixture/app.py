from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.methods import Methods


class Application:

    def __init__(self, base_url="http://forum.attnauka.webd.pro"):
        self.wd = WebDriver()
        #self.wd.implicitly_wait(10)
        self.base_url = base_url
        self.methods = Methods(self)

    def destroy(self):
        self.wd.close()
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


__author__ = 'GiSDeCain'
