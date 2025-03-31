import builtins
from selenium.common import NoSuchElementException
from typing import Union, Literal, Optional

from constants.all_books_data import BOOK_OUTLET_BOOKS
from constants.home_page import HomePageLocators, HomePageOptions, HomePageAttributes
from page_objects.browser_wrapper import BrowserWrapper
from page_objects.abstract_page import AbstractPage
# from tests.conftest import cart_page
from utils.data_generator import generate_random_number, choose_items


class HomePage(AbstractPage):

    def __init__(self):
        super().__init__()

    def close_cookie_dialog(self) -> None:
        """
        Attempts to close the cookie dialog on the page by clicking the close button.

        The method first waits for the page to load and checks if the close button for the cookie dialog is displayed.
        If the button is visible, it will be clicked. If the button is not found or is not visible, no action is taken.
        If the button is not present on the page, a NoSuchElementException is caught, and no further action is performed.

        :return: None
        """
        try:
            self.wait_for_page_to_load()
            self.click(locator=HomePageLocators.COOKIE_DIALOG_CLOSE__BUTTON) if \
                self.element_displayed(locator=HomePageLocators.COOKIE_DIALOG_CLOSE__BUTTON) else None
        except NoSuchElementException:
            pass

    def add_books_to_cart(self, book_adder: Union[str, list, int, tuple]) -> None:
        """
        The method adds one specific book OR specific number of random books from storage OR
        random number of random books from storage
        The method changes its behaviour depending on the book_adder data type

        :param book_adder: str | list | int | tuple A book title string OR an integer specifying the number
        of books to add OR
        a set of border values to generate random number of books.
        :return: None
        """
        match type(book_adder):
            case builtins.str:
                self.click_add_button_for_titles_in(book_titles_list=[book_adder])
            case builtins.int:
                titles_list = self.create_books_list(fixed_number_of_books=book_adder)
                self.click_add_button_for_titles_in(book_titles_list=titles_list)
            case builtins.list:
                self.click_add_button_for_titles_in(book_titles_list=book_adder)
            case builtins.tuple:
                titles_list = self.create_books_list(range_number_of_books=book_adder)
                self.click_add_button_for_titles_in(book_titles_list=titles_list)

    def click_add_button_for_titles_in(self, book_titles_list: list) -> None:
        """
        calls click the add book button method iteratively for the list of book titles

        :param book_titles_list:
        :return: None
        """
        [self.click_add_book_button(book_title=title) for title in book_titles_list]

    def click_add_book_button(self, book_title: str):
        """
        Clicks the 'Add to Cart' button for a specified book and closes the related popup

        This method performs the following steps:
        1. Clicks the 'Add to Cart' button for the book with the specified title.
        2. Clicks the 'Close' button on the popup that confirms the book has been added to the cart.

        :param book_title: str - the title of the book to be added to the cart
        :return:
        """
        self.click(locator=HomePageLocators.ADD__BUTTON.format(book_title))
        self.click(locator=HomePageLocators.BOOK_ADDED_POPUP_CLOSE__BUTTON)
        return self

    def create_books_list(self, fixed_number_of_books: int = None, range_number_of_books: tuple = None) -> list[str]:
        """
        Provides a random books list with fixed or random length

        :param fixed_number_of_books: int - length of the book list to be randomly generated (optional, required if
        range_number_of_books is not provided).
        :param range_number_of_books: tuple - boundary values for random generation of the book list length (optional,
        required if element is not provided).
        :return: list - a list of books
        """
        assert fixed_number_of_books or range_number_of_books
        if fixed_number_of_books:
            books_list = self.generate_books_list(list_length=fixed_number_of_books)
        elif range_number_of_books:
            generated_number_of_books = generate_random_number(min_value=range_number_of_books[0],
                                                               max_value=range_number_of_books[1])
            books_list = self.generate_books_list(list_length=generated_number_of_books)
        else:
            books_list = []
        return books_list

    def generate_books_list(self, list_length: int) -> list[str]:
        """
        Generates list of books based on storage data

        :param list_length: int - required list length
        :return: list[str] - generated list of books
        """
        chosen_books_ids = choose_items(list_of_items=list(BOOK_OUTLET_BOOKS.keys()),
                                        number_of_items_to_choose=list_length)
        return [BOOK_OUTLET_BOOKS[chosen_book_id]["title"] for chosen_book_id in chosen_books_ids]

    def go_to_cart(self) -> None:
        """
        Opens a cart page in the current tab

        :return: None
        """
        self.click(locator=HomePageLocators.CART__A)

    def go_to_cart_in_a_new_tab(self) -> None:
        """
        Opens a cart page in the new tab

        :return: None
        """
        current_tab = self.get_current_browser_tab()
        self.ctrl_click(locator=HomePageLocators.CART__A)
        self.switch_to_tab(self.get_new_tab(current_tab=current_tab))


    def sort_books(self, by: Literal["asc_title", "dsc_title"]) -> None:
        """
        Switches the sorting method of the books shown on the page

        :param by: str - a string parameter to choose the sorting method
        :return: None
        """
        match by:
            case "asc_title":
                self.select_option(locator=HomePageLocators.SORT_BY__SELECT,
                                   option=HomePageOptions.ASCENDING_TITLE__OPTION)
            case "dsc_title":
                self.select_option(locator=HomePageLocators.SORT_BY__SELECT,
                                   option=HomePageOptions.DESCENDING_TITLE__OPTION)

    def filter_books_by_price(self, min_price: int, max_price: int):
        """
        Applies a price filter to the books shown on the page

        :param min_price: int - minimum price value
        :param max_price: int - maximum price value
        :return: None
        """
        self.click(locator=HomePageLocators.FILTER_BY_PRICE__DIV)
        for price, locator in zip([min_price, max_price], [HomePageLocators.MIN_PRICE__INPUT,
                                                           HomePageLocators.MAX_PRICE__INPUT]):
            self.send_keys(locator=locator, value=str(price))
        self.click(locator=HomePageLocators.APPLY__BUTTON)

    def switch_books_category_to(self, category: str):
        """
        Switches category of the books shown on the page

        :param category: str - a category name
        :return: None
        """
        self.hover(locator=HomePageLocators.BOOK_CATEGORIES__BUTTON)
        self.click(locator=HomePageLocators.CATEGORY__A.format(category=category))

    def get_all_books_on_the_page(self) -> list[str]:
        books_elements = self.wait_for_elements_to_be_visible(HomePageLocators.GENERAL_BOOK__DIV)
        return [book_element.get_attribute(HomePageAttributes.book_item_name) for book_element in books_elements]

    def get_all_prices_on_the_page(self) -> list[float]:
        prices_elements = self.wait_for_elements_to_be_visible(HomePageLocators.GENERAL_PRICE__SPAN)
        return [float(self.get_text(element=price_element).replace("$", ""))
                for price_element in prices_elements]

    def get_category_flag(self) -> str:
        self.wait_for_elements_to_be_visible(HomePageLocators.GENERAL_BOOK__DIV)
        return self.get_text(locator=HomePageLocators.CATEGORY_FLAG__SPAN)

    def switch_language_filter_to(self, language: str):
        self.click(locator=HomePageLocators.FILTER_BY_LANGUAGE__DIV)
        self.click(locator=HomePageLocators.LANGUAGE_OPTION__DIV.format(language=language))

    def get_books_links(self) -> list[str]:
        link_elements =  self.wait_for_elements_to_be_visible(HomePageLocators.GENERAL_BOOK_CARD__A)
        return [link_element.get_attribute("href") for link_element in link_elements]



    # to discuss
    # def get_opened_home_page_tab_name(self) -> str:
    #     return self.driver.title
