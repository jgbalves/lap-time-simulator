import pandas as pd
import numpy as np

# everythimg that have ## is to delete later

# # file = r'C:\Users\jgbal\Github\lap-time-simulator\Point-mass\track_coordinates\Sample_track.csv'

# # def sum1forline(file):
# #    with open(file) as f:
# #        return sum(1 for line in f)

# # csv_size = sum1forline(file)

df = pd.read_csv("C:\\Users\\jgbal\\Github\\lap-time-simulator\\Point-mass\\track_coordinates\\Sample_track.csv", sep = ';', low_memory = False)

# convert column "cx" of a DataFrame
df["cx"] = pd.to_numeric(df["cx"], downcast = 'float')

# convert column "cy" of a DataFrame
df["cy"] = pd.to_numeric(df["cy"], downcast = 'float')

# To add new columns df['New column'] = 'test'
# to find a row (string) print(df.iloc[1])

# finding 3 distances between three generic points in the space

index = 0

a = []
b = []
c = []

cx = df['cx']
cy = df['cy']

for index in range(0, cx.size):

# Locating the indexes of the points used in space (point in question, the point before and the point after)

    cx_bef = cx.iat[index - 1]
    cx_act = cx.iat[index + 0]
    cx_nxt = cx.iat[(index + 1)%cx.size]

    cy_bef = cy.iat[index - 1]
    cy_act = cy.iat[index + 0]
    cy_nxt = cy.iat[(index + 1)%cx.size]

    a.append(
        np.sqrt(
        (cx_nxt - cx_bef)**2 +
        (cy_nxt - cy_bef)**2
        )
    )

    b.append(
        np.sqrt(
        (cx_nxt - cx_act)**2 +
        (cy_nxt - cy_act)**2
        )
    )

    c.append(
    np.sqrt(
        (cx_act - cx_bef)**2 +
        (cy_act - cy_bef)**2
        )
    )


# Converting from array to series
a = pd.Series(data = a)
b = pd.Series(data = b)
c = pd.Series(data = c)

# finding the angle created by these three points, with an generic center
cos_A = (
    (b ** 2 + c ** 2 - a ** 2) /
    (2 * b * c)
    )


A_rad = np.arccos(cos_A)

# Probably it will not be used but there's the conversion from rad to deg
A_deg = A_rad * 180 / np.pi

df2 = pd.DataFrame(data = {'Distance_A':a,'Angle_Radians':A_rad})

# finally, the radius
def turn_radius (n, d):
    if d ==0: return 0
    return n/d

def calculate_turn_radius (row):
    return turn_radius(row.Distance_A, (2 * np.sin(np.pi - row.Angle_Radians)))

df['Corner Radius'] = df2.apply(calculate_turn_radius, axis = 1)


df.to_csv(r'C:\Users\jgbal\Github\lap-time-simulator\Point-mass\track_coordinates\calculated radiuses.csv')

# print(csv_size)

