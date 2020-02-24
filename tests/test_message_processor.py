from unittest import TestCase
from message_processor import MessageProcessor
import pandas as pd

class TestMessageProcessor(TestCase):

    def setUp(self):
        self.test_input = create_test_input()
        self.message_processor = MessageProcessor(self.test_input)

    def test_get_sales(self):
        expected_sales_products = list(self.test_input['product'])
        expected_sales_values = list(self.test_input['value'])
        self.message_processor.process_sales()
        actual_sales = self.message_processor.sales
        actual_sales_products = [item.product_type for item in actual_sales]
        actual_sales_values = [item.value for item in actual_sales]
        self.assertEqual(expected_sales_products, actual_sales_products)
        self.assertEqual(expected_sales_values, actual_sales_values)



def create_test_input():
    """ Make some test input """
    sales_dict = {'product': ['orange', 'banana', 'squid'], 'value': [0.30, 0.50, 5.67]}
    return pd.DataFrame.from_dict(sales_dict)
