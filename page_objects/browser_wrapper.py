from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

from constants.configurations import WEB_DRIVER_WAIT_TIMEOUT


class BrowserWrapper:
    driver: webdriver = None

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

    def wait_for_page_to_load(self):
        driver = self.driver

        def is_page_loaded(driver):
            return driver.execute_script('return document.readyState') == 'complete'

        WebDriverWait(driver, 60).until(is_page_loaded)

    def wait_for_the_element_blink(self, locator):
        self.wait_for_element_to_be_visible(locator)
        self.wait_for_element_to_be_invisible(locator)

    def get_element(self, locator, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, locator)

    def click(self, locator=None, element=None):
        assert element or locator
        if element:
            self.scroll_to_element(element)
            element.click()
        elif locator:
            element = self.wait_for_element_to_be_clickable(locator)
            self.scroll_to_element(element)
            element.click()

    def get_text(self, locator):
        element = self.wait_for_element_to_be_visible(locator)
        return element.text

    def clear_browser(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.execute_script("window.sessionStorage.clear();")
        self.driver.refresh()
        return self

    def scroll_to_element(self, element):
        self.actions.move_to_element(element).perform()


