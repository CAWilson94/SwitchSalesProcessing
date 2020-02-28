import pandas as pd
from sale import Sale

from sales_recorder import SalesRecorder

class MessageProcessor:

    MAX_REPORT = 50

    def __init__(self, input):
        self.input = input
        self.sales_recorder = SalesRecorder()

    def process_sales(self):
        """ Get sales from the input given """
        for row in self.input.iloc[:self.MAX_REPORT].itertuples():
            self.sales_recorder.record_sale(Sale(row.product, round(row.value, 2),
                                                 amount=row.amount, adjustment=row.operation))


def main():
    input = pd.read_csv('generated_product_data.csv')
    mp = MessageProcessor(input)
    mp.process_sales()

if __name__ == '__main__':
    main()