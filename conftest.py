import pytest
from playwright.sync_api import expect

from support.page_object.home_page import HomePage
from support.page_object.login_page import LoginPage
from support.page_object.product_page import ProductPage

expect.set_options(timeout=10_000)  # expect timeout


@pytest.fixture  # (autouse=True) may not be necessary
def _short_timeouts(page):
    page.set_default_timeout(5_000)             # action timeout
    page.set_default_navigation_timeout(5_000)  # navigation timeout


# default scope is function (the fixture is destroyed at the end of the test)
@pytest.fixture
def product_page(page):
    return ProductPage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def home_page(page):
    return HomePage(page)
