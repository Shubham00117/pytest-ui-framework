from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BTN = (By.XPATH, "//button[@id='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//h1[normalize-space()='Logged In Successfully']")
    ERROR_MESSAGE = (By.XPATH, "//div[@id='error']")

    def login(self, username, password):
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        
    def is_login_successful(self):
        return self.is_visible(self.SUCCESS_MESSAGE)
    
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
