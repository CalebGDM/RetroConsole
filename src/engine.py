from machine import Pin
from animated_sprite import Animated_Sprite
import time
class Core:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.buttons = {
            'A': Pin(17, Pin.IN, Pin.PULL_DOWN),
            'B': Pin(18, Pin.IN, Pin.PULL_DOWN),
            'UP': Pin(19, Pin.IN, Pin.PULL_DOWN),
            'DOWN': Pin(20, Pin.IN, Pin.PULL_DOWN),
            'LEFT': Pin(21, Pin.IN, Pin.PULL_DOWN),
            'RIGHT': Pin(22, Pin.IN, Pin.PULL_DOWN)
        }
        self.input_event = None
        self.target_fps = 30
        self.frame_duration = 1 / self.target_fps
        self.sprites = []
        self.paused = False 
        
    def check_input(self):
        for button_name, button in self.buttons.items():
                if button.value() == 1:
                    return button_name
        return None
    
    def draw(self):
        self.screen.clear()
        for sprite in self.sprites:
            if isinstance(sprite, Animated_Sprite):
                sprite.animate()
            self.screen.sprite(sprite)
        self.screen.show()

    def loop(self):
        while True:
            frame_start = time.time()
            self.input_event = self.check_input()
           
            for obj in self.objects:
                obj.update(self.input_event)
                obj.sprite.x = obj.x
                obj.sprite.y = obj.y
            
            self.draw()
            frame_time = time.time() - frame_start
            if frame_time < self.frame_duration:
                time.sleep(self.frame_duration - frame_time)
                
    def add_sprite(self, sprite):
        self.sprites.append(sprite)
        
    def add_object(self, game_object):
        self.objects.append(game_object)
    
            
