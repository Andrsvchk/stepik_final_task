from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    TRANSITION_TO_BASKET_BUTTON = (By.XPATH, "//button[@data-toggle='dropdown']/../a")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    PRODUCT_NAME = (By.XPATH, "//li[@class='active']")
    TOTAL_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    NO_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#basket_totals")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket is empty')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

