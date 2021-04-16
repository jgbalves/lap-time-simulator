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

def compare(car_1, car_2, car_3):

    ## Plotting    
    fig, speed_plot = plt.subplots()
    speed_plot.plot(car_1.distance, car_1.speed_kph, car_1.distance, car_2.speed_kph, car_1.distance, car_3.speed_kph)

    plt.show()

car_1 = Car_outing('car_data_1_turn_radius_outing.csv')
car_2 = Car_outing('car_data_2_turn_radius_outing.csv')
car_3 = Car_outing('car_data_3_turn_radius_outing.csv')

compare(car_1, car_2, car_3)