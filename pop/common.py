

class Common:

    def __init__(self, app):
        self.app = app

    def close_browser(self):
        wd = self.app.wd
        wd.close()
        wd.quit()

    def get_page_title(self):
        wd = self.app.wd
        return wd.find_element_by_tag_name("title")


__author__ = 'GiSDeCain'
