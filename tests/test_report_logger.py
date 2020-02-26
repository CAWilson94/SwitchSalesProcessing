from unittest import TestCase
from sale import Sale
import mock
import pandas as pd
from report_logger import ReportLogger

class TestReportLogger(TestCase):

    def setUp(self):
        sales_list = mock.MagicMock()
        self.report_logger = ReportLogger(sales_list)

    @mock.patch('report_logger.ReportLogger._get_sales_dict')
    def test_basic_report(self, mock_sales_dict):
        mock_sales_dict.return_value = self.test_df_input()
        print(mock_sales_dict.return_value)
        actual_output = self.report_logger.basic_report()
        print(actual_output)
        actual_counts = list(actual_output['count'])
        actual_products = list(actual_output['product'])
        actual_full_values = list(actual_output['full_value'])
        self.assertEqual(actual_counts, [2,1])
        self.assertEqual(actual_full_values, [140, 10])
        self.assertEqual(actual_products, ['apple', 'orange'])

    def test_df_input(self):
        dict = {'product': ['orange', 'apple', 'apple'],
                'value': [10,20,20],
                'amount':[1,2,5]
                }
        return pd.DataFrame.from_dict(dict)


    def test_end_report(self):
        actual_report = self.report_logger.end_report()
        self.assertEqual(actual_report, 0)
