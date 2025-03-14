from constants.home_page_locators import ADD_BUTTON_LOCATOR, CART_BUTTON_LOCATOR
from page_objects.browser_wrapper import BrowserWrapper


class HomePage(BrowserWrapper):

    def __init__(self):
        super().__init__()

    def click_add_book_button(self, book_title: str):
        formatted_locator = ADD_BUTTON_LOCATOR.format(book_title)
        self.click(formatted_locator)

    def click_cart_button(self):
        self.click(CART_BUTTON_LOCATOR)
