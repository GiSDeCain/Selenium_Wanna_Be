from selenium.webdriver.chrome.webdriver import WebDriver
import configparser

config = configparser.ConfigParser()
config.read("cfg_att.py")
forum_url = config.get("user", "url")
user_name = config.get("user", "name")
passwd = config.get("user", "passwd")


def setUp():
    wd = WebDriver()
    wd.get(forum_url)


setUp()


__author__ = 'GiSDeCain'
