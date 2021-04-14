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
## Calculating curvature from longitudinal speed and accelerations


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

def print(car_1, car_2, car_3):
    
    fig, report_plot = plt.subplots(2)
    ## Plotting
    fig, report_plot = plt.subplots(2)

    # First plot (turn radiuses)
    report_plot[0].plot(car_1.distance, turn_radius, 'r')
    report_plot[0].set_ylim([0, 200])

    # Second plot (speed profile)
    report_plot[1].plot(distance_m, speed_profile_kph, 'r')

    # Lap time stamp
    plt.text(1, 1, f'{lt_minutes:.0f}:{lt_seconds:.2f}', bbox=dict(facecolor='white', alpha=0.5))

    plt.show()
    pass

car_1 = Car_outing()
car_2 = Car_outing()
car_3 = Car_outing()


print()