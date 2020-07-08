from NokiaLCD import nokiaLCD
screen = nokiaLCD()

import time
import Controler



#functions
def setSpeed(speed, X, Y):
    screen.clearImagePart(X, X+15, Y, Y+15)
    screen.printText(str(speed), X, Y)
    screen.displayImage()

def drawMenu(speed):
    screen.drawLine(0, 83, 15, 15)
    screen.drawLine(42, 42, 15, 47)
    screen.printText("Endless Snake", 3, 2)
    screen.printText("START", 8, 25)
    screen.printText("SPEED", 50, 20)
    setSpeed(speed,60,30)

    screen.displayImage()

# Start Menu


def Menu(max_speed):
    # locals
    menu_previous_controler_state = ""
    game_started = False
    speed = 1

    drawMenu(speed)

    while not game_started:

        # buttons value changed
        menu_currnet_controler_state = Controler.getControlerState()
        if menu_currnet_controler_state != menu_previous_controler_state and menu_currnet_controler_state != "Idle" and menu_currnet_controler_state != "Both":
            if menu_currnet_controler_state == "Left":
                game_started = True

            else:
                speed += 1
                if speed > max_speed:
                    speed = 1
                else:
                    pass

                setSpeed(speed, 60, 30)

        menu_previous_controler_state = menu_currnet_controler_state

        time.sleep(0.1)

    return speed
