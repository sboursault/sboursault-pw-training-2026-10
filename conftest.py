import pytest
from playwright.sync_api import APIRequestContext, Page, Playwright, expect

from support.api.basket_api import BasketApi
from support.page_object.home_page import HomePage
from support.page_object.login_page import LoginPage
from support.page_object.product_page import ProductPage

expect.set_options(timeout=10_000)  # expect timeout


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "locale": "fr-FR"}


@pytest.fixture(autouse=True)
def _page_settings(page: Page):
    page.set_default_timeout(5_000)              # action timeout
    page.set_default_navigation_timeout(10_000)  # navigation timeout


@pytest.fixture
def api_request(playwright: Playwright, base_url: str):
    ctx = playwright.request.new_context(base_url=base_url)
    yield ctx
    ctx.dispose()

# default scope is function (the fixture is destroyed at the end of the test)


@pytest.fixture
def basket_api(api_request: APIRequestContext) -> BasketApi:
    return BasketApi(api_request)


@pytest.fixture
def product_page(page):
    return ProductPage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def home_page(page):
    return HomePage(page)
