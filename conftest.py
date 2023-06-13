import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.login_page import LoginPage

link = 'https://орешкофф.рф/'


def pytest_addoption(parser):
    parser.addoption("--email", action="store", default=None, help="email of user")
    parser.addoption("--password", action="store", default=None, help="password of user")


def pytest_collection_modifyitems(config, items):
    if config.getoption("email") and config.getoption("password"):
        return
    skip_user = pytest.mark.skip(reason="need --email and --password options to run")
    for item in items:
        if "user" in item.keywords:
            item.add_marker(skip_user)


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9515")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def setup(browser, request):
    email = request.config.getoption("email")
    password = request.config.getoption("password")
    lp = LoginPage(browser, link)
    lp.authorization(email, password)
