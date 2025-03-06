from constants.locators import ADDED_BOOK_LOCATOR
from page_objects.browser_wrapper import BrowserWrapper

class CartPage:
    def __init__(self, session: BrowserWrapper):
        self.session = session

    def get_book_title(self):
        return self.session.get_text(ADDED_BOOK_LOCATOR)