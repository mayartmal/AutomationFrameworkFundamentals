import pytest
from selenium import webdriver

from constants.applications import BOOK_STORE_SITE
from page_objects.browser_wrapper import BrowserWrapper
from page_objects.cart_page import CartPage
from page_objects.home_page import HomePage
from sandbox2 import book_title


# @pytest.fixture(scope="session", autouse=True)
@pytest.fixture(scope="function", autouse=True)
def init():
    driver = webdriver.Chrome()
    driver.get(BOOK_STORE_SITE)
    driver.delete_all_cookies()
    BrowserWrapper.driver = driver
    yield
    driver.quit()


@pytest.fixture
def home_page():
    return HomePage()


@pytest.fixture
def cart_page():
    return CartPage()

@pytest.fixture
def add_book_to_cart(request, home_page, cart_page):
    home_page.clear_browser() \
             .click_add_book_button(book_title=request.param) \
             .click_cart_button()
    # we return book title here
    return request.param


@pytest.fixture
def add_books_to_cart(request, home_page, cart_page):
    home_page.clear_browser()
    home_page.add_books_to_cart(book_title=request.param)
    home_page.click_cart_button()
    return request.param





