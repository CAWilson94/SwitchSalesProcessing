from message_processor import MessageProcessor
from report_logger import ReportLogger

class MessageProcessingApp: 

    MAX_REPORT_ITER = 50
    BASIC_REPORT_ITER = 10

    def __init__(self, sales_multi_input_path): 
        self.sales_multi_input_path = sales_multi_input_path
        self.sales_list = []
        self.number_messages = 0

    def process_sales_messages(self):
        """ Process messages, record sales and log. """
        input_file = open(self.sales_multi_input_path, 'r')        
        message_processor = MessageProcessor(self.sales_list)
        for message in input_file: 
            try: 
                message_processor.process_message(message)                        
                if (self.number_messages % self.BASIC_REPORT_ITER == 0) and (self.number_messages > 0): 
                    self.sales_list = message_processor.sales_list  
                    self._prepare_report()
                    if (self.number_messages % self.MAX_REPORT_ITER == 0):                                    
                        break
                self.number_messages += 1
            except UnicodeDecodeError as e: 
                logging.warn("Input Error: %s", e)


    def _prepare_report(self): 
        """ Prepare report """ 
        for sale in self.sales_list:
            sale.apply_adjustments()
        sales_report_logger = ReportLogger(self.sales_list)
        if self.number_messages < self.MAX_REPORT_ITER: 
            sales_report_logger.basic_report()
        if self.number_messages == self.MAX_REPORT_ITER: 
            sales_report_logger.end_report()            

def main(): 
    mpa = MessageProcessingApp("input_messages.txt")
    mpa.process_sales_messages()

if __name__ == "__main__":
    main()

