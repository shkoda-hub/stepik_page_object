from datetime import datetime
import pytest
from pages.bo_login_page import BOLoginPage
from pages.bo_main_page import BoMainPage
from pages.product_configurator_page import ProductConfigurator


class TestCreateNewVerticalAndGroup():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        bo_login_page = BOLoginPage(browser, 'https://back-office-pr-416.dev.it-banda.com/login')
        bo_login_page.login_to_bo_by_admin_user()
        bo_main_page = BoMainPage(browser, browser.current_url)
        bo_main_page.bo_menu_navigate('Global Settings', 'Product Configurator')

    def test_add_new_vertical(self, browser):
        configurator = ProductConfigurator(browser, browser.current_url)
        vertical_name = str(datetime.now())
        configurator.add_new_vertical(vertical_name)
        configurator.should_be_present_new_vertical(vertical_name)

    def test_add_new_group(self, browser):
        bo_main_page = BoMainPage(browser, browser.current_url)
        bo_main_page.bo_tab_navigate('Groups')
        configurator = ProductConfigurator(browser, browser.current_url)
        group_name = str(datetime.now())
        configurator.add_new_group(group_name)
        configurator.should_be_present_new_group(group_name)
