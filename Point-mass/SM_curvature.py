# # ==============================================================================
# #
# #   _____ ____  ________________     __  ___________________  _____________
# #  / ___// __ \/ ____/ ____/ __ \   /  |/  / ____/_  __/ __ \/  _/ ____/   |
# #  \__ \/ /_/ / __/ / __/ / / / /  / /|_/ / __/   / / / /_/ // // /   / /| |
# # ___/ / ____/ /___/ /___/ /_/ /  / /  / / /___  / / / _, _// // /___/ ___ |
# #/____/_/   /_____/_____/_____/  /_/  /_/_____/ /_/ /_/ |_/___/\____/_/  |_|
# #
# #                           www.speedmetrica.com
# #
# # ==============================================================================
# # Calculating curvature from longitudinal speed and accelerations


# # Importing libraries
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


# # Building the dataframe

# choosing file
source_file = Path(Path.home(), 'Github', 'lap-time-simulator', 'Point-mass', 'motec_exports', 'Interlagos_Ohira.csv')  # Import data as table
source_df = pd.read_csv(source_file, sep=',', low_memory=False, skiprows=13)    # Creating Table

# Dropping null value columns out to avoid errors
source_df.dropna(inplace = True)    # Excluding null values

# # Choosing columns to calculate the necessary values

# converting dataframe colums to numeric to avoid errors
source_df['G Force Lat'] = pd.to_numeric(source_df['G Force Lat'], downcast='float')
source_df['Corr Speed'] = pd.to_numeric(source_df['Corr Speed'], downcast='float')
source_df['Distance'] = pd.to_numeric(source_df['Distance'], downcast='float')

g_lat = source_df['G Force Lat']
g_lat_ms2 = source_df['G Force Lat'] * 9.81
speed_ms = source_df['Corr Speed'] / 3.6
distance_m = source_df['Distance']

# Filtering the lat acceleration
fs = 50    # Sampling frequency, according to the source_file sampling frequency
fc = 1    # Cutoff frequency, lower values filter more
w = fc / (fs / 2)   # Normalized frequency
b, a = signal.butter(5, w, 'low')    # Appliying a Butterworth filter (order, critical freq, filter type)
filtered_g_lat_ms2 = signal.filtfilt(b, a, g_lat_ms2)

# # Creating the radius signal
turn_radius = speed_ms ** 2 / filtered_g_lat_ms2
turn_radius_norm = np.sqrt(turn_radius ** 2)

# # Output
# Output dataframe
output_df = pd.DataFrame(data={'Distance':distance_m, 'Turn Radius': turn_radius_norm})


# Exporting it
output_path = Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', 'track_coordinates', 'turn_radius.csv')
output_df.to_csv(output_path)


# # Plots
fig, ax = plt.subplots(3)
fig.suptitle('Turn Radius Profile')

# first plot - Lateral Acceleration raw vs filtered
ax[0].plot(distance_m, g_lat_ms2, 'r', Label = 'raw (m)')
ax[0].plot(distance_m, filtered_g_lat_ms2, 'b', Label='filtered (m)')
ax[0].set_title('Lat Accel raw vs filtered')

# second plot - Turn Radius
ax[1].plot(distance_m, turn_radius, 'r', Label='raw (m)')
ax[1].set_title('Turn Radius')
ax[1].set_ylim([-200, 200])    # putting limit on the y axis

# third plot - Curvature
ax[2].plot(distance_m, turn_radius_norm, 'r', Label='raw (m)')
ax[2].set_title('Curvature')
ax[2].set_ylim([0, 200])    # Putting limit on the y axis

fig.tight_layout(pad=1.0)    # Spacing, so plot titles don't go over each other

plt.show()
