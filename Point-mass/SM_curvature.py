## ==============================================================================
##
##                           www.speedmetrica.com
##
## ==============================================================================
## Calculating curvature from longitudinal speed and accelerations


## Importing libraries
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

## Building the dataframe

# choosing file
source_file = Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', 'motec_exports', 'Interlagos_Ohira.csv')
source_df = pd.read_csv(source_file, sep = ',', low_memory = False, skiprows=13)

# Dropping null value columns out to avoid errors
source_df.dropna(inplace = True)

## Choosing columns to calculate the necessary values

# converting dataframe colums to numeric to avoid errors

source_df['G Force Lat'] = pd.to_numeric(source_df['G Force Lat'], downcast= 'float')
source_df['Corr Speed']  = pd.to_numeric(source_df['Corr Speed'], downcast = 'float')
source_df['Distance']    = pd.to_numeric(source_df['Distance'], downcast = 'float')

g_lat_ms2  = source_df['G Force Lat'] * 9.81
speed_ms   = source_df['Corr Speed'] / 3.6
distance_m = source_df['Distance']

## Creating the radius signal

turn_radius = speed_ms ** 2 / g_lat_ms2

## Plot arranging
fig, ax = plt.subplots(2)
fig.suptitle('Turn Radius Profile')

# first plot

ax[0].plot(distance_m, turn_radius, 'r', Label = 'Turn radius (m)')
ax[0].set_title('Turn Radius / Distance')

#putting limit on the y axis

ax[0].set_ylim([-200, 200]) 

plt.show()

'''
## disposable commands
print(turn_radius)
'''



