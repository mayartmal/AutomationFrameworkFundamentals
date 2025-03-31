import pytest
from selenium import webdriver

from constants.applications import BOOK_STORE_SITE
from page_objects.browser_wrapper import BrowserWrapper
from page_objects.common_page import CommonPage
from page_objects.cart_page import CartPage
from page_objects.home_page import HomePage
from page_objects.item_page import ItemPage


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
def abstract_page():
    return CommonPage()


@pytest.fixture
def home_page():
    return HomePage()


@pytest.fixture
def cart_page():
    return CartPage()

@pytest.fixture
def item_page():
    return ItemPage()


@pytest.fixture
def prepare_home_page(home_page):
    home_page.clear_browser()
    home_page.close_cookie_dialog()


@pytest.fixture
def add_books_to_cart(request, prepare_home_page, home_page, cart_page):
    home_page.add_books_to_cart(book_adder=request.param)
    return request.param


@pytest.fixture
def switch_to_cart(request, home_page):
    if request.param == "new tab":
        home_page.go_to_cart_in_a_new_tab()
    elif request.param == "current tab":
        home_page.go_to_cart()
    else:
        home_page.go_to_cart()


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
