from sprite import Sprite
class Animated_Sprite(Sprite):
    def __init__(self, x, y, animations, default_animation, w, h):
        self.animations = animations
        self.default_animation = default_animation
        self.curr_animation = 0
        self.curr_frame_index = 0
        super().__init__( x, y, self.animations[self.curr_animation][self.curr_frame_index], w, h)
        
    def animate(self):
        self.curr_frame_index = (self.curr_frame_index + 1) % len(self.animations[self.curr_animation])
        self.set_sprite(self.animations[self.curr_animation][self.curr_frame_index])
        
