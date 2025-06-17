from PicoEngine import GraphicsEngine, StorageManager, Input_Handler
from machine import I2C, Pin
import time

i2c = I2C(1, scl=Pin(27), sda=Pin(26), freq=400000)

screen = GraphicsEngine(i2c)
input_ = Input_Handler()
screen.clear()
screen.text('PicoBoy', 35, 30)
screen.show()
time.sleep(3)

try:
    memory = StorageManager()
    games = memory.list_games()
except Exception as e:
    screen.clear()
    screen.text('Inserta SD', 25, 30)
    screen.show()
    raise SystemExit

curr_game = 0

while True: 
    game_selected = False
    while not game_selected:
        input_.scan()
        if input_.state['A']:
            game_selected = True
            screen.clear()
            screen.text("Cargando...", 30, 30)
            screen.show()
            memory.load_game(games[curr_game])  
            break
        if input_.state['RIGHT']:
            curr_game = (curr_game + 1) % len(games)
        if input_.state['LEFT']:
            curr_game = (curr_game - 1) % len(games)
        
        screen.clear()
        screen.text('Selecciona un', 15, 10)
        screen.text(' juego (A)', 25, 20)
        screen.text(games[curr_game], 40, 40)
        screen.show()
        time.sleep(0.08)

