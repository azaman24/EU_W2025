# Import necessary modules from MicroPython
from machine import Pin, time_pulse_us  # Import Pin for GPIO control and time_pulse_us for measuring pulse duration
import time  # Import time module for delays

# Define the GPIO pins where Trig and Echo are connected
TRIG_PIN = 3   # Changed to GP3 as per your Wokwi connections
ECHO_PIN = 5   # Changed to GP5 as per your Wokwi connections

# Initialize the Trig pin as an output
trig = Pin(TRIG_PIN, Pin.OUT)
# Initialize the Echo pin as an input
echo = Pin(ECHO_PIN, Pin.IN)

def get_distance():
    """
    This function sends out an ultrasonic pulse and measures the time it takes
    for the echo to return. It then calculates and returns the distance based
    on the time measured.
    """
    # Ensure Trig is low
    trig.value(0)
    time.sleep_us(2)  # Wait for 2 microseconds

    # Send a 10 microsecond pulse to trigger the sensor
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    try:
        # Measure the duration of the echo pulse in microseconds
        duration = time_pulse_us(echo, 1, 30000)  # Timeout after 30,000 microseconds (30 ms)
    except OSError:
        # If no echo is received within the timeout, return -1
        return -1

    # Speed of sound is approximately 343 meters per second
    # Convert duration from microseconds to seconds and calculate distance
    # Distance = (Duration * Speed of Sound) / 2
    # 34300 cm/s is equivalent to 0.0343 cm/μs
    distance_cm = (duration * 0.0343) / 2

    return distance_cm

# Main loop to continuously measure and print distance
while True:
    distance = get_distance()  # Call the function to get distance

    if distance >= 0:
        print("Distance:", distance, "cm")  # Print the distance in centimeters
    else:
        print("No echo received")  # Print message if no echo is received

    time.sleep(1)  # Wait for 1 second before measuring again
