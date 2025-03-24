from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from typing import Literal
import time

from constants.configurations import WEB_DRIVER_WAIT_TIMEOUT


class BrowserWrapper:
    driver: webdriver.Chrome = None

    def __init__(self):
        self.actions = ActionChains(self.driver)

    def driver_waiter(self, locator, condition, locator_type=By.XPATH):
        return WebDriverWait(self.driver, WEB_DRIVER_WAIT_TIMEOUT).until(condition((locator_type, locator)))

    def wait_for_element_to_be_clickable(self, locator):
        return self.driver_waiter(locator, EC.element_to_be_clickable)

    def wait_for_element_to_be_invisible(self, locator):
        return self.driver_waiter(locator, EC.invisibility_of_element)

    def wait_for_element_to_be_visible(self, locator):
        return self.driver_waiter(locator, EC.visibility_of_element_located)

    def wait_for_element_to_be_presence(self, locator):
        return self.driver_waiter(locator, EC.presence_of_element_located)

    def element_displayed(self, locator):
        return self.driver.find_element(By.XPATH, locator).is_displayed()

    def wait_for_page_to_load(self):
       while self.driver.execute_script('return document.readyState') != 'complete':
           self.driver.implicitly_wait(.2)

    def wait_for_the_element_blink(self, locator):
        self.wait_for_element_to_be_visible(locator)
        self.wait_for_element_to_be_invisible(locator)

    def get_element(self, locator, wait_for: Literal["presence", "clickable", "visible"]=None, locator_type=By.XPATH):
        if wait_for == "presence":
            self.wait_for_element_to_be_presence(locator)
        elif wait_for == "clickable":
            self.wait_for_element_to_be_clickable(locator)
        elif wait_for == "visible":
            self.wait_for_element_to_be_visible(locator)
        return self.driver.find_element(locator_type, locator)

    def get_elements(self, locator):
        return self.driver.find_elements(By.XPATH, locator)

    def click(self, locator=None, element=None):
        assert element or locator
        if element:
            self.move_to_element(element)
            element.click()
        elif locator:
            element = self.wait_for_element_to_be_clickable(locator)
            self.move_to_element(element)
            element.click()

    def hover_to_element(self, locator=None, element=None):
        assert element or locator
        if element:
            self.move_to_element(element=element)
        elif locator:
            self.move_to_element(element=self.get_element(locator=locator, wait_for="visible"))



    def get_text(self, locator: str=None, element: WebElement=None):
        if locator:
            return self.wait_for_element_to_be_visible(locator).text
        elif element:
            return element.text

    def input_text_for(self, element, variable: str):
        self.move_to_element(element)
        self.driver.execute_script("window.scrollBy(0, 100);")
        element.send_keys(variable)

    def clear_browser(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.execute_script("window.sessionStorage.clear();")
        self.driver.refresh()
        return self

    def move_to_element(self, element):
        self.actions.move_to_element(element).perform()

    def scroll_to_element(self, element):
        return self.actions.scroll_to_element(element)

    def select_option(self, element: WebElement, option: str):
        select = Select(element)
        select.select_by_value(option)


