import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\jgbal\\Github\\lap-time-simulator\\Point-mass\\track_coordinates\\Sample_track.csv", sep = ';', low_memory = False)

# To add new columns df['New column'] = 'values'

# to find a row (string) df.iloc[x]
# to find a row's value (string) df.iat[x,y]


# finding 3 distances between three generic points in the space

a_two = np.sqrt(
    (int(df.iat[2,0]) - int(df.iat[0,0]))**2 + 
    (int(df.iat[2,1]) - int(df.iat[0,1]))**2
    )

b_two = np.sqrt(
    (int(df.iat[2,0]) - int(df.iat[1,0]))**2 + 
    (int(df.iat[2,1]) - int(df.iat[1,1]))**2
    )

c_two = np.sqrt(
    (int(df.iat[1,0]) - int(df.iat[0,0]))**2 + 
    (int(df.iat[1,1]) - int(df.iat[0,1]))**2
    )

# finding the angle created by these three points, with an generic center

cos_A = (
    (b_two ** 2 + c_two ** 2 - a_two ** 2) /
    (2 * b_two * c_two)
    )

A_rad = np.arccos(cos_A)

A_deg = A_rad * 180 / np.pi

# finally, the radius
def turn_radius (n, d):
    if d ==0: return 0
    return n/d




df['Corner Radius'] = 'Value'

df.at[1,'Corner Radius'] = turn_radius(a_two, (2 * np.sin(np.pi - A_rad)))

print(df.head())