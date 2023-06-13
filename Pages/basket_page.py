from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *


class BasketPage(BasePage):

    # Getting
    def get_checkout_button(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (BasketPageLocators.CHECKOUT_BUTTON))

    # Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()

    # Methods
    def should_be_product_in_basket(self):
        assert self.is_element_present(BasketPageLocators.BASKET_PRODUCT), "The product is not in basket, but " \
                                                                           "should be"
