import re
from playwright.sync_api import Page, expect

from support.page_object.product_page import ProductPage


def test_add_to_basket(page: Page, product_page: ProductPage):

    page.goto("/fr/catalogue/cryptonomicon_3/")

    page.pause()

    expect(page.locator('#top_page').get_by_role('button', name='Panier')).not_to_contain_text('1')

    product_page.add_to_basket()

    expect(page.locator('#top_page').get_by_role('button', name='Panier')).to_contain_text('1')

    page.pause()
