import logging
import pandas as pd

from sale import Sale
from sales_recorder import SalesRecorder
from report_logger import ReportLogger

class MessageProcessor:

    MAX_REPORT_ITER = 50
    BASIC_REPORT_ITER = 10
    OPERATIONS = set(["add", "subtract", "multiply"])
    UNUSED_WORDS = ['of', 'at', 'each']

    def __init__(self, input_path):
        self.input_path = input_path
        self.sales_recorder = SalesRecorder()   

    def _parse_message_one(self, word_list): 
        """ Parse messages showing product and value, assuming amount is one per sale. """ 
        try:
            word_list = [word for word in word_list if word not in self.UNUSED_WORDS]
            value = float(word_list[-1])
            product = " ".join(word_list[:-1]).title()
            sale = Sale(product, value=value)
            return sale
        except Exception as e:
            logging.warn("Cannot parse messagee type one: {}. Expected format <product> at <value>".format(e))

    def _parse_message_two(self, word_list): 
        """ Parse messages showing product, value and amount of products in sale. """ 
        try:
            word_list = [word for word in word_list if word not in self.UNUSED_WORDS]
            amount = int(word_list[0])
            value = float(word_list[-1])
            product = " ".join(word_list[1: -1]).title()
            sale = Sale(product, amount=amount, value=value)
            return sale
        except Exception as e:
            logging.warn("Cannot parse messagee type two: {}. Expected format <amount> of <product> at <value> each".format(e))

    def _apply_adjustments(self, word_list): 
        """ Parse messgage that shows adjustments for product. """ 
        try:
            operation = word_list[0]
            try: 
                amount = float(word_list[1])
            except Exception as e: 
                logging.warn("what is this: {}".format(e))
            product = " ".join(word_list[2:]).title() # allowing for spaces in product namne           
            for sale in self.sales_recorder.sales: 
                if sale.product.lower() == product.lower(): 
                    sale.add_adjustment(operation, amount)
                       
        except Exception as e:
            logging.warn("Cannot parse adjustment message: {}".format(e))

    def process_messages(self): 
        """ Determine message type and process into sales """        
        input_file = open(self.input_path, 'r')
        number_messages = 0
        for line in input_file:             
            word_list = line.lower().split()
            if self.OPERATIONS.intersection(word_list):
                self._apply_adjustments(word_list) #  message three being the one with adjustments                                 
            elif word_list[0].isdigit(): 
                sale = self._parse_message_two(word_list) # message two is amount of product message
                self.sales_recorder.record_sale(sale)
            elif(word_list[-1].isdigit): # message one is basic type and value 
                sale = self._parse_message_one(word_list)
                self.sales_recorder.record_sale(sale)
            else: 
                logging.info(f"input: {line} could not be processed.")                                 
                continue # probably don't want to store NO sale 
            number_messages += 1
            if (number_messages%self.BASIC_REPORT_ITER ==0) and (number_messages>0): 
                self._prepare_report(number_messages)
                if (number_messages%self.MAX_REPORT_ITER ==0): # should have already done end report as 50 can divide by 10 also                       
                    break

    def _prepare_report(self, number_messages):
        """ Apply adjustments for sales and call report """  
        for sale in self.sales_recorder.sales: 
            sale.apply_adjustments()
        sales_report_logger = ReportLogger(self.sales_recorder.sales)
        if number_messages < self.MAX_REPORT_ITER: 
            sales_report_logger.basic_report()
        if number_messages == self.MAX_REPORT_ITER: 
            sales_report_logger.end_report()
            print("THE END IS NIGH.")

    def process_sales(self):
        """ Get sales from the input given """
        for row in self.input.iloc[:self.MAX_REPORT].itertuples():
            self.sales_recorder.record_sale(Sale(row.product, round(row.value, 2),
                                                 amount=row.amount, adjustment=row.operation))


def main():
    #input = pd.read_csv('generated_product_data.csv')
    input_path = "input_messages.txt"
    mp = MessageProcessor(input_path)
    mp.process_messages()

if __name__ == '__main__':
    main()