from machine import Pin
from time import sleep

# Define the LCD pin connections
lcd = LCD(rs=2, e=3, d4=4, d5=5, d6=6, d7=7)

# Clear the display and show initial text
lcd.clear()
lcd.putstr("Hello, World!")  # Display static text on the first row
lcd.move_to(0, 1)  # Move to the second row
lcd.scroll_text("This is a scrolling message on the LCD.", row=1)