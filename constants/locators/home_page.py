class HomePageLocators:
    ADD__BUTTON: str = ("//div[@class='MuiGrid-root MuiGrid-container' and "
                        "@data-cnstrc-item-name='{0}']"
                        "//button[@data-cnstrc-btn='add_to_cart']")
    BOOK_ADDED_POPUP_CLOSE__BUTTON: str = ".//button[@aria-label='close']"
    CART__A: str = ".//a[contains(@aria-label, 'Shopping cart')]"
    COOKIE_DIALOG_CLOSE__BUTTON: str = ".//button[@class=' osano-cm-dialog__close osano-cm-close ']"
    SORT_BY__SELECT: str = "//select[@aria-label='Sort by']"

    FILTER_BY_PRICE__DIV: str = "//div[@id='facetName-price']/.."
    FILTER_BY_LANGUAGE__DIV: str ="//div[@id='facetName-language']/.."
    LANGUAGE_OPTION__DIV: str = FILTER_BY_LANGUAGE__DIV + "/..//span[text()='{language}']/../.."
    MIN_PRICE__INPUT: str = "//input[@id='minValue']"
    MAX_PRICE__INPUT: str = "//input[@id='maxValue']"
    APPLY__BUTTON: str = "//span[text()='Set a custom price range:']/../..//button"
    BOOK_CATEGORIES__BUTTON: str = "//span[text()='Book Categories']/.."
    CATEGORY__A: str = "//div[contains(@class, 'MuiPaper-root MuiPopover-paper')]//span[text()='{category}']/../../.."
    GENERAL_BOOK_CARD__A = "//a[contains(@aria-label, 'open product')]"
    GENERAL_BOOK__DIV: str = GENERAL_BOOK_CARD__A + "/div"
    GENERAL_PRICE__SPAN: str = GENERAL_BOOK_CARD__A + "/div/div/p/span/span[last()]"
    CATEGORY_FLAG__SPAN: str = "//div[@id='pill-item']/div/span"


class HomePageOptions:
    ASCENDING_TITLE__OPTION: str = "item_name||ascending"
    DESCENDING_TITLE__OPTION: str = "item_name||descending"


class HomePageAttributes:
    book_item_name = "data-cnstrc-item-name"

# region obsolete locators for the bookcart.azurewebsites.net app
# button[span[contains(text(), 'Add to Cart')]]" use this
# use ancestor to find a btn
# ADD_BUTTON_LOCATOR: str = "//mat-card[.//text()[contains(.,'{0}')]]//button[span[contains(text(), 'Add to Cart')]]"
# CART_BUTTON_LOCATOR: str= "//button[.//mat-icon[text()='shopping_cart']]"
# BOOK_ADDED_POPUP_LOCATOR: str = "//simple-snack-bar[.//text()[contains(., ' One Item added to cart')]]"
# endregion
