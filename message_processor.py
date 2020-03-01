import pandas as pd
from sale import Sale

from sales_recorder import SalesRecorder

class MessageProcessor:

    MAX_REPORT = 50
    OPERATIONS = set(["add", "subtract", "multiply"])

    def __init__(self, input_path):
        self.input_path = input_path
        self.sales_recorder = SalesRecorder()   

    def _parse_message_one(self, word_list): 
        """ Parse messages showing product and value, assuming amount is one per sale. """ 
        try:
            print(word_list)
        except expression as e:
            print("use a logger instead")        

    def _parse_message_two(self, word_list): 
        """ Parse messages showing product, value and amount of products in sale. """ 
        try:
            print(word_list)
        except expression as e:
            print("use a logger instead")

    def _parse_message_three(self, word_list): 
        """ Parse messgage that shows adjustments for product. """ 
        try:
            operation = word_list[0]
            amount = word_list[1][1:] # gives us item 1 from list then index 1 onwards for this (skipping the £)
            product = " ".join(word_list[2:]) # allowing for spaces in product namne
            sale = Sale(product)
            sale.add_adjustment(operation, amount)
            return sale
        except Exception as e:
            logger.warn("Cannot parse adjustment message: {}".format(e))

    def parse_messages(self): 
        """ Determine message type and parse """
        input_file = open(self.input_path, 'r')
        for line in input_file:             
            word_list = line.lower().split()
            if self.OPERATIONS.intersection(word_list):
                self._parse_message_three(word_list) #  message three being the one with adjustments 
            elif word_list[0].isdigit(): 
                self._parse_message_two(word_list) # message two is amount of product message
            elif (len(word_list) == 3) and (word_list[2].isdigit) and (type(word_list[0]) == str): # message one is basic type and value 
                self._parse_message_one(word_list)
            else: 
                print(f"input: {line} could not be processed.")                                 

    def process_sales(self):
        """ Get sales from the input given """
        for row in self.input.iloc[:self.MAX_REPORT].itertuples():
            self.sales_recorder.record_sale(Sale(row.product, round(row.value, 2),
                                                 amount=row.amount, adjustment=row.operation))


def main():
    #input = pd.read_csv('generated_product_data.csv')
    input_path = "input_messages.txt"
    mp = MessageProcessor(input_path)
    mp.parse_messages()

if __name__ == '__main__':
    main()