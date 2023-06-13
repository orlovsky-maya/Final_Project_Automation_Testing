from selenium.webdriver.common.by import By


class MainPageLocators:
    CATALOG_MENU = (By.CSS_SELECTOR, '.btn.btn-catalog')
    NUTS = (By.CSS_SELECTOR, '.left_block > .cp_link.has_child:nth-child(2)')
    FILTER = (By.CSS_SELECTOR, '.sort_block')
    PRICE_DESCENDING = (By.CSS_SELECTOR, '.sort_items > .sb_item:nth-child(4)')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.products_listing > .product_item:nth-child(1) > .product_data > span')
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, '.total_price.js_total_price')


class BasketPageLocators:
    BASKET_PRODUCT = (By.CSS_SELECTOR, '.cart_rows')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '.btn.btn-cart.check_price')


class BasePageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '.header-link.basket_block.ic_cart')


class LoginFormLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.header-link.ic_login.login_js')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[name="login"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[name="password"]')
    ENTER_BUTTON = (By.CSS_SELECTOR, '.btn.btn-login')
