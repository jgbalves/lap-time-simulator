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
## Plotting vehicle speeds to compare the results


## Importing libraries
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


class Car_outing():
    def __init__(self, csv_name):
        self.csv_name = csv_name
        car_data_path = Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', csv_name)
        car_df = pd.read_csv(car_data_path)
        self.speed_kph = car_df['speed (km/h)']
        self.distance = car_df['Distance']
        self.time = car_df['t(s)']

def compare(car_1, car_2, car_3):

    ## Plotting    
    # Plot image
    fig, speed_plot = plt.subplots()
    speed_plot.plot(car_1.distance, car_1.speed_kph, 'b')
    speed_plot.plot(car_1.distance, car_2.speed_kph, 'g')
    speed_plot.plot(car_1.distance, car_3.speed_kph, 'r')

    # Time stamp
    lap_time_1 = car_1.time.sum()
    lap_time_2 = car_2.time.sum()
    lap_time_3 = car_3.time.sum()
    lt_minutes_1 = lap_time_1//60
    lt_seconds_1 = lap_time_1 % 60
    lt_minutes_2 = lap_time_2//60
    lt_seconds_2 = lap_time_2 % 60
    lt_minutes_3 = lap_time_3//60
    lt_seconds_3 = lap_time_3 % 60
    
    fig.text(0.7, 0.3, f'{lt_minutes_1:.0f}:{lt_seconds_1:.2f}', bbox=dict(facecolor='black', alpha=0.5))
    fig.text(0.7, 0.4, f'{lt_minutes_2:.0f}:{lt_seconds_2:.2f}', bbox=dict(facecolor='green', alpha=0.5))
    fig.text(0.7, 0.5, f'{lt_minutes_3:.0f}:{lt_seconds_3:.2f}', bbox=dict(facecolor='red', alpha=0.5))

    plt.show()

car_1 = Car_outing('car_data_1_turn_radius_outing.csv')
car_2 = Car_outing('car_data_2_turn_radius_outing.csv')
car_3 = Car_outing('car_data_3_turn_radius_outing.csv')

compare(car_1, car_2, car_3)