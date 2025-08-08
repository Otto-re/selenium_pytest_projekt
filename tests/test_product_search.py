
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utils.constants import USERNAME, PASSWORD
import time

@pytest.mark.parametrize("keyword, expected_message", [
    ("milk", None),                          # Gültiger Suchbegriff → keine Fehlermeldung
    ("xyz123", "No products found"),         # Ungültiger Begriff → Fehlermeldung
    ("!@#$%", "No products found"),          # Sonderzeichen → Fehlermeldung oder Sanitize
])
def test_product_search_keywords(driver, keyword, expected_message):
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    shop_page = ShopPage(driver)
    shop_page.search(keyword)

    if expected_message:
        try:
            message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f"//p[contains(text(), '{expected_message}')]"))
            )
            assert message.is_displayed(), f" Erwartete Nachricht '{expected_message}' wurde nicht angezeigt"
        except TimeoutException:
            assert False, f" Nachricht '{expected_message}' ist nicht erschienen – Fehler im Verhalten"
    else:
        # Bei gültigem Keyword prüfen, ob mindestens 1 Vorschlag erscheint
        suggestions = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "suggestion-item"))
        )
        assert len(suggestions) > 0, " Keine Vorschläge trotz gültigem Keyword"