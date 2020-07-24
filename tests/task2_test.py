# ========== 2. Parse Data ========== 
# Description
# In this task, you already have the data for the system, but
# the JSON that the company sent you is messed up and you'll
# have to parse the data in a format that's more readable
# for the ERP system.
# Your taks is to clean the data, use meaningful names for
# the variables, convert values to the correct types
# (native Python types), create objects (if needed) and any
# other clean/conversion that is suitable for the data.
# [...]

# Expected Result
# Two cleaned up lists of supplier prices and transactions.


import tests.helper as helper
import json

def run():
    print('Running Task 2 test')
    try:
        data = helper.evse_charging.importSupplierPricesData()
        result = helper.evse_charging.cleanSupplierPricesData(data)
        print('Validating result')
        any_with_unspecified=False
        any_without_evseId=False
        # Searches for any invalid supplier price
        for sp in result['supplier_prices']:
            if (sp.fee is None and sp.time is None and sp.kwh is None):
                any_with_unspecified=True                                       # not really perfomatic but tests aren't supposed to be ran a lot
            try:
                x=sp.evseId # EAFP approach as to check if the object has te attribute
            except:
                any_without_evseId=True
        print('Any result with a Unspecified Price: ' + str(any_with_unspecified))
        print('Any result without a EVSE ID: ' + str(any_without_evseId))
        any_invalid_transaction=False
        # Searches for any invalid transaction
        for tr in result['transactions']:
            if (tr.uId is None):
                any_invalid_transaction=True
                break
        print('Any invalid transaction: ' + str(any_invalid_transaction))
        if (any_with_unspecified or any_invalid_transaction):
            raise 'Clean data must not have any Unspecified Supplier Price or Invalid Transaction'
        print('Test completed.')
    except:
        print('Test failed.')
        raise

run()