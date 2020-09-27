from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.maximize_window()

    def open(self):
        self.browser.get(self.url)

    def input_text(self, locator_type, locator, text):
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((locator_type, locator))
        )
        self.browser.find_element(locator_type, locator).send_keys(text)

    def click_on_element(self, locator_type, locator):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((locator_type, locator))
        )
        self.browser.find_element(locator_type, locator).click()

    def is_element_present(self, locator_type, locator, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((locator_type, locator))
            )
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False
        return True
