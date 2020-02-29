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

        adjustment_types = [x for x in df['adjustment'].unique() if isinstance(x, str)]
        product_types = df['product'].unique()
        

        product_groups = df.groupby(['product'])
        frames = []
        for group in product_groups:
            frames.append(group[1].groupby(['product', 'adjustment'])['adjustment'].count().reset_index(name="num_adjust"))
        result = pd.concat(frames)
        result = result.pivot(index="product", columns="adjustment", values="num_adjust")
        result = result.fillna(0.0)     
        
        for index, row in result.iterrows(): 
            print("Adjustments for ", index, " are ", end = " ")
            [print(item, " : ", row[item], end=" ") for item in adjustment_types]
            print("\n")

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