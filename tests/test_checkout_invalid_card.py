import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from pages.age_verification_page import AgeVerificationPage
from utils.constants import BASE_URL, USERNAME, PASSWORD
import time

@pytest.mark.parametrize(
    "birth_date, card_number, card_name, expiry_date, cvv, expected_success",
    [
        ("01-01-1990", "1234", "Max Mustermann", "12/26", "abc", False),
        ("01-01-1990", "1234 4546 2125 4847", "Max Mustermann", "12/2623", "abc", False),
        ("01-01-1990", "1234 4546 2125 4847", "Max Mustermann", "12/2023", "777", True),
        ("01-01-2000", "1234", "Max Mustermann", "12/2656", "abc", False)

    ]
)
def test_cart_age_verification(driver, birth_date, card_number, card_name, expiry_date, cvv, expected_success):
    wait = WebDriverWait(driver, 10)

    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    # Shop öffnen
    shop_page = ShopPage(driver)
    shop_page.open_shop()

    # Altersprüfung
    age_page = AgeVerificationPage(driver)
    age_page.handle_age_verification(birth_date)

    shop_page.open_category("Alocohol")
    try:
        WebDriverWait(driver, timeout=10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.product-card:first-of-type button.btn-cart"))
        )
    except TimeoutException:
        if expected_success:
            pytest.fail("Produkt konnte nicht ausgewählt werden – Test erwartet Erfolg")
        else:
            return

    shop_page.add_first_product_to_cart()

    header_icons = driver.find_elements(By.CSS_SELECTOR, "div.headerIcon")
    header_icons[2].click()

    WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img.checkout-card-image"))
    )

    shipment_fields = driver.find_elements(By.CSS_SELECTOR, "input.shipment-input")
    assert len(shipment_fields) >= 3, "Nicht alle Zahlungsfelder gefunden"
    shipment_fields[0].send_keys("Rabenhof")
    shipment_fields[1].send_keys("Bielefeld")
    shipment_fields[2].send_keys("33609")

    payment_fields = driver.find_elements(By.CSS_SELECTOR, "input.payment-input")
    assert len(payment_fields) >= 4, "Nicht alle Zahlungsfelder gefunden"
    payment_fields[0].send_keys(card_number)
    payment_fields[1].send_keys(card_name)
    payment_fields[2].send_keys(expiry_date)
    payment_fields[3].send_keys(cvv)

    buy_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    buy_button.click()

    if expected_success:
        try:
            success_heading = WebDriverWait(driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[text()='Fresh']"))
            )
            assert success_heading.is_displayed(), "Erfolg erwartet, aber keine Bestätigung gefunden"
        except TimeoutException:
            pytest.fail("Bezahlung sollte erfolgreich sein, aber 'Fresh' wurde nicht gefunden")
    else:
        try:
            WebDriverWait(driver, timeout=5).until(
                EC.presence_of_element_located((By.XPATH, "//h1[text()='Fresh']"))
            )
            pytest.fail("Bezahlung sollte fehlschlagen, aber 'Fresh' wurde angezeigt")
        except TimeoutException:
            pass
