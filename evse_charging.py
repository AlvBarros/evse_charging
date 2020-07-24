# all steps: Import, clean up the data, calculate prices and
# finally export the models either to CSV or JSON file

import lib.import_data as importer
import lib.clean_data as cleaner

def importSupplierPricesData():
    return importer.importSupplierPricesData()

def cleanSupplierPricesData(data):
    return cleaner.cleanSupplierPricesData(data)

def calculatePrices():
    pass

def exportModels():
    pass