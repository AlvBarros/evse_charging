import math
import json

from lib.business.supplierPrice import SupplierPrice
from lib.business.charge import Charge
from lib.business.price import Price

def calculatePricesFromCleanData(clean_data):
    result = []

    for charge in clean_data['transactions']:
        
        # TODO: Not every supplier price is found
        # Every transaction has a EVSE ID that identifies which Supplier Price is it from (supposedly)
        sp = getSupplierPriceFromEvseId(clean_data['supplier_prices'], charge.evseId)
        if (sp is not None):
            # print('identifier: ' + sp.identifier)
            # print('sessionId : ' + charge.sessionId)
            price = Price(sp.identifier, charge.sessionId)
            
            if (sp.fee is not None):
                price.set_feePrice(calculateFeePrice(sp.fee))
            if (sp.time is not None):
                price.set_timePrice(calculateTimePrice(sp.time, charge))
            if (sp.kwh is not None):
                price.set_kwhPrice(calculatekWhPrice(sp.kwh, charge))
            
            result.append({
                "fee_price": price.get_feePrice(),
                "time_price": price.get_timePrice(),
                "kwh_price": price.get_kwhPrice(),
                "total_price": price.get_totalPrice(),
                "session_id": price.sessionId,
                "supplier_price_id": price.supplierPriceId
            })
    return result

def getSupplierPriceFromEvseId(supplier_prices, evseId):
    for sp in supplier_prices:
        try:
            # print('checking if ' + str(sp.evseId) + ' is like ' + evseId)
            if (sp.evseId == evseId):
                return sp
        except:
            raise 'Supplier Price without EVSE ID'

def calculateFeePrice(feePrice):
    return feePrice.sessionFee

def calculateTimePrice(timePrice, charge):
    if (timePrice.complexity == 'simple'):
        # Duration (in minutes) * Minute Price
        # Be aware of the minimum duration
        if (
            timePrice.simpleMinutePrice is None
            ):
            print('smp: ' + str(timePrice.simpleMinutePrice))
            raise 'Invalid values for Simple Time Price'
        else:
            duration = charge.durationInMinutes()
            if (timePrice.minDuration is not None and duration < timePrice.minDuration):
                duration = timePrice.minDuration
            return (duration * timePrice.simpleMinutePrice)

    elif (timePrice.complexity == 'complex'):
        # TODO: Finish complex calculation
        return 0

        # Calculate using the minute price for that time price
        total_hours_charging_time = timePrice.durationInMinutes()/60
        if (timePrice.interval == 'start'):
            total_hours_charging_time = math.ceil(total_hours_charging_time)
        elif (timePrice.interval == 'end'):
            total_hours_charging_time = math.floor(total_hours_charging_time)
        else:
            raise 'Invalid interval'
    else:
        raise 'Invalid complexity for TimePrice calculation'

def calculatekWhPrice(kWhPrice, charge):
    if (kWhPrice.complexity == 'simple'):
        # Consumed kWh * kWh price
        # Be aware of the minimum consumption
        if (
            kWhPrice.kwhPrice is None
        ):
            raise 'Invalid kWhPrice'
        else:
            duration = charge.durationInMinutes()/60
            if (kWhPrice.minConsumption is not None and duration < kWhPrice.minConsumption):
                # Duration is in hours, minConsumption is in k or time?
                duration = kWhPrice.minConsumption
            return duration * kWhPrice.kwhPrice
    elif (kWhPrice.complexity == 'complex'):
        # TODO: Finish complex calculation
        return 0
    else:
        raise 'Invalid '