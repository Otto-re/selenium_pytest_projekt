import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from pages.age_verification_page import AgeVerificationPage
from utils.constants import BASE_URL, USERNAME, PASSWORD
import time

@pytest.mark.parametrize(
    "birth_date, expect_button",
    [
        ("01-01-1990", True),   # über 18
        ("01-01-2010", False),  # unter 18
        ("", False),
    ]
)
def test_cart_age_verification(driver, birth_date, expect_button):
    # Login
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    # Shop öffnen
    shop_page = ShopPage(driver)
    shop_page.open_shop()

    # Altersprüfung
    age_page = AgeVerificationPage(driver)
    age_page.handle_age_verification(birth_date)

    shop_page.open_category("Alocohol")

    if expect_button:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.product-card:first-of-type button.btn-cart")
            )
        )

        shop_page.add_first_product_to_cart()

        header_icons = driver.find_elements(By.CSS_SELECTOR, "div.headerIcon")
        header_icons[2].click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "img.checkout-card-image")
            )
        )

    else:
        # Für unter 18 oder kein Alter wird ein Hinweis angezeigt
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'underage')]")
            )
        )
    time.sleep(12)

