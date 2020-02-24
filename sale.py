class Sale:

    def __init__(self, product_type, value):
        self.product_type = product_type
        self.value = value


"""
Sale comes in --> 
    Record it 
    When a sale is recorded, a message comes with it so this is "processed" ... aye
    
Every 10th Message -->
    Log a report detailing the number of sales for each product and their total value 
        Do I need a product class?
        
After 50 Messages --> 
    Application should log that it is pausing 
    Stop accepting new messages and log a report of adjustments that have been made to EACH SALE TYPE while the
    application was running 
    
e.g. product = apple 
     1 sale 
     10p 
     
     product = apple 
     20 sales 
     10p each 
     
     product = apple 
     operation add 
     adjustment value 20p 
     (add this to EACH sale of apples ALREADY recorded) 
     
     after 10 messages:
     21 sales of apples 
     total value = 21 * 10 ==> 210
     (21 * 10) + (20 * 21) ==> 210 + 420 ==> 630
     
     So now after 50 messages: 
     Product: apple 
     number sales: 21 
     adjustments: add 20p, others here  

"""
