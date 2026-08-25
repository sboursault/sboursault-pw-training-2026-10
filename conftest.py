import pytest
from support.page_object.product_page import ProductPage


@pytest.fixture
def product_page(page):
    return ProductPage(page)
    