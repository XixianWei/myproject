import unittest
from shop import Shop

class TestShop(unittest.TestCase):
    def setUp(self):
        self.shop = Shop()

    def test_items(self):
        self.assertEqual(self.shop.get_items(), {'Apple': 10, 'Shoes': 120, 'Book': 30})

    def test_add_money(self):
        self.shop.add_money(100)
        self.assertEqual(self.shop.customer_money, 200)

    def test_purchase_item(self):
        message = self.shop.purchase_item('Apple')
        self.assertEqual(message, "Here's your Apple!")

    def test_purchase_item_not_exists(self):
        with self.assertRaises(ValueError):
            self.shop.purchase_item('NotExist')

    def test_purchase_item_not_enough_money(self):
        with self.assertRaises(ValueError):
            self.shop.purchase_item('Shoes')

if __name__ == '__main__':
    unittest.main()
