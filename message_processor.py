import pandas as pd
from sale import Sale

class MessageProcessor:

    def __init__(self, input):
        self.input = input
        self.sales =[]

    def process_sales(self):
        """ Get sales from the input given """
        for row in self.input.itertuples():
            self.sales.append(Sale(row.product, round(row.value, 2)))


def main():
    input = pd.read_csv("products.csv")
    processor = MessageProcessor(input)
    processor.get_sales()
    for sale_item in processor.sales:
        print("1 copy of {} has been sold for £{}".format(sale_item.product_type, sale_item.value))

if __name__ == '__main__':
    main()