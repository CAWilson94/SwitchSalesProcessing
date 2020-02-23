from unittest import TestCase
import pandas as pd
from data_generator import DataGenerator as dg

def generate_test_input():
    data = [
        ['Animal Crossing', 49.99],
        ['Mario Kart', 49.99],
        ['Super Mario Maker 2', 32.29],
        ['Untitled Goose Game ', 17.99],
        ['Cat Quest ', 9.99],
        ['Spyro Reignited Trilogy', 34.99],
        ['The Witcher III: Th...Wild Hunt', 34.99],
        ['Pokemon Sword ', 60.0],
        ['Pokemon Shield ', 60.0],
        ['Hollow Knight', 10.99]
    ]
    columns = ['product', 'value']
    return pd.DataFrame(data=data, columns=columns)

class TestDataGenerator(TestCase):

    def test__add_random_operation(self):
        products = generate_test_input()
        data_generator =dg()
        test_df = data_generator.generate_input_data(products)
        expected_df_len = 10
        self.assertEqual(expected_df_len, len(test_df))


