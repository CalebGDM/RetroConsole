from GraphicsEngine import  GraphicsEngine
from machine import  Pin, I2C
from engine import Core
import time
i2c = I2C(1,scl=Pin(27), sda=Pin(26), freq=400000)


screen = GraphicsEngine(i2c)
screen.fill(1)
screen.show()
game = Core(screen)
game.loop()

