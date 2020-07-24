# Class that holds the calculated prices for charges
class Price:
    def __init__(self, supplierPriceId, sessionId):
        self.supplierPriceId=supplierPriceId
        self.sessionId = sessionId
        self.feePrice = None
        self.timePrice = None
        self.kWhPrice = None
    
    def get_feePrice(self):
        if (self.feePrice is None):
            return 0
        else:
            return self.feePrice
    def set_feePrice(self, price):
        self.feePrice=price

    def get_timePrice(self):
        if (self.timePrice is None):
            return 0
        else:
            return self.timePrice
    def set_timePrice(self, price):
        self.timePrice=price

    def get_kwhPrice(self):
        if (self.kWhPrice is None):
            return 0
        else:
            return self.kWhPrice
    def set_kwhPrice(self, price):
        self.kWhPrice=price
    
    # Returns total price based on Fee minimum and maximum price logic
    def get_totalPrice(self):
        # Any category that is not present returns 0
        total = self.get_feePrice() + self.get_timePrice() + self.get_kwhPrice()
        # If is of Fee category
        if (self.feePrice is not None):
            # Maximum session fee (session value) indicates the maximum value allowed to 
            # charge the customer for a charge.
            if (self.feePrice.maxSessionFee > 0 and self.feePrice.maxSessionFee < total):
                return self.feePrice.maxSessionFee
            # Minimum billing threshold indicates the minimum value for 
            # the whole charge, else no price should be charged of the customer
            if (self.feePrice.minBillingAmount > 0 and total < self.feePrice.minBillingAmount):
                return 0
        else:
            return total