import time
import RPi.GPIO as io
io.setmode(io.BCM)

pir_pin = 21 
door_down_pin = 17
door_up_pin = 27

io.setup(pir_pin, io.IN)         # activate input
io.setup(door_down_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp
io.setup(door_up_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

while True:
    if io.input(pir_pin):
        print("Motion Detected!")
    if io.input(door_down_pin):
        print("DOOR is DOWN!")
    if io.input(door_up_pin):
        print("DOOR is UP!")
    time.sleep(1)
    print(" ")
