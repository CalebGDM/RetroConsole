from graphics_engine import  GraphicsEngine
from machine import  Pin, I2C
from engine import Core
from sprite import Sprite
from animated_sprite import Animated_Sprite
from game_object import Game_Object
import time
i2c = I2C(1,scl=Pin(27), sda=Pin(26), freq=400000)
player_frames = [
    [
        bytearray([0x7e, 0x81, 0xa3, 0xa3, 0x81, 0x81, 0xff, 0xc3]),
        bytearray([0x00, 0x7e, 0x81, 0xa3, 0xa3, 0xc1, 0x79, 0x07]),
        bytearray([0x7e, 0x81, 0xa3, 0xa3, 0x81, 0x99, 0x7e, 0x38]),
        bytearray([0x00, 0x7e, 0x81, 0xa3, 0xa3, 0x81, 0x7e, 0x66])
    ]    
]
anim_player = Animated_Sprite(30, 30, player_frames, 0, 8,8)

class Player(Game_Object):
    def __init__(self, sprite, hp):
        super().__init__(30, 20, sprite)
        self.hp = hp
        self.speed = 5
    
    def update(self, input_event):
        if input_event == 'RIGHT':
            self.x += self.speed
        if input_event == 'LEFT':
            self.x -= self.speed
        
screen = GraphicsEngine(i2c)
screen.fill(1)
screen.show()
game = Core(screen)
game.add_sprite(Sprite(10, 10, bytearray([0x7e, 0x81, 0xa3, 0xa3, 0x81, 0x81, 0xff, 0xc3]), 8, 8))
game.add_sprite(anim_player)
player = Player(anim_player, 5)
game.add_object(player)

game.loop()

