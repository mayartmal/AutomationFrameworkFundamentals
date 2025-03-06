import pytest
from selenium import webdriver

from constants.applications import BOOK_STORE_SITE
from page_objects.browser_wrapper import BrowserWrapper
from page_objects.cart_page import CartPage
from page_objects.home_page import HomePage


@pytest.fixture(scope="session", autouse=True)
def init():
    driver = webdriver.Chrome()
    driver.get(BOOK_STORE_SITE)
    BrowserWrapper.driver = driver
    yield
    driver.quit()


@pytest.fixture
def home_page():
    return HomePage()


@pytest.fixture
def cart_page():
    return CartPage()
