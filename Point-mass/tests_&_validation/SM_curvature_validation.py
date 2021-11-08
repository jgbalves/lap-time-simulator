# # ==============================================================================
# #
# #   _____ ____  ________________     __  ___________________  _____________
# #  / ___// __ \/ ____/ ____/ __ \   /  |/  / ____/_  __/ __ \/  _/ ____/   |
# #  \__ \/ /_/ / __/ / __/ / / / /  / /|_/ / __/   / / / /_/ // // /   / /| |
# # ___/ / ____/ /___/ /___/ /_/ /  / /  / / /___  / / / _, _// // /___/ ___ |
# #/____/_/   /_____/_____/_____/  /_/  /_/_____/ /_/ /_/ |_/___/\____/_/  |_|
# #
# #                           www.speedmetrica.com
# #
# # ==============================================================================
# # Comparing calculated signal from SM_curvature with data generated by motec i2

# # Importing libraries
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# # Getting the data
data_from_i2 = 'interlagos_corner_data.csv'    # Data from motec i2, for validation
data_from_lts = '../track_coordinates/turn_radius.csv'    # Data from the lap time simulator (LTS)

df_lts = pd.read_csv(data_from_lts, sep=',')    # LTS data transformed to dataframe
df_i2 = pd.read_csv(data_from_i2, sep=',', low_memory=False, skiprows=13)    # motec data transformed to dataframe
df_i2 = df_i2.drop([0], axis=0)
df_i2['Corner Radius Norm'].fillna(method='ffill', inplace=True)    # Cleaning motec data (NaN subst. by prev value)
df_i2['Corner Radius Norm'] = pd.to_numeric(df_i2['Corner Radius Norm'])

# # Creating plot Subfigure
fig = make_subplots(
        rows=1, cols=1
    )
fig.update_layout(title='Corner Radius - i2 vs LTS',
                  plot_bgcolor='rgb(230, 230,230)',
                  showlegend=True)
fig.update_yaxes(range=[0, 2000])

# Adding the data
data_1 = fig.add_trace(
            go.Scatter(
                x=df_i2['Distance'],
                y=df_i2['Corner Radius Norm'],
                mode='lines',
                name='motec i2 channel'
            ),
            row=1, col=1
        )

data_2 = fig.add_trace(
            go.Scatter(
                x=df_lts['Distance'],
                y=df_lts['Turn Radius'],
                mode='lines',
                name='LTS channel'
            ),
            row=1, col=1
        )

fig.show()
