# make uppercase names
# split locators in separate files for each page (page object pattern)
# read about page object pattern

ADD_BTN_LOCATOR: str = '//mat-card[.//text()[contains(.,"{0}")]]//button[span[contains(text(), "Add to Cart")]]'
CART_BTN_LOCATOR: str= '//button[.//mat-icon[text()="shopping_cart"]]'
ADDED_BOOK_LOCATOR: str = '//td[contains(@class, "mat-column-title")]//a'