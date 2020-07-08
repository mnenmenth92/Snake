import RPi.GPIO as GPIO
import time

#config
right_func_pin = 21
left_func_pin = 20
#locals
function_return = ''
last_button_state = ''
right_func_state = True
left_func_state = True


#GPIO.setmode(GPIO.BCM) #bibloteka lcd ustala bcm


GPIO.setup(right_func_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(left_func_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def getControlerState():

    right_func_state = GPIO.input(right_func_pin)
    left_func_state = GPIO.input(left_func_pin)

    time.sleep(0.1)


    if right_func_state == True and left_func_state == True:
        function_return = 'Idle'
    elif right_func_state == False and left_func_state == True:
        function_return = 'Right'
    elif right_func_state == True and left_func_state == False:
        function_return = 'Left'
    else:
        function_return = 'Both'

    return function_return


def cleanup():
    GPIO.cleanup()




