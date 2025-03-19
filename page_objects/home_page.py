from typing import Union, Literal

from page_objects.browser_wrapper import BrowserWrapper
from constants.home_page_locators import (
    ADD_BUTTON_LOCATOR,
    CART_BUTTON_LOCATOR,
    BOOK_ADDED_POPUP_LOCATOR
)
from constants.all_books_data import BOOKS
from utils.data_generator import generate_random_number, choose_items


class HomePage(BrowserWrapper):

    def __init__(self):
        super().__init__()

    def click_add_book_button(self, book_title: str):
        self.click(locator=ADD_BUTTON_LOCATOR.format(book_title))
        self.wait_for_the_element_blink(BOOK_ADDED_POPUP_LOCATOR)
        return self

    def add_books_to_cart(self, book_adder: Union[str, int, tuple]):
        """
        The method adds one specific book OR specific number of random books from storage OR
        random number of random books from storage
        The method changes its behaviour depending on the book_adder data type
        :param book_adder: A book title string OR an integer specifying the number of books to add OR
        a set of border values to generate random number of books.
        :return: None
        """
        match type(book_adder):
            case str():
                # self.click_add_book_button(book_title=book_adder)
                self.click_add_button_for_titles_in(book_titles_list=[book_adder])
            case int():
                titles_list = self.get_book_titles_list(fixed_number_of_books=book_adder)
                self.click_add_button_for_titles_in(book_titles_list=titles_list)
            case tuple():
                titles_list = self.get_book_titles_list(range_number_of_books=book_adder)
                self.click_add_button_for_titles_in(book_titles_list=titles_list)

    def click_cart_button(self):
        self.click(locator=CART_BUTTON_LOCATOR)

    def click_add_button_for_titles_in(self, book_titles_list: list):
        [self.click_add_book_button(book_title=title) for title in book_titles_list]

    def get_book_titles_list(self, fixed_number_of_books = None, range_number_of_books = None):
        if fixed_number_of_books:
            book_titles_list = self.generate_book_titles_list(fixed_number_of_books)
        elif range_number_of_books:
            generated_number_of_books = generate_random_number(range_number_of_books[0], range_number_of_books[1])
            book_titles_list = self.generate_book_titles_list(generated_number_of_books)
        else:
            book_titles_list = None
        return book_titles_list

    def generate_book_titles_list(self, number_of_books):
        chosen_books_ids = choose_items(list(BOOKS.keys()), number_of_books)
        return [BOOKS[chosen_book_id]["title"] for chosen_book_id in chosen_books_ids]


