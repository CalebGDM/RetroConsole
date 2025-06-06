import time
from game_utils import flip_sprite_horizontal

import time

class Player:
    def __init__(self, x, y, input_event, screen):
        self.x = x
        self.y = y
       # Referencia a la pantalla para ver límites y colisiones
        self.input_event = input_event  # Sistema de entrada para controlar al jugador
        self.hp = 10
        self.speed = 4
        self.jumping = False
        self.air_time = 300000000  # 0.3 segundos en nanosegundos
        self.cooldown_time = 300000000  # 0.3 segundos en nanosegundos
        self.last_shot = 0
        self.last_jump = 0
        self.jumping_time = 0
        self.jumps = 0
        self.moving = False
        self.direction = 1  # 1 para derecha, -1 para izquierda
        self.width = 128  # Ancho estimado del jugador
        self.height = 64  # Alto estimado del jugador
        self.gravity = 0.5
        self.velocity_y = 0
        self.on_ground = False
        self.current_frame = 0
        self. player_frames = [
            bytearray([0x7e, 0x81, 0xa3, 0xa3, 0x81, 0x81, 0xff, 0xc3]),
            bytearray([0x00, 0x7e, 0x81, 0xa3, 0xa3, 0xc1, 0x79, 0x07]),
            bytearray([0x7e, 0x81, 0xa3, 0xa3, 0x81, 0x99, 0x7e, 0x38]),
            bytearray([0x00, 0x7e, 0x81, 0xa3, 0xa3, 0x81, 0x7e, 0x66])
        ]
        player_frames_left = [flip_sprite_horizontal(frame) for frame in self.player_frames]
        self.player_idle = bytearray([0x7e, 0x81, 0xa3, 0xa3, 0x81, 0x81, 0xff, 0xc3])

    def move(self):
        self.moving = True
        self.x += self.speed * self.direction
        
        # Limitar al jugador dentro de los bordes de la pantalla
        screen_width = self.screen.get_width() if self.screen else 800  # Valor por defecto
        if self.x < 0:
            self.x = 0
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width

    def jump(self):
        now = time.time_ns()
        if (now - self.last_jump >= self.air_time and self.jumps < 2) or self.on_ground:
            self.last_jump = now
            self.velocity_y = -12  # Fuerza del salto
            self.jumping = True
            self.on_ground = False
            self.jumps += 1

    def check_collisions(self, platforms=None):
        if platforms is None:
            platforms = []
            
        # Aplicar gravedad
        self.velocity_y += self.gravity
        self.y += self.velocity_y
        
        # Reiniciar estado de suelo antes de verificar colisiones
        self.on_ground = False
        
        # Verificar colisión con el "suelo" (parte inferior de la pantalla)
        screen_height = self.screen.get_height() if self.screen else 600  # Valor por defecto
        if self.y >= screen_height - self.height:
            self.y = screen_height - self.height
            self.velocity_y = 0
            self.on_ground = True
            self.jumps = 0
            self.jumping = False
        
        # Verificar colisión con plataformas
        for platform in platforms:
            # Verificar si el jugador está encima de una plataforma
            if (self.x + self.width > platform.x and 
                self.x < platform.x + platform.width and 
                self.y + self.height >= platform.y and 
                self.y + self.height <= platform.y + 10 and  # Margen pequeño para la colisión
                self.velocity_y > 0):  # Solo colisionar cuando está cayendo
                
                self.y = platform.y - self.height
                self.velocity_y = 0
                self.on_ground = True
                self.jumps = 0
                self.jumping = False
            
            # Verificar colisión lateral con plataformas
            elif (self.y + self.height > platform.y and 
                  self.y < platform.y + platform.height):
                # Colisión por la izquierda
                if (self.x + self.width >= platform.x and 
                    self.x < platform.x and 
                    self.direction == 1):  # Moviéndose a la derecha
                    self.x = platform.x - self.width
                
                # Colisión por la derecha
                elif (self.x <= platform.x + platform.width and 
                      self.x + self.width > platform.x + platform.width and 
                      self.direction == -1):  # Moviéndose a la izquierda
                    self.x = platform.x + platform.width

    def update(self, platforms):
        # Manejar entrada del usuario
        if self.input_event == 'left':
            self.direction = -1
            self.move()
        if self.input_event == 'right':
            self.direction = 1
            self.move()
        if self.input_event == 'jump':
            self.jump()
            
        # Aplicar fricción o detener movimiento cuando no hay entrada
        if not (self.input_event == 'left' or self.input_event == 'right'):
            self.moving = False
            
        # Verificar colisiones
        self.check_collisions(platforms)
        
    def draw(self):
        # Asegurarse que current_frame existe
        if not hasattr(self, 'current_frame'):
            self.current_frame = 0
            
        # Dibujar según dirección y estado
        if self.direction == 1:  # Derecha
            if self.moving:
                sprite = self.player_frames_right[self.current_frame]
            else:
                sprite = self.player_idle_right  # Asume que tienes un sprite idle para cada dirección
        else:  # Izquierda
            if self.moving:
                sprite = self.player_frames_left[self.current_frame]
            else:
                sprite = self.player_idle_left
        
        draw_sprite(self.x, self.y, sprite, 8, 8)
        
        # Avanzar animación solo si se está moviendo
        if self.moving:
            self.current_frame = (self.current_frame + 1) % len(player_frames_right)

