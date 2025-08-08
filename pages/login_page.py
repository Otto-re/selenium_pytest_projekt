from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_icon = (By.CSS_SELECTOR, "svg.headerIcon-size")
        self.username_input = (By.CSS_SELECTOR, "input[type='email']")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def open_homepage(self):
        self.open("/")

    def open_login_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_icon)
        )
        self.click(self.login_icon)

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        )
        self.type(self.username_input, username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        )
        self.type(self.password_input, password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        self.click(self.login_button)

    def login(self, username, password):
        self.open_homepage()
        self.open_login_modal()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()