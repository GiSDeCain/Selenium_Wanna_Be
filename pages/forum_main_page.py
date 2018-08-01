from config.cfg import Config


class MainPage:

    def __init__(self, app):
        self.app = app

    def open_subforum(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//a[@class='forumtitle' and text()='%s']" % Config.subforumName)
        try:
            element
            element.click()
        except NoSuchElementException:
            pass


__author__ = 'GiSDeCain'
