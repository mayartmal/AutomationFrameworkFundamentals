# ADDED_BOOK_LOCATOR: str = "//td[contains(@class, 'mat-column-title')]//a"
# ADDED_BOOK_LOCATOR: str = "(.//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2 MuiGrid-item MuiGrid-grid-xs-12']//h6)[1]"
# DELETE_BUTTON_LOCATOR: str = "//button[@mattooltip='Delete item']"
# ADDED_BOOK_NAME__TEXT_ELEMENT: str = "//div[@id='desktop_cartItemsGrid']/..//div[contains(@style, 'width')]//h6"
DELETE_BUTTON_LOCATOR: str = "//div[@id='desktop_cartItemsGrid']/..//div[contains(@style, 'width')]//button[span[contains(text(), 'Remove')]]"
EMPTY_CART_LOCATOR: str = "//div[@class='jss21']//p[contains(text(), 'Your Shopping Cart is Empty!')]"
CHECKOUT_BUTTON_LOCATOR: str = "//button[.//text()[contains(., 'CheckOut')]]"
CLEAR_CART_BUTTON_LOCATOR: str = "//button[.//text()[contains(., 'Clear cart')]]"
CART_TABLE_LOCATOR: str = "//table"
SHOPPING_CART_LOCATOR: str = "//app-shoppingcart"
BOOKS_QUANTITY_LOCATOR: str = "//div[contains(@class, 'MuiContainer-root MuiContainer-maxWidthLg')][.//div[@id='desktop_cartItemsGrid']]//input[@aria-label='Change product quantity.']"



# add class cart page locators


class CartPageLocator:
    ADDED_BOOK_NAME__TEXT_ELEMENT: str = "//div[@id='desktop_cartItemsGrid']/..//div[contains(@style, 'width')]//h6"
