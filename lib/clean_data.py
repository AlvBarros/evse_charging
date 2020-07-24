import import_data as importer
from business.supplierPrice import SupplierPrice

def cleanSupplierPricesData(data):
    print('Initializing data cleaning')
    supplier_prices = data['supplier_prices']
    clean_supplier_prices = []
    print('Suppliers count: ' + str(len(supplier_prices)))
    n_unsp=0
    n_fee=0
    n_time=0
    n_kwh=0
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
            n_time = n_time + 1
        elif (s.type == 'kwh'):
            n_kwh = n_kwh + 1

    print('Results:')
    print('Unspecified: ' + str(n_unsp))
    print('Fee: ' + str(n_fee))
    print('Time: ' + str(n_time))
    print('kWh: ' + str(n_kwh))
    # transactions = data['transactions']
    # clean_transactions = []
    # print('Transactions count: ' + str(len(transactions)))
    # for (tr in transactions):
    #     pass


cleanSupplierPricesData(importer.importSupplierPricesData())