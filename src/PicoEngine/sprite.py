class Sprite:
    def __init__(self, x, y, sprite, w, h):
        self.x = x
        self.y = y
        self._sprite_data = sprite
        self.width = w
        self.height = h
    
        
class Animated_Sprite(Sprite):
    def __init__(self, x, y, animations, default_animation, w, h, speed):
        self.animations = animations
        self.curr_animation = 'idle'
        self.frame_index = 0
        self.anim_speed = speed #fps(framse per step)
        self.counter = 0
        super().__init__( x, y, self.animations['idle'][0], w, h)
        
    def set_animation(self, name):
        if name != self.curr_animation:
            self.curr_animation = name
            self.frame_index = 0
            self.counter = 0
            self.update()
            
    def update(self):
        self.counter += 1
        if self.counter >= self.anim_speed:
            self.counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.curr_animation])
            self._update_frame()
            
            
    def _update_frame(self):
        self._sprite_data = self.animations[self.curr_animation][self.frame_index]