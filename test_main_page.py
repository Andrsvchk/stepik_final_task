from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     main_page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     main_page.open()                      # открываем страницу
#     main_page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     main_page = MainPage(browser, link)
#     main_page.open()
#     main_page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_basket_button()
    main_page.transit_to_basket()
    basket_page = BasketPage(browser, link)
    basket_page.no_products_in_basket()
    basket_page.basket_is_empty_message()