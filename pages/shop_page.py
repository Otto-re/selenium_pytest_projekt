from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import BASE_URL_store

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.shop_menu = (By.XPATH, "//a[normalize-space()='Shop']")
        self.cart_icons = (By.CSS_SELECTOR, "div.headerIcon")
        self.shipping_fee_area = (By.CSS_SELECTOR, ".checkout-card-body")
        self.remove_buttons = (By.CSS_SELECTOR, "button.checkout-card-remove")

    def open_shop(self):
        # Warten bis der Link "Shop" klickbar ist
        shop_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Shop"))
        )
        shop_link.click()

    def add_first_product_to_cart(self):
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-cart"))
        )
        add_button.click()

    def open_category(self, category_name: str):
        """Klickt auf eine Kategorie in der Sidebar."""
        category_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//a[normalize-space()='{category_name}']")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", category_link)
        category_link.click()

    def open_first_category(self):
        """
        Öffnet die erste Kategorie in der Sidebar (unabhängig vom Namen).
        """
        categories = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.sidebar-container a")
            )
        )
        first_category = categories[0]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", first_category)
        first_category.click()

    def open_cart(self):
        """Klickt auf das dritte Header-Icon (Warenkorb)."""
        icons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.cart_icons)
        )
        icons[2].click()

    def get_shipping_fee_text(self):
        """Liest den Textbereich mit Versandkosten aus."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.shipping_fee_area)
        )
        return self.driver.find_element(*self.shipping_fee_area).text

    def remove_first_product_from_cart(self):
        """
        Entfernt das erste Produkt aus dem Warenkorb.
        """
        remove_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.remove_buttons)
        )
        remove_button.click()

    def search(self, keyword: str):
        """Füllt das Suchfeld aus und wartet auf Vorschläge."""
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search Products']"))
        )
        search_input.clear()
        search_input.send_keys(keyword)

        # Warte auf Vorschlags-Container
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "suggestions"))
        )