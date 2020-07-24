from lib.business.supplierPrice import SupplierPrice
from lib.business.charge import Charge

def cleanSupplierPricesData(data):
    print('Initializing data cleaning')
    supplier_prices = data['supplier_prices']

    # Initialize empty list
    clean_supplier_prices = []

    # Set numeric values for logging purposes
    total=len(supplier_prices)          # Total number o supplier prices
    n_unsp=0                            # Number of unspecified
    n_fee=0                             # Number of Fee
    n_time_c=0                          # Number of Complex Time Price
    n_time_s=0                          # Number of Simple Time Price
    n_kwh_c=0                           # Number of Complex kWh Price
    n_kwh_s=0                           # Number of Simple kWh Price

    # Clean one by one
    for sp in supplier_prices:
        # Observation: A Supplier Price can charge in all three categories, 
        # Fee, Time and kWh. So, you could receive Supplier Prices with all 
        # attributes, but you CAN’T have a simple and complex field from the same category.

        # Instanciate a SupplierPrice object (which creates each category as its properties)
        s=SupplierPrice(sp)

        # If no category has been found, add one to the unspecified count
        # PS: This value must be 0!!
        if (s.fee is None and s.time is None and s.kwh is None):
            n_unsp = n_unsp + 1
        else:
            # Add one to the fee count
            if (s.fee is not None):
                n_fee = n_fee + 1

            # Add one to the time count (simple or complex)
            if (s.time is not None):
                if (s.time.complexity == 'complex'):
                    n_time_c = n_time_c + 1
                elif (s.time.complexity == 'simple'):
                    n_time_s = n_time_s + 1

            # Add one to the kWh count (simple or complex)
            if (s.kwh is not None):
                if (s.kwh.complexity == 'complex'):
                    n_kwh_c = n_kwh_c + 1
                elif (s.kwh.complexity == 'simple'):
                    n_kwh_s = n_kwh_s + 1
        
        # If has any of the three categories (which every one should) add it to the list
        if (s.fee is not None or s.time is not None or s.kwh is not None):
            clean_supplier_prices.append(s)

    # Log its numbers and percentages
    print('===================== Supplier Prices ('+str(total)+') =====================')
    print('    Unspecified: ' + str(n_unsp) + '(' + str(round(n_unsp/total*100, 1)) + '%)')
    print('    Fee: ' + str(n_fee) + '(' + str(round(n_fee/total*100, 1)) + '%)')
    print('    Time: ' + str(n_time_s+n_time_c) + '(' + str(round((n_time_s + n_time_c)/total*100, 1)) + '%)')
    print('        Simple: ' + str(n_time_s) + '(' + str(round(n_time_s/(n_time_s+n_time_c)*100, 1)) + '%)    Complex: ' + str(n_time_c) + '(' + str(round(n_time_c/(n_time_s+n_time_c)*100, 1)) + '%)')
    print('    kWh: ' + str(n_kwh_s+n_kwh_c) + '(' + str(round(n_kwh_s+n_kwh_c/total*100, 1)) + '%)')
    print('        Simple: ' + str(n_kwh_s) + '(' + str(round(n_kwh_s/(n_kwh_s+n_kwh_c)*100, 1)) + '%)    Complex: ' + str(n_kwh_c) + '(' + str(round(n_kwh_c/(n_kwh_s+n_kwh_c)*100, 1)) + '%)')
    print('=================================================================\n')

    transactions = data['transactions']
    # Initialize empty list
    clean_transactions = []
    print('Transactions count: ' + str(len(transactions)))
    # Clean one by one
    for tr in transactions:
        # Instanciate a Charge object
        t=Charge(tr)
        clean_transactions.append(t)
    
    # Dictionary result
    return {'supplier_prices': clean_supplier_prices, 'transactions': clean_transactions}