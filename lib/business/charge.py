class Charge:
    def __init__(self, sessionId, providerId, evseId, partnerProductId,
                 uId, meteringSignature, chargingStart, chargingEnd,
                 sessionStart, sessionEnd, meterValueStart, meterValueEnd,
                 countryCode):
        self.sessionId=sessionId
        self.providerId=providerId
        self.evseId=evseId
        self.partnerProductId=partnerProductId
        self.uId=uId
        self.meteringSignature=meteringSignature
        self.chargingStart=chargingStart
        self.chargingEnd=chargingEnd
        self.sessionStart=sessionStart
        self.sessionEnd=sessionEnd
        self.meterValueStart=meterValueStart
        self.meterValueEnd=meterValueEnd
        self.countryCode=countryCode