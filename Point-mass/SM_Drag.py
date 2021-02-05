import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Track path and car path (track must be a straight line)
track_details_path = Path(Path.home(), 'Github', 'lap-time-simulator', 'Point-mass', 'track_coordinates', 'calculated_radiuses.csv')
car_data_path = Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', 'car_data.csv')

track_df = pd.read_csv(track_details_path)
car_df = pd.read_csv(car_data_path)

# Dropping out null value columns to avoid errors
car_df.dropna(inplace = True)

# Converting dataframe columns to numeric, to avoid errors

#track
track_df['cx'] = pd.to_numeric(track_df['cx'], downcast= 'float')
track_df['cy'] = pd.to_numeric(track_df['cy'], downcast= 'float')

#car
g_lat = pd.to_numeric(car_df.iloc[3,1], downcast='float')
tranny_efc = pd.to_numeric(car_df.iloc[5,1], downcast='float') / 100
Power = pd.to_numeric(car_df.iloc[4,1], downcast='float') * 745.7 * tranny_efc
air_density =  pd.to_numeric(car_df.iloc[6,1], downcast='float')
frontal_area = pd.to_numeric(car_df.iloc[1,1], downcast='float')
drag_coef = pd.to_numeric(car_df.iloc[2,1], downcast='float')
car_mass = pd.to_numeric(car_df.iloc[0,1], downcast='float')

# Passing columns as variables to simplify
cx = track_df['cx']
cy = track_df['cy']

# Converting from array to series
cx = pd.Series(data= cx)
cy = pd.Series(data= cy)

# Counting the distances between each point

dx = []

for index in range(0, cx.size):
    cx_bfr = cx.iat[index -1]
    cx_act = cx.iat[index]

    cy_bfr = cy.iat[index -1]
    cy_act = cy.iat[index]

    dx.append(
        np.sqrt(
            (cx_act - cx_bfr)**2 + (cy_act - cy_bfr)**2
        )
    )

track_df['dx'] = dx
dx = track_df['dx']

# Accelerating

track_df['Velocity'] = 0
velocity = track_df['Velocity']
velocity = pd.Series(data = velocity)

for index in range(1,cx.size):

    spd_bfr = velocity.iat[index -1]
    drag = drag_coef * air_density * spd_bfr ** 2 * frontal_area / 2

    if spd_bfr == 0:
        velocity.at[index] = np.sqrt1(spd_bfr**2 + 2 * dx[index] * g_lat * 9.81)
    else:
        velocity.at[index] = np.sqrt(spd_bfr**2 + 2 * dx[index] * ((Power/spd_bfr) - drag) / car_mass)


print(track_df.head())

# track_df.to_csv(Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', 'outing.csv'))

# Plotting results

# fig, ax = plt.subplots(2)

# fig.suptitle('Results')

# ax[0].plot(velocity, 'r', Label= 'speed (km/h)')

# plt.show()
