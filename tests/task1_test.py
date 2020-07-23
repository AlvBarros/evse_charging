# ========== 1. Get JSON with Data ========== 
# Description
# In this task, you'll connect to the server and get the 
# base JSON file with all information. [...]

# Expected Result
# The JSON received from the server with the list of the
# supplier_prcies and charges (transactions)

import helper
import json

def run():
    print('Running Task 1 test')
    try:
        result = helper.evse_charging.importSupplierPricesData()
        print('Validating result')
        jsonResult = json.loads(result)
        print('Response result length: ' + str(len(result)))
        print('JSON object length: ' + str(len(jsonResult)))
        has_js = len(result) > 0
        has_sp = 'supplier_prices' in jsonResult
        has_tr = 'transactions' in jsonResult
        print('JSON object has "supplier_prices": ' + str(has_sp))
        print('JSON object has "transactions": ' + str(has_tr))
        print('Test completed.')
    except:
        print('Test failed.')
        raise


# PS: This test should have more cases like forcing a 404 error

run()