from selenium.webdriver.chrome.webdriver import WebDriver
from cfg import config


def driver():
    wd = WebDriver()
    return wd


def open_main_page(wd):
    wd.get(config.url)


def close_browser(wd):
    wd.close()
    wd.quit()


def login_user(wd):
    wd.find_element_by_id("username").clear()
    wd.find_element_by_id("username").send_keys(config.userName)
    wd.find_element_by_id("password").clear()
    wd.find_element_by_id("password").send_keys(config.passwd)
    wd.find_element_by_name("login").click()
    element = wd.find_element_by_link_text(config.userName)
    assert element.text == config.userName


__author__ = 'GiSDeCain'
