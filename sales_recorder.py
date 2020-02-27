from report_logger import ReportLogger

class SalesRecorder:

    def __init__(self):
        self.sales = []

    def record_sale(self, sale):
        """ Store individual sales in collection of sale"""
        self.sales.append(sale)
        self._sales_logger_check() #rename

    def _sales_logger_check(self):
        """ Checking when we need to log sales """
        sales_logger = ReportLogger(self.sales)
        if (int(len(self.sales)%10) and int(len(self.sales)< 50)) == 0:
            print(sales_logger.basic_report())
        if (int(len(self.sales) % 50)) == 0:
            print(sales_logger.end_report())
        # probably want to store these in a df?
        # check if sale count is divisible perfectly by 10 -> so when we get 10, 20, 30 etc we will spit out logs
        # second check for divisible by 50 for second logging
