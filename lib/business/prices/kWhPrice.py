import json
from lib.business.prices import convert_float as convert

class kWhPrice():
    def __init__(self, json):
        self.identifier = json['identifier']
        self.evseId = json['evse id']
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
        
        if ('min consumption' in json and convert.isFloat(json['min consumption'])):
            self.minConsumption = convert.convertToFloat(json['min consumption'])
        else:
            self.minConsumption = float(str(0))
        
        if ('has time based kwh' in json):
            self.hasTimeBasedkWh = (json['has time based kwh'] == True or json['has time based kwh'] == 'true')
        else:
            self.hasTimeBasedkWh = None
        
        if ('kwh price' in json):
            self.kwhPrice = convert.convertToFloat(json['kwh price'])
        else:
            self.kwhPrice = None
        
        if ('min consumption' in json):
            self.minConsumption = convert.convertToFloat(json['min consumption'])
        else:
            self.minConsumption = None
        

        

        