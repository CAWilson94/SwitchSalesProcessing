from unittest import TestCase
from sale import Sale


class TestSale(TestCase):

    def test_add_adjustment(self):
        sale = Sale("product", value=10, amount=3)
        sale.add_adjustment("subtract", 40)
        expected_list = [sale.Adjustment(operation="subtract", adjusted_amount=40)]
        actual_list = sale.adjustments
        self.assertListEqual(expected_list, actual_list)

    def test_apply_adjustments_sub(self):
        sale = Sale("product", value=10, amount=3)
        sale.add_adjustment("subtract", 40)
        expected_value = -30
        expected_total_value = -90
        sale.apply_adjustments()
        self.assertEqual(expected_value, sale.value)
        self.assertEqual(expected_total_value, sale.total_value)

    def test_apply_adjustments_add(self):
        sale = Sale("product", value=100, amount=2)
        sale.add_adjustment("add", 40)
        expected_value = 140
        expected_total_value = 280
        sale.apply_adjustments()
        self.assertEqual(expected_value, sale.value)
        self.assertEqual(expected_total_value, sale.total_value)

    def test_apply_adjustments_mul(self):
        sale = Sale("product", value=2, amount=2)
        sale.add_adjustment("multiply", 3)
        expected_value = 6
        expected_total_value = 12
        sale.apply_adjustments()
        self.assertEqual(expected_value, sale.value)
        self.assertEqual(expected_total_value, sale.total_value)

    def test__add_applied_adjustment_to_dict(self):
        sale = Sale("product", value=10, amount=3)
        sale._add_applied_adjustment_to_dict("Add", 2)
        expected_dict = {
            'product': ['product'],
            'value': [10],
            'operation': ['Add'],
            'adjusted_amount': [2],
            'new_price': [10],
            'number_items': [3],
            'total_adjusted_value': [30]
        }
        actual_dict = sale.applied_adjustments_dict  #
        self.assertDictEqual(expected_dict, actual_dict)

    def test__create_applied_adjustments_dict(self):
        sale = Sale("product", value=10, amount=3)
        expected_dict = {
            'product': [], 'value': [],
            'operation': [], 'adjusted_amount': [],
            'new_price': [], 'number_items': [],
            'total_adjusted_value': []
        }

        actual_dict = sale.applied_adjustments_dict
        self.assertEqual(expected_dict, actual_dict)

    def test_to_dict(self):
        sale = Sale("product", value=10, amount=3)
        actual_dict = sale.to_dict()
        expected_dict = {
            'product': 'product',
            'amount': 3, 'adjusted_value': 10,
            'original_value': 10,
            'original_sale_total_value': 30,
            'adjusted_total_value': 30}
        self.assertDictEqual(expected_dict, actual_dict)
