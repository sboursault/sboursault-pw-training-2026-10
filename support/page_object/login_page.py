from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/fr/accounts/login/")

    def login(self, email: str, password: str):
        self.page.get_by_role(
            "textbox", name="Adresse électronique *").fill(email)
        self.page.get_by_role("textbox", name="Mot de passe *").fill(password)
        self.page.get_by_role("button", name="Connexion").click()
