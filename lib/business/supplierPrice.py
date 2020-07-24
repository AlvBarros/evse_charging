from lib.business.prices.feePrice import FeePrice
from lib.business.prices.timePrice import TimePrice
from lib.business.prices.kWhPrice import kWhPrice

# Method for checking if specific supplier_price is of Fee category
def checkIfFee(json):
    try:
        return (
            'has minimum billing threshold' in json
            and 'session fee' in json  # and isFloat(json['session fee']) 
            and 'max_session fee' in json 
            and isFloat(json['max_session fee'])
        )
    except:
        return False

# Method for checking if specific supplier_price is of Time category
def checkIfTime(json):
    try:
        return (
            (
                'has complex minute price' in json
                and 'simple minute price' in json # and isFloat(json['simple minute price'])
                and 'min_duration' in json # and isFloat(json['min_duration'])
            ) or (
                'has complex minute price' in json
                and 'has hour day' in json
                and 'interval' in json
                and 'min duration' in json
            )
        )
    except:
        return False

# Method for checking if specific supplier_price is of kWh category
def checkIfKwh(json):
    try:
        return ((
            'has kwh price' in json
            and 'kwh price' in json # and isFloat(json['kwh price'])
            and 'min cosumed energy' in json # and isFloat(json['min cosumed energy'])
            ) or (
            'has time based kwh' in json
            and 'has hour day' in json
            and 'min consumption' in json)
        )
    except:
        return False

# Supplier Price class
class SupplierPrice:
    def __init__(self, json):
        self.evseId = json['evse id']
        self.identifier = json['identifier']

        # If it is of Fee category, add as an object
        if (checkIfFee(json)):
            self.fee = FeePrice(json)
        else:
            self.fee = None

        # If it is of Time category, add as an object
        if (checkIfTime(json)):
            self.time = TimePrice(json)
        else:
            self.time = None

        # If it is of kWh category, add as an object
        if (checkIfKwh(json)):
            self.kwh = kWhPrice(json)
        else:
            self.kwh = None

        # A supplier price must have a category. If not, something's wrong with the check methods
        if (self.fee is None and self.time is None and self.kwh is None):
            raise 'Supplier price must be of a category'