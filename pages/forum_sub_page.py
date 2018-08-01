

class SubPage:

    def __init__(self, app):
        self.app = app

    def check_if_in_good_subforum(self):
        wd = self.app.wd
        return wd.find_element_by_class_name("forum-title").text




__author__ = 'GiSDeCain'
