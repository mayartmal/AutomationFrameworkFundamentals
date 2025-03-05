from constants.locators import ADD_BTN_LOCATOR, CART_BTN_LOCATOR, ADDED_BOOK_LOCATOR
from constants.applications import BOOK_STORE_HOME_PAGE
from page_objects.browser_wrapper import BrowserWrapper

class HomePage:
    def __init__(self):
        self.browser_wrapper = BrowserWrapper()
        self.browser_wrapper.driver.get(BOOK_STORE_HOME_PAGE)

    def click_add_book_button(self, book_title: str):
        formatted_locator = ADD_BTN_LOCATOR.format(book_title)
        self.browser_wrapper.click(formatted_locator)

    def click_cart_button(self):
        self.browser_wrapper.click(CART_BTN_LOCATOR)

    def get_book_title(self):
        return self.browser_wrapper.get_text(ADDED_BOOK_LOCATOR)