import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

#site rendered
#click by 'add to cart' for Harry Potter and the Chamber of Secrets
#click by cart pictogram
#get title of added book
#compare titles of book

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def test_site_can_be_opened():
    locator = '//app-root'
    driver = webdriver.Chrome()
    driver.get('https://bookcart.azurewebsites.net/')
    element = None
    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, locator)))
    finally:
        driver.quit()
    assert element is not None

def test_add_book_btn_clickable():
    book_name = 'Harry Potter and the Chamber of Secrets'
    locator = f'//mat-card[.//text()[contains(.,"{book_name}")]]//button[span[contains(text(), "Add to Cart")]]'
    driver = webdriver.Chrome()
    driver.get('https://bookcart.azurewebsites.net/')
    try:
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, locator)))
    finally:
        driver.quit()
    assert element is not None

def test_book_can_be_added_to_cart():
    book_title = 'Harry Potter and the Chamber of Secrets'
    add_btn_locator = f'//mat-card[.//text()[contains(.,"{book_title}")]]//button[span[contains(text(), "Add to Cart")]]'
    cart_btn_locator = '//button[.//mat-icon[text()="shopping_cart"]]'
    added_book_locator = '//td[contains(@class, "mat-column-title")]//a'

    driver = webdriver.Chrome()
    driver.get('https://bookcart.azurewebsites.net/')
    try:
        add_btn_element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, add_btn_locator)))
        add_btn_element.click()
        cart_btn_element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, cart_btn_locator)))
        cart_btn_element.click()
        added_book_title_element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, added_book_locator)))
        added_book_title = added_book_title_element.text
        logger.info(added_book_title)
    finally:
        driver.quit()
    assert book_title == added_book_title
    #есть ли простой способ вывода диагностической информации в консоль? логгер как будто не работает



