import json
from lib.business.prices import convert_float as convert

class TimePrice():
    def __init__(self, json):
        self.identifier = json['identifier']
        self.evseId = json['evse id']
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
        
        if ('simple minute price' in json and convert.isFloat(json['simple minute price'])):
            self.simpleMinutePrice = convert.convertToFloat(json['simple minute price'])
        else:
            self.simpleMinutePrice = None
        
        if ('min duration' in json and convert.isFloat(json['min duration'])):
            self.minDuration = convert.convertToFloat(json['min duration'])
        else:
            self.minDuration = None
        
        if ('interval' in json):
            self.interval = json['interval']
        else:
            self.interval = None
        
        if ('time_price' in json):
            self.time_price = json['time_price']
        else:
            self.time_price = None
        
        