from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/catalogue/")

    def goto_login(self):
        self.page.get_by_role("link", name=" Compte").click()

    def expect_logged_in(self, email: str):
        expect(self.page.get_by_role("button", name=email)).to_be_visible()
        expect(
            self.page.get_by_role("heading", name="Tous les produits")
        ).to_be_visible()
        expect(self.page.get_by_text("Bienvenue")).to_be_visible()
