#pip3 install fitparse

import fitparse 
import pandas as pd
# Load the FIT file
fitfile = fitparse.FitFile('activity.fit')

# Iterate over all messages of type "record"
# (other types include "device_info", "file_creator", "event", etc)

df = pd.DataFrame()
for record in fitfile.get_messages('record'):
    # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
    d = {}
    units = {}
    for data in record:
        d[data.name] = data.value
        units[data.name] = data.units
        
    df = df.append(d, ignore_index=True)
    
# conversion from semicircles to degrees
df['longtitude'] = df['position_long'].apply(lambda x:x * ( 180.0 / 2**31 ))
df['latitude'] = df['position_lat'].apply(lambda x:x * ( 180.0 / 2**31 ))
df.set_index(timestamp',inplace=True)
print(f'dataframe size:\t{df.shape}')
#print(units)

print('creating csv...')
df.to_csv("activity.csv")
