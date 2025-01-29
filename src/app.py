import machine # type: ignore
import time
import os as uos
from wavePlayer import wavePlayer # type: ignore
from PiicoDev_VEML6030 import PiicoDev_VEML6030 # type: ignore

#Setup the onboard LED Pin -
LED = machine.Pin("LED", machine.Pin.OUT)

PIRState = False
light = PiicoDev_VEML6030()
player = wavePlayer()

PIR = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)

def PirIRQHandler(pin):    
    global PIRState
    if pin == PIR:
        PIRState = True

def bark():
    print("playing sound")
    LED.value(True)
    player.play("sounds/animal-dog-bark-01.wav") 
    LED.value(False)

def onMotionDetected():
    lightVal = light.read()
    print("motion detected, light is", lightVal)
    if (lightVal < 10):
        bark()        
    else: 
        print("It's not dark, skipping")
    time.sleep(3)

PIR.irq(trigger = machine.Pin.IRQ_RISING, handler = PirIRQHandler)

LED.value(True)
time.sleep(1)
bark()
LED.value(False)

while True:
    # Do nothing in main loop. IRQ will take care of the rest.
    if (PIRState):
        PIRState = False # Clear until next detection
        onMotionDetected()
    time.sleep(1)
