import json
import datetime as datetime

import os,sys,inspect

# objs is the Dictionary that is supposed to be exported
def exportModels(objs):
    now = datetime.datetime.now()

    # Gets the current directory that the script is running
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    # Gets the root directory of the project
    current_dir = current_dir.split('\\evse_charging')[0]+'\\evse_charging'
    # Adds /exports folder
    exports_dir = current_dir + '\\exports'
    # Create folder if it does not exists
    if (not os.path.exists(exports_dir)):
        os.makedirs(exports_dir)
    # Sets the file name based on time the script is being run
    file_name = f'EVSE_CHARGING_{now.year:04d}_{now.month:02d}_{now.day:02d}_{now.hour:02d}_{now.minute:02d}_{now.second:02d}'
    # Sets both the paths of .json and .csv files
    paths = [os.path.join(exports_dir, f'{file_name}.json'), os.path.join(exports_dir, f'{file_name}.csv')]
    # Writes whole JSON to .json file
    with open(paths[0], 'w') as outfile:
        json.dump(objs, outfile)
    # Writes line by line to .csv file
    with open(paths[1], 'a') as outfile:
        outfile.write("fee_price;time_price;kwh_price;total_price;session_id;supplier_price_id\n")
        for obj in objs:
            outfile.write(f"{obj['fee_price']};{obj['time_price']};{obj['kwh_price']};{obj['total_price']};{obj['session_id']};{obj['supplier_price_id']}\n")
    # Return file names
    return paths