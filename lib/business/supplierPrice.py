def isFloat(v):
    s=str(v)
    try:
        floatStr=float(s.replace(',','.'))
        return True
    except:
        return False

def checkIfFee(json):
    try:
        return (
            'has minimum billing threshold' in json # doesnt need to have value if this is false
            and 'session fee' in json 
            and isFloat(json['session fee']) 
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
                and 'simple minute price' in json and isFloat(json['simple minute price'])
                and 'min_duration' in json and isFloat(json['min_duration'])
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
            and 'kwh price' in json and isFloat(json['kwh price'])
            and 'min cosumed energy' in json and isFloat(json['min cosumed energy'])
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
        self.type='unspecified'
        if (checkIfFee(json)):
            FeePrice.__init__(self, json)
        elif (checkIfTime(json)):
            TimePrice.__init__(self, json)
        elif (checkIfKwh(json)):
            kWhPrice.__init__(self, json)
        else:
            print(json)
        # Should return as type 'unspecified' if nothing else

# Children classes

class kWhPrice(SupplierPrice):
    def __init__(self, json):
        self.type='fee'
        # if ('has kwh price' not in json or not json['has kwh price']):
        #     raise 'Not possible to create kWhPrice object'

class TimePrice(SupplierPrice):
    def __init__(self, json):
        self.type='time'
        pass

class FeePrice(SupplierPrice):
    def __init__(self, json):
        self.type='kwh'
        pass