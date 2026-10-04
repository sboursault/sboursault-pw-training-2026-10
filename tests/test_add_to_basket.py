from support.page_object.product_page import ProductPage


def test_add_to_basket(product_page: ProductPage):

    product_page.goto()

    product_page.expect_empty_basket()

    product_page.add_to_basket()

    product_page.expect_basket_count(1)
