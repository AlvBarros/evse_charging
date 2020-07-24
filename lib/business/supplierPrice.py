from lib.business.prices.feePrice import FeePrice
from lib.business.prices.timePrice import TimePrice
from lib.business.prices.kWhPrice import kWhPrice

def checkIfFee(json):
    try:
        return (
            'has minimum billing threshold' in json
            and 'session fee' in json 
            # and isFloat(json['session fee']) 
            and 'max_session fee' in json 
            and isFloat(json['max_session fee'])
        )
    except:
        return False

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

# Parent class

class SupplierPrice:
    def __init__(self, json):
        self.evseId = json['evse id']
        self.identifier = json['identifier']

        if (checkIfFee(json)):
            self.fee = FeePrice(json)
        else:
            self.fee = None

        if (checkIfTime(json)):
            self.time = TimePrice(json)
        else:
            self.time = None

        if (checkIfKwh(json)):
            self.kwh = kWhPrice(json)
        else:
            self.kwh = None

        if (self.fee is None and self.time is None and self.kwh is None):
            print(json)