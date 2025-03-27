class HomePageLocators:
    ADD__BUTTON: str = ("//div[@class='MuiGrid-root MuiGrid-container' and "
                        "@data-cnstrc-item-name='{0}']"
                        "//button[@data-cnstrc-btn='add_to_cart']")
    BOOK_ADDED_POPUP_CLOSE__BUTTON: str = ".//button[@aria-label='close']"
    CART__A: str = ".//a[contains(@aria-label, 'Shopping cart')]"
    COOKIE_DIALOG_CLOSE__BUTTON: str = ".//button[@class=' osano-cm-dialog__close osano-cm-close ']"
    SORT_BY__SELECT: str = "//select[@aria-label='Sort by']"

    FILTER_BY_PRICE__DIV: str = "//div[@id='facetName-price']/.."
    MIN_PRICE__INPUT: str = "//input[@id='minValue']"
    MAX_PRICE__INPUT: str = "//input[@id='maxValue']"
    APPLY__BUTTON: str = "//span[text()='Set a custom price range:']/../..//button"
    BOOK_CATEGORIES__BUTTON: str = "//span[text()='Book Categories']/.."
    CATEGORY__A: str = "//div[contains(@class, 'MuiPaper-root MuiPopover-paper')]//span[text()='{category}']/../../.."


class HomePageOptions:
    ASCENDING_TITLE__OPTION: str = "item_name||ascending"
    DESCENDING_TITLE__OPTION: str = "item_name||descending"

# region obsolete locators for the bookcart.azurewebsites.net app
# button[span[contains(text(), 'Add to Cart')]]" use this
# use ancestor to find a btn
# ADD_BUTTON_LOCATOR: str = "//mat-card[.//text()[contains(.,'{0}')]]//button[span[contains(text(), 'Add to Cart')]]"
# CART_BUTTON_LOCATOR: str= "//button[.//mat-icon[text()='shopping_cart']]"
# BOOK_ADDED_POPUP_LOCATOR: str = "//simple-snack-bar[.//text()[contains(., ' One Item added to cart')]]"
# endregion
