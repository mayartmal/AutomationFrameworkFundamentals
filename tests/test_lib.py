import pytest
#fixtures how to implement and how to use
#browser configuration before test


def test_book_can_be_added_to_cart(home_page, cart_page):
    book_title = 'Harry Potter and the Chamber of Secrets'
    home_page.click_add_book_button(book_title=book_title)
    home_page.click_cart_button()
    assert book_title == cart_page.get_book_title()
