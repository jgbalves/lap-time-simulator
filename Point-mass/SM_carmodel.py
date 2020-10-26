import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\jgbal\Github\lap-time-simulator\Point-mass\track_coordinates.csv', sep= ',', low_memory= False)

print(df.head())