class Game_Object:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.sprite.x = self.x
        self.sprite.y = self.y
        
    def update(self):
        pass