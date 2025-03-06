from constants.applications import BOOK_STORE_SITE
from page_objects.browser_wrapper import BrowserWrapper
browser_wrapper = BrowserWrapper()

class SessionRunner:
    def __init__(self):
        self.session = None

    def run_new_home_page_session(self):
        session = browser_wrapper.open_new_page(BOOK_STORE_SITE)
        self.session = session
