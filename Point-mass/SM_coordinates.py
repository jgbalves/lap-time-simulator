import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\jgbal\\Github\\lap-time-simulator\\Point-mass\\track_coordinates\\Sample_track.csv", sep = ';', low_memory = False)

# convert column "cx" of a DataFrame
df["cx"] = pd.to_numeric(df["cx"], downcast = 'float')

# convert column "cy" of a DataFrame
df["cy"] = pd.to_numeric(df["cy"], downcast = 'float')

# To add new columns df['New column'] = 'test'
# to find a row (string) print(df.iloc[1])

# finding 3 distances between three generic points in the space

# a is the distance between the point before to the next
# sqrt((Xn+1 - Xn-1)² + (Yn+1 - Yn-1)²)
# b is the distance between the actual point to the next
# sqrt((Xn+1 - Xn)² + (Yn+1 - Yn)²)
# c is the distance between the actual point to before
# sqrt((Xn - Xn-1)² + (Yn - Yn-1)²)

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

# populating the empty a b and c lists

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
# cos A = (b² + c² - a²)/2bc
cos_A = (
    (b ** 2 + c ** 2 - a ** 2) /
    (2 * b * c)
    )


A_rad = np.arccos(cos_A)

# Probably it will not be used but there's the conversion from rad to deg
A_deg = A_rad * 180 / np.pi

# Creating an auxiliary dataframe with distance a and angle, to do the next calculations
df2 = pd.DataFrame(data = {'Distance_A':a,'Angle_Radians':A_rad})

# finally, the radius (if three points are in straight, the denominator will be zero)
# R = a / (2 * sin(180-A))

def turn_radius (n, d):
    if d ==0: return np.inf
    return n/d

def calculate_turn_radius (row):
    return turn_radius(row.Distance_A, (2 * np.sin(np.pi - row.Angle_Radians)))


# aplying the two functions combined, so we can write the calculation for row to row
df['Corner Radius'] = df2.apply(calculate_turn_radius, axis = 1)

# recording the resulting dataframe in a csv
df.to_csv(r'C:\Users\jgbal\Github\lap-time-simulator\Point-mass\track_coordinates\calculated radiuses.csv')
