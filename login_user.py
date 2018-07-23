from selenium.webdriver.chrome.webdriver import WebDriver
import configparser

config = configparser.ConfigParser()
config.read("cfg_att.py")
forum_url = config.get("user", "url")

print(forum_url)


__author__ = 'GiSDeCain'
