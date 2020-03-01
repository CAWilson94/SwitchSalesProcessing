import pandas as pd

class Report: 

    def __init__(self, df): 
        self.df = df

    def basic_report(self): 
        self.df['total_value'] = self.df.apply(lambda row: row['amount'] * row['value'], axis=1)
        total_value_df = self.df.groupby(['product'])['total_value'].sum().reset_index(name='full_value')
        count_df = self.df.groupby(['product'])['amount'].sum().reset_index(name='count')
        basic_report_df = pd.merge(count_df, total_value_df, on=['product'])
        return basic_report_df

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