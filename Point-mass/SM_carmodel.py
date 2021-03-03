import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# Track details & car data
track_details_path = Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', 'track_coordinates', 'calculated_radiuses.csv')
car_data_path = Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', 'car_data.csv')

df = pd.read_csv(track_details_path)
df2 = pd.read_csv(car_data_path)

# Dropping null value columns out to avoid errors
df2.dropna(inplace = True)

# converting dataframe colums to numeric to avoid errors

# Track data
df['cx'] = pd.to_numeric(df['cx'], downcast= 'float')
df['cy'] = pd.to_numeric(df['cy'], downcast= 'float')
df['Corner Radius'] = pd.to_numeric(df['Corner Radius'], downcast= 'float')

# Car data
g_lat = pd.to_numeric(df2.iloc[3,1], downcast='float')
tranny_efc = pd.to_numeric(df2.iloc[5,1], downcast='float') / 100
Power = pd.to_numeric(df2.iloc[4,1], downcast='float') * 745.7 * tranny_efc
air_density =  pd.to_numeric(df2.iloc[6,1], downcast='float')
frontal_area = pd.to_numeric(df2.iloc[1,1], downcast='float')
drag_coef = pd.to_numeric(df2.iloc[2,1], downcast='float')
car_mass = pd.to_numeric(df2.iloc[0,1], downcast='float')


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
df['dx'] = dx


# getting note of the corner names, so we can get the minimum velocity values of them all later 
corner_names = []

# Accelerating V = sqrt(Vo² + 2*dx/m * (Power/m - drag))
for t in apexes:
    df[f'Accel {t}'] = 0.0
    cs = df[f'Accel {t}']
    cs = pd.Series(data= cs)

    # Putting the corner names in the list
    corner_names.append(f'Accel {t}')

    start = t
          
    # Simple corner velocity (centripetal) V = (g_lat * 9,81 * Radius) ^ 1/2 
    spd_apex = np.sqrt(
        g_lat * df.at[start, 'Corner Radius'] * 9.81
    )

    df.at[start, f'Accel {t}'] = spd_apex

    #Accelerating from apex onward
    for index in range (start + 1, cx.size):
        cx_bfr = cx.iat[index -1]
        cx_act = cx.iat[index]

        cy_bfr = cy.iat[index -1]
        cy_act = cy.iat[index]
        spd_bfr = cs.iat[index -1]

        s_distance = np.sqrt((cx_act - cx_bfr)**2 + (cy_act - cy_bfr)**2)
        drag = drag_coef * air_density * spd_bfr ** 2 * frontal_area / 2

        cs.at[index] = np.sqrt(spd_bfr**2 + 2 * s_distance * (Power/spd_bfr - drag) / car_mass)


    for index in range (0, start):
        cx_bfr = cx.iat[index -1]
        cx_act = cx.iat[index]

        cy_bfr = cy.iat[index -1]
        cy_act = cy.iat[index]
        spd_bfr = cs.iat[index -1]

        s_distance = np.sqrt((cx_act - cx_bfr)**2 + (cy_act - cy_bfr)**2)
        drag = drag_coef * air_density * spd_bfr ** 2 * frontal_area / 2

        
        cs.at[index] = np.sqrt(spd_bfr**2 + 2 * s_distance * (Power/spd_bfr - drag) / car_mass)

# Deccelerating V = sqrt(Vo² + 2 * dx (mi * g + drag / m))
for t in apexes:
    df[f'Decel {t}'] = 0.0
    cs = df[f'Decel {t}']
    cs = pd.Series(data= cs)

    # Putting the corner names in the list
    corner_names.append(f'Decel {t}')

    start = t
          
    # Simple corner velocity (centripetal) V = (g_lat * 9,81 * Radius) ^ 1/2 
    spd_apex = np.sqrt(
        g_lat * df.at[start, 'Corner Radius'] * 9.81
    )

    df.at[start, f'Decel {t}'] = spd_apex

    for index in range (start - 1, -1, -1):
        cx_act = cx.iat[index]
        cx_nxt = cx.iat[index +1]

        cy_act = cy.iat[index]
        cy_nxt = cy.iat[index +1]

        spd_nxt = cs.iat[index +1]

        s_distance = np.sqrt((cx_nxt - cx_act)**2 + (cy_nxt - cy_act)**2)
        drag = drag_coef * air_density * spd_nxt ** 2 * frontal_area / 2

        cs.at[index] = np.sqrt(spd_nxt**2 + (2 * s_distance * (9.81 * g_lat + drag/car_mass)))

    for index in range (cx.size - 1, start, -1):
        cx_act = cx.iat[index]
        cx_nxt = cx.iat[(index +1)%cx.size]

        cy_act = cy.iat[index]
        cy_nxt = cy.iat[(index +1)%cx.size]

        spd_nxt = cs.iat[(index +1)%cx.size]

        s_distance = np.sqrt((cx_nxt - cx_act)**2 + (cy_nxt - cy_act)**2)
        drag = drag_coef * air_density * spd_nxt ** 2 * frontal_area / 2

        cs.at[index] = np.sqrt(spd_nxt**2 + (2 * s_distance * (9.81 * g_lat + drag/car_mass)))

    df2 = pd.DataFrame(data= {f'Accel {t}', f'Decel {t}'})


# making a report
# df.to_csv(r'C:\Users\jgbal\Github\lap-time-simulator\Point-mass\outing.csv')

# getting all the minimum speeds and organizing them in a signal
turns = df[corner_names]
speed_profile = turns.min(axis = 1)
speed_profile_kph = speed_profile * 3.6

# lap time
df['speed'] = speed_profile
df['speed (km/h)'] = speed_profile_kph
df['t(s)'] = df['dx'] / df['speed']
lap_time = df['t(s)'].sum()

lt_minutes = lap_time//60
lt_seconds = lap_time % 60


# Plot time!

fig, ax = plt.subplots(2)
fig.suptitle('[Piloto]: Braia / [Pista]: Interlagos')

ax[0].plot(speed_profile_kph, 'r', Label = 'Speed (km/h)')
ax[0].set_title('Speed')
plt.text(1, 1, f'{lt_minutes:.0f}:{lt_seconds:.2f}', bbox=dict(facecolor='white', alpha=0.5))

ax[1].plot(cx,cy,'r')
ax[1].set_title('Track map')

plt.show()