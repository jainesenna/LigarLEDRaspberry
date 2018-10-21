import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)

gpio.setup(12,gpio.OUT)

gpio.setup(12,gpio.HIGH)
time.sleep(2)
gpio.setup(12,gpio.LOW)
time.sleep(2)

gpio.cleanup()
