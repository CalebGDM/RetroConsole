from machine import Pin
from sprite import Animated_Sprite
from input_handler import Input_Handler
import time
class PicoEngine:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.input_handler = Input_Handler()
        self.target_fps = 30
        self.frame_duration = 1 / self.target_fps
        self.sprites = []
        self.paused = False 
        
    def draw(self):
        self.screen.clear()
        for sprite in self.sprites:
            if isinstance(sprite, Animated_Sprite):
                sprite.update()
            self.screen.sprite(sprite)
        self.screen.show()

    def loop(self):
        while True:
            frame_start = time.time()
            self.input_handler.scan()
           
            for obj in self.objects:
                obj.update(self.input_handler.state)
            
            self.draw()
            frame_time = time.time() - frame_start
            if frame_time < self.frame_duration:
                time.sleep(self.frame_duration - frame_time)
                
    def add_sprite(self, sprite):
        self.sprites.append(sprite)
        
    def add_object(self, game_object):
        self.objects.append(game_object)
        self.add_sprite(game_object.sprite)
    
            
