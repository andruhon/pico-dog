import machine # type: ignore
import time
import os as uos
from wavePlayer import wavePlayer # type: ignore

# Test audio output

LED = machine.Pin("LED", machine.Pin.OUT)

PIRState = False
player = wavePlayer()

while True:
    LED.value(True)
    player.play("sounds/animal-dog-bark-01.wav")
    LED.value(False)
    time.sleep(1)