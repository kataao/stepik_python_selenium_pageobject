import pytest
import time
import random
import string
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

product_1_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
product_2_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
promo = "/?promo=offer"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        user_email = str(time.time()) + "@fakemail.org"
        user_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(9))
        product_page = ProductPage(browser, product_1_link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(user_email, user_password)
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = product_1_link
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.add_to_cart()
        product_page.should_display_success_message()
        product_page.should_display_correct_price()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        url = product_1_link
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.add_to_cart()
        product_page.should_not_present_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('offer_num', (1, 2, 3, 4, 5, 6,
                                       pytest.param(7, marks=pytest.mark.xfail),
                                       8, 9, 10))
def test_guest_can_add_product_to_basket(browser, offer_num):
    url = product_1_link + promo + str(offer_num)
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_display_success_message()
    page.should_display_correct_price()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    url = product_2_link
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = product_1_link
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.open_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_display_empty_message()


def test_guest_cant_see_success_message(browser):
    url = product_1_link
    page = ProductPage(browser, url)
    page.open()
    page.should_not_present_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = product_1_link
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.should_not_present_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    url = product_2_link
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = product_1_link
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.should_disappear_success_message()
