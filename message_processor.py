import logging
import pandas as pd

from sale import Sale
from sales_recorder import SalesRecorder
from report_logger import ReportLogger

class MessageProcessor:
   
    OPERATIONS = set(["add", "subtract", "multiply"])
    UNUSED_WORDS = ['of', 'at', 'each']

    def __init__(self, sales_list):
      self.sales_list = sales_list


    def process_message(self, message): 
        """ Determine message type and process into sales """               
           
        word_list = message.lower().split()
        try: 
            if self.OPERATIONS.intersection(word_list):
                self._apply_adjustments(word_list) #  message three being the one with adjustments                                 
            elif word_list[0].isdigit(): 
                sale = self._parse_message_two(word_list) # message two is amount of product message
                self.sales_list.append(sale)
            elif(word_list[-1].isdigit): # message one is basic type and value 
                sale = self._parse_message_one(word_list)
                self.sales_list.append(sale)
        except Exception as e:              
            logging.info("Could not parse message %s.\n%s", message, e) 


    def _apply_adjustments(self, word_list): 
        """ Parse messgage that shows adjustments for product. """ 
        try:
            operation = word_list[0]
            try: 
                amount = float(word_list[1])
            except Exception as e: 
                logging.warn("what is this: {}".format(e))
            product = " ".join(word_list[2:]).title() # allowing for spaces in product namne           
            for sale in self.sales_list: 
                if sale.product.lower() == product.lower(): 
                    sale.add_adjustment(operation, amount)
                       
        except Exception as e:
            logging.warn("Cannot parse adjustment message: {}".format(e))


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

    

                
        