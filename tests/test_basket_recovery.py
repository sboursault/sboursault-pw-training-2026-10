import re
from base64 import b64encode

from playwright.sync_api import APIRequestContext, Page, expect

from support.api.basket_api import BasketApi
from support.page_object.home_page import HomePage
from support.page_object.login_page import LoginPage
from support.page_object.product_page import ProductPage


def test_recover_basket(
        home_page: HomePage,
        product_page: ProductPage,
        login_page: LoginPage,
        page: Page,
        basket_api: BasketApi):

    basket_api.clear_basket("tom@test.test", "tom@test.test")

    login_page.goto()
    login_page.login("tom@test.test", "tom@test.test")
    home_page.expect_logged_in("tom@test.test")

    product_page.goto()
    product_page.expect_empty_basket()
    product_page.add_to_basket()
    product_page.expect_basket_count(1)

    page.goto('/fr/accounts/logout/')
    product_page.expect_empty_basket()

    home_page.goto()
    home_page.goto_login()
    login_page.login("tom@test.test", "tom@test.test")
    home_page.expect_logged_in("tom@test.test")
    product_page.expect_basket_count(1)
