from sprite import Sprite
from machine import Pin
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
        
    def check_input(self):
        for button_name, button in self.buttons.items():
                if button.value() == 1:
                    return button_name
        return None           

    def loop(self):
        while True:
            frame_start = time.time()
            self.input_event = self.check_input()
            print(self.input_event)
            
            frame_time = time.time() - frame_start
            if frame_time < self.frame_duration:
                time.sleep(self.frame_duration - frame_time)
            
