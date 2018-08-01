

class MainPage:

    def __init__(self, app):
        self.app = app

    def open_subforum(self):
        wd = self.app.wd
        return wd.find_element_by_link_text('Konrad').click()


__author__ = 'GiSDeCain'
