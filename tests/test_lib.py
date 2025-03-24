import pytest
import time
import random

from constants.test import BookNames, BookCount
from constants.cart_page_states import EMPTY_CART_STATE
from constants.all_books_data import BOOKS
from tests.conftest import home_page

from selenium import webdriver
from constants.applications import BOOK_STORE_SITE

# def test_open():
#     print("Step1")
#     print("Step2")


@pytest.mark.parametrize("run", range(1))
@pytest.mark.parametrize("add_book_to_cart", [BookNames.HEIR_OF_FIRE], indirect=True)
def test_book_can_be_added_to_the_cart(add_book_to_cart, cart_page, run):
    # assert add_book_to_cart == cart_page.get_book_title()
    assert BookNames.HEIR_OF_FIRE == cart_page.get_book_title()


@pytest.mark.parametrize("run", range(1))
@pytest.mark.parametrize("add_book_to_cart", [BookNames.HEIR_OF_FIRE], indirect=True)
def test_book_can_be_deleted_from_the_cart(add_book_to_cart, cart_page, run):
    assert add_book_to_cart == cart_page.get_book_title()
    cart_page.click_delete_button()
    assert EMPTY_CART_STATE == cart_page.get_cart_empty_status()

@pytest.mark.parametrize("run", range(1))
@pytest.mark.parametrize("add_books_to_cart", [BookCount.NUMBER_OF_BOOKS], indirect=True)
def test_adding_a_few_random_books_and_checking_the_quantity(add_books_to_cart, cart_page, run):
    assert BookCount.NUMBER_OF_BOOKS == cart_page.get_the_number_of_book_in_the_cart()


@pytest.mark.parametrize("run", range(1))
@pytest.mark.parametrize("add_books_to_cart", [[BookNames.HEIR_OF_FIRE, BookNames.LEGENDBORN, BookNames.CROWN]],
                         indirect=True)
def test_adding_a_few_random_books_and_checking_the_titles(add_books_to_cart, cart_page, run):
    expected_result = add_books_to_cart
    actual_result = cart_page.get_titles_of_books_in_the_cart()
    assert len(actual_result) == len(expected_result)
    for item in actual_result:
        assert item in expected_result


def test_switch_sorting(home_page):
    print("start sorting test")
    home_page.clear_browser()
    home_page.click_close_cookie_button()
    home_page.alphabetize_books()
    print("end sorting test")

@pytest.mark.parametrize("run", range(100))
def test_filter_by_price(home_page, run):
    print("start filter test")
    home_page.clear_browser()
    home_page.click_close_cookie_button()
    home_page.filter_books_by_price(min_price=0, max_price=5)
    print("end filter test")

def test_switch_categories(home_page):
    home_page.clear_browser()
    home_page.switch_books_category_to("Fiction")
    time.sleep(10)



