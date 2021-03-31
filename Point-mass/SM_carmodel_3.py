## ==============================================================================
## 
##   _____ ____  ________________     __  ___________________  _____________ 
##  / ___// __ \/ ____/ ____/ __ \   /  |/  / ____/_  __/ __ \/  _/ ____/   |
##  \__ \/ /_/ / __/ / __/ / / / /  / /|_/ / __/   / / / /_/ // // /   / /| |
## ___/ / ____/ /___/ /___/ /_/ /  / /  / / /___  / / / _, _// // /___/ ___ |
##/____/_/   /_____/_____/_____/  /_/  /_/_____/ /_/ /_/ |_/___/\____/_/  |_|
##                                                                        
##                           www.speedmetrica.com
##
## ==============================================================================
## Point mass lap time simulator, going through a curvature section

## Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

class Car():
    def __init__(self, csv_name):
        car_data_path = Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', csv_name)
        self.csv_name = csv_name

        car_df = pd.read_csv(car_data_path)
        car_df.dropna(inplace = True)

        self.g_lat = pd.to_numeric(car_df.iloc[3,1], downcast='float')
        self.tranny_efc = pd.to_numeric(car_df.iloc[5,1], downcast='float') / 100
        self.power = pd.to_numeric(car_df.iloc[4,1], downcast='float') * 745.7 * self.tranny_efc
        self.air_density =  pd.to_numeric(car_df.iloc[6,1], downcast='float')
        self.frontal_area = pd.to_numeric(car_df.iloc[1,1], downcast='float')
        self.drag_coef = pd.to_numeric(car_df.iloc[2,1], downcast='float')
        self.car_mass = pd.to_numeric(car_df.iloc[0,1], downcast='float')

class Track():
    def __init__(self, csv_name):
        track_details_path = Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', 'track_coordinates', csv_name)
        self.csv_name = csv_name

        speeds_df = pd.read_csv(track_details_path)
        self.distance_m = pd.to_numeric(speeds_df['Distance'], downcast= 'float')
        self.turn_radius= pd.to_numeric(speeds_df['Turn Radius'], downcast= 'float')

        ## Finding apexes (local minima of radiuses)
        # Converting Radiuses in arrays so they can be used in local minima function
        self.turn_radius = np.array(self.turn_radius)
        # finding local minima (turn apex)
        K = np.r_[True, self.turn_radius[1:] < self.turn_radius[:-1]] & np.r_[self.turn_radius[:-1] < self.turn_radius[1:], True]
        # Taking note of apex positions
        self.apexes = [i for i, x in enumerate(K) if x]
        


def simulate(car:Car, track:Track):
    ## Calculating velocities at apex, then accelerating and braking from them
    # Taking note of turn names
    corner_names = []
    speeds_df = pd.DataFrame(data={'dummy_col': [0] * track.distance_m.size})
    for start in track.apexes:
        # Simple corner velocity (centripetal): V = (g_lat * 9,81 * Radius) ^ 1/2 
        speed_apex = np.sqrt(car.g_lat * 9.81 * track.turn_radius[start])

        ## Accelerating Section
        # Organizing the accelerations in columns
        speeds_df.at[start, f'Accel {start}'] = speed_apex
        corner_speed = speeds_df[f'Accel {start}']
        corner_names.append(f'Accel {start}')

        #accelerating from apex: V = sqrt(Vo² + 2*dx/m * (Power/Vo - drag))
        for index in range(start + 1, track.distance_m.size):

            dx = track.distance_m[index] - track.distance_m[index - 1]
            speed_bfr = corner_speed.iat[index - 1]
            car_drag = car.drag_coef * car.air_density * speed_bfr ** 2 * car.frontal_area / 2
            corner_speed.at[index] = np.sqrt(
                speed_bfr ** 2 + 2 * dx / car.car_mass * (car.power/speed_bfr - car_drag)
                )

        for index in range(0, start):

            dx = track.distance_m[index] - track.distance_m[index - 1]
            speed_bfr = corner_speed.iat[index - 1]
            car_drag = car.drag_coef * car.air_density * speed_bfr ** 2 * car.frontal_area / 2
            corner_speed.at[index] = np.sqrt(
                speed_bfr ** 2 + 2 * dx / car.car_mass * (car.power/speed_bfr - car_drag)
                )

        ## Braking Section

        # Organizing the decelerations in columns
        speeds_df.at[start, f'Decel {start}'] = speed_apex
        corner_speed = speeds_df[f'Decel {start}']
        corner_names.append(f'Decel {start}')

        #Decelerating from apex: V = sqrt(Vo² - 2 * dx (mi * g + drag / m))
        for index in range(start -1, -1, -1):
            dx = track.distance_m[index] - track.distance_m[(index + 1)%track.distance_m.size]
            speed_nxt = corner_speed.iat[(index + 1)%track.distance_m.size]
            car_drag = car.drag_coef * car.air_density * speed_nxt ** 2 * car.frontal_area / 2
            corner_speed.at[index] = np.sqrt(speed_nxt**2 - 2 * dx * (car.g_lat * 9.81 + car_drag/car.car_mass))

        for index in range(track.distance_m.size - 1, start, -1):
            dx = track.distance_m[index] - track.distance_m[(index + 1)%track.distance_m.size]
            speed_nxt = corner_speed.iat[(index + 1)%track.distance_m.size]
            car_drag = car.drag_coef * car.air_density * speed_nxt ** 2 * car.frontal_area / 2
            corner_speed.at[index] = np.sqrt(speed_nxt**2 - 2 * dx * (car.g_lat * 9.81 + car_drag/car.car_mass))    

        #calculating the distance steps
        for index in range(1, track.distance_m.size):
            dx = track.distance_m[index] - track.distance_m[(index - 1)]
            speeds_df.at[0, 'dx'] = 0.0
            speeds_df.at[index, 'dx'] = dx

        ## lap time
        # getting the minimum speed of all columns (turns) and creating just one column
        speeds_df['speed'] = speeds_df[corner_names].min(axis = 1)
        speeds_df['speed (km/h)'] = speeds_df['speed'] * 3.6
        speeds_df['t(s)'] = speeds_df['dx'] / speeds_df['speed']

        export_df = speeds_df[['speed', 'speed (km/h)', 'dx', 't(s)']]
        return export_df.to_csv(Path(Path.home(), 'Github', 'lap-time-simulator', 'Point-mass', f'{car.csv_name}_outing.csv'))

car = Car('car_data.csv')
track = Track('turn_radius.csv')

simulate(car,track)
# import ipdb; ipdb.set_trace()