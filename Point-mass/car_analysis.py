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

# # Importing libraries
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import ipdb


class CarOuting:
    def __init__(self, csv_name):
        self.csv_name = csv_name
        car_data_path = Path(Path.home(), 'Github', 'lap-time-simulator', 'Point-mass', 'car_data', f'{csv_name[0:10]}'+'.csv')
        car_outing_path = Path(Path.home(), 'Github', 'lap-time-simulator', 'Point-mass', 'outings', csv_name)
        car_outing_df = pd.read_csv(car_outing_path)
        self.speed_kph = car_outing_df['speed (km/h)']
        self.distance = car_outing_df['Distance']
        self.time = car_outing_df['t(s)']
        car_data_df = pd.read_csv(car_data_path)
        self.car_data = car_data_df['value']


def compare(car_1, car_2, car_3):

    # # Plotting
    # Plot image

    fig, speed_plot = plt.subplots(2, 1)  # speeds on top, car data at bottom
    # The 3 speed signals
    car_signal_speed1, = speed_plot[0].plot(car_1.distance, car_1.speed_kph, 'b')
    car_signal_speed2, = speed_plot[0].plot(car_1.distance, car_2.speed_kph, 'g')
    car_signal_speed3, = speed_plot[0].plot(car_1.distance, car_3.speed_kph, 'r')

    # Time stamp (dividing the XXXs into mm:ss,sss)
    lap_time_1 = car_1.time.sum()
    lap_time_2 = car_2.time.sum()
    lap_time_3 = car_3.time.sum()
    lt_minutes_1 = lap_time_1//60
    lt_seconds_1 = lap_time_1 % 60
    lt_minutes_2 = lap_time_2//60
    lt_seconds_2 = lap_time_2 % 60
    lt_minutes_3 = lap_time_3//60
    lt_seconds_3 = lap_time_3 % 60
    
    lap_time_1 = f'{lt_minutes_1:.0f}:{lt_seconds_1:.2f}'
    lap_time_2 = f'{lt_minutes_2:.0f}:{lt_seconds_2:.2f}'
    lap_time_3 = f'{lt_minutes_3:.0f}:{lt_seconds_3:.2f}'

    # car_signal_speed1.set_label(f'{car_1}, {lap_time_1}')
    car_signal_speed1.set_label(f'Car_1, {lap_time_1}')
    car_signal_speed2.set_label(f'Car_2, {lap_time_2}')
    car_signal_speed3.set_label(f'Car_3, {lap_time_3}')

    speed_plot[0].legend()

    df = pd.DataFrame(car_1.car_data)
    # ipdb.set_trace()
    collabel = ("car_1", "car_2", "car_3")
    # car_data = speed_plot[1].table(cellText=clust_data_1, colLabels=collabel, loc='center')
    # pd.plotting.table(speed_plot[1], clust_data_1, loc="upper right")
    speed_plot[1].(df.plot(table=True))


    plt.show()


car_1 = CarOuting('car_data_1_turn_radius_outing.csv')
car_2 = CarOuting('car_data_2_turn_radius_outing.csv')
car_3 = CarOuting('car_data_3_turn_radius_outing.csv')

compare(car_1, car_2, car_3)
