class CartPageLocators:
    ADDED_BOOK_NAME__TEXT_ELEMENT: str = "//div[@id='desktop_cartItemsGrid']/..//div[contains(@style, 'width')]//h6"
    DELETE__BUTTON: str = ("//div[@id='desktop_cartItemsGrid']/..//"
                           "div[contains(@style, 'width')]//button[span[contains(text(), 'Remove')]]")
    EMPTY_CART__P: str = "//div[@class='jss21']//p[contains(text(), 'Your Shopping Cart is Empty!')]"
    BOOKS_QUANTITY__INPUT: str = ("//div[contains(@class, 'MuiContainer-root MuiContainer-maxWidthLg')]"
                                  "[.//div[@id='desktop_cartItemsGrid']]//"
                                  "input[@aria-label='Change product quantity.']")

# region obsolete locators for the bookcart.azurewebsites.net app
# CHECKOUT_BUTTON_LOCATOR: str = "//button[.//text()[contains(., 'CheckOut')]]"
# CLEAR_CART_BUTTON_LOCATOR: str = "//button[.//text()[contains(., 'Clear cart')]]"
# CART_TABLE_LOCATOR: str = "//table"
# SHOPPING_CART_LOCATOR: str = "//app-shoppingcart"
# BOOKS_QUANTITY_LOCATOR: str = ("//div[contains(@class, 'MuiContainer-root MuiContainer-maxWidthLg')]"
#                                "[.//div[@id='desktop_cartItemsGrid']]//"
#                                "input[@aria-label='Change product quantity.']")
# ADDED_BOOK_LOCATOR: str = "//td[contains(@class, 'mat-column-title')]//a"
# DELETE_BUTTON_LOCATOR: str = "//button[@mattooltip='Delete item']"
# endregion
