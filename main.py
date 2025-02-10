import sys
import select
from lcd import LCD
from time import sleep

# Initialize LCD
lcd = LCD(rs=2, e=3, d4=4, d5=5, d6=6, d7=7)
lcd.clear()
lcd.move_to(0, 1)
lcd.putstr("<<<<<Gemini>>>>>")

# Initial display on the bottom row
lcd.move_to(0, 0)
lcd.putstr("<<Waiting>>")

#Continuously check for incoming serial data
while True:
    # Use select to check if there is any data on stdin without blocking
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        # Read the incoming line and remove extra whitespace/newline
        line = sys.stdin.readline().strip()
        if line:  # If a non-empty string is received
            lcd.clear()
            lcd.move_to(0, 1)
            lcd.putstr("<<<<<Gemini>>>>>")
            lcd.move_to(0, 0)
            lcd.scroll_text(line, row=0, delay=0.7)
    sleep(0.1)  #Small delay to avoid hogging the CPU