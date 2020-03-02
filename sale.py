import collections 
from operator import add, sub, mul

from report import Report

class Sale:

    OPERATIONS = {'add': add, 'subtract': sub, 'multiply': mul}

    def __init__(self, product_type, value=0, amount=1):
        self.product = product_type
        self.value = value
        self.adjusted_value = value # starts out this way ...
        self.amount = amount     
        self.total_value = mul(self.value, self.amount)   
        self.adjusted_total_value = self.total_value # starts out this way 
        self.Adjustment = collections.namedtuple('Adjustment', 'operation adjusted_amount')        
        self.adjustments_made = []
        self.adjustments_dict = self._adjustments_to_dict()

    def add_adjustment(self, operation, amount): 
        """ Add operations and amount for operations to be applied to sale """ 
        adjusment = self.Adjustment(operation=operation, adjusted_amount=amount)
        self.adjustments_made.append(adjusment)

    def apply_adjustments(self):
        """ Should apply adjustments in order """       
        for adjustment in self.adjustments_made: 
            self.adjusted_value = self.OPERATIONS[adjustment.operation](self.value, adjustment.adjusted_amount)   
            self.adjusted_total_value = mul(self.adjusted_value, self.amount)  
            self._add_adjustment_to_dict(adjustment.operation, adjustment.adjusted_amount)
            # new value which can be adjusted 
            self.value = self.adjusted_value
            self.total_value = self.adjusted_total_value

    def _add_adjustment_to_dict(self, operation, amount_adjusted): 
        self.adjustments_dict["product"].append(self.product)
        self.adjustments_dict["value"].append(self.value)
        self.adjustments_dict["operation"].append(operation)
        self.adjustments_dict["adjusted_amount"].append(amount_adjusted)
        self.adjustments_dict["new_price"].append(self.adjusted_value)
        self.adjustments_dict["number_items"].append(self.amount)
        self.adjustments_dict["total_adjusted_value"].append(mul(self.amount, self.adjusted_value))


    def _adjustments_to_dict(self, operation="no op", amount_adjusted=0): 
        """ create dictionary """ 
        return {
            "product": [],
            "value": [],
            "operation": [],
            "adjusted_amount": [],
            "new_price": [],
            "number_items": [],
            "total_adjusted_value": [],  
            }


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

