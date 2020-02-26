
import mock
import pandas as pd
from unittest import TestCase

from message_processor import MessageProcessor

class TestMessageProcessor(TestCase):

    def setUp(self):
        self.test_input = create_test_input()
        self.message_processor = MessageProcessor(self.test_input)

    @mock.patch('message_processor.SalesRecorder.record_sale')
    def test_process_sales(self, mock_record_sale):
        self.message_processor.process_sales()
        actual_amount_calls = [item[0][0].amount for item in mock_record_sale.call_args_list]
        actual_value_calls = [item[0][0].value for item in mock_record_sale.call_args_list]
        actual_product_calls = [item[0][0].product for item in mock_record_sale.call_args_list]
        self.assertEqual(mock_record_sale.call_count, len(self.test_input))
        self.assertEqual(['orange', 'banana', 'squid','banana'], actual_product_calls)
        self.assertEqual([0.30, 0.50, 5.67, 0.50], actual_value_calls)
        self.assertEqual([1, 1, 1, 8], actual_amount_calls)

def create_test_input():
    """ Make some test input """
    sales_dict = {
        'product': ['orange', 'banana', 'squid', 'banana'],
        'value': [0.30, 0.50, 5.67, 0.50],
        'amount': [1, 1, 1, 8],
    }
    return pd.DataFrame.from_dict(sales_dict)
