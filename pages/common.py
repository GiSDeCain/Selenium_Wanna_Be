

class Common:

    def __init__(self, app):
        self.app = app

    def close_browser(self):
        wd = self.app.wd
        wd.close()
        wd.quit()


__author__ = 'GiSDeCain'
