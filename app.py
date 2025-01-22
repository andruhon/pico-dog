import machine
import utime
import os as uos
from wavePlayer import wavePlayer

#Setup the onboard LED Pin -
LED = machine.Pin("LED", machine.Pin.OUT)

PIRState = False

PIR = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)

def PirIRQHandler(pin):    
    global PIRState
    if pin == PIR:
        if PIRState == True:
            PIRState = False
        else:
            PIRState = True

def bark():
    player = wavePlayer()
    print("init player")
    player.play("animal-dog-bark-01.wav")
    print("played sound")

PIR.irq(trigger = machine.Pin.IRQ_RISING, handler = PirIRQHandler)

while True:
    LED.value(PIRState) # light onboard led for motion
    if PIRState:
        print("motion detected")
        bark()
        utime.sleep(1)
