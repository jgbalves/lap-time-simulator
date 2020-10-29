import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\jgbal\Github\lap-time-simulator\Point-mass\track_coordinates\calculated_radiuses.csv")

x = df['cx']
y = df['cy']
R = df['Corner Radius']
z = np.array(df['Corner Radius'])

def corner_velocity (acc, R):
    if R == np.inf: return np.nan
    return np.sqrt(acc * R)

# finding local minima
K = np.r_[True, z[1:] < z[:-1]] & np.r_[z[:-1] < z[1:], True]

