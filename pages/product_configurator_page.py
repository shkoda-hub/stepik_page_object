from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import ProductConfiguratorLocators


class ProductConfigurator(BasePage):

    def add_new_vertical(self, vertical_name):
        self.input_text(*ProductConfiguratorLocators.VERTICAL_NAME_FIELD, vertical_name)
        self.click_on_element(*ProductConfiguratorLocators.ADD_VERTICAL_BUTTON)

    def should_be_present_new_vertical(self, vertical_name):
        assert self.is_element_present(By.XPATH, f'//div[text() = "{vertical_name}"]'), 'New vertical not present, ' \
                                                                                        'but should be'

    def add_new_group(self, group_name):
        self.click_on_element(*ProductConfiguratorLocators.ADD_GROUP_BUTTON)
        self.input_text(*ProductConfiguratorLocators.GROUP_NAME_FIELD, group_name)
        self.click_on_element(*ProductConfiguratorLocators.SELECT_SERVICE_DROP_DOWN)
        self.click_on_element(*ProductConfiguratorLocators.GAME_SERVICE_DROP_DOWN_ITEM)
        self.click_on_element(*ProductConfiguratorLocators.SELECT_VERTICAL_DROP_DOWN)
        self.click_on_element(*ProductConfiguratorLocators.SELECT_VERTICAL_DROP_DOWN_FIRST_ITEM)
        self.click_on_element(*ProductConfiguratorLocators.SAVE_GROUP_BUTTON)

    def should_be_present_new_group(self, group_name):
        self.input_text(*ProductConfiguratorLocators.SEARCH_GROUP_BY_NAME_FIELD, group_name)
        assert self.is_element_present(By.LINK_TEXT, group_name), 'New group not present, but should be'
