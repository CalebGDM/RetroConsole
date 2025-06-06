import machine
import time
import framebuf

class GraphicsEngine:
    def __init__(self, i2c, address=0x3C, width=128, height=64, col_offset=2):
        self.i2c = i2c
        self.address = address
        self.width = width
        self.height = height
        self.col_offset = col_offset
        self.pages = height // 8
        self.buffer = bytearray(width * self.pages)
        self.framebuf = framebuf.FrameBuffer(self.buffer, width, height, framebuf.MONO_VLSB)
        
        if address not in i2c.scan():
            raise RuntimeError("Display not found I2C")
        
        self.init_display()
        self.clear()
        self.show()

    def send_command(self, *commands):
        payload = bytearray()
        for cmd in commands:
            payload.append(0x00)
            payload.append(cmd)
        self.i2c.writeto(self.address, payload)
        

    def send_data(self, data):
        chunk_size = 32 
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i+chunk_size]
            payload = bytearray([0x40])
            payload.extend(chunk)
            self.i2c.writeto(self.address, payload)
            

    def init_display(self):
        init_sequence = [
            0xAE,        
            0xD5, 0x80, 
            0xA8, 0x3F,  
            0xD3, 0x00,  
            0x40,        
            0x20, 0x00,  
            0xA1,        
            0xC8,        
            0xDA, 0x12,  
            0x81, 0x80,  
            0xD9, 0xF1,  
            0xDB, 0x30,  
            0x8D, 0x14,  
            0xA4,        
            0xA6,        
            0xAF       
        ]
        
        for cmd in init_sequence:
            if isinstance(cmd, list):
                self.send_command(*cmd)
            else:
                self.send_command(cmd)
            
        
        self.send_command(0xAD, 0x30)
        

    def set_col_offset(self, offset):
        self.col_offset = offset
        self.show()

    def set_contrast(self, contrast):
        self.send_command(0x81, contrast)

    def clear(self):
        self.framebuf.fill(0)

    def show(self):
        for page in range(self.pages):
            col_low = self.col_offset & 0x0F
            col_high = (self.col_offset >> 4) | 0x10
            
        
            self.send_command(
                0xB0 | page,  
                col_high,     
                col_low       
            )
            
            
            start = page * self.width
            self.send_data(self.buffer[start:start + self.width])

    def pixel(self, x, y, color=1):
        self.framebuf.pixel(x, y, color)
    
    def text(self, string, x, y, color=1):
        self.framebuf.text(string, x, y, color)
    
    def line(self, x0, y0, x1, y1, color=1):
        self.framebuf.line(x0, y0, x1, y1, color)
        
    def fill(self, color):
        fill_byte = 0xFF if color else 0x00
        for i in range(len(self.buffer)):
            self.buffer[i] = fill_byte
    
    def rect(self, x, y, w, h, color=1, fill=False):
        if fill:
            self.framebuf.fill_rect(x, y, w, h, color)
        else:
            self.framebuf.rect(x, y, w, h, color)
            
    def sprite(self, sprite):
        for dy in range(sprite.height):
            row = sprite.sprite[dy]  
            for dx in range(sprite.width):
                if row & (1 << (sprite.width - 1 - dx)):  
                    self.pixel(sprite.x + dx, sprite.y + dy, 1) 
