from machine import Pin
import time

# wait for USB to become ready
time.sleep(0.1)

button = Pin(15, Pin.IN)

while True:
    if button.value():
        print("BUTTON PRESSED!")
    
    #
    # take a 10 millis rest
    # each time we poll the 
    # button
    #
    time.sleep(0.01)