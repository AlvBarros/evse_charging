import math
import json

from lib.business.supplierPrice import SupplierPrice
from lib.business.charge import Charge
from lib.business.price import Price

def calculatePricesFromCleanData(clean_data):
    # Initialize empty list
    result = []

    # For every Charge inside clean result
    for charge in clean_data['transactions']:
        # TODO: Not every supplier price is found
        # Every transaction (supposedly) has a EVSE ID that identifies which Supplier Price is it from
        # This method searches for such a SupplierPrice
        sp = getSupplierPriceFromEvseId(clean_data['supplier_prices'], charge.evseId)
        if (sp is not None):
            # Instanciate a Price object
            price = Price(sp.identifier, charge.sessionId)
            
            # If SupplierPrice is in Fee category
            if (sp.fee is not None):
                # Set its price as the one calculated below
                price.set_feePrice(calculateFeePrice(sp.fee))
            # If SupplierPrice is in Time category
            if (sp.time is not None):
                # Set its price as the one calculated below
                price.set_timePrice(calculateTimePrice(sp.time, charge))
            # If SupplierPrice is in kWh category
            if (sp.kwh is not None):
                # Set its price as the one calculated below
                price.set_kwhPrice(calculatekWhPrice(sp.kwh, charge))
            
            # Add to Dictionary result (which is pretty much like a JSON already)
            result.append({
                "fee_price": price.get_feePrice(),
                "time_price": price.get_timePrice(),
                "kwh_price": price.get_kwhPrice(),
                "total_price": price.get_totalPrice(),
                "session_id": price.sessionId,
                "supplier_price_id": price.supplierPriceId
            })
    
    # Return list of calculated prices
    return result

def getSupplierPriceFromEvseId(supplier_prices, evseId):
    # Search through the list for the one that has this EVSE ID
    for sp in supplier_prices:
        if (sp.evseId == evseId):
                return sp
    return None

def calculateFeePrice(feePrice):
    # The minimum/maximum calculations are done at Price.get_totalPrice method
    return feePrice.sessionFee

def calculateTimePrice(timePrice, charge):
    if (timePrice.complexity == 'simple'):
        # The formula is:
        # Duration (in minutes) * Minute Price
        # *Be aware of the minimum duration
        if (
            timePrice.simpleMinutePrice is None
            ):
            raise 'Invalid values for Simple Time Price'
        else:
            duration = charge.durationInMinutes()
            if (timePrice.minDuration is not None and duration < timePrice.minDuration):
                # If duration is less than the minimum, sets the minimum instead
                duration = timePrice.minDuration
            return (duration * timePrice.simpleMinutePrice)

    elif (timePrice.complexity == 'complex'):
        # TODO: Finish complex calculation
        return 0

        # >> Just ignore this code below.
        # Calculate using the minute price for that time price
        # total_hours_charging_time = timePrice.durationInMinutes()/60
        # if (timePrice.interval == 'start'):
        #     total_hours_charging_time = math.ceil(total_hours_charging_time)
        # elif (timePrice.interval == 'end'):
        #     total_hours_charging_time = math.floor(total_hours_charging_time)
        # else:
        #     raise 'Invalid interval'
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
                # If duration is less than the minimum, sets the minimum instead
                # Duration is in hours, but minConsumption is in kWh, kW or hours?
                duration = kWhPrice.minConsumption
            return duration * kWhPrice.kwhPrice
    elif (kWhPrice.complexity == 'complex'):
        # TODO: Finish complex calculation
        return 0
    else:
        raise 'Invalid complexity for kWhPrice calculation'