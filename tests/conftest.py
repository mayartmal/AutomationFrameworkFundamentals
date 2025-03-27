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
def add_books_to_cart(request, home_page, cart_page):
    home_page.clear_browser()
    home_page.close_cookie_dialog()
    print(request.param[0])
    print(request.param[1])
    home_page.add_books_to_cart(book_adder=request.param[0])
    home_page.go_to_cart(in_the_new_tab=request.param[1])
    import time
    time.sleep(5)
    return request.param[0]




# region obsolete fixtures
# @pytest.fixture
# def add_book_to_cart(request, home_page, cart_page):
#     home_page.clear_browser()
#     home_page.click_close_cookie_button()
#     print(request.param[0])
#     print(request.param[1])
#     home_page.click_add_book_button(book_title=request.param[0])
#     home_page.go_to_cart(in_the_new_tab=request.param[1])
#     return request.param[0]
# endregion
