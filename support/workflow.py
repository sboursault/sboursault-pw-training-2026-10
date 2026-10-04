from playwright.sync_api import Page

from support.page_object.home_page import HomePage
from support.page_object.login_page import LoginPage


class Workflow:
    def __init__(self, home_page: HomePage, login_page: LoginPage, page: Page):
        self.page = page
        self.home_page = home_page
        self.login_page = login_page

    def login(self, login: str, password: str):
        # self.login_page.goto()
        # self.login_page.login(login, password)
        # self.home_page.expect_logged_in(login)

        self.page.request.post(
            '/api/login/',
            data={
                "username": login,
                "password": password
            },
            fail_on_status_code=True
        )
