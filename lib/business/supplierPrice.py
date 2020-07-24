supplier_price_types = ['unspecified', 'fee', 'time', 'kwh']
complexity_types = ['simple', 'complex']

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

        # This is kind of a factory approach to solving inheritance
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

class FeePrice(SupplierPrice):
    def __init__(self, json):
        self.type='fee'
        self.complexity = 'simple' # should not have any complexity

class TimePrice(SupplierPrice):
    def __init__(self, json):
        self.type='time'
        if (
            'simple minute price' in json
            and 'has complex minute price' in json
            and (json['has complex minute price'] == False or json['has complex minute price'] == 'false')
            and 'min_duration' in json
        ):
            self.complexity='simple'
        elif (
            'has complex minute price' in json
            and (json['has complex minute price'] == True or json['has complex minute price'] == 'true')
            and 'has hour day' in json
            and 'interval' in json
            and 'min duration' in json
        ):
            self.complexity='complex'
        else: # should not be possible
            raise 'TimePrice must be either simple or complex. JSON: ' + str(json)

class kWhPrice(SupplierPrice):
    def __init__(self, json):
        self.type='kwh'
        if (
            'has kwh price' in json
            and 'kwh price' in json
            and 'min cosumed energy' in json # shouldnt it be "coNsumed"?
        ):
            self.complexity='simple'
        elif (
            'has time based kwh' in json
            and 'has hour day' in json
            and 'min consumption' in json
        ):
            self.complexity='complex'
        else: # should not be possible
            raise 'kWhPrice must be either simple or complex. JSON: ' + str(json)