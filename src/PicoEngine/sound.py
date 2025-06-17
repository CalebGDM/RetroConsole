from machine import PWM, Pin, Timer
import ujson
import os

class Sound:
    def __init__(self, pin_buzzer=15):
        self.buzzer = PWM(Pin(pin_buzzer))
        self.notes = []          # Almacena las notas: [[freq, time, duty], ...]
        self.current_note = 0    # Nota actual
        self.timer = Timer()     # Timer para cambios de nota
        self.loop = False        # Por defecto, no loopear
        self.is_playing = False  # Estado de reproducción

    def load_from_sd(self, filename):
        """Carga música desde un archivo JSON en la SD."""
        try:
            with open(filename, 'r') as f:
                self.notes = ujson.load(f)
            print(f"Loaded {len(self.notes)} notes from {filename}")
        except Exception as e:
            print("Error loading music:", e)
            self.notes = []

    def play_note(self, timer=None):
        """Reproduce la nota actual y avanza al siguiente paso."""
        if self.current_note < len(self.notes):
            freq, time, duty = self.notes[self.current_note]
            if freq == 0:  # Silencio
                self.buzzer.duty_u16(0)
            else:
                self.buzzer.freq(freq)
                self.buzzer.duty_u16(duty * 65535 // 100)
            
            # Configura el timer para la siguiente nota
            self.timer.deinit()  # Detiene el timer anterior
            if time > 0:  # Evita división por cero
                self.timer.init(
                    mode=Timer.ONE_SHOT,
                    period=time,
                    callback=self.play_note
                )
            self.current_note += 1
        else:
            # Fin de la lista de notas
            if self.loop:
                self.current_note = 0
                self.play_note()  # Reinicia
            else:
                self.stop()

    def play_music(self, notes=None, loop=False):
        """Inicia la reproducción con opción de loop."""
        if notes:
            self.notes = notes  # Sobrescribe las notas si se proporcionan
        if not self.notes:
            print("No notes to play!")
            return
        
        self.loop = loop
        self.current_note = 0
        self.is_playing = True
        self.play_note()  # Comienza la reproducción

    def stop(self):
        """Detiene la reproducción y apaga el buzzer."""
        self.timer.deinit()
        self.buzzer.duty_u16(0)
        self.is_playing = False

    def deinit(self):
        """Limpia recursos (llamar al terminar)."""
        self.stop()
        self.buzzer.deinit()
        


        