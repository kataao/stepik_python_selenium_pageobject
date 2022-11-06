from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_display_success_message(self):
        actual_product_title = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        expected_product_title = self.get_product_title()
        assert actual_product_title == expected_product_title, \
            f"Product title in message is incorrect, " \
            f"expected: {expected_product_title}, actual: {actual_product_title}"

    def should_display_correct_price(self):
        actual_product_price = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        expected_product_price = self.get_product_price()
        assert actual_product_price == expected_product_price, \
            f"Cart total in message is incorrect, " \
            f"expected: {expected_product_price}, actual: {actual_product_price}"

    def should_not_present_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
