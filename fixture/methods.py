from selenium.webdriver.chrome.webdriver import WebDriver
from config.cfg import config


def driver():
    wd = WebDriver()
    return wd




def close_browser(wd):
    wd.close()
    wd.quit()


def login_user(wd):
    wd.find_element_by_id("username").clear()
    wd.find_element_by_id("username").send_keys(config.userName)
    wd.find_element_by_id("password").clear()
    wd.find_element_by_id("password").send_keys(config.passwd)
    wd.find_element_by_name("login").click()


def get_logged_username(wd):
    return wd.find_element_by_id("username_logged_in").text


def get_page_title(wd):
    return wd.find_element_by_tag_name("title")


__author__ = 'GiSDeCain'
