import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # initialise Page Object, pass the driver and url address in the constructor
        page = MainPage(browser, link)
        # open page
        page.open()
        # execute page method — go to login page
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.open_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_display_empty_message()


def test_guest_should_see_login_page(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
