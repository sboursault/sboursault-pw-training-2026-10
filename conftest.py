import pytest
from playwright.sync_api import APIRequestContext, Page, Playwright, expect

from support.api.basket_api import BasketApi
from support.page_object.home_page import HomePage
from support.page_object.login_page import LoginPage
from support.page_object.product_page import ProductPage
from support.workflow import Workflow

# Playwrigth settings and base fixtures


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict):
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


# Api fixtures

@pytest.fixture
def basket_api(api_request: APIRequestContext):
    return BasketApi(api_request)


# Workflow fixtures

@pytest.fixture
def workflow(home_page: HomePage, login_page: LoginPage):
    return Workflow(home_page, login_page)


# Page object fixtures

@pytest.fixture
def product_page(page: Page):
    return ProductPage(page)


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture
def home_page(page: Page):
    return HomePage(page)
