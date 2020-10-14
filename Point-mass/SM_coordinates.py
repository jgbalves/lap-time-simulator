import pandas as pd

df = pd.read_csv("C:\\Users\\jgbal\\Github\\lap-time-simulator\\Point-mass\\track_coordinates\\Sample_track.csv", sep = ';', low_memory = False)

df['New column'] = 'default'



print(df.head())