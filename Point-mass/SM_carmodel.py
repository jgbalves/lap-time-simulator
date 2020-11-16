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

# Converting Radiuses in arrays so they can be used in local minima function
tr = np.array(tr)
# finding local minima (turn apex)
K = np.r_[True, tr[1:] < tr[:-1]] & np.r_[tr[:-1] < tr[1:], True]

# where are the apexes(indexes)
apexes = [i for i, x in enumerate(K) if x]

for t in apexes:
    df[f'Test {t}'] = np.nan
    cs = df[f'Test {t}']

    start = t

    spd_apex = np.sqrt(
        g_lat * df.at[start, 'Corner Radius'] * 9.81
    )

# Simple corner velocity (centripetal) V = (g_lat * 9,81 * Radius) ^ 1/2 

# Creating the column where the corner speeds will be put
df['speed turn 1'] = np.nan
cs = df['speed turn 1']

start = 6
spd1 = np.sqrt(g_lat * df.at[start, 'Corner Radius'] * 9.81)
df.at[start,'speed turn 1'] = spd1

# convert from array to series
cx = pd.Series(data= cx)
cy = pd.Series(data= cy)
tr = pd.Series(data= tr)
cs = pd.Series(data= cs)

for index in range (start+1, cx.size):
    cx_bfr = cx.iat[index -1]
    cx_act = cx.iat[index]

    cy_bfr = cy.iat[index -1]
    cy_act = cy.iat[index]

    spd_bfr = cs.iat[index-1]
    # import ipdb; ipdb.set_trace()

    cs.at[index] = np.sqrt(
            spd_bfr**2 + 2 * 9.81 * g_lat * np.sqrt(
                (cx_act - cx_bfr)**2 + (cy_act - cy_bfr)**2
            )
        )

for index in range (0, start):
    cx_bfr = cx.iat[index -1]
    cx_act = cx.iat[index]

    cy_bfr = cy.iat[index -1]
    cy_act = cy.iat[index]

    spd_bfr = cs.iat[index-1]
    # import ipdb; ipdb.set_trace()

    cs.at[index] = np.sqrt(
            spd_bfr**2 + 2 * 9.81 * g_lat * np.sqrt(
                (cx_act - cx_bfr)**2 + (cy_act - cy_bfr)**2
            )
        )

df.to_csv(r'C:\Users\jgbal\Github\lap-time-simulator\Point-mass\outing.csv')