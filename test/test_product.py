import unittest

from product import Product

class ProductTestCase(unittest.TestCase):
  def test_transform_name_for_sku(self):
    small_black_shoes = Product('shoes', 'S', 'black')
    expected_value = 'SHOES'
    actual_value = small_black_shoes.transform_name_for_sku()
    self.assertEqual(expected_value, actual_value)


# 통합 테스트
import unittest

from cart import ShoppingCart
from product import Product

class ShoppingCartTestCase(unittest.TestCase):
  def test_add_and_remove_product(self):
    cart = ShoppingCart()
    product = Product('shoes', 'S', 'blue')

    cart.add_product(product)
    cart.remove_product(product)

    self.assertDictEqual({}, cart.products)