from machine import Pin
from time import sleep
from servo import Servo

claw = Servo(pin_id=20)

claw.write(10)
sleep(1)


claw.write(35)
sleep(1)

claw.off()
