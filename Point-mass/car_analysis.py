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
        pass

def print(car_1, car_2, car_3):
    
    pass

car_1 = Car_outing()
car_2 = Car_outing()
car_3 = Car_outing()


print()