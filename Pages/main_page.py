from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *


class MainPage(BasePage):

    # Getting

    def get_catalog_menu(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (MainPageLocators.CATALOG_MENU))

    def get_nuts(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (MainPageLocators.NUTS))

    def get_filter(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (MainPageLocators.FILTER))

    def get_price_descending(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (MainPageLocators.PRICE_DESCENDING))

    def get_add_to_basket_button(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (MainPageLocators.ADD_TO_BASKET))

    # Actions

    def click_catalog_menu(self):
        self.get_catalog_menu().click()

    def click_nuts(self):
        self.get_nuts().click()

    def click_filter(self):
        self.get_filter().click()

    def click_price_descending(self):
        self.get_price_descending().click()

    def add_product_1_to_basket(self):
        self.get_add_to_basket_button().click()

    # Methods

    def should_be_total_price_in_basket(self):
        assert self.is_element_present(MainPageLocators.TOTAL_BASKET_PRICE), 'Total price is not presented in basket'

    def select_product_1(self):
        self.open()
        self.click_catalog_menu()
        self.click_nuts()
        self.click_filter()
        self.click_price_descending()
        self.add_product_1_to_basket()
        print('Product1 is added to basket')
