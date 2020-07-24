import import_data as importer
from business.supplierPrice import SupplierPrice

def cleanSupplierPricesData(data):
    print('Initializing data cleaning')
    supplier_prices = data['supplier_prices']
    clean_supplier_prices = []
    total=len(supplier_prices)         # Total number o supplier prices
    print('Suppliers count: ' + str(total))
    n_unsp=0        # Number of unspecified
    n_fee=0         # Number of Fee
    n_time_c=0      # Number of Complex Time Price supplier
    n_time_s=0      # Number of Simple Time Price supplier
    n_kwh_c=0       # Number of Complex kWh Price supplier
    n_kwh_s=0       # Number of Simple kWh Price supplier
    for sp in supplier_prices:
        # Observation: A Supplier Price can charge in all three categories, 
        # Fee, Time and kWh. So, you could receive Supplier Prices with all 
        # attributes, but you CAN’T have a simple and complex field from the same category.
        s=SupplierPrice(sp)
        if (s.type == 'unspecified'):
            n_unsp = n_unsp + 1

        elif (s.type == 'fee'):
            n_fee = n_fee + 1

        elif (s.type == 'time'):
            if (s.complexity == 'complex'):
                n_time_c = n_time_c + 1
            elif (s.complexity == 'simple'):
                n_time_s = n_time_s + 1

        elif (s.type == 'kwh'):
            if (s.complexity == 'complex'):
                n_kwh_c = n_kwh_c + 1
            elif (s.complexity == 'simple'):
                n_kwh_s = n_kwh_s + 1
        
        if (s.type != 'unspecified'):
            clean_supplier_prices.append(s)

    print('Results:')
    print('    Unspecified: ' + str(n_unsp) + '(' + str(round(n_unsp/total*100, 1)) + '%)')
    print('    Fee: ' + str(n_fee) + '(' + str(round(n_fee/total*100, 1)) + '%)')
    print('    Time: ' + str(n_time_s+n_time_c) + '(' + str(round((n_time_s + n_time_c)/total*100, 1)) + '%)')
    print('        Simple: ' + str(n_time_s) + '(' + str(round(n_time_s/(n_time_s+n_time_c)*100, 1)) + '%)    Complex: ' + str(n_time_c) + '(' + str(round(n_time_c/(n_time_s+n_time_c)*100, 1)) + '%)')
    print('    kWh: ' + str(n_kwh_s+n_kwh_c) + '(' + str(round(n_kwh_s+n_kwh_c/total*100, 1)) + '%)')
    print('        Simple: ' + str(n_kwh_s) + '(' + str(round(n_kwh_s/(n_kwh_s+n_kwh_c)*100, 1)) + '%)    Complex: ' + str(n_kwh_c) + '(' + str(round(n_kwh_c/(n_kwh_s+n_kwh_c)*100, 1)) + '%)')
    # transactions = data['transactions']
    # clean_transactions = []
    # print('Transactions count: ' + str(len(transactions)))
    # for (tr in transactions):
    #     pass


cleanSupplierPricesData(importer.importSupplierPricesData())