from Snake import snake
from Snake import oneSnakeElement
from StartMenu import Menu
import time
import Controler

#Config
speed = 1 #less is quicker
initial_snake_length = 3
loop_delay = 0.005
main_max_speed = 5

#locals
previous_controler_state = ""
speed_counter = 0
current_dir = "left"
previous_dir = "left"

def numberToDir(number):
    if number == 0:
        return "left"
    elif number == 1:
        return "up"
    elif number == 2:
        return "right"
    elif number == 3:
        return "down"
    elif number > 3:  # 3+1 - dir == down, right pressed
        return "left"
    else:             # 0-1 - dir = left, left pressed
        return "down"

def dirToNumber(dir):
    if dir == "left":
        return 0
    elif dir == "up":
        return 1
    elif dir == "right":
        return 2
    elif dir == "down":
        return 3


def updateDirection(button_pressed, previous_direction):
    number_dir = dirToNumber(previous_direction)
    if button_pressed == "Left":
        number_dir -= 1
    else:
        number_dir += 1
    return numberToDir(number_dir)

speed = main_max_speed - Menu(main_max_speed) +1 #


#initilalize fruit
fruit = oneSnakeElement(0,0)
fruit.setFill(0)
fruit.jumpFruit()
fruit.printFruit()
#initialize snake
snake = snake(initial_snake_length)
snake.printSnake()
snake.displaySnake()

while True:

    #buttons value changed
    currnet_controler_state = Controler.getControlerState()
    if currnet_controler_state != previous_controler_state and currnet_controler_state != "Idle" and currnet_controler_state != "Both":
        current_dir = updateDirection(currnet_controler_state,previous_dir)
        previous_dir = current_dir

    previous_controler_state = currnet_controler_state

    #snake speed
    if speed_counter >= speed:
        speed_counter = 0
        snake.moveAndPrint(current_dir)
        fruit.printFruit()
        snake.displaySnake()

    #checkFruit
        snakes_head = snake.snake_elements[0]
        if fruit.checkFruitPos(snakes_head.getX(), snakes_head.getY()):
            fruit.jumpFruit()
            snake.eatFruit()


    time.sleep(loop_delay)
    speed_counter += 1