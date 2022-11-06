from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Items in basket are presented, but should not be"

    def should_display_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Message 'Your basket is empty' element is not displayed"
        assert len(self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text) > 0, \
            "Message 'Your basket is empty' is not displayed"
