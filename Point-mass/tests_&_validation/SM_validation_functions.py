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
import pdb

import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


class TurnRadiusValidation(object):
    def __init__(self, csv_path_i2=None, csv_path_lts=None):
        # # Getting the data

        self.data_from_i2 = csv_path_i2  # Data from motec i2, for validation
        self.data_from_lts = csv_path_lts  # Data from the lap time simulator (LTS)

        self.df_lts = pd.read_csv(self.data_from_lts, sep=',')  # LTS data transformed to dataframe
        self.df_i2 = pd.read_csv(self.data_from_i2, sep=',', low_memory=False, skiprows=13)  # motec data transformed to dataframe
        self.df_i2 = self.df_i2.drop([0], axis=0)
        self.df_i2['Corner Radius Norm'].fillna(method='ffill', inplace=True)  # Cleaning motec data (NaN subst. by prev value)
        # self.df_i2['Corner Radius Norm'] = pd.to_numeric(self.df_i2['Corner Radius Norm'])
        self.df_i2 = self.df_i2.astype(float)

    def corner_radius(self):

        # # Creating plot Subfigure
        fig = make_subplots(
                rows=1, cols=1
            )
        fig.update_layout(title='Corner Radius - i2 vs LTS',
                          plot_bgcolor='rgb(230, 230,230)',
                          showlegend=True)
        fig.update_yaxes(range=[0, 2000])

        # Adding the data
        data_i2 = fig.add_trace(
                    go.Scatter(
                        x=self.df_i2['Distance'],
                        y=self.df_i2['Corner Radius Norm'],
                        mode='lines',
                        name='motec i2 channel'
                    ),
                    row=1, col=1
                )

        data_lts = fig.add_trace(
                    go.Scatter(
                        x=self.df_lts['Distance'],
                        y=self.df_lts['Turn Radius'],
                        mode='lines',
                        name='LTS channel'
                    ),
                    row=1, col=1
                )

        return fig


class SpeedValidation(object):
    def __init__(self, csv_path_i2=None, csv_path_lts=None):
        # # Getting the data

        self.speed_from_i2 = csv_path_i2  # Data from motec i2, for validation
        self.speed_from_lts = csv_path_lts  # Data from the lap time simulator (LTS)

        self.df_lts = pd.read_csv(self.speed_from_lts, sep=',')  # LTS data transformed to dataframe
        self.df_i2 = pd.read_csv(self.speed_from_i2, sep=',', low_memory=False, skiprows=13)  # motec data transformed to dataframe
        self.df_i2 = self.df_i2.drop([0], axis=0)
        self.df_i2 = self.df_i2.astype(float)

    def speed_comparison(self):

        # # Creating plot subfigure
        fig = make_subplots(
                rows=1, cols=1
            )
        fig.update_layout(title='Speed - i2 vs LTS',
                          plot_bgcolor='rgb(230, 230,230)',
                          showlegend=True)

        # Adding data
        speedline_i2 = fig.add_trace(
            go.Scatter(
                x=self.df_i2['Distance'],
                y=self.df_i2['Corr Speed'],
                mode='lines',
                name='motec i2 channel'
            )
        )

        speedline_lts = fig.add_trace(
            go.Scatter(
                x=self.df_lts['Distance'],
                y=self.df_lts['speed (km/h)'],
                mode='lines',
                name='LTS channel'
            )
        )
        return fig



