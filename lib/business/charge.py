class Charge:
    def __init__(self, json):
        self.sessionId=json['session id']
        self.providerId=json['proveider id'] # shouldnt it be provIder?
        self.evseId=json['evseid']
        self.partnerProductId=json['partner product id']
        self.uId=json['uid']
        self.meteringSignature=json['metering signature']
        self.chargingStart=json['charging start']
        self.chargingEnd=json['charging end']
        self.sessionStart=json['session start']
        self.sessionEnd=json['session end']
        self.meterValueStart=json['meter value start']
        self.meterValueEnd=json['meter value end']
        self.countryCode=json['countrycode']