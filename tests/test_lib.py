import pytest
# import time
import random
from selenium import webdriver

from constants.all_books_data import BOOK_OUTLET_BOOKS
from constants.applications import BOOK_STORE_SITE
from constants.test import BookNames, TestSuites, ElementsStates, TabParameter
from tests.conftest import home_page


@pytest.mark.parametrize("add_books_to_cart", [TestSuites.DEFAULT_BOOK], indirect=True)
@pytest.mark.parametrize("switch_to_cart", [TabParameter.current_tab], indirect=True)
def test_book_can_be_added_to_the_cart(add_books_to_cart, switch_to_cart, cart_page):
    """
    1) adds a specific book to the cart
    2) switch to the cart
    3) checks if it is available in the cart
    """
    expected_result = add_books_to_cart
    actual_result = cart_page.get_book_title()
    assert expected_result == actual_result


@pytest.mark.parametrize("add_books_to_cart", [TestSuites.DEFAULT_BOOK], indirect=True)
@pytest.mark.parametrize("switch_to_cart", [TabParameter.new_tab], indirect=True)
def test_book_can_be_added_to_the_cart_with_a_new_tab(add_books_to_cart, switch_to_cart, cart_page):
    """
    1) adds a specific book to the cart
    2) switch to the cart in the new tab
    3) checks if it is available in the cart (
    """
    expected_result = add_books_to_cart
    actual_result = cart_page.get_book_title()
    assert expected_result == actual_result


@pytest.mark.parametrize("add_books_to_cart", [TestSuites.DEFAULT_BOOK], indirect=True)
@pytest.mark.parametrize("switch_to_cart", [TabParameter.current_tab], indirect=True)
def test_book_can_be_deleted_from_the_cart(add_books_to_cart, switch_to_cart, cart_page):
    """
    1) adds a specific book to the cart
    2) checks if it is available in the cart
    3) removes a specific book from the cart
    4) checks the status of the cart
    """
    expected_result = add_books_to_cart
    actual_result = cart_page.get_book_title()
    assert expected_result == actual_result

    cart_page.click_delete_button()
    expected_result = ElementsStates.EMPTY_CART_STATE
    actual_result = cart_page.get_cart_empty_status()
    assert expected_result == actual_result


@pytest.mark.parametrize("add_books_to_cart", [TestSuites.NUMBER_OF_BOOKS], indirect=True)
@pytest.mark.parametrize("switch_to_cart", [TabParameter.current_tab], indirect=True)
def test_adding_a_few_random_books_and_checking_the_quantity(add_books_to_cart, switch_to_cart, cart_page):
    """
    1) adds a few random books from the test list (test.py)
    2) checks the number of books added
    """
    expected_result = TestSuites.NUMBER_OF_BOOKS
    actual_result = cart_page.get_the_number_of_book_in_the_cart()
    assert expected_result == actual_result


@pytest.mark.parametrize("add_books_to_cart", [TestSuites.DEFAULT_BOOKS_LIST],
                         indirect=True)
@pytest.mark.parametrize("switch_to_cart", [TabParameter.current_tab], indirect=True)
def test_adding_a_few_books_and_checking_the_titles(add_books_to_cart, switch_to_cart, cart_page):
    """
    1) adds a few specific books
    2) checks the titles of the added books
    """
    expected_result = add_books_to_cart
    actual_result = cart_page.get_titles_of_books_in_the_cart()
    assert len(actual_result) == len(expected_result)
    for item in actual_result:
        assert item in expected_result


def test_switch_sorting(prepare_home_page, home_page):
    """
    1) switches sorting to A-Z
    2) checks the sorting of books on the page
    """
    home_page.sort_books(by="asc_title")
    actual_result = home_page.get_all_books_on_the_page()
    expected_result = sorted(actual_result)
    assert expected_result == actual_result


def test_filter_by_price(prepare_home_page, home_page):
    """
    1) switches the price filter to the specific range
    2) checks if the prices match with the filter
    """
    home_page.filter_books_by_price(min_price=TestSuites.MIN_PRICE, max_price=TestSuites.MAX_PRICE)
    prices = home_page.get_all_prices_on_the_page()
    assert all( price >= TestSuites.MIN_PRICE and price <= TestSuites.MAX_PRICE for price in prices)


def test_switch_categories(prepare_home_page, home_page):
    """
    1) switches the category of books shown
    2) checks if the displayed category flag is correct
    """
    home_page.switch_books_category_to(TestSuites.CATEGORY)
    expected_result = TestSuites.CATEGORY
    actual_result = home_page.get_category_flag()
    assert expected_result == actual_result

def test_language_filter(prepare_home_page, abstract_page, home_page, item_page):
    """
    1) switch to desired language
    2) scan all displayd books for language propertie
    3) check result
    """
    home_page.switch_language_filter_to(TestSuites.LANGUAGE)
    books_links = home_page.get_books_links()
    expected_result = TestSuites.LANGUAGE
    actual_results = []
    for book_link in books_links:
        current_tab = home_page.get_current_browser_tab()
        home_page.open_new_tab_and_switch_to_it(path=book_link)
        actual_results.append(item_page.get_item_language())
        home_page.close_tab()
    assert all(actual_result == expected_result for actual_result in actual_results)





