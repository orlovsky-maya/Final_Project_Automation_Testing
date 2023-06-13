import datetime
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.locators import *


class BasePage:

    def __init__(self, browser, url, timeout=30):
        self.browser = browser
        self.timeout = timeout
        self.url = url

    def assert_url(self, result):
        get_url = self.browser.current_url
        assert result == get_url, "incorrect url"

    def get_current_url(self):
        current_url = self.browser.current_url
        print(current_url)

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y_%m_%d.%H.%M.%S")
        name_screenshot = f'finish_scr_{now_date}.png'
        self.browser.save_screenshot(f'/home/maya/PycharmProjects/Final_task_for_building_test_project/Screens/'
                                     f'{name_screenshot}')

    def go_to_basket(self):
        basket_button = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located
                                                                        (BasePageLocators.BASKET_BUTTON))

        basket_button.click()

    def is_element_present(self, selector):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located(selector))
        except TimeoutException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)
