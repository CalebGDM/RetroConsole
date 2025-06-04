from GraphicsEngine import  GraphicsEngine
from machine import  Pin, I2C
import time
i2c = I2C(1,scl=Pin(27), sda=Pin(26), freq=400000)

player_frames = [
    bytearray([0x7e, 0x81, 0xa3, 0xa3, 0x81, 0x81, 0xff, 0xc3]),
    bytearray([0x00, 0x7e, 0x81, 0xa3, 0xa3, 0xc1, 0x79, 0x07]),
    bytearray([0x7e, 0x81, 0xa3, 0xa3, 0x81, 0x99, 0x7e, 0x38]),
    bytearray([0x00, 0x7e, 0x81, 0xa3, 0xa3, 0x81, 0x7e, 0x66])
]


display = GraphicsEngine(i2c)
current_frame = 0

while True:
    display.clear()
    display.text("Hello World", 10, 10)
    display.rect(5, 30, 8, 10)
    display.sprite(10, 50, player_frames[0], 8, 8)
    display.sprite(60, 40, player_frames[current_frame], 8, 8)
    display.show()
    current_frame = (current_frame + 1) % len(player_frames)
    time.sleep_ms(80)
