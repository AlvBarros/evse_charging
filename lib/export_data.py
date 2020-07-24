import json
import datetime as datetime

import os,sys,inspect

def exportModels(objs):
    now = datetime.datetime.now()

    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    current_dir = current_dir.split('\\evse_charging')[0]+'\\evse_charging'
    exports_dir = current_dir + '\\exports'
    if (not os.path.exists(exports_dir)):
        os.makedirs(exports_dir)

    file_name = f'EVSE_CHARGING_{now.year:04d}_{now.month:02d}_{now.day:02d}_{now.hour:02d}_{now.minute:02d}_{now.second:02d}'
    paths = [os.path.join(exports_dir, f'{file_name}.json'), os.path.join(exports_dir, f'{file_name}.csv')]

    with open(paths[0], 'w') as outfile:
        json.dump(objs, outfile)

    with open(paths[1], 'a') as outfile:
        outfile.write("fee_price;time_price;kwh_price;total_price;session_id;supplier_price_id\n")
        for obj in objs:
            outfile.write(f"{obj['fee_price']};{obj['time_price']};{obj['kwh_price']};{obj['total_price']};{obj['session_id']};{obj['supplier_price_id']}\n")
    return paths