import re

from playwright.sync_api import Page, expect

from support.page_object.product_page import ProductPage


def test_login_ok(page: Page):

    page.goto("/fr/catalogue/")

    page.get_by_role("link", name=" Compte").click()

    page.get_by_role(
        "textbox", name="Adresse électronique *"
    ).fill("tom@test.test")
    page.get_by_role("textbox", name="Mot de passe *").fill("tom@test.test")
    page.get_by_role("button", name="Connexion").click()

    expect(page.get_by_role("button", name=" tom@test.test")).to_be_visible()
    expect(page.get_by_role("heading", name="Tous les produits")).to_be_visible()
    expect(page.get_by_text("Bienvenue")).to_be_visible()
