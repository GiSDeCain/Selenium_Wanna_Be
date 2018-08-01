

class SubPage:

    def __init__(self, app):
        self.app = app

    def check_if_in_subforum(self):
        wd = self.app.wd
        return wd.find_element_by_class_name("list-inner").text




__author__ = 'GiSDeCain'
