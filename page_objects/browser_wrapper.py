from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from typing import Literal, Optional, List
import time

from constants.configurations import WEB_DRIVER_WAIT_TIMEOUT


class BrowserWrapper:
    driver: webdriver.Chrome = None

    def __init__(self):
        self.actions = ActionChains(self.driver)

    # region element waits OK
    def driver_waiter(self, locator: str, condition: EC, locator_type: By = By.XPATH) -> WebElement:
        """
        Waits for an element using a specified locator and condition.

        :param locator: str - a locator string of the web element.
        :param condition: EC - an expected condition to wait for before proceeding.
        :param locator_type: By - a type of the locator.
        :return: WebElement - the web element that is returned after the waits completes.
        """
        return WebDriverWait(self.driver, WEB_DRIVER_WAIT_TIMEOUT).until(condition((locator_type, locator)))

    def wait_for_element_to_be_clickable(self, locator: str) -> WebElement:
        """
        Waits for an element to become clickable using the specified locator.

        :param locator: str - the locator string of the web element.
        :return: WebElement - the clickable web element.
        """
        return self.driver_waiter(locator, EC.element_to_be_clickable)

    def wait_for_element_to_be_invisible(self, locator: str) -> None:
        """
        Waits for an element to become invisible using the specified locator.

        :param locator: str: - the locator string of the web element.
        :return: None - the method does not return a WebElement, as the element becomes invisible.
        """
        self.driver_waiter(locator, EC.invisibility_of_element)

    def wait_for_element_to_be_visible(self, locator: str) -> WebElement:
        """
         Waits for an element to become visible using the specified locator.

        :param locator: str - the locator string of the web element.
        :return: WebElement - the visible web element.
        """
        return self.driver_waiter(locator, EC.visibility_of_element_located)

    def wait_for_element_to_be_presence(self, locator: str) -> WebElement:
        """
        Waits for the presence of an element in the DOM using the specified locator.

        :param locator: str - the locator string of the web element.
        :return: WebElement - the web element that is found in the DOM.
        """
        return self.driver_waiter(locator, EC.presence_of_element_located)

    def wait_for_the_element_blink(self, locator: str) -> None:
        """
        Waits for an element to blink (become visible and then invisible) using specified locator

        :param locator: str - the locator string of the web element
        :return: None
        """
        self.wait_for_element_to_be_visible(locator)
        self.wait_for_element_to_be_invisible(locator)

    def wait_for_page_to_load(self) -> None:
        """
        Waits for the page to completely loaded

        Repeatedly checks the document's readyState and waits until it is 'complete',
        indicating that the page has fully loaded

        :return: None
        """
        while self.driver.execute_script('return document.readyState') != 'complete':
            self.driver.implicitly_wait(.2)

    # endregion

    # region element states OK
    def element_displayed(self, locator: str) -> bool:
        """
        Checks if an element is displayed on the page using specified locator.

        :param locator: str - the locator string of the web element
        :return: bool - True if the element is displayed, False otherwise
        """
        return self.driver.find_element(By.XPATH, locator).is_displayed()

    # endregion

    # region element getters OK
    def get_element(self, locator: str, locator_type: By = By.XPATH) -> WebElement:
        """
        Gets a web element based on the specified locator

        :param locator: str - the locator string of the web element.
        :param locator_type: By - a type of the locator.
        :return: WebElement - a web element found
        """

        return self.driver.find_element(locator_type, locator)

    def get_elements(self, locator: str, locator_type: By = By.XPATH) -> list[WebElement]:
        """
        Gets a list of web element based on the specified locator

        :param locator: str - the locator string of the web elements.
        :param locator_type: By - a type of the locator.
        :return: list[WebElement] - a list of web elements found
        """
        return self.driver.find_elements(locator_type, locator)

    # endregion

    # region user actions OK
    def click(self, locator: str = None, element: WebElement = None) -> None:
        """
        Clicks on a web element either by its locator or a given WebElement instance.

        :param locator: str - the locator string of the web element (optional, required if element is not provided).
        :param element: WebElement - the WebElement instance to be clicked (optional, required if locator is not provided).
        :return: None
        """
        assert element or locator
        if locator:
            element = self.wait_for_element_to_be_clickable(locator)
            self.move_to_element(element)
            element.click()
        elif element:
            self.move_to_element(element)
            element.click()

    def ctrl_click(self, locator: str, element: WebElement = None) -> None:
        """
        Performs a Ctrl + Click action on a web element by its locator or a given WebElement instance.

        :param locator: str - the locator string of the web element (optional, required if element is not provided).
        :param element: WebElement - the WebElement instance to be clicked (optional, required if locator is not provided).
        :return: None
        """
        assert locator or element
        if locator:
            element = self.wait_for_element_to_be_clickable(locator=locator)
            self.move_to_element(element)
            self.actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
        elif element:
            self.move_to_element(element)
            self.actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

    def hover_to_element(self, locator: str = None, element: WebElement = None) -> None:
        """
        Moves the mouse pointer over a specified web element.

        :param locator: str - the locator string of the web element (optional, required if element is not provided).
        :param element: WebElement - the WebElement instance to hover over (optional, required if locator is not provided).
        :return: None
        """
        assert element or locator
        if locator:
            element = self.wait_for_element_to_be_visible(locator=locator)
            self.move_to_element(element=element)
        elif element:
            # why this case is necessary?
            self.move_to_element(element=element)

    # endregion

    # region page navigation OK
    def move_to_element(self, element: WebElement) -> None:
        """
        Moves the mouse pointer to the specified web element.

        This method uses the Actions class to move the cursor to the given element
        and immediately performs the action.
        If `.perform()` is removed, it will return an ActionChain instance, allowing
        to build a chain of multiple actions.

        :param element: WebElement - The web element to move the mouse pointer to.
        :return: None
        """
        self.actions.move_to_element(element).perform()

    # endregion

    # region tab actions OK
    def get_all_browsers_tabs(self) -> List[str]:
        return self.driver.window_handles

    def get_current_browser_tab(self) -> str:
        return self.driver.current_window_handle

    def switch_to_tab(self, tab: str) -> None:
        return self.driver.switch_to.window(tab)

    def get_new_tab(self, current_tab):
        return [tab for tab in self.get_all_browsers_tabs() if tab != current_tab][0]

    def open_new_tab(self, path) -> str:
        tab_before = self.get_current_browser_tab()
        self.driver.execute_script(f'''window.open("{path}");''')
        return self.get_new_tab(tab_before)

    def open_new_tab_and_switch_to_it(self, path) -> None:
        new_tab = self.open_new_tab(path)
        self.switch_to_tab(new_tab)

    def close_tab(self):
        self.driver.close()
        self.switch_to_tab(self.get_all_browsers_tabs()[0])

    # endregion

    # region element data getters/setters OK
    def get_text(self, locator: str = None, element: WebElement = None) -> Optional[str]:
        """
        Gets the text content of a web element.

        :param locator: str - the locator string to find the web element (optional, required if element is not provided).
        :param element: WebElement - an existing web element to extract text from (optional, required if locator is not provided).
        :return: str | None - the text content of the element, or None if the element is not found.
        """
        assert locator or element
        if locator:
            return self.wait_for_element_to_be_visible(locator).text
        elif element:
            return element.text

    def select_option(self, locator: str, option: str) -> None:
        """
        Selects an option from a dropdown menu by its value.

        :param locator: str - the locator string of the dropdown element.
        :param option: str - the value string of the option to be selected.
        :return: None
        """
        select = Select(self.wait_for_element_to_be_clickable(locator))
        select.select_by_value(option)

    def send_keys(self, locator: str, value: str) -> None:
        """
        Sends the specified keys to a clickable web element.

        :param locator: str - the locator string of the web element.
        :param value: str - the value to be sent to the element.
        :return: None
        """
        element = self.wait_for_element_to_be_clickable(locator)
        self.move_to_element(element)
        self.driver.execute_script("window.scrollBy(0, 100);")
        element.send_keys(value)

    # endregion

    # region auxiliary actions OK
    def clear_browser(self) -> None:
        """
        Clears browser cookies, local storage, and session storage, then refreshes the page.

        return: None
        """
        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.execute_script("window.sessionStorage.clear();")
        self.driver.refresh()
    # endregion
