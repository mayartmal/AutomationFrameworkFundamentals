from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowserWrapper:
    def __init__(self):
        self.driver = None

    def open_new_page(self, page_address: str):
        self.driver = webdriver.Chrome()
        self.driver.get(page_address)
        return self

    def click(self, locator):
        add_btn_element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, locator)))
        add_btn_element.click()

    def get_text(self, locator):
        return WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, locator))).text