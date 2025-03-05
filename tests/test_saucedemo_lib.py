import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

page_address = 'https://www.saucedemo.com/'

def test_page_can_be_opened():
    driver = webdriver.Chrome()
    driver.get(page_address)
    time.sleep(5)
