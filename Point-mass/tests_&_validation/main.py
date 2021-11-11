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
# # Running validation functions

# # Importing Libraries
import SM_validation_functions as SMv


def main():
    data_from_i2 = 'interlagos_corner_data.csv'
    data_from_lts = '../track_coordinates/turn_radius.csv'
    app = SMv.ValidationPlots(data_from_i2, data_from_lts)
    plot = app.corner_radius()
    plot.show()


if __name__ == '__main__':
    main()
