import pandas as pd
from sale import Sale

from sales_recorder import SalesRecorder

class MessageProcessor:

    MAX_REPORT = 50 # change to 50

    def __init__(self, input):
        self.input = input
        self.sales_recorder = SalesRecorder()

    def process_sales(self):
        """ Get sales from the input given """
        for row in self.input.iloc[:self.MAX_REPORT].itertuples():
            self.sales_recorder.record_sale(Sale(row.product, round(row.value, 2)))



def main():
    input = pd.read_csv("products.csv")
    processor = MessageProcessor(input)
    processor.process_sales()
    #for sale_item in processor.sales:
    #    print("1 copy of {} has been sold for £{}".format(sale_item.product_type, sale_item.value))

if __name__ == '__main__':
    main()