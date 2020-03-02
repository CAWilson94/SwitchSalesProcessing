import collections 
from operator import add, sub, mul

from report import Report

class Sale:

    OPERATIONS = {'add': add, 'subtract': sub, 'multiply': mul}

    def __init__(self, product_type, value=0, amount=1):
        self.product = product_type
        self.value = value
        self.adjusted_value = value 
        self.amount = amount     
        self.total_value = mul(self.value, self.amount)   
        self.adjusted_total_value = self.total_value 
        self.Adjustment = collections.namedtuple('Adjustment', 'operation adjusted_amount')        
        self.adjustments = []
        self.applied_adjustments_dict = self._create_applied_adjustments_dict()

    def add_adjustment(self, operation, amount): 
        """ Add operations and amount for operations to be applied to sale """ 
        adjusment = self.Adjustment(operation=operation, adjusted_amount=amount)
        self.adjustments.append(adjusment)

    def apply_adjustments(self):
        """ Should apply adjustments in order """       
        for adjustment in self.adjustments: 
            self.adjusted_value = self.OPERATIONS[adjustment.operation](self.value, adjustment.adjusted_amount)   
            self.adjusted_total_value = mul(self.adjusted_value, self.amount)  
            self._add_applied_adjustment_to_dict(adjustment.operation, adjustment.adjusted_amount)            
            self.value = self.adjusted_value # New value which can be adjusted.
            self.total_value = self.adjusted_total_value

    def _add_applied_adjustment_to_dict(self, operation, amount_adjusted): 
        """ Add applied adjustment values to dictionary. """ 
        self.applied_adjustments_dict["product"].append(self.product)
        self.applied_adjustments_dict["value"].append(self.value)
        self.applied_adjustments_dict["operation"].append(operation)
        self.applied_adjustments_dict["adjusted_amount"].append(amount_adjusted)
        self.applied_adjustments_dict["new_price"].append(self.adjusted_value)
        self.applied_adjustments_dict["number_items"].append(self.amount)
        self.applied_adjustments_dict["total_adjusted_value"].append(mul(self.amount, self.adjusted_value))


    def _create_applied_adjustments_dict(self): 
        """ Create dictionary for applied adjustments. """ 
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
        """ Sale object to dictionary for data frame usage and easy processing. """
        return{
            'product': self.product,
            'original_value': self.value,
            'original_sale_total_value': self.total_value,
            'amount': self.amount,     
            'adjusted_value': self.adjusted_value,
            'adjusted_total_value': self.adjusted_total_value,       
        }

