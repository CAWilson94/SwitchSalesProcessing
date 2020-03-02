"""
    Was thinking of Generator 1 with basic rule, then generator 2 with basic + extra
    then generator 3 with generator 2 + extra (kind of propagating rules) but this
    introduces a coupling between d3 and d2 so if they are separate it means d2 can
    be amended/deleted without d3 being effected.
"""

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
    def _calculate_total_value(self, row):
        return mul(row['value'], row['amount'])

    def generate_input_data(self, products_df):
        """ Standard columns for messages & random product amount sold generated """
        products_df = super(DataGeneratorType2, self).generate_input_data(products_df)
        products_df['amount'] = np.random.randint(2, 10, size=len(products_df))
        products_df['total_value'] = products_df.apply(self._calculate_total_value, axis=1)
        return products_df

class DataGeneratorType3(DataGenerator):


    def _add_random_operation(self, row):
        """ Random operation generated for product adjustment """
        return random.choice(list(operations.keys()))

    def _calculate_adjusted_value(self, row):
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
        products_df['amount'] = np.random.randint(2, 10, size=len(products_df))
        products_df['total_value'] = products_df.apply(self._calculate_total_value, axis=1)
        return products_df

def main():
    input_df = pd.read_csv("products.csv")
    input_df['message_type'] = np.random.randint(1, 4, size=len(input_df))
    input_df_list = [frame for message_type, frame in input_df.groupby('message_type')]

    data_generator_type1 = DataGenerator()
    data_generator_type2 = DataGeneratorType2()
    data_generator_type3 = DataGeneratorType3()

    data_generated_t1 = data_generator_type1.generate_input_data(input_df_list[0])
    data_generated_t2 = data_generator_type2.generate_input_data(input_df_list[1])
    data_generated_t3 = data_generator_type3.generate_input_data(input_df_list[2])

    input_file_path =  "input_messages.txt"
    fo = open(input_file_path, "a+")

    pound = "U+00A3"

    for index, row in data_generated_t1.iterrows(): 
        line = f"{row['product']} at {row['value']}\n"
        fo.writelines(line)

    for index, row in data_generated_t2.iterrows(): 
        line = f"{row['amount']} of {row['product']} at {row['value']} each\n"
        fo.writelines(line)

    for index, row in data_generated_t3.iterrows(): 
        line = f"{row['operation']} {row['random_val_op']} {row['product']}\n"
        fo.writelines(line)

    fo.close()

    # shuffling data for realistic input ... 
    lines = open(input_file_path).readlines()
    random.shuffle(lines)
    open(input_file_path, 'w').writelines(lines)
    
    #all_generated_data = pd.concat([data_generated_t1, data_generated_t2, data_generated_t3])
    #all_generated_data = all_generated_data.sample(frac=1).reset_index(drop=True) # shuffling our data
    #print(all_generated_data)
    #all_generated_data.to_csv("generated_product_data.csv")
    


if __name__ == '__main__':
    main()