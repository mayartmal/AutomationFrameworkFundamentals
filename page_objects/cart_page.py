from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from constants.cart_page import CartPageLocators
from page_objects.browser_wrapper import BrowserWrapper


class CartPage(BrowserWrapper):

    def __init__(self):
        super().__init__()

    def get_book_title(self) -> str:
        """
        Gets a book added to the cart after the page is fully loaded

        :return: str - book title string
        """
        self.wait_for_page_to_load()
        return self.get_text(locator=CartPageLocators.ADDED_BOOK_NAME__TEXT_ELEMENT)

    def get_the_number_of_book_in_the_cart(self) -> int:
        """
        Gets the quantity of all books in the cart

        :return: int - quantity of all books in the cart
        """
        elements = self.get_elements(locator=CartPageLocators.BOOKS_QUANTITY__INPUT)
        return sum([int(element.get_property("value")) for element in elements])

    def get_titles_of_books_in_the_cart(self) -> list[str]:
        """
        Gets the names of all books in the cart

        :return: list[str] - list of all books in the cart
        """
        elements = self.get_elements(locator=CartPageLocators.ADDED_BOOK_NAME__TEXT_ELEMENT)
        return [self.get_text(element=element) for element in elements]

    def click_delete_button(self) -> None:
        """
        Clicks delete button iteratively to avoid StaleElementReferenceException

        :return: None
        """
        is_clicked = False
        while not is_clicked:
            try:
                self.click(locator=CartPageLocators.DELETE__BUTTON)
                is_clicked = True
            except StaleElementReferenceException:
                is_clicked = False
            except TimeoutException:
                break

    def get_cart_empty_status(self) -> str:
        """
        Gets a string describes that the cart is empty

        :return: str - empty cart status string
        """
        return self.get_text(locator=CartPageLocators.EMPTY_CART__P)

    def get_opened_cart_page_tab_name(self) -> str:
        return self.driver.title

    def close_cart_page_tab(self) -> None:

        self.close_tab()
