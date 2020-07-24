import lib.import_data as importer
import lib.clean_data as cleaner
import lib.calculate_prices as calculator
import lib.export_data as exporter

def importSupplierPricesData():
    return importer.importSupplierPricesData()

def cleanSupplierPricesData(data):
    return cleaner.cleanSupplierPricesData(data)

def calculatePrices(clean_data):
    return calculator.calculatePricesFromCleanData(clean_data)

def exportModels(calculatedPrices):
    return exporter.exportModels(calculatedPrices)

# all steps: Import, clean up the data, calculate prices and
# finally export the models either to CSV or JSON file
def importAndExportData():
    data = importSupplierPricesData()
    cleaned_data = cleanSupplierPricesData(data)
    calculated_prices = calculatePrices(cleaned_data)
    paths = exportModels(calculated_prices)
    print('Files have been created:')
    for p in paths:
        print(p)