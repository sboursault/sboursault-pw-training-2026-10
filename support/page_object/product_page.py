from playwright.sync_api import Page, expect


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/catalogue/cryptonomicon_3/")

    def expect_empty_basket(self):
        expect(
            self.page.locator('#top_page').get_by_role('button', name='Panier')
        ).not_to_contain_text('(')

    def expect_basket_count(self, count: int):
        expect(
            self.page.locator('#top_page').get_by_role('button', name='Panier')
        ).to_contain_text(f'({count})')

    def add_to_basket(self):
        self.page.get_by_role('button', name='Ajouter au panier').click()
