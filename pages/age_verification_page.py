from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AgeVerificationPage:
    def __init__(self, driver):
        self.driver = driver

    def handle_age_verification(self, birth_date="01-01-1990"):
        try:
            # Warten, ob der Dialog auftaucht
            date_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='DD-MM-YYYY']")
                )
            )
            if birth_date:
                date_input.clear()
                date_input.send_keys(birth_date)

            confirm_button = self.driver.find_element(
                By.XPATH, "//button[contains(., 'Confirm')]"
            )
            confirm_button.click()

            # Warten bis der Dialog weg ist
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, "//button[contains(., 'Confirm')]")
                )
            )
        except:
            # Wenn kein Dialog da ist, einfach weitermachen
            pass