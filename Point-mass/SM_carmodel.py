import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Track details & car data
df = pd.read_csv(r"C:\Users\jgbal\Github\lap-time-simulator\Point-mass\track_coordinates\calculated_radiuses.csv")
df2 = pd.read_csv(r'C:\Users\jgbal\Github\lap-time-simulator\Point-mass\car_data.csv')

# Dropping null value columns out to avoid errors
df2.dropna(inplace = True)

# converting dataframe colums to numeric to avoid errors
df['cx'] = pd.to_numeric(df['cx'], downcast= 'float')
df['cy'] = pd.to_numeric(df['cy'], downcast= 'float')
df['Corner Radius'] = pd.to_numeric(df['Corner Radius'], downcast= 'float')
g_lat = pd.to_numeric(df2.iloc[2,1], downcast='float')

# Giving the columns variable names to simplify
cx = df['cx']
cy = df['cy']
tr = df['Corner Radius']

# converting from array to series
cx = pd.Series(data = cx)
cy = pd.Series(data = cy)
tr = pd.Series(data = tr)

# Simple corner velocity (centripetal) V = (g_lat * 9,81 * Radius) ^ 1/2 
corner_velocity = np.sqrt(g_lat * tr * 9.81)

# In few moments we will need to create x columns for each local minima
# Converting Radiuses in arrays so they can be used in local minima function
# z = np.array(df['Corner Radius'])
# finding local minima
# K = np.r_[True, z[1:] < z[:-1]] & np.r_[z[:-1] < z[1:], True]

start = 6
finish = start - 2
corner_speed = []

df['speed turn 1'] = np.nan
df.at[start,'speed turn 1'] = np.sqrt(g_lat * df.at[start, 'Corner Radius'] * 9.81)


corner_speed_rolled = np.roll(df['speed turn 1'],-start)
cx_rolled = np.roll(cx, -start)
cy_rolled = np.roll(cy, -start)


for index in range(0, cx.size):
    cx_bfr = cx_rolled.iat[index - 1]
    cx_act = cx_rolled.iat[index]
    
    cy_bfr = cy_rolled.iat[index -1]
    cy_act = cy_rolled.iat[index]

    index = np.sqrt(
        index ** 2 + 2 * g_lat * np.sqrt((cx_act - cx_bfr)**2+(cy_act - cy_bfr)**2)
    )

    corner_speed.append(index)


corner_speed_unrolled = np.roll(df['speed turn 1'],start)
cx_unrolled = np.roll(cx, start)
cy_unrolled = np.roll(cy, start)

  

df.to_csv(r'C:\Users\jgbal\Github\lap-time-simulator\Point-mass\outing.csv')