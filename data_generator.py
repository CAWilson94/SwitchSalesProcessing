from operator import add, sub, mul
import numpy as np
import pandas as pd
import random

operations = {'Add': add, 'Subtract': sub, 'Multiply': mul}


class DataGenerator:


    def _add_random_operation(self, row):
        return random.choice(list(operations.keys()))


    def _apply_operations(self, row):
        return round(operations[row['operation']](row['value'], (row['random_val_op'])), 2)


    def _apply_total_value(self, row):
        return mul(row['adjusted_value'], row['amount'])


    def generate_input_data(self, products):
        products['amount'] = np.random.randint(1, 10, size=len(products))
        products['operation'] = products.apply(self._add_random_operation, axis=1)
        products['random_val_op'] = np.random.randint(1,6, size=len(products))
        products['adjusted_value'] = products.apply(self._apply_operations, axis=1)
        products['total_value'] = products.apply(self._apply_total_value, axis=1)
        products['message_type'] = np.random.randint(1,4, size=len(products))
        return products


def main():
    product_input = pd.read_csv('products.csv')
    dataGenerator = DataGenerator()
    df = dataGenerator.generate_input_data(product_input)
    print(df)

if __name__ == '__main__':
    main()