import pytest
from playwright.sync_api import APIRequestContext, Page, Playwright, expect

from support.api.basket_api import BasketApi
from support.page_object.home_page import HomePage
from support.page_object.login_page import LoginPage
from support.page_object.product_page import ProductPage

# Playwrigth settings and base fixtures


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Override browser locale
    """
    return {**browser_context_args, "locale": "fr-FR"}


@pytest.fixture
def page(page: Page):
    """
    Override default timeout for navigation, actions and verifications
    """
    page.set_default_navigation_timeout(10_000)
    page.set_default_timeout(5_000)
    expect.set_options(timeout=5_000)
    return page


@pytest.fixture
def api_request(playwright: Playwright, base_url: str):
    """
    Define the api_request fixture:
    an isolated APIRequestContext instance to make http request
    """
    ctx = playwright.request.new_context(base_url=base_url)
    yield ctx
    ctx.dispose()


# Workflow fixtures


# Api fixtures

@pytest.fixture
def basket_api(api_request: APIRequestContext) -> BasketApi:
    return BasketApi(api_request)


# Page object fixtures


@pytest.fixture
def product_page(page):
    return ProductPage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def home_page(page):
    return HomePage(page)
