from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import BASE_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, value):
        field = self.wait.until(EC.presence_of_element_located(locator))
        field.clear()
        field.send_keys(value)

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text

    def open(self, path=""):
        """Öffnet die Basis-URL plus optionalen Pfad"""
        url = BASE_URL if path == "" else BASE_URL + path
        self.driver.get(url)