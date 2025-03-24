import time
from typing import Union, Literal
import builtins
from selenium.common import NoSuchElementException
from selenium import webdriver

from page_objects.browser_wrapper import BrowserWrapper
from constants.home_page_locators import (
    ADD_BUTTON_LOCATOR,
    CART_BUTTON_LOCATOR,
    COOKIE_DIALOG_CLOSE_BUTTON,
    # BOOK_ADDED_POPUP_LOCATOR
    BOOK_ADDED_POPUP_BUTTON_LOCATOR,
    SORT_BY__DROP_DOWN,
    ALPHABETICAL__OPTION,
    FILTER_BY_PRICE__DIV,
    MIN_PRICE__INPUT,
    MAX_PRICE__INPUT,
    APPLY__BUTTON,
    BOOK_CATEGORIES__BUTTON,
    CATEGORY__A
)
from constants.all_books_data import BOOKS, BOOKOUTLET_BOOKS
from utils.data_generator import generate_random_number, choose_items


class HomePage(BrowserWrapper):

    def __init__(self):
        super().__init__()

    def click_close_cookie_button(self):
        try:
            self.click(locator=COOKIE_DIALOG_CLOSE_BUTTON)if self.element_displayed(locator=COOKIE_DIALOG_CLOSE_BUTTON
                                                                                     ) else None
        except NoSuchElementException:
            pass

    def click_add_book_button(self, book_title: str):
        self.click(locator=ADD_BUTTON_LOCATOR.format(book_title))
        self.click(locator=BOOK_ADDED_POPUP_BUTTON_LOCATOR)
        # self.wait_for_the_element_blink(BOOK_ADDED_POPUP_LOCATOR)
        return self

    def add_books_to_cart(self, book_adder: Union[str, list, int, tuple]):
        """
        The method adds one specific book OR specific number of random books from storage OR
        random number of random books from storage
        The method changes its behaviour depending on the book_adder data type
        :param book_adder: A book title string OR an integer specifying the number of books to add OR
        a set of border values to generate random number of books.
        :return: None
        """
        # print("inside_add_books")
        # print(book_adder)
        # print(type(book_adder))
        # print(str())
        # print(type(str()))
        match type(book_adder):
            case builtins.str:
                # self.click_add_book_button(book_title=book_adder)
                print("inside_string")
                self.click_add_button_for_titles_in(book_titles_list=[book_adder])
            case builtins.int:
                print("inside_int")
                titles_list = self.get_book_titles_list(fixed_number_of_books=book_adder)
                self.click_add_button_for_titles_in(book_titles_list=titles_list)
            case builtins.list:
                print("inside_list")
                self.click_add_button_for_titles_in(book_titles_list=book_adder)
            case builtins.tuple:
                print("inside_tuple")
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
        chosen_books_ids = choose_items(list(BOOKOUTLET_BOOKS.keys()), number_of_books)
        return [BOOKOUTLET_BOOKS[chosen_book_id]["title"] for chosen_book_id in chosen_books_ids]

    def alphabetize_books(self):
        select_element = self.get_element(locator=SORT_BY__DROP_DOWN, wait_for="clickable")
        self.select_option(element=select_element, option=ALPHABETICAL__OPTION)
        import time
        time.sleep(10)

    def filter_books_by_price(self, min_price: int, max_price: int):
        self.click(FILTER_BY_PRICE__DIV)
        for price, locator in zip([min_price, max_price], [MIN_PRICE__INPUT, MAX_PRICE__INPUT]):
            self.input_text_for(self.get_element(locator, wait_for="clickable"), str(price))
        self.click(APPLY__BUTTON)

    def switch_books_category_to(self, category):
        element = self.get_element(locator=BOOK_CATEGORIES__BUTTON, wait_for="clickable")
        self.hover_to_element(element=element)
        self.click(locator=CATEGORY__A.format(category=category))




