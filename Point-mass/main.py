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
# # Point mass lap time simulator

# # Importing Libraries
import SM_carmodel_v3 as lts
import SM_car_analysis as ltsplt


def main():
    # To run the car around the track
    # car = lts.Car('car_data_2.csv')
    # track = lts.Track('turn_radius.csv')
    # lts.simulate(car, track)

    # To plot the cars created
    car_1 = ltsplt.CarOuting('car_data_1_turn_radius_outing.csv')
    car_2 = ltsplt.CarOuting('car_data_2_turn_radius_outing.csv')
    car_3 = ltsplt.CarOuting('car_data_3_turn_radius_outing.csv')
    ltsplt.compare(car_1, car_2, car_3)


if __name__ == '__main__':
    main()
