

class Common:

    def __init__(self, app):
        self.app = app

    def close_browser(self):
        wd = self.app.wd
        wd.close()
        wd.quit()

    def get_logged_username(self):
        wd = self.app.wd
        return wd.find_element_by_id("username_logged_in").text


__author__ = 'GiSDeCain'
