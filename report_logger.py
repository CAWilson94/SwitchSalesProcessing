from functools import reduce

import pandas as pd

from sale import Sale

class ReportLogger:
    """
        Keeping this name generic as it could be used
        for items that are not sales ...
    """

    def __init__(self, sales):
        self.sales_list = sales
        #self.sales_calculator = SalesCalculator(sales)

    def _get_sales_dict(self):
        df = pd.DataFrame.from_records([sale.to_dict() for sale in self.sales_list])
        return df

    def basic_report(self):
        """ return a basic report """
        df = self._get_sales_dict()
        df['total_value'] = df.apply(lambda row: row['amount'] * row['value'], axis=1)
        total_value_df = df.groupby(['product'])['total_value'].sum().reset_index(name='full_value')
        count_df = df.groupby(['product'])['amount'].sum().reset_index(name='count')
        basic_report_df = pd.merge(count_df, total_value_df, on=['product'])
        return basic_report_df

    def end_report(self):
        """ return the end report """
        """
        adjustments that have been made to each sale type while the app was running
        """
        df = self._get_sales_dict()

        adjustment_types = df.adjustment.unique() # columns of new df
        # need number of occurrences of each of these per product
        boop = df.groupby(['product'])
        frames = []
        for item in boop:
            frames.append(item[1].groupby(['product', 'adjustment'])['adjustment'].count().reset_index(name="numAdjust"))
        result = pd.concat(frames)
        result = result.pivot(index="product", columns="adjustment", values="numAdjust")
        result = result.fillna(0.0)
        products = list(set(df['product']))

        for item in products: # add adjustment types here too
            print(item, "Add:", result.loc[item]['Add'],
                  "Multiply:", result.loc[item]['Multiply'],
                  "Subtract:", result.loc[item]['Subtract'])


        # have it with a separate df per product but I want it to be a df showing product, add, mult, sub as col headers
        # and num adjustments as row values under those headers


        adj_type = "Subtract"

        return "you have reached the end "



def main(): # add type checks for all in Sale?
    sales = [Sale("orange", 10, adjustment="Add"), Sale("orange", 10, adjustment="Add"),
             Sale("orange", 10, adjustment="Add"), Sale("orange", 10, adjustment="Multiply"),
             Sale("potato", 10, adjustment="Subtract"), Sale("potato", 10, adjustment="Subtract"),
             Sale("potato", 10, adjustment="Multiply"), Sale("potato", 10, adjustment="Multiply"),
             Sale("potato", 10, adjustment="Add")
             ]

    rl = ReportLogger(sales)
    rl.end_report()



if __name__ == '__main__':
    main()