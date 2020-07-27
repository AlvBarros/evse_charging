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

import os,sys,inspect

def run():
    print('Running Task 4 test')
    try:
        export_result_files = helper.evse_charging.importAndExportData()
        print('Validating result')
        # Gets the current directory that the script is running
        current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        # Gets the root directory of the project
        if (current_dir.find('\\') > -1):
            # Windows 
            dir_separator = '\\'
        elif (current_dir.find('/') > -1):
            # MacOS
            dir_separator = '/'
        else:
            raise 'No dir separator found'
        current_dir = current_dir.split(f'{dir_separator}evse_charging')[0]+f'{dir_separator}evse_charging'
        # Adds exports folder
        exports_dir = current_dir + f'{dir_separator}exports'
        # Check if folder does not exists
        if (not os.path.exists(exports_dir)):
            raise "Exports folder couldn't be created"
        # Check if files do not exist
        if (not os.path.exists(f'{export_result_files[0]}')):
            raise "JSON file couldn't be created"
        elif (not os.path.exists(f'{export_result_files[1]}')):
            raise "CSV file couldn't be created"
        else:
            print('Export files successfully created')
        print('Test completed.')
    except:
        print('Test failed.')
        raise

run()