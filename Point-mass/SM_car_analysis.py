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
# # Plotting vehicle speeds to compare the results

# # Importing libraries
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


class CarOuting:
    def __init__(self, csv_name):
        self.csv_name = csv_name
        car_data_path = Path(Path.home(), 'Github', 'lap-time-simulator', 'Point-mass', 'car_data', f'{csv_name[0:10]}'+'.csv')
        car_outing_path = Path(Path.home(), 'Github', 'lap-time-simulator', 'Point-mass', 'outings', csv_name)
        car_outing_df = pd.read_csv(car_outing_path)
        self.speed_kph = car_outing_df['speed (km/h)']
        self.distance = car_outing_df['Distance']
        self.time = car_outing_df['t(s)']
        self.car_data_df = pd.read_csv(car_data_path)
        self.car_data_property = self.car_data_df['car data']
        self.car_data_value = self.car_data_df['value']
        self.car_data_unit = self.car_data_df['unit']


def compare(car_1, car_2, car_3):

    # # Plotting
    # Defining the lap time stamps to be printed
    lap_time_1 = car_1.time.sum()
    lap_time_2 = car_2.time.sum()
    lap_time_3 = car_3.time.sum()
    lt_minutes_1 = lap_time_1//60
    lt_seconds_1 = lap_time_1 % 60
    lt_minutes_2 = lap_time_2//60
    lt_seconds_2 = lap_time_2 % 60
    lt_minutes_3 = lap_time_3//60
    lt_seconds_3 = lap_time_3 % 60

    # Defining image
    fig, speed_plot = plt.subplots(2, 1)  # speeds on top, car data at bottom

    # The 3 speed signals of the first plot
    car_signal_speed1, = speed_plot[0].plot(car_1.distance, car_1.speed_kph, 'b')
    car_signal_speed2, = speed_plot[0].plot(car_1.distance, car_2.speed_kph, 'g')
    car_signal_speed3, = speed_plot[0].plot(car_1.distance, car_3.speed_kph, 'r')

    # Time stamp (transforming sss,ss into mm:ss,sss)
    
    lap_time_1 = f'{lt_minutes_1:.0f}:{lt_seconds_1:.2f}'
    lap_time_2 = f'{lt_minutes_2:.0f}:{lt_seconds_2:.2f}'
    lap_time_3 = f'{lt_minutes_3:.0f}:{lt_seconds_3:.2f}'

    # car_signal_speed1.set_label(f'{car_1}, {lap_time_1}')
    car_signal_speed1.set_label(f'Car_1, {lap_time_1}')
    car_signal_speed2.set_label(f'Car_2, {lap_time_2}')
    car_signal_speed3.set_label(f'Car_3, {lap_time_3}')

    # Legend with colors and lap time
    speed_plot[0].legend()

    # Organizing the car data from the 3 cars to the second plot
    s0 = pd.Series(car_1.car_data_property, name='Car Properties')
    s1 = pd.Series(car_1.car_data_value, name='Car_1')
    s2 = pd.Series(car_2.car_data_value, name='Car_2')
    s3 = pd.Series(car_3.car_data_value, name='Car_3')
    s4 = pd.Series(car_1.car_data_unit, name='Value Units')
    table = pd.concat([s0, s1, s2, s3, s4], axis=1)
    cell_text = []  # Creating a dict to be used as text in the car data table
    for row in range(0, len(table)):
        cell_text.append(table.iloc[row])  # Populating the dict

    # Plotting the table
    speed_plot[1].axis('off')  # hiding the plot so just the table exhibits
    speed_plot[1].table(cellText=cell_text, colLabels=table.columns, loc='center')  # Table

    plt.show()

