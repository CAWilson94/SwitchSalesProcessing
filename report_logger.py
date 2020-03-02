from functools import reduce

import pandas as pd


from sale import Sale
from report import Report

class ReportLogger:
    """
        Keeping this name generic as it could be used
        for items that are not sales ...
    """

    def __init__(self, sales):
        self.sales_list = sales
        df = self._get_sales_df()        
        self.report = Report(df)

    def _get_sales_df(self):
        df = pd.DataFrame.from_records([sale.to_dict() for sale in self.sales_list])
        return df

    def basic_report(self):
        """ return a basic report """        
        # just need to print in plain text now? 
        print(self.report.basic_report())
        

    def end_report(self):
        """ return the end report """                      
        #result = self.report.end_report()
        adjustments_cols = self.sales_list[0].adjustments_dict.keys()
        adjustment_df_init = pd.DataFrame(columns=adjustments_cols)
        df = pd.DataFrame()
        for sale in self.sales_list: 
            df = pd.DataFrame.from_dict(sale.adjustments_dict)
            df = pd.concat([adjustment_df_init, df])
        print(df)

        
        """
        for index, row in result.iterrows(): 
            print("Adjustments for ", index, " are ", end = " ")
            [print(item, " : ", row[item], end=" ") for item in adjustment_types]
            print("\n")        
        """

