import copy
import random

from NokiaLCD import nokiaLCD
screen = nokiaLCD()

#config
screen_size_x = 83
screen_size_y = 47



class oneSnakeElement():
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.fill = 255

    def jumpFruit(self):
        self.X = random.randint(0, screen_size_x-2) # -2 zeby fruit nie wychodzil poza obrys ekranu
        self.Y = random.randint(0, screen_size_y-2) # -2 zeby fruit nie wychodzil poza obrys ekranu

    def checkFruitPos(self, X, Y ):
        return X >= self.X -2 and X <= self.X+2 and Y >= self.Y -2 and Y <= self.Y+2

    def printFruit(self):
        screen.drawPoint(self.X, self.Y, 0)

    def setX(self,X):
        self.X = X

    def setY(self, Y):
        self.Y = Y

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def setFill(self,fill):
        self.fill = fill

    def printElement(self):
        screen.drawPoint(self.X, self.Y, 255)

    def moveToOtherEdgeX(self):
        if self.X < 0:
            self.X = screen_size_x
        elif self.X > screen_size_x:
            self.X = 0
        else:
            pass
        return self.X

    def moveToOtherEdgeY(self):
        if self.Y < 0:
            self.Y = screen_size_y
        elif self.Y > screen_size_y:
            self.Y = 0
        else:
            pass
        return self.Y

    def moveElement(self, dir):
        if dir == "up":
            self.Y -= 2
            self.moveToOtherEdgeY()
        elif dir == "down":
            self.Y += 2
            self.moveToOtherEdgeY()
        elif dir == "left":
            self.X -= 2
            self.moveToOtherEdgeX()
        elif dir == "right":
            self.X += 2
            self.moveToOtherEdgeX()
        else:
            pass

class snake():
    def __init__(self, snake_length):
        self.fruit_eaten = 0
        self.snake_elements = []
        for i in range(0,snake_length):
            self.snake_elements.append(oneSnakeElement(2*i + 50, 20))


    def printSnake(self):
        for one_snake_element in self.snake_elements:
            one_snake_element.printElement()

    def eatFruit(self):
        self.fruit_eaten = True


    def displaySnake(self):
        screen.displayImage()

    def debugSnake(self):
        print(str(one_snake_element.getX()) +" ; " + str(one_snake_element.getY()))
        print("----------")

    def moveSnake(self, dir):
        new_element = copy.deepcopy(self.snake_elements[0])
        new_element.moveElement(dir)
        self.snake_elements.insert(0, new_element)
        if not self.fruit_eaten:
            self.snake_elements.pop()
        else:
            self.fruit_eaten = False

    def moveAndPrint(self,dir):
        screen.clearImage()
        self.moveSnake(dir)
        self.printSnake()

