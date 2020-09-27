from .base_page import BasePage
from .locators import BoLoginPageLocators


class BOLoginPage(BasePage):

    def login_to_bo_by_admin_user(self):
        self.open()
        self.input_text(*BoLoginPageLocators.INPUT_LOGIN_FIELD, 'Art.admin')
        self.input_text(*BoLoginPageLocators.INPUT_PASSWORD_FIELD, 'qwerty123')
        self.click_on_element(*BoLoginPageLocators.SIGN_IN_BUTTON)
