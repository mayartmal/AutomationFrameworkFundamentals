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
