from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):

    def no_products_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.NO_PRODUCTS_IN_BASKET), \
            "Product is presented, basket is NOT empty"

    def basket_is_empty_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), \
            "No 'Basket is empty' message"