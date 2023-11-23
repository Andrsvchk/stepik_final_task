from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest
import time

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        time.sleep(2)
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email, password)
        time.sleep(5)
        product_page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.test_guest_cant_see_success_message()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        time.sleep(2)
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        email = str(time.time()) + "@fakemail.com"
        password = str(time.time())
        login_page.register_new_user(email, password)
        time.sleep(5)
        product_page.should_be_authorized_user()
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        time.sleep(5)
        product_page.product_in_basket()
        time.sleep(5)
        product_page.product_price_in_basket()

# @pytest.mark.parametrize('link', [
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                                marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_to_basket()
#     product_page.solve_quiz_and_get_code()
#     time.sleep(5)
#     product_page.product_in_basket()
#     time.sleep(5)
#     product_page.product_price_in_basket()
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.test_guest_cant_see_success_message()
#
# @pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207",
#                                                marks=pytest.mark.xfail)])
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_to_basket()
#     product_page.test_guest_cant_see_success_message_after_adding_product_to_basket()
#
# @pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207",
#                                                marks=pytest.mark.xfail)])
# def test_message_disappeared_after_adding_product_to_basket(browser, link):
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_to_basket()
#     product_page.test_message_disappeared_after_adding_product_to_basket()
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_basket_button()
#     product_page.transit_to_basket()
#     basket_page = BasketPage(browser, link)
#     basket_page.no_products_in_basket()
#     basket_page.basket_is_empty_message()
