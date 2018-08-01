from config.cfg import Config


class MainPage:

    def __init__(self, app):
        self.app = app

    def open_subforum(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//a[@class='forumtitle' and text()='%s']" % Config.subforumName)
        if len(element) > 0:
            element[0].click()
        else:
            print("dupa")


__author__ = 'GiSDeCain'
