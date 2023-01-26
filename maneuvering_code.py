from picarx_improved import Picarx
import time


def simple_move(car, dist, dir, angle, speed):
    car.set_dir_servo_angle(angle)
    time_to_sleep = abs(dist)/speed

    if dir == 0:
        car.forward(speed)
    elif dir == 1:
        car.backward(speed)
    time.sleep(time_to_sleep)
    car.stop()

def paralell_park(car, direction, dist_sideways, dist_fwd_bkwd):
    pass

def k_turn(car):
    pass


if __name__ == "__main__":
    px = Picarx()
    simple_move(px, 100, 0, 0, 100)
    simple_move(px, 100, 1, 0, 100)
    simple_move(px, 100, 0, 35, 100)
    simple_move(px, 100, 0, -35, 100)
    px.stop()