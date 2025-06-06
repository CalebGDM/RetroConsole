class Sprite:
    def __init__(self, x, y, sprite, w, h):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.width = w
        self.height = h
    
    def set_sprite(self, sprite):
        self.sprite = sprite