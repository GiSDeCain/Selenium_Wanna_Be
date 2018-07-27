from selenium.webdriver.chrome.webdriver import WebDriver


class App:

    def __init__(self, base_url):
        self.wd = WebDriver
        self.base_url = base_url

    def open_main_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.close()
        self.wd.quit()


__author__ = 'GiSDeCain'
