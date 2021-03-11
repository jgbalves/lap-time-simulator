import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


## Track details & car data
track_details_path = Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', 'track_coordinates', 'turn_radius.csv')
car_data_path = Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', 'car_data.csv')

track_df = pd.read_csv(track_details_path)
car_df = pd.read_csv(car_data_path)

# Dropping null value columns out to avoid errors
car_df.dropna(inplace = True)

# converting dataframe colums to numeric to avoid errors
# Track data
track_df['Turn Radius'] = pd.to_numeric(track_df['Turn Radius'], downcast= 'float')
track_df['Distance']    = pd.to_numeric(track_df['Distance'], downcast= 'float')

# Car data
g_lat = pd.to_numeric(car_df.iloc[3,1], downcast='float')
tranny_efc = pd.to_numeric(car_df.iloc[5,1], downcast='float') / 100
Power = pd.to_numeric(car_df.iloc[4,1], downcast='float') * 745.7 * tranny_efc
air_density =  pd.to_numeric(car_df.iloc[6,1], downcast='float')
frontal_area = pd.to_numeric(car_df.iloc[1,1], downcast='float')
drag_coef = pd.to_numeric(car_df.iloc[2,1], downcast='float')
car_mass = pd.to_numeric(car_df.iloc[0,1], downcast='float')


# Giving the columns variable names to simplify
distance_m  = track_df['Distance']
turn_radius = track_df['Turn Radius']

#adopting apex at index 349
start = 349

# Simple corner velocity (centripetal): V = (g_lat * 9,81 * Radius) ^ 1/2 
speed_apex = np.sqrt(g_lat * 9.81 * track_df.at[start, 'Turn Radius'])
track_df.at[start, f'Accel {start}'] = speed_apex
corner_speed = track_df[f'Accel {start}']


#accelerating from apex: V = sqrt(Vo² + 2*dx/m * (Power/Vo - drag))

for index in range(start + 1, distance_m.size):
    dx = distance_m[index] - distance_m[index - 1]
    speed_bfr = corner_speed.iat[index - 1]
    car_drag = drag_coef * air_density * speed_bfr ** 2 * frontal_area / 2
    track_df.at[index, f'Accel {start}'] = np.sqrt(
        speed_bfr ** 2 + 2 * dx / car_mass * (Power/speed_bfr - car_drag)
        )

for index in range(0, start - 1):
    track_df.at[index, f'Accel {start}'] = np.sqrt(
        speed_bfr ** 2 + 2 * dx / car_mass * (Power/speed_bfr - car_drag)
        )


'''

track_df.to_csv(Path(Path.home(), 'Github', 'lap-time-simulator', 'Point-mass', 'outing_test.csv'))

'''

fig, report_plot = plt.subplots(2)

report_plot[0].plot(corner_speed)

plt.show()