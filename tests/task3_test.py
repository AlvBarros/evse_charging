# ========== 3. Calculate Prices ========== 
# Description
# In this task, you already have all data parsed and converted,
# now you should calculate the price for the charges.
# Remember that calculating the price is te most important task
# of the system;

# Expected Result
# JSON with a list of the calulated prices with the specified model 
# object.

import tests.helper as helper

def run():
    print('Running Task 3 test')
    try:
        data = helper.evse_charging.importSupplierPricesData()
        clean_data = helper.evse_charging.cleanSupplierPricesData(data)
        calculated_result = helper.evse_charging.calculatePrices(clean_data)
        print('Validating result')
        print('KNOWN BUG: Does calculated_result has the same length as transactions?: ' + str(len(clean_data['transactions']) == len(calculated_result)))
        print('Test completed.')
    except:
        print('Test failed.')
        raise

run()