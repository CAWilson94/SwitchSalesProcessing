import pandas as pd


class Report:

    def __init__(self, sales_list):
        self.sales_list = sales_list
        self.df = self._sales_dict()

    def log_basic_report(self):
        """ Output log for a basic report. """
        report = self._basic_report_df()
        for index, row in report.iterrows():
            print(f"{row['number_sales']} sales of {row['product']} at a total value of {round(row['total_value_sales'],2)}")
        print("\n")

    def log_end_report(self):
        """ Output log for an end report. """
        sale_type_adjustment = self._end_report_df()
        print("Message processor is pausing, messages will stop being accepted now.\n")
        for adjustments_made in sale_type_adjustment:
            if(len(adjustments_made) > 0):
                details = adjustments_made.iloc[0]
                print(f"For {details['product']} with original value {details['value']} and number of products of {details['number_items']}, the adjustments made were:")
                pd.set_option('display.width', None)
                pd.set_option('display.max_columns', None)
                pd.set_option('display.max_rows', None)
                print(adjustments_made)
                print("\n")

    def _basic_report_df(self):
        """ Create basic report dataframe. """
        total_value_df = self._total_value_df()
        number_sales_df = self._number_sales_df()
        basic_report_df = pd.merge(
            number_sales_df, total_value_df, on=['product'])
        return basic_report_df

    def _end_report_df(self):
        """ Create end report dataframe. """
        df_list = []
        for sale in self.sales_list:
            df = pd.DataFrame.from_dict(sale.applied_adjustments_dict)
            df_list.append(df)
        return df_list

    def _total_value_df(self):
        """ Get total value of sales, represented as a column total_value_sales. """
        total_value_df = self.df.groupby(['product'])[
            'adjusted_total_value'].sum().reset_index(name='total_value_sales')
        return total_value_df

    def _number_sales_df(self):
        """ Get number of sales of each product, represented as a column number_sales. """
        return self.df.groupby(['product'])['amount'].sum().reset_index(name='number_sales')

    def _sales_dict(self):
        """ """
        df = pd.DataFrame.from_records(
            [sale.to_dict() for sale in self.sales_list])
        return df
