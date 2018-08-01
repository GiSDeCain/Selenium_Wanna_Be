

class MainPage:

    def __init__(self, app):
        self.app = app

    def open_subforum(self):
        wd = self.app.wd
        wd.find_element_by_link_text('Konrad').click()
        assert wd.find_element_by_class_name("list-inner").text == 'Topics'


__author__ = 'GiSDeCain'
