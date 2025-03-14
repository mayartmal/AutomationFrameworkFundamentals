from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from constants.cart_page_locators import ADDED_BOOK_LOCATOR, DELETE_BUTTON_LOCATOR, EMPTY_CART_LOCATOR, \
    CART_TABLE_LOCATOR, \
    SHOPPING_CART_LOCATOR, CLEAR_CART_BUTTON_LOCATOR, CHECKOUT_BUTTON_LOCATOR
from page_objects.browser_wrapper import BrowserWrapper


class CartPage(BrowserWrapper):

    def __init__(self):
        super().__init__()

    def get_book_title(self):
        self.wait_for_element_to_be_visible(ADDED_BOOK_LOCATOR)
        return self.get_text(ADDED_BOOK_LOCATOR)

    def click_delete_button(self):
        try:
            self.wait_for_element_to_be_visible(SHOPPING_CART_LOCATOR)
            self.wait_for_element_to_be_visible(CART_TABLE_LOCATOR)
            self.wait_for_element_to_be_clickable(CLEAR_CART_BUTTON_LOCATOR)
            self.wait_for_element_to_be_clickable(CHECKOUT_BUTTON_LOCATOR)
            self.wait_for_element_to_be_clickable(DELETE_BUTTON_LOCATOR)
            element = self.get_element(DELETE_BUTTON_LOCATOR)
            self.click(element=element)
        except StaleElementReferenceException:
            self.driver.implicitly_wait(1)
            element = self.get_element(DELETE_BUTTON_LOCATOR)
            self.click(element=element)

    def click_delete_button_looped(self):
        click_attempts_number = 5
        for attempt in range(click_attempts_number):
            try:
                self.wait_for_element_to_be_clickable(DELETE_BUTTON_LOCATOR)
                element = self.get_element(DELETE_BUTTON_LOCATOR)
                self.click(element=element)
                return
            except TimeoutException:
                break
        raise Exception(f"Element unavailable {click_attempts_number} times")

    def get_cart_empty_status(self):
        return self.get_text(EMPTY_CART_LOCATOR)
