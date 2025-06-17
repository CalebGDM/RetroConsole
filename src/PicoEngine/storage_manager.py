import ujson
import uos
from machine import SPI, Pin
import sdcard, os

SPI_BUS = 0
SCK_PIN = 18
MOSI_PIN = 19
MISO_PIN = 16
CS_PIN = 17

class StorageManager:
    def __init__(self, base_path="/sd"):
        self.base_path = base_path
        spi = SPI(SPI_BUS,sck=Pin(SCK_PIN), mosi=Pin(MOSI_PIN), miso=Pin(MISO_PIN))
        cs = Pin(CS_PIN, Pin.OUT)
        sd = sdcard.SDCard(spi, cs)
        os.mount(sd, self.base_path)
    
    def read_json(self, filename):
        """Lee un archivo JSON desde la SD."""
        try:
            with open(f"{self.base_path}/{filename}", "r") as f:
                return ujson.load(f)
                
        except Exception as e:
            print(f"Error al leer {filename}:", e)
            return None
        
    def load_game_data(self, filename):
        """Lee un archivo JSON desde la SD."""
        try:
            with open(f"{self.base_path}/{filename}", "r") as f:
                return ujson.load(f)
        except Exception as e:
            print(f"Error al leer {filename}:", e)
            return None
        
    def load_game(self, filename):
        try:
            with open(f"{self.base_path}/games/{filename}/__init__.py", "r") as f:
                script = f.read()
                namespace = {}
                exec(script, namespace)
                

        except Exception as e:
            print(f"Error al ejecutar {filename}:", e)
    
    def write_json(self, filename, data):
        """Escribe datos en un archivo JSON."""
        try:
            with open(f"{self.base_path}/{filename}", "w") as f:
                ujson.dump(data, f)
            return True
        except Exception as e:
            print(f"Error al escribir {filename}:", e)
            return False
    
    def list_files(self, directory):
        """Lista archivos en un directorio."""
        return uos.listdir(f"{self.base_path}/{directory}")
    def list_games(self):
        return self.list_files('games')