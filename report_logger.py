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
        df_list = []
        for sale in self.sales_list: 
            df = pd.DataFrame.from_dict(sale.applied_adjustments_dict)
            df_list.append(df)
        df = pd.concat(df_list)
        print(df)

