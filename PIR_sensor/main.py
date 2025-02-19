from machine import Pin
from time import sleep

# Define the PIR sensor pin
pir = Pin(14, Pin.IN)

# Define the LED pin (optional, for indication)
led = Pin(2, Pin.OUT)

print("PIR Motion Sensor Ready...")

while True:
    if pir.value():  # Motion detected
        print("Motion detected!")
        led.value(1)  # Turn on LED
        sleep(2)  # Wait for a while before checking again
    else:
        led.value(0)  # Turn off LED
    sleep(0.1)  # Small delay to reduce CPU usage
