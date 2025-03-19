# button[span[contains(text(), 'Add to Cart')]]" use this
# use ancestor to find a btn
ADD_BUTTON_LOCATOR: str = "//mat-card[.//text()[contains(.,'{0}')]]//button[span[contains(text(), 'Add to Cart')]]"
CART_BUTTON_LOCATOR: str= "//button[.//mat-icon[text()='shopping_cart']]"
BOOK_ADDED_POPUP_LOCATOR: str = "//simple-snack-bar[.//text()[contains(., ' One Item added to cart')]]"
