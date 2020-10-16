import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\jgbal\\Github\\lap-time-simulator\\Point-mass\\track_coordinates\\Sample_track.csv", sep = ';', low_memory = False)

# To add new columns df['New column'] = 'teste'



# print(df.head())

# to find a row (string) print(df.iloc[1])

# Positions 
# x_pos
# y_pos

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

print(c_two)
