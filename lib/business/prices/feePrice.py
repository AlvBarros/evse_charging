import json
from lib.business.prices import convert_float as convert

class FeePrice():
    def __init__(self, json):
        self.identifier = json['identifier']
        self.evseId = json['evse id']
        self.complexity = 'simple' # should not have any complexity
        if ('has minimum billing threshold' in json):
            self.hasMinimumBillingThreshold = (json['has minimum billing threshold'] == True or json['has minimum billing threshold'] == 'true')
            if (self.hasMinimumBillingThreshold and 'min billing amount' in json and convert.isFloat(json['min billing amount'])):
                self.minBillingAmount = convert.convertToFloat(json['min billing amount'])
        else:
            self.hasMinimumBillingThreshold = False
            self.minBillingAmount = float(str(0))

        if ('has max session fee' in json):
            self.hasMaximumSessionFee = (json['has max session fee'] == True or json['has max session fee'] == 'true')
            if (self.hasMaximumSessionFee and 'max_session fee' in json and convert.isFloat(json['max_session fee'])):
                self.maxSessionFee = convert.convertToFloat(json['max_session fee'])
        else:
            self.hasMaximumSessionFee = False
            self.maxSessionFee = float(str(0))
        
        if (isFloat(json['session fee'])):
            self.sessionFee = convert.convertToFloat(json['session fee'])
        else:
            self.sessionFee = float(str(0))
            