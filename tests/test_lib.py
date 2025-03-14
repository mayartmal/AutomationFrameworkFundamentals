import pytest
import time

from constants.test import BookNames


def test_book_can_be_added_to_the_cart(home_page, cart_page, browser):
    browser.clear_browser()
    book_title = BookNames.HARRY_POTTER_2
    home_page.click_add_book_button(book_title=book_title)
    home_page.click_cart_button()
    assert book_title == cart_page.get_book_title()

@pytest.mark.parametrize("run", range(3))
def test_book_can_be_deleted_from_the_cart(home_page, cart_page, browser, run):
    browser.clear_browser()
    book_title =  BookNames.HARRY_POTTER_2
    empty_cart_status = 'Your shopping cart is empty.'
    home_page.click_add_book_button(book_title=book_title)
    home_page.click_cart_button()
    assert book_title == cart_page.get_book_title()
    cart_page.click_delete_button_looped()
    assert empty_cart_status == cart_page.get_cart_empty_status()


# def test_search_book_by_title(home_page):
#     book_title = 'Harry Potter and the Chamber of Secrets'
#
# def test_price_filter(home_page):
#     pass

#add ~5 books (check titles)
#add ~5 rnd books (check quantity )
#add check details by link (from cart)