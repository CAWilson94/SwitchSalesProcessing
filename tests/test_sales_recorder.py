import mock
from unittest import TestCase

from sales_recorder import SalesRecorder

class TestSalesRecorder(TestCase):

    def setUp(self):
        self.sales_recorder = SalesRecorder()

    @mock.patch('sales_recorder.ReportLogger')
    def test_record_sale(self, mock_report_logger):
        sale = mock.MagicMock()
        test_list = [sale] * 49
        self.sales_recorder.sales = mock.MagicMock()
        self.sales_recorder.sales = test_list
        self.sales_recorder.record_sale(sale)
        mock_report_logger.return_value.basic_report.assert_any_call()
        mock_report_logger.return_value.end_report.assert_any_call()

    @mock.patch('sales_recorder.ReportLogger')
    def test_record_sale_NoReports(self, mock_report_logger):
        sale = mock.MagicMock()
        mock_report_logger.return_value.basic_report = mock.MagicMock()
        mock_report_logger.return_value.end_report = mock.MagicMock()
        test_list = [sale] * 3
        self.sales_recorder.sales = mock.MagicMock()
        self.sales_recorder.sales = test_list
        self.sales_recorder.record_sale(sale)
        self.assertFalse(mock_report_logger.return_value.basic_report.called)
        self.assertFalse(mock_report_logger.return_value.end_report.called)





