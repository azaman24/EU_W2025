from machine import Pin
from time import sleep

class LCD:
    def __init__(self, rs, e, d4, d5, d6, d7):
        self.rs = Pin(rs, Pin.OUT)
        self.e = Pin(e, Pin.OUT)
        self.d4 = Pin(d4, Pin.OUT)
        self.d5 = Pin(d5, Pin.OUT)
        self.d6 = Pin(d6, Pin.OUT)
        self.d7 = Pin(d7, Pin.OUT)

        self._init_lcd()

    def _init_lcd(self):
        sleep(0.02)  # Wait for LCD to power up
        self._send_nibble(0x03)
        sleep(0.005)
        self._send_nibble(0x03)
        sleep(0.0001)
        self._send_nibble(0x03)
        self._send_nibble(0x02)  # Set to 4-bit mode

        # Configure LCD
        self._send_command(0x28)  # 4-bit, 2-line, 5x8 dots
        self._send_command(0x0C)  # Display ON, Cursor OFF
        self._send_command(0x06)  # Entry mode (left to right)
        self._send_command(0x01)  # Clear screen
        sleep(0.002)

    def _send_nibble(self, data):
        self.d4.value((data >> 0) & 1)
        self.d5.value((data >> 1) & 1)
        self.d6.value((data >> 2) & 1)
        self.d7.value((data >> 3) & 1)
        self._toggle_enable()

    def _send_byte(self, data, is_data=True):
        self.rs.value(is_data)
        self._send_nibble(data >> 4)
        self._send_nibble(data & 0x0F)

    def _send_command(self, cmd):
        self._send_byte(cmd, False)

    def putstr(self, text):
        for char in text:
            self._send_byte(ord(char), True)

    def clear(self):
        self._send_command(0x01)
        sleep(0.002)

    def move_to(self, col, row):
        addresses = [0x80, 0xC0]  # 0x80 for row 0, 0xC0 for row 1
        self._send_command(addresses[row] + col)

    def _toggle_enable(self):
        self.e.value(1)
        sleep(0.0005)
        self.e.value(0)
        sleep(0.0005)

    def scroll_text(self, text, row=1, delay=0.3):
        """
        Scrolls text on the LCD's given row if it exceeds 16 characters.

        :param text: The text to scroll
        :param row: The row to display the text on (default is bottom row)
        :param delay: The delay between each shift (default is 0.3s)
        """
        self.move_to(0, row)
        if len(text) <= 16:
            self.putstr(text)  # If the text fits, just display it
            return

        # Add padding to create smooth scrolling effect
        text = text + " " * 16  # Space padding at the end
        for i in range(len(text) - 15):
            self.move_to(0, row)
            self.putstr(text[i:i + 16])  # Display only 16 characters at a time
            sleep(delay)

