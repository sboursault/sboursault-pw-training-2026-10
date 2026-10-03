import re

from playwright.sync_api import Page, expect

from support.page_object.home_page import HomePage
from support.page_object.login_page import LoginPage
from support.page_object.product_page import ProductPage


def test_login_ok(page: Page, home_page: HomePage, login_page: LoginPage):

    home_page.goto()

    home_page.goto_login()

    login_page.login("tom@test.test", "tom@test.test")

    home_page.expect_logged_in("tom@test.test")
