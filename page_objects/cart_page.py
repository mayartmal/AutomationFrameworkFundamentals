from constants.locators import ADDED_BOOK_LOCATOR
from page_objects.browser_wrapper import BrowserWrapper


class CartPage(BrowserWrapper):

    def __init__(self):
        super().__init__()

    def get_book_title(self):
        return self.get_text(ADDED_BOOK_LOCATOR)
