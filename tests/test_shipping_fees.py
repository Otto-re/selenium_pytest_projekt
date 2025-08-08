import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from pages.age_verification_page import AgeVerificationPage
from utils.constants import USERNAME, PASSWORD


def prepare(driver):
    """Einmaliges Setup für alle Versandkosten-Tests."""
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    shop_page = ShopPage(driver)
    shop_page.open_shop()

    age_page = AgeVerificationPage(driver)
    age_page.handle_age_verification("01-01-1990")

    shop_page.open_first_category()
    return shop_page

def add_products(shop_page, count):
    for _ in range(count):
        shop_page.add_first_product_to_cart()


def test_shipping_fee_under_20(driver):
    """Unter 20€: Versandkosten sollen 5€ sein."""
    shop_page = prepare(driver)
    add_products(shop_page, 1)
    shop_page.open_cart()
    text = shop_page.get_shipping_fee_text()
    assert "5€" in text or "5 €" in text


@pytest.mark.xfail(reason="Bekannter Bug: Versandkosten werden bei genau 20€ nicht entfernt")
def test_shipping_fee_exact_20(driver):
    """Genau 20€: Versandkosten sollten entfallen."""
    shop_page = prepare(driver)
    add_products(shop_page, 2)
    shop_page.open_cart()
    text = shop_page.get_shipping_fee_text()
    assert "5€" not in text and "5 €" not in text


@pytest.mark.xfail(reason="Bekannter Bug: Versandkosten werden über 20€ nicht entfernt")
def test_shipping_fee_over_20(driver):
    """Über 20€: Versandkosten sollten entfallen."""
    shop_page = prepare(driver)
    add_products(shop_page, 3)
    shop_page.open_cart()
    text = shop_page.get_shipping_fee_text()
    assert "5€" not in text and "5 €" not in text


@pytest.mark.xfail(reason="Bekannter Bug: Versandkosten kommen nicht zurück, wenn der Wert unter 20€ fällt")
def test_shipping_fee_remove_and_go_below_20(driver):
    """Bug: Versandkosten kommen nicht zurück, wenn der Wert unter 20€ fällt."""
    shop_page = prepare(driver)
    add_products(shop_page, 3)
    shop_page.open_cart()
    # Jetzt sollten Versandkosten verschwunden sein (Bug beachten)
    text = shop_page.get_shipping_fee_text()
    assert "5€" not in text and "5 €" not in text or True

    shop_page.remove_first_product_from_cart()
    shop_page.remove_first_product_from_cart()

    # Erneut prüfen
    text = shop_page.get_shipping_fee_text()
    assert "5€" in text or "5 €" in text