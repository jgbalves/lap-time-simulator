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

# convert from array to series
cx = pd.Series(data= cx)
cy = pd.Series(data= cy)
tr = pd.Series(data= tr)


for t in apexes:
    df[f'Accel {t}'] = np.nan
    cs = df[f'Accel {t}']
    cs = pd.Series(data= cs)

    start = t
          
    # Simple corner velocity (centripetal) V = (g_lat * 9,81 * Radius) ^ 1/2 
    spd_apex = np.sqrt(
        g_lat * df.at[start, 'Corner Radius'] * 9.81
    )

    df.at[start, f'Accel {t}'] = spd_apex

    for index in range (start + 1, cx.size):
        cx_bfr = cx.iat[index -1]
        cx_act = cx.iat[index]

        cy_bfr = cy.iat[index -1]
        cy_act = cy.iat[index]

        spd_bfr = cs.iat[index -1]

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

        spd_bfr = cs.iat[index -1]

        cs.at[index] = np.sqrt(
            spd_bfr**2 + 2 * 9.81 * g_lat * np.sqrt(
                (cx_act - cx_bfr)**2 + (cy_act - cy_bfr)**2
            )
        )

for t in apexes:
    df[f'Decel {t}'] = np.nan
    cs = df[f'Decel {t}']
    cs = pd.Series(data= cs)

    start = t
          
    # Simple corner velocity (centripetal) V = (g_lat * 9,81 * Radius) ^ 1/2 
    spd_apex = np.sqrt(
        g_lat * df.at[start, 'Corner Radius'] * 9.81
    )

    df.at[start, f'Decel {t}'] = spd_apex

    for index in range (start + 1, cx.size):
        cx_bfr = cx.iat[index -1]
        cx_act = cx.iat[index]

        cy_bfr = cy.iat[index -1]
        cy_act = cy.iat[index]

        spd_bfr = cs.iat[index -1]

        cs.at[index] = np.sqrt(
            spd_bfr**2 - 2 * 9.81 * g_lat * np.sqrt(
                (cx_act - cx_bfr)**2 + (cy_act - cy_bfr)**2
            )
        )

    for index in range (0, start):
        cx_bfr = cx.iat[index -1]
        cx_act = cx.iat[index]

        cy_bfr = cy.iat[index -1]
        cy_act = cy.iat[index]

        spd_bfr = cs.iat[index -1]

        cs.at[index] = np.sqrt(
            spd_bfr**2 - 2 * 9.81 * g_lat * np.sqrt(
                (cx_act - cx_bfr)**2 + (cy_act - cy_bfr)**2
            )
        )


# Check the braking values, compare what is best, to change the + to - or to change the coordinates from bfr and act to act and next

df.to_csv(r'C:\Users\jgbal\Github\lap-time-simulator\Point-mass\outing.csv')