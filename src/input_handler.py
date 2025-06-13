from machine import Pin
class Input_Handler:
    BUTTONS = {
            'A': Pin(17, Pin.IN, Pin.PULL_DOWN),
            'B': Pin(18, Pin.IN, Pin.PULL_DOWN),
            'UP': Pin(19, Pin.IN, Pin.PULL_DOWN),
            'DOWN': Pin(20, Pin.IN, Pin.PULL_DOWN),
            'LEFT': Pin(21, Pin.IN, Pin.PULL_DOWN),
            'RIGHT': Pin(22, Pin.IN, Pin.PULL_DOWN)
    }
    def __init__(self):
        self.state = {
            'A': False,
            'B': False,
            'UP': False,
            'DOWN': False,
            'LEFT': False,
            'RIGHT': False
        }
        
    def scan(self):
        for button_name, button in self.BUTTONS.items():
            self.state[button_name] = button.value() 
