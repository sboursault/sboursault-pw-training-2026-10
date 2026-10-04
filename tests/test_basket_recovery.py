from playwright.sync_api import Page

from support.api.basket_api import BasketApi
from support.page_object.product_page import ProductPage
from support.workflow import Workflow


def test_recover_basket(
        product_page: ProductPage,
        workflow: Workflow,
        page: Page,
        basket_api: BasketApi):

    basket_api.clear_basket("tom@test.test", "tom@test.test")

    workflow.login("tom@test.test", "tom@test.test")

    product_page.goto()
    product_page.expect_empty_basket()
    product_page.add_to_basket()
    product_page.expect_basket_count(1)

    page.goto('/fr/accounts/logout/')
    product_page.expect_empty_basket()

    workflow.login("tom@test.test", "tom@test.test")

    product_page.goto()
    product_page.expect_basket_count(1)
