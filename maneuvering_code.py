from picarx_improved import Picarx
import time

def simple_move(car, dist, dir, angle, speed):
    car.set_dir_servo_angle(angle)
    time_to_sleep = abs(dist)/speed/4
    if dir == 0:
        car.forward(speed)
    elif dir == 1:
        car.backward(speed)
    time.sleep(time_to_sleep)
    car.stop()

def paralell_park(car, direction, dist_between, speed):
    if direction == "left":
        dir_modifier = -1
    elif direction == "right":
        dir_modifier = 1

    simple_move(car, dist_between, 0, 0, speed)
    time.sleep(0.15)
    #Move to 45 degree angle
    simple_move(car, 150, 1, dir_modifier*30, speed)
    time.sleep(0.05)
    #Back up most of the way
    simple_move(car, dist_between/2, 1, 0, speed)
    time.sleep(0.05)
    #re-orient
    simple_move(car, 150, 1, -dir_modifier*30, speed)
    time.sleep(0.15)
    #Finish parking
    simple_move(car, dist_between/3, 0, 0, speed)
    car.stop()


def k_turn(car):
    pass


if __name__ == "__main__":

    testing_speed = 50

    px = Picarx()
    simple_move(px, 100, 0, 0, testing_speed)
    time.sleep(0.2)
    simple_move(px, 100, 1, 0, testing_speed)
    time.sleep(0.2)
    simple_move(px, 100, 0, 30, testing_speed)
    time.sleep(0.2)
    simple_move(px, 100, 1, 30, testing_speed)
    time.sleep(0.2)
    simple_move(px, 100, 0, -15, testing_speed)
    time.sleep(0.2)
    simple_move(px, 100, 1, -15, testing_speed)

    time.sleep(0.5)

    paralell_park(px, "right", 200, testing_speed)

    time.sleep(0.5)

    paralell_park(px, "left", 200, testing_speed)


    px.stop()
