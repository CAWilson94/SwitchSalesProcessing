import mock
from unittest import TestCase

from message_processor import MessageProcessor


class TestMessageProcessor(TestCase):

    def setUp(self):
        self.message_processor = MessageProcessor(create_test_input_list())

    def test_process_message(self):
        message = create_test_input_list()[0]
        self.message_processor._parse_message_two = mock.MagicMock()
        self.message_processor._apply_adjustments = mock.MagicMock()
        self.message_processor._parse_message_one = mock.MagicMock()
        self.message_processor.process_message(message)
        self.message_processor._parse_message_two.assert_called_with(message.lower().split())
        message = create_test_input_list()[3]
        self.message_processor.process_message(message)
        self.message_processor._apply_adjustments.assert_called_with(message.lower().split())
        message = create_test_input_list()[1]
        self.message_processor.process_message(message)
        self.message_processor._parse_message_one.assert_called_with(message.lower().split())

    @mock.patch('message_processor.logging')
    def test_invalid_message_process_type_one(self, mock_logging):
        with self.assertRaises(Exception) as context:
            message = "Metroid Prime 4 at eightQuid"
            self.message_processor.process_message(message)
            expected_error = "Float required for product value: {}".format(message)
            self.assertTrue(mock_logging.warning.called)
            self.assertTrue(expected_error in context.exception)

    @mock.patch('message_processor.logging')
    def test_invalid_message_process(self, mock_logging):
        with self.assertRaises(Exception) as context:
            message = None
            self.message_processor.process_message(message)
            expected_error = "AttributeError: 'NoneType' object has no attribute 'lower'"
            self.assertTrue(expected_error in context.exception)
            self.assertTrue(mock_logging.warning.called)
            mock_logging.assert_called_with("Could not parse message Some invalid input. \n %s", expected_error)

    def test__apply_adjustments(self):
        pass

    def test__parse_message_one(self):
        pass

    def test__parse_message_two(self):
        pass

def create_test_input_list():
    """ Generic test input. """
    return [
        "9 of Mario Kart at 49.99 each", "Super Mario Maker 2 at 32.29",
        "8 of Animal Crossing at 49.99 each", "Add 2 Animal Crossing",
        "Untitled Goose Game  at 17.99", "Multiply 2 Untitled Goose Game",
        "Add 5 Animal Crossing", "9 of Mario Kart at 49.99 each", "Super Mario Maker 2 at 32.29",
        "8 of Animal Crossing at 49.99 each", "Add 2 Animal Crossing",
        "Untitled Goose Game  at 17.99", "Multiply 2 Untitled Goose Game",
        "Add 5 Animal Crossing"
    ]
