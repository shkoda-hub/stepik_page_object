from selenium.webdriver.common.by import By


class BoLoginPageLocators():
    INPUT_LOGIN_FIELD = (By.CSS_SELECTOR, '#input-login')
    INPUT_PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'div.form-group>button')


class ProductConfiguratorLocators():
    VERTICAL_NAME_FIELD = (By.CSS_SELECTOR, '#addVerticalName')
    ADD_VERTICAL_BUTTON = (By.CSS_SELECTOR, '.form-inline>button')
    ADD_GROUP_BUTTON = (By.CSS_SELECTOR, 'bo-card-actions>button')
    GROUP_NAME_FIELD = (By.CSS_SELECTOR, '[formcontrolname="name"]')
    SELECT_SERVICE_DROP_DOWN = (By.CSS_SELECTOR, '[placeholder="Select service"]>button')
    GAME_SERVICE_DROP_DOWN_ITEM = (By.CSS_SELECTOR, '.option-list>nb-option:nth-child(2)')
    SELECT_VERTICAL_DROP_DOWN = (By.CSS_SELECTOR, '[placeholder="Select vertical"]>button')
    SELECT_VERTICAL_DROP_DOWN_FIRST_ITEM = (By.CSS_SELECTOR, '.option-list>nb-option')
    SAVE_GROUP_BUTTON = (By.CSS_SELECTOR, '.justify-content-end>div>button:nth-child(1)')
    SEARCH_GROUP_BY_NAME_FIELD = (By.CSS_SELECTOR, '[placeholder = "Group"]')
