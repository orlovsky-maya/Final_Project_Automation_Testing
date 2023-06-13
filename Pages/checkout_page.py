from Base.base_page import BasePage

result_link = 'https://xn--e1akkch1aa2a.xn--p1ai/checkout/'


class CheckoutPage(BasePage):

    # Getting

    # Actions

    # Methods
    def check_checkout_link(self):
        self.assert_url(result_link)
        self.get_screenshot()
