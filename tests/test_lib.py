import pytest

from page_objects.cart_page import CartPage
from page_objects.home_page import HomePage
from page_objects.session_runner import SessionRunner
session_runner = SessionRunner()
session_runner.run_new_home_page_session()
home_page = HomePage(session_runner.session)
cart_page = CartPage(session_runner.session)


def test_book_can_be_added_to_cart():
    book_title = 'Harry Potter and the Chamber of Secrets'
    home_page.click_add_book_button(book_title=book_title)
    home_page.click_cart_button()
    assert book_title == cart_page.get_book_title()




