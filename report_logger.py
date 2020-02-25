from sales_calculator import SalesCalculator

class ReportLogger:
    """
        Keeping this name generic as it could be used
        for items that are not sales ...

        These reports will probably share some functionality ...

    """

    def __init__(self, sales):
        self.sales_calculator = SalesCalculator()

    def basic_report(self):
        """ return a basic report """

    def end_report(self):
        """ return the end report """