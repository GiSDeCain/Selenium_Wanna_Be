

class LoginPage:

    def __init__(self, app):
        self.app = app

    def login_user(self, username, password):
        wd = self.app.wd
        usernameInputBox = wd.find_element_by_id("username")
        passwordInputBox = wd.find_element_by_id("password")
        usernameInputBox.clear()
        usernameInputBox.send_keys(username)
        passwordInputBox.clear()
        passwordInputBox.send_keys(password)
        wd.find_element_by_name("login").click()


__author__ = 'GiSDeCain'
