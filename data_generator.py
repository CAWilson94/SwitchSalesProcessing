from operator import add, sub, mul
import numpy as np
import pandas as pd
import random

operations = {'Add': add, 'Subtract': sub, 'Multiply': mul}


class DataGenerator:
    """
        Data generation for messages to be processed
        Type 1 - value and product only.

    """

    def generate_input_data(self, products_df):
        """ Add standard columns for messages """
        products_df['amount'] = 1
        products_df['operation'] = None
        products_df['random_val_op'] = None
        products_df['adjusted_value'] = None
        products_df['total_value'] = products_df['value']
        return products_df

class DataGeneratorType2(DataGenerator):
    """
        Data generation for messages of type 2
        Should generate product, value and amount
        of each product sold.
    """

    def generate_input_data(self, products_df):
        """ Standard columns for messages & random product amount sold generated """
        products_df = super(DataGeneratorType2, self).generate_input_data(products_df)
        products_df['amount'] = np.random.randint(1, 10, size=len(products_df))
        return products_df

class DataGeneratorType3(DataGenerator):


    def _add_random_operation(self, row):
        """ Random operation generated for product adjustment """
        return random.choice(list(operations.keys()))

    def _calculate_adjusted_value(self, row): #TODO: - may need to add to propagate previous sales?
        """ Calculate the total value of products sold  """
        return round(operations[row['operation']](row['value'], (row['random_val_op'])), 2)

    def _calculate_total_value(self, row):
        return mul(row['adjusted_value'], row['amount'])

    def generate_input_data(self, products_df):
        """ Generate input data for type 3: product, value, amount and adjustments """
        products_df = super(DataGeneratorType3, self).generate_input_data(products_df)
        products_df['operation'] = products_df.apply(self._add_random_operation, axis=1)
        products_df['random_val_op'] = np.random.randint(1,6, size=len(products_df))
        products_df['adjusted_value'] = products_df.apply(self._calculate_adjusted_value, axis=1)
        products_df['total_value'] = products_df.apply(self._calculate_total_value, axis=1)
        #products_df['message_type'] = np.random.randint(1,4, size=len(products_df)) # will need to do this for overall generation
        return products_df
