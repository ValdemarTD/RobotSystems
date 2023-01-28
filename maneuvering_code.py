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

def parallel_park(car, direction, dist_between, speed):
    if direction == "left":
        dir_modifier = -1
    elif direction == "right":
        dir_modifier = 1

    simple_move(car, dist_between, 0, 0, speed)
    time.sleep(0.15)
    #Move to backup angle
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


def k_turn(car, direction, speed):
    if direction == "left":
        dir_modifier = -1
    elif direction == "right":
        dir_modifier = 1
    simple_move(car, 200, 0, dir_modifier*30, speed)
    time.sleep(0.1)
    simple_move(car, 200, 1, -dir_modifier*30, speed)
    time.sleep(0.1)
    simple_move(car, 200, 0, 0, speed)


def demo_simple_move(car, testing_speed):
    simple_move(px, 150, 0, 0, testing_speed)
    time.sleep(0.2)
    simple_move(px, 150, 1, 0, testing_speed)
    time.sleep(0.2)
    simple_move(px, 150, 0, 30, testing_speed)
    time.sleep(0.2)
    simple_move(px, 150, 1, 30, testing_speed)
    time.sleep(0.2)
    simple_move(px, 150, 0, -15, testing_speed)
    time.sleep(0.2)
    simple_move(px, 150, 1, -15, testing_speed)

def demo_parallel_park(car, testing_speed):
    parallel_park(px, "right", 200, testing_speed)
    time.sleep(0.5)
    parallel_park(px, "left", 200, testing_speed)

def demo_k_turn(car, testing_speed):
    k_turn(car, "right", testing_speed)
    time.sleep(1)
    k_turn(car, "right", testing_speed)

if __name__ == "__main__":

    speed = 75

    px = Picarx()
    
    demo_simple_move(px, speed)

    time.sleep(0.5)

    demo_parallel_park(px, speed)

    time.sleep(0.5)

    demo_k_turn(car, speed)

    px.stop()
