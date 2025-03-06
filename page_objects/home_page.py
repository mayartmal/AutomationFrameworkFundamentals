from constants.locators import ADD_BTN_LOCATOR, CART_BTN_LOCATOR
from page_objects.browser_wrapper import BrowserWrapper

class HomePage:
    def __init__(self, session: BrowserWrapper):
        self.session = session

    def click_add_book_button(self, book_title: str):
        formatted_locator = ADD_BTN_LOCATOR.format(book_title)
        self.session.click(formatted_locator)

    def click_cart_button(self):
        self.session.click(CART_BTN_LOCATOR)
