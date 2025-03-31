from page_objects.browser_wrapper import BrowserWrapper
from constants.item_page import ItemPageLocators

class ItemPage(BrowserWrapper):

    def __init__(self):
        super().__init__()


    def get_item_language(self) -> str:
        self.click(ItemPageLocators.ADDITIONAL_INFO__BUTTON)
        return self.get_text(locator=ItemPageLocators.LANGUAGE__A)

