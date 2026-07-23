from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
time = 10
while time > 0:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
        time -= 1
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
