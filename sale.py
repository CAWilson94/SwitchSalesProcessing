import collections 
import operator

class Sale:

    def __init__(self, product_type, value=0, amount=1):
        self.product = product_type
        self.value = value
        self.adjusted_value = value # starts out this way ...
        self.amount = amount     
        self.total_value = self.value   
        self.adjusted_total_value = value # starts out this way 
        self.Adjustment = collections.namedtuple('Adjustment', 'operation adjusted_amount')        
        self.adjustments_made = []

    def add_adjustment(self, operation, amount): 
        """ Add operations and amount for operations to be applied to sale """ 
        adjusment = self.Adjustment(operation=operation, adjusted_amount=amount)
        self.adjustments_made.append(adjusment)

    def apply_adjustments(self):
        """ Should apply adjustments in order """ 
        for item in self.adjustments_made: 
            self.value = operator.item.operation(self.value, item.adjusted_amount)   
            self.total_value = operator.mul(self.value, self.amount)     

    def to_dict(self):
        """ Object to dictionary for data frame usage """
        return{
            'product': self.product,
            'original_value': self.value,
            'original_sale_total_value': self.total_value,
            'amount': self.amount,     
            'adjusted_value': self.adjusted_value,
            'adjusted_total_value': self.adjusted_total_value,       
        }

