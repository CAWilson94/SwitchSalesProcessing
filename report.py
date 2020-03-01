import pandas as pd

class Report: 

    def __init__(self, df): 
        self.df = df

    def basic_report(self): 
        total_value_df = self._total_value_df()
        number_sales_df = self._number_sales_df()
        basic_report_df = pd.merge(number_sales_df, total_value_df, on=['product'])
        return basic_report_df

    def _total_value_df(self): 
        """ Get total value of sales, represented as a column total_value_sales """       
        total_value_df = self.df.groupby(['product'])['adjusted_total_value'].sum().reset_index(name='total_value_sales')
        return total_value_df
    
    def _number_sales_df(self): 
        """ Get number of sales of each product, represented as a column number_sales""" 
        return self.df.groupby(['product'])['amount'].sum().reset_index(name='number_sales')

    def end_report_adjustment_stats(self): 
        adjustment_types = [x for x in self.df['adjustment'].unique() if isinstance(x, str)]
        product_types = self.df['product'].unique()        
        product_groups = self.df.groupby(['product'])
        frames = []
        for group in product_groups:
            frames.append(group[1].groupby(['product', 'adjustment'])['adjustment'].count().reset_index(name="num_adjust"))
        result = pd.concat(frames)
        result = result.pivot(index="product", columns="adjustment", values="num_adjust")
        result = result.fillna(0.0)     
        return result


#witcher III: 
#price was x, adjustment made - add 40p, new price x + 40p 
#price was x, adjustment made - sub 10, new price x - 10