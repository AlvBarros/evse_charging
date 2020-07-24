# all steps: Import, clean up the data, calculate prices and
# finally export the models either to CSV or JSON file

import lib.import_data as importer
import lib.clean_data as cleaner
import lib.calculate_prices as calculator

def importSupplierPricesData():
    return importer.importSupplierPricesData()

def cleanSupplierPricesData(data):
    return cleaner.cleanSupplierPricesData(data)

def calculatePrices(clean_data):
    return calculator.calculatePricesFromCleanData(clean_data)

def exportModels():
    pass