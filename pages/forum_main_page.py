from selenium.common.exceptions import NoSuchElementException
from config.cfg import Config


class MainPage:

    def __init__(self, app):
        self.app = app

    def open_subforum(self):
        wd = self.app.wd
       wd.find_element_by_xpath("//a[@class='forumtitle' and text()='%s']" % Config.subforumName).click()



__author__ = 'GiSDeCain'
