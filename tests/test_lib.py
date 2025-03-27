import pytest
import time
import random
from selenium import webdriver

from constants.all_books_data import BOOK_OUTLET_BOOKS
from constants.applications import BOOK_STORE_SITE
from constants.cart_page_states import EMPTY_CART_STATE
from constants.test import BookNames, BookCount
from tests.conftest import home_page

# def test_open():
#     print("Step1")
#     print("Step2")

# page object methods audit
# implement add books to 1st test
# add asserts for tests


# @pytest.mark.parametrize("run", range(1))
# @pytest.mark.parametrize("add_book_to_cart", [[BookNames.LEGENDBORN, False]], indirect=True)
# def test_book_can_be_added_to_the_cart(add_book_to_cart, cart_page, run):
#     """
#     1) adds a specific book to the cart
#     2) checks if it is available in the cart
#     """
#     assert BookNames.LEGENDBORN == cart_page.get_book_title()

@pytest.mark.parametrize("run", range(1))
@pytest.mark.parametrize("add_books_to_cart", [[BookNames.LEGENDBORN, False]], indirect=True)
def test_book_can_be_added_to_the_cart(add_books_to_cart, cart_page, run):
    """
    1) adds a specific book to the cart
    2) checks if it is available in the cart
    """
    assert BookNames.LEGENDBORN == cart_page.get_book_title()



@pytest.mark.parametrize("run", range(1))
@pytest.mark.parametrize("add_books_to_cart", [[BookNames.LEGENDBORN, True]], indirect=True)
def test_book_can_be_added_to_the_cart_with_a_new_tab(add_books_to_cart, cart_page, run):
    """
    1) adds a specific book to the cart
    2) switch to the new tab with name 'cart'
    3) check the name of a tab
    4) checks if book is available in the cart
    5) switch back to home tab
    6) switches back to the home tab
    7) checks the name of the home tab
    """
    assert cart_page.get_opened_cart_page_tab_name() == "Cart"
    assert BookNames.LEGENDBORN == cart_page.get_book_title()
    # time.sleep(5)
    cart_page.close_cart_page_tab()
    # time.sleep(5)
    # print("home page name")



    # assert
    # assert current tab name == home tab name


@pytest.mark.parametrize("run", range(1))
@pytest.mark.parametrize("add_books_to_cart", [[BookNames.LEGENDBORN, False]], indirect=True)
def test_book_can_be_deleted_from_the_cart(add_books_to_cart, cart_page, run):
    """
    1) adds a specific book to the cart
    2) checks if it is available in the cart
    3) removes a specific book from the cart
    4) checks the status of the cart
    """
    assert add_books_to_cart == cart_page.get_book_title()
    cart_page.click_delete_button()
    assert EMPTY_CART_STATE == cart_page.get_cart_empty_status()


@pytest.mark.parametrize("run", range(1))
@pytest.mark.parametrize("add_books_to_cart", [[BookCount.NUMBER_OF_BOOKS, False]], indirect=True)
def test_adding_a_few_random_books_and_checking_the_quantity(add_books_to_cart, cart_page, run):
    """
    1) adds a few random books from the test list (test.py)
    2) checks the number of books added
    """
    assert BookCount.NUMBER_OF_BOOKS == cart_page.get_the_number_of_book_in_the_cart()


@pytest.mark.parametrize("run", range(1))
@pytest.mark.parametrize("add_books_to_cart", [[[BookNames.LEGENDBORN, BookNames.CROWN], False]],
                         indirect=True)
def test_adding_a_few_books_and_checking_the_titles(add_books_to_cart, cart_page, run):
    """
    1) adds a few specific books
    2) checks the titles of the added books
    """
    expected_result = add_books_to_cart
    actual_result = cart_page.get_titles_of_books_in_the_cart()
    assert len(actual_result) == len(expected_result)
    for item in actual_result:
        assert item in expected_result


def test_switch_sorting(home_page):
    """
    1) switches sorting to A-Z
    2) checks the sorting of books on the page
    """
    print("start sorting test")
    home_page.clear_browser()
    home_page.close_cookie_dialog()
    home_page.sort_books(by="asc_title")
    time.sleep(5)
    home_page.sort_books(by="dsc_title")
    time.sleep(5)
    print("end sorting test")
#    add assert with list and sorted list

@pytest.mark.parametrize("run", range(1))
def test_filter_by_price(home_page, run):
    """
    1) switches the price filter to the specific range
    2) checks if the prices match with the filter
    """
    print("start filter test")
    home_page.clear_browser()
    home_page.close_cookie_dialog()
    home_page.filter_books_by_price(min_price=0, max_price=5)
    time.sleep(10)
    print("end filter test")
# add assert with all prices <5

def test_switch_categories(home_page):
    """
    1) switches the category of books shown
    2) checks if the books shown match the category
    """
    home_page.clear_browser()
    home_page.switch_books_category_to("Fiction")
    time.sleep(5)
#     assert with test book (see cat)   it is possible to select random book(s) on the page and checks the category





