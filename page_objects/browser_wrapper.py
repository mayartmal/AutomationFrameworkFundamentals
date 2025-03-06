from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants.configurations import WEB_DRIVER_WAIT_TIMEOUT


class BrowserWrapper:

    driver = None

    def driver_waiter(self, locator, condition, locator_type=By.XPATH):
        return WebDriverWait(self.driver, WEB_DRIVER_WAIT_TIMEOUT).until(condition((locator_type, locator)))

    def click(self, locator):
        add_btn_element = self.driver_waiter(locator, EC.element_to_be_clickable)
        add_btn_element.click()

    def get_text(self, locator):
        return self.driver_waiter(locator, EC.presence_of_element_located).text
