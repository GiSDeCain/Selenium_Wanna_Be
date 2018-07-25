from selenium.webdriver.chrome.webdriver import WebDriver
from cfg import config


def setup():
    wd = WebDriver()
    wd.get(config.url)
    wd.find_element_by_id("username").clear()
    wd.find_element_by_id("username").send_keys(config.userName)
    wd.find_element_by_id("password").clear()
    wd.find_element_by_id("password").send_keys(config.passwd)
    wd.find_element_by_name("login").click()
    element = wd.find_element_by_link_text(config.userName)
    assert element.text == config.userName
    wd.close()
    wd.quit()


setup()


__author__ = 'GiSDeCain'
