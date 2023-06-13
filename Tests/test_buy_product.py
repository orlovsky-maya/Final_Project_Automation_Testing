import pytest
from Pages.main_page import MainPage
from Pages.basket_page import BasketPage
from Pages.checkout_page import CheckoutPage
from conftest import link


@pytest.mark.guest
def test_guest_can_add_product_1_from_main_page(browser):
    mp = MainPage(browser, link)
    mp.select_product_1()
    mp.should_be_total_price_in_basket()

    baskp = BasketPage(browser, link)
    baskp.go_to_basket()
    baskp.should_be_product_in_basket()
    baskp.click_checkout_button()

    cp = CheckoutPage(browser, link)
    cp.check_checkout_link()
    print('FINISH')


@pytest.mark.user
def test_user_can_add_product_1_from_main_page(browser, setup):
    mp = MainPage(browser, link)
    mp.select_product_1()
    mp.should_be_total_price_in_basket()

    baskp = BasketPage(browser, link)
    baskp.go_to_basket()
    baskp.should_be_product_in_basket()
    baskp.click_checkout_button()

    cp = CheckoutPage(browser, link)
    cp.check_checkout_link()
    print('FINISH')

