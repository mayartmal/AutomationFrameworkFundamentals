# button[span[contains(text(), 'Add to Cart')]]" use this
# use ancestor to find a btn
# ADD_BUTTON_LOCATOR: str = "//mat-card[.//text()[contains(.,'{0}')]]//button[span[contains(text(), 'Add to Cart')]]"
# CART_BUTTON_LOCATOR: str= "//button[.//mat-icon[text()='shopping_cart']]"
# BOOK_ADDED_POPUP_LOCATOR: str = "//simple-snack-bar[.//text()[contains(., ' One Item added to cart')]]"

ADD_BUTTON_LOCATOR: str = ("//div[@class='MuiGrid-root MuiGrid-container' and "
                           "@data-cnstrc-item-name='{0}']"
                           "//button[@data-cnstrc-btn='add_to_cart']")
BOOK_ADDED_POPUP_BUTTON_LOCATOR: str = ".//button[@aria-label='close']"
CART_BUTTON_LOCATOR: str = ".//a[contains(@aria-label, 'Shopping cart')]"
COOKIE_DIALOG_CLOSE_BUTTON: str = ".//button[@class=' osano-cm-dialog__close osano-cm-close ']"
SORT_BY__DROP_DOWN = "//select[@aria-label='Sort by']"
ALPHABETICAL__OPTION = "item_name||ascending"
FILTER_BY_PRICE__DIV = "//div[@id='facetName-price']/.."
MIN_PRICE__INPUT = "//input[@id='minValue']"
MAX_PRICE__INPUT = "//input[@id='maxValue']"
APPLY__BUTTON = "//span[text()='Set a custom price range:']/../..//button"
BOOK_CATEGORIES__BUTTON = "//span[text()='Book Categories']/.."
CATEGORY__A= "//div[contains(@class, 'MuiPaper-root MuiPopover-paper')]//span[text()='{category}']/../../.."

