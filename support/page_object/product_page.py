class ProductPage:
    def __init__(self, page):
        self.page = page
        self.add_to_basket_button = page.get_by_role('button', name='Ajouter au panier')


    def add_to_basket(self):
        self.add_to_basket_button.click()