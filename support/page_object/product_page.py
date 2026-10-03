from playwright.sync_api import Page, expect


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_basket_button = page.get_by_role(
            'button', name='Ajouter au panier')

    def expect_empty_basket(self):
        expect(
            self.page.locator('#top_page').get_by_role(
                'button', name='Panier')
        ).not_to_contain_text('1')

    def add_to_basket(self):
        self.add_to_basket_button.click()
