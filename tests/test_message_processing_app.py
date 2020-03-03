import mock
from unittest import TestCase

from sale import  Sale
from message_processing_app import MessageProcessingApp


class TestMessageProcessingApp(TestCase):

    def setUp(self):
        self.input_test_path = "test_input_messages.txt"
        self.mpa = MessageProcessingApp(self.input_test_path)
        basic_report__mock_input = create_test_input()
        self.data = "/n".join(basic_report__mock_input)

    @mock.patch('message_processing_app.Report')
    @mock.patch('message_processing_app.logging')
    @mock.patch('message_processing_app.MessageProcessor')
    def test_basic_report_process_sales_messages(self, mock_message_processor, mock_logging, mock_report):
        """ Testing specifically basic report. """
        test_sale = mock.MagicMock()
        self.mpa.sales_list = [test_sale] * 10
        self.mpa.number_messages = mock.MagicMock()
        mock_message_processor.return_value.sales_list = [test_sale] * 10
        with mock.patch("builtins.open", mock.mock_open(read_data=self.data)) as mock_file:
            self.mpa.number_messages = 10
            self.mpa.process_sales_messages()
            mock_message_processor.return_value.process_message.assert_called_with(self.data)
            mock_report.return_value.log_basic_report.assert_any_call()
            self.mpa.sales_list[0].apply_adjustments.assert_any_call()


    @mock.patch('message_processing_app.Report')
    @mock.patch('message_processing_app.logging')
    @mock.patch('message_processing_app.MessageProcessor')
    def test_end_report_process_sales_messages(self, mock_message_processor, mock_logging, mock_report):
        """ Testing specifically end report. """
        test_sale = mock.MagicMock()
        self.mpa.sales_list = [test_sale] * 10
        self.mpa.number_messages = mock.MagicMock()
        with mock.patch("builtins.open", mock.mock_open(read_data=self.data)) as mock_file:
            self.mpa.number_messages = 50
            self.mpa.process_sales_messages()
            mock_report.return_value.log_end_report.assert_any_call()

    @mock.patch('message_processing_app.Report')
    @mock.patch('message_processing_app.logging')
    @mock.patch('message_processing_app.MessageProcessor')
    def test_process_sales_messages_no_input(self, mock_message_processor, mock_logging, mock_report):
        with self.assertRaises(Exception) as context:
            self.mpa.process_sales_messages()
            expected_error = "[Errno 2] No such file or directory: 'test_input_messages.txt'"
            self.assertTrue(expected_error in context.exception)
            self.assertTrue(mock_logging.warning.called)
            self.assertTrue(mock_logging.assert_called_with(
                "Input Error: [Errno 2] No such file or directory: 'test_input_messages.txt'"))


def create_test_input():
    """ Generic test input. """
    test_input = [
        "9 of Mario Kart at 49.99 each", "Super Mario Maker 2 at 32.29",
        "8 of Animal Crossing at 49.99 each", "Add 2 Animal Crossing",
        "Untitled Goose Game  at 17.99", "Multiply 2 Untitled Goose Game",
        "Add 5 Animal Crossing", "9 of Mario Kart at 49.99 each", "Super Mario Maker 2 at 32.29",
        "8 of Animal Crossing at 49.99 each", "Add 2 Animal Crossing",
        "Untitled Goose Game  at 17.99", "Multiply 2 Untitled Goose Game",
        "Add 5 Animal Crossing"
    ]
    return test_input
