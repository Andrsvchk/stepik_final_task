from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()

    def product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            ("Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE),\
            ("Message about adding is not presented")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text

        assert product_name == product_in_message, "Product name is different"

    def product_price_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE_IN_MESSAGE), \
            ("Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            ("Product price is not presented")
        product_price_in_message = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_IN_MESSAGE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert product_price_in_message == product_price, "Product price is different"

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"