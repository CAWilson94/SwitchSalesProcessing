from report import Report
from sale import Sale

import mock
import pandas as pd
from unittest import TestCase


class TestReport(TestCase):

    def setUp(self):
        mock_sale = mock.MagicMock()
        mock_sales_list = [mock_sale] * 10
        self.sales_list = mock_sales_list

    @mock.patch('builtins.print')
    def test_log_basic_report(self, mock_print):
        report = Report(self.sales_list)
        report.df = create_basic_report_data()
        report._basic_report_df = mock.MagicMock()
        report.log_basic_report()
        self.assertTrue(report._basic_report_df.called)
        self.assertTrue(mock_print.called)

    def test__basic_report_df(self):
        report = Report(self.sales_list)
        report.df = create_basic_report_data()
        actual_report = report._basic_report_df()
        self.assertTrue(actual_report.equals(expected_basic_report_df()))

    def test__end_report_df(self):
        report = Report(self.sales_list)
        report.df = create_basic_report_data()
        report.sales_list = create_test_sales_list()
        actual_report = report._end_report_df()
        self.assertEquals(len(actual_report),10)

    def test__total_value_df(self):
        report = Report(self.sales_list)
        report.df = create_basic_report_data()
        actual_report = report._total_value_df()
        self.assertTrue(actual_report.equals(expected_total_value_df()))

    def test__number_sales_df(self):
        report = Report(self.sales_list)
        report.df = create_basic_report_data()
        actual_report = report._number_sales_df()
        self.assertTrue(actual_report.equals(expected_number_sales_df()))

def create_basic_report_data():
    cols = ['product', 'original_value', 'original_sale_total_value', 'amount',
            'adjusted_value', 'adjusted_total_value']
    data = [
        ['Super Mario Maker 2', 32.29, 32.29, 1, 32.29, 32.29],
        ['Animal Crossing', 49.99, 249.95000000000002, 5, 49.99, 249.95000000000002],
        ['Untitled Goose Game', 17.99, 107.94, 6, 17.99, 107.94],
        ['Super Mario Maker 2', 32.29, 32.29, 1, 32.29, 32.29],
        ['Animal Crossing', 49.99, 249.95000000000002, 5, 49.99, 249.95000000000002]
    ]

    return pd.DataFrame(data=data, columns=cols)


def expected_total_value_df():
    cols = ['product', 'total_value_sales']
    data = [
        ['Animal Crossing', 499.90000000000003],
        ['Super Mario Maker 2', 64.58],
        ['Untitled Goose Game', 107.94]
    ]
    return pd.DataFrame(data=data, columns=cols)


def expected_number_sales_df():
    cols = ['product', 'number_sales']
    data = [
        ['Animal Crossing', 10],
        ['Super Mario Maker 2', 2],
        ['Untitled Goose Game', 6]
    ]
    return pd.DataFrame(data=data, columns=cols)

def expected_basic_report_df():
    cols = ['product', 'number_sales', 'total_value_sales']
    data = [
        ['Animal Crossing', 10, 499.90000000000003],
        ['Super Mario Maker 2', 2, 64.58],
        ['Untitled Goose Game', 6, 107.94]
    ]
    return pd.DataFrame(data=data, columns=cols)


def create_test_sales_list():
    sale = Sale("Product", value=10, amount=2)
    sale.applied_adjustments_dict ={
        'product':["Product"],
        'value':[10],
        'operation':["Add"],
        'adjusted_amount':[2],
        'new_price':[12],
        'number_items':[2],
        'total_adjusted_value':[24]
    }
    return [sale] * 10