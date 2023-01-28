import maneuvering_code
from picarx_improved import Picarx
from os import system
import logging

logging_format = "%(asctime)s : %(message)s "
logging.basicConfig( format = logging_format, level = logging.DEBUG, datefmt ="%H:%M:%S")

logging.getLogger().setLevel( logging.DEBUG )


#I combined some recursive stuff, some loops, it's kinda awful and I do apologize for that.
#Truth be told, I don't really like making UIs.
class ManeuveringUI():
    def __init__(self, car):
        self.car = car
        print()

    def display_main_page(self):
        valid_responses = {
            "1" : self.simple_move,
            "2" : self.parallel_park,
            "3" : self.k_turn,
            "4" : self.exit_program
        }
        script = """Please select the maneuver you'd wish to perform:\n(1) Simple movement forwards or backwards\n(2) Parallel Parking\n(3) Perform a K-Turn\n(4) Close UI\n>>>"""
        response = input(script)
        if not response in valid_responses.keys():
            #system('clear')
            print(f"I'm sorry. The response {response} does not appear to be a valid option. Please try again.")
            return self.display_main_page()
        #The way this is structured, returning false means "The program is NOT going to exit" while True means "The program SHOULD exit"
        return valid_responses[response]()
        

    def sanitize_to_number(self, val):
        sanitized = val
        while not sanitized.isdigit():
            sanitized = input("I'm sorry, it does not appear that your response was a number. Please try again.\n>>>")
        return int(sanitized)

    def simple_move(self):
        dist = 100
        dir = 0
        angle = 0
        speed = 50

        script = f"""Currently running: Simple Move. Please select and enter parameters\n\nCurrent values:\nDistance: {dist}\nDirection: {dir}\nAngle: {angle}\nSpeed: {speed}\n\nOptions:\n(1) Distance\n(2) Direction (0 for forwards, 1 for backwards)\n(3) Angle\n(4) Speed (Less than 100 recommended)\n(5) Run function\n(6) Back to main\n>>>"""

        response = input(script)
        while response != "6":
            if response == "1":
                num = input("Please enter an integer value: ")
                dist = self.sanitize_to_number(num)
            elif response == "2":
                num = input("Please enter an integer value: ")
                dir = self.sanitize_to_number(num)
                while dir != 0 and dir != 1:
                    num = input("I'm sorry, that does not appear to be a valid input. Please input 0 or 1\n")
                    dir = self.sanitize_to_number(num)
            elif response == "3":
                num = input("Please enter an integer value: ")
                angle = self.sanitize_to_number(num)
            elif response == "4":
                num = input("Please enter an integer value: ")
                dir = self.sanitize_to_number(num)
            elif response == "5":
                print("Running move command")
                maneuvering_code.simple_move(self.car, dist, dir, angle, speed)
            else:
                print("\n\nI'm sorry, that doesn't appear to be a valid option. Please try again.")

            script = f"""Currently running: Simple Move. Please select and enter parameters\n\nCurrent values:\nDistance: {dist}\nDirection: {dir}\nAngle: {angle}\nSpeed: {speed}\n\nOptions:\n(1) Distance\n(2) Direction (0 for forwards, 1 for backwards)\n(3) Angle\n(4) Speed (Less than 100 recommended)\n(5) Run function\n(6) Back to main\n>>>"""

            print("\n\n")

            if response != "5":
                response = input(script)
            else:
                break

        print("\n")
        return False

    def parallel_park(self):
        dist = 100
        dir = "right"
        speed = 50

        script = f"""Currently running: Simple Move. Please select and enter parameters\n\nCurrent values:\nDistance: {dist}\nDirection: {dir}\nSpeed: {speed}\n\nOptions:\n(1) Distance between adjacent obstacles\n(2) Direction (enter \"left\" or \"right\")\n(3) Speed (Less than 100 recommended)\n(4) Run function\n(5) Back to main\n>>>"""

        response = input(script)
        while response != "5":
            if response == "1":
                num = input("Please enter an integer value: ")
                dist = self.sanitize_to_number(num)
            elif response == "2":
                dir = input("Please enter \"left\" or \"right\": ")
                while dir != "left" and dir != "right":
                    dir = input("I'm sorry, that does not appear to be a valid input. Please input left or right\n")
            elif response == "3":
                num = input("Please enter an integer value: ")
                speed = self.sanitize_to_number(num)
            elif response == "4":
                print("Running move command")
                maneuvering_code.parallel_park(self.car, dir, dist, speed)
            else:
                print("\n\nI'm sorry, that doesn't appear to be a valid option. Please try again.")

            script = f"""Currently running: Simple Move. Please select and enter parameters\n\nCurrent values:\nDistance: {dist}\nDirection: {dir}\nSpeed: {speed}\n\nOptions:\n(1) Distance between adjacent obstacles\n(2) Direction (enter \"left\" or \"right\")\n(3) Speed (Less than 100 recommended)\n(4) Run function\n(5) Back to main\n>>>"""

            print("\n\n")

            if response != "4":
                response = input(script)
            else:
                break

        print("\n")
        return False

    def k_turn(self):
        dir = "right"
        speed = 50

        script = f"""Currently running: Simple Move. Please select and enter parameters\n\nCurrent values:\nDirection: {dir}\nSpeed: {speed}\n\nOptions:\n(1) Direction (enter \"left\" or \"right\")\n(2) Speed (Less than 100 recommended)\n(3) Run function\n(4) Back to main\n>>>"""

        response = input(script)
        while response != "4":
            if response == "1":
                dir = input("Please enter \"left\" or \"right\": ")
                while dir != "left" and dir != "right":
                    dir = input("I'm sorry, that does not appear to be a valid input. Please input left or right\n")
            elif response == "2":
                num = input("Please enter an integer value: ")
                speed = self.sanitize_to_number(num)
            elif response == "3":
                print("Running move command")
                maneuvering_code.k_turn(self.car, dir, speed)
            else:
                print("\n\nI'm sorry, that doesn't appear to be a valid option. Please try again.")

            script = f"""Currently running: Simple Move. Please select and enter parameters\n\nCurrent values:\nDirection: {dir}\nSpeed: {speed}\n\nOptions:\n(1) Direction (enter \"left\" or \"right\")\n(2) Speed (Less than 100 recommended)\n(3) Run function\n(4) Back to main\n>>>"""

            print("\n\n")

            if response != "3":
                response = input(script)
            else:
                break

        print("\n")
        return False

    def exit_program(self):
        return True

if __name__=="__main__":
    px = Picarx()
    ui = ManeuveringUI(px)
    exit = False
    #system('clear')
    while not exit:
        exit = ui.display_main_page()