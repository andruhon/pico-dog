import machine
import time
import os as uos
from wavePlayer import wavePlayer

#Setup the onboard LED Pin -
LED = machine.Pin("LED", machine.Pin.OUT)

PIRState = False
player = wavePlayer()

PIR = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)

def PirIRQHandler(pin):    
    global PIRState
    if pin == PIR:
        if PIRState == True:
            PIRState = False
        else:
            PIRState = True

def bark():
    print("init player")
    player.play("sounds/animal-dog-bark-01.wav")
    print("played sound")

PIR.irq(trigger = machine.Pin.IRQ_RISING, handler = PirIRQHandler)

LED.value(True)
time.sleep(1)
bark()

while True:
    LED.value(PIRState) # light onboard led for motion
    if PIRState:
        print("motion detected")
        bark()
        PIRState = False # clear state until next detection
        time.sleep(3)
