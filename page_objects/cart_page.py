from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
# replace cart page locators with class (CartPageLocators)
from constants.cart_page_locators import (
    DELETE_BUTTON_LOCATOR,
    EMPTY_CART_LOCATOR,
    BOOKS_QUANTITY_LOCATOR,
    CART_TABLE_LOCATOR,
    SHOPPING_CART_LOCATOR,
    CLEAR_CART_BUTTON_LOCATOR,
    CHECKOUT_BUTTON_LOCATOR
)
from page_objects.browser_wrapper import BrowserWrapper
from constants.cart_page_locators import CartPageLocator


class CartPage(BrowserWrapper):

    def __init__(self):
        super().__init__()

    def get_book_title(self):
        self.wait_for_page_to_load()

        self.wait_for_element_to_be_visible(CartPageLocator.ADDED_BOOK_NAME__TEXT_ELEMENT)
        return self.get_text(CartPageLocator.ADDED_BOOK_NAME__TEXT_ELEMENT)

    def get_the_number_of_book_in_the_cart(self):
        elements = self.get_elements(BOOKS_QUANTITY_LOCATOR)
        return sum([int(element.get_property("value")) for element in elements])

    def get_titles_of_books_in_the_cart(self):
        elements = self.get_elements(CartPageLocator.ADDED_BOOK_NAME__TEXT_ELEMENT)
        return [self.get_text(element=element) for element in elements]

    def click_delete_button(self):
        is_clicked = False
        while not is_clicked:
            try:
                self.wait_for_element_to_be_clickable(DELETE_BUTTON_LOCATOR)
                element = self.get_element(DELETE_BUTTON_LOCATOR)
                self.click(element=element)
                is_clicked = True
            except StaleElementReferenceException:
                is_clicked = False
            except TimeoutException:
                break

    def get_cart_empty_status(self):
        return self.get_text(EMPTY_CART_LOCATOR)
