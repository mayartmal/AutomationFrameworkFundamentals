import pytest
from selenium import webdriver

from constants.applications import BOOK_STORE_SITE
from page_objects.browser_wrapper import BrowserWrapper
from page_objects.cart_page import CartPage
from page_objects.home_page import HomePage



# @pytest.fixture(scope="session", autouse=True)
@pytest.fixture(scope="function", autouse=True)
def init():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=options)
    driver.set_window_position(0, 0)
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
    home_page.clear_browser()
    home_page.click_close_cookie_button()
    home_page.click_add_book_button(book_title=request.param)
    home_page.click_cart_button()
    # we return book title here OR NUMBER !!!
    return request.param

@pytest.fixture
def add_books_to_cart(request, home_page, cart_page):
    home_page.clear_browser()
    home_page.click_close_cookie_button()
    home_page.add_books_to_cart(book_adder=request.param)
    home_page.click_cart_button()
    import time
    time.sleep(5)
    return request.param





