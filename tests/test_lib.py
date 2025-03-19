import pytest
import time
import random

from constants.test import BookNames
from constants.cart_page_states import EMPTY_CART_STATE
from constants.all_books_data import BOOKS
from tests.conftest import home_page


@pytest.mark.parametrize("add_book_to_cart", [*BookNames.FAILED_BOOKS_LIST], indirect=True)
def test_book_can_be_added_to_the_cart(cart_page, add_book_to_cart):
    assert add_book_to_cart == cart_page.get_book_title()


@pytest.mark.parametrize("run", range(1))
@pytest.mark.parametrize("add_book_to_cart", [BookNames.HP_COS, 1], indirect=True)
def test_book_can_be_deleted_from_the_cart(add_book_to_cart, cart_page, run):
    assert add_book_to_cart == cart_page.get_book_title()
    cart_page.click_delete_button_looped()
    assert EMPTY_CART_STATE == cart_page.get_cart_empty_status()
