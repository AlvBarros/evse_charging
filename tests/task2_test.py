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


import helper
import json

def run():
    print('Running Task 2 test')
    try:
        datas = []
        num_datas = 5
        for n in range(0, num_datas):
            datas.append(helper.evse_charging.importSupplierPricesData())
        
        results = []
        for d in datas:
            results.append(helper.evse_charging.cleanSupplierPricesData(d))
        

        print('Validating result')
        print('Imports made: ' + str(num_datas))

        any_with_unspecified=False
        for result in results:
            sps = result['supplier_prices']
            for sp in sps:
                if (sp.fee is None and sp.time is None and sp.kwh is None):
                    any_with_unspecified=True                                       # not really perfomatic but tests aren't supposed to be ran a lot
                    break
        print('Any result with a Unspecified Price: ' + str(any_with_unspecified))

        any_invalid_transaction=False
        for result in results:
            trs = result['transactions']
            for tr in trs:
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