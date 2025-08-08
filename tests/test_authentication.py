from utils.constants import USERNAME, PASSWORD, BASE_URL
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from dotenv import load_dotenv
from selenium.common.exceptions import TimeoutException


load_dotenv()

def test_example(driver):
    driver.get(BASE_URL)
    assert "Market Mate" in driver.title

@pytest.mark.parametrize("username, password", [
    (USERNAME, PASSWORD),
    ("wrong", "wrong"),
    ("", ""),
    ("hans@t-online.de", "papa")
])

def test_login(driver, username, password):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 5)

    login_page = LoginPage(driver)
    login_page.open_login_modal()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    if username == USERNAME and password == PASSWORD:
        try:
            fresh_heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Fresh']")))
            vegetables_heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Vegetables']")))
            assert fresh_heading.is_displayed(), "'Fresh' heading is not displayed"
            assert vegetables_heading.is_displayed(), "'Vegetables' heading is not displayed"
        except TimeoutException:
            pytest.fail("Login sollte erfolgreich sein, aber 'Fresh' oder 'Vegetables' wurden nicht gefunden")

    else:
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Fresh']")))
            pytest.fail("Login sollte fehlschlagen, aber 'Fresh' wurde gefunden")
        except TimeoutException:
            pass


