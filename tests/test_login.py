import pytest

from support.page_object.home_page import HomePage
from support.page_object.login_page import LoginPage


@pytest.mark.smoke
def test_login_ok(home_page: HomePage, login_page: LoginPage):

    home_page.goto()

    home_page.goto_login()

    login_page.login("tom@test.test", "tom@test.test")

    home_page.expect_logged_in("tom@test.test")
