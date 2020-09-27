from .base_page import BasePage
from selenium.webdriver.common.by import By


class BoMainPage(BasePage):

    def bo_menu_navigate(self, *menu_items):
        for item in menu_items:
            self.click_on_element(By.CSS_SELECTOR, f'[title = "{item}"]')

    def bo_tab_navigate(self, *tab_items):
        for tab in tab_items:
            self.click_on_element(By.XPATH, f'//span[text() = "{tab}"]')