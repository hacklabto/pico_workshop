from machine import Pin
import time

# wait for USB to become ready

led = Pin(14, Pin.OUT)
button = Pin(15, Pin.IN)

while True:
    if button.value():
        # Toggle the LED state!
        led.toggle()
        
        # Print out to the console that the button press
        # was detected
        print("BUTTON PRESSED!")

        # Debounce the button
        time.sleep(0.5) 
    
    #
    # Take a 10 millis rest
    # each time we poll the button
    #
    time.sleep(0.01)
    
