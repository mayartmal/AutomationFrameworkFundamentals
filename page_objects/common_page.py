from abc import abstractmethod

from page_objects.browser_wrapper import BrowserWrapper

class CommonPage(BrowserWrapper):

    def __init__(self):
        super().__init__()


    #
    # @abstractmethod
    # def is_page_opened(self):
    #     pass

