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
    corner_data_from_i2 = 'interlagos_corner_data.csv'
    corner_data_from_lts = '../track_coordinates/turn_radius.csv'

    speed_data_from_i2 = 'interlagos_speed_data.csv'
    speed_data_from_lts = '../outings/car_data_1_turn_radius_outing.csv'

    app = SMv.TurnRadiusValidation(corner_data_from_i2, corner_data_from_lts)
    # app.corner_radius().show()

    app2 = SMv.SpeedValidation(speed_data_from_i2, speed_data_from_lts)
    app2.speed_comparison().show()


if __name__ == '__main__':
    main()
