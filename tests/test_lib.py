import pytest
from page_objects.home_page import HomePage
home_page = HomePage()

def test_book_can_be_added_to_cart():
    book_title = 'Harry Potter and the Chamber of Secrets'
    home_page.click_add_book_button(book_title=book_title)
    home_page.click_cart_button()
    assert book_title == home_page.get_book_title()




