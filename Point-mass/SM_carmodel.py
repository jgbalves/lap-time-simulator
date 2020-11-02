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


cx = df['cx']
cy = df['cy']
tr = df['Corner Radius']

# converting from array to series

cx = pd.Series(data = cx)
cy = pd.Series(data = cy)
tr = pd.Series(data = tr)

corner_velocity = np.sqrt(g_lat * tr * 9.81)

df['speed turn 1'] = corner_velocity

# Converting Radiuses in arrays so they can be used in another function
# z = np.array(df['Corner Radius'])

# def corner_velocity (acc, R):
#    if R == np.inf: return np.nan
#    return np.sqrt(acc * R)

# df['veloc'] = df.apply(corner_velocity(g_lat, R), axis = 1)

# finding local minima
# K = np.r_[True, z[1:] < z[:-1]] & np.r_[z[:-1] < z[1:], True]

df.to_csv(r'C:\Users\jgbal\Github\lap-time-simulator\Point-mass\outing.csv')