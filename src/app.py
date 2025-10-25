import machine # type: ignore
import time
from sound import sound
from PiicoDev_VEML6030 import PiicoDev_VEML6030 # type: ignore

#Setup the onboard LED Pin
LED = machine.Pin("LED", machine.Pin.OUT)
snd = sound()

PIRState = False
light = PiicoDev_VEML6030()

PIR = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_DOWN)

def PirIRQHandler(pin):    
    global PIRState
    if pin == PIR:
        PIRState = True

def bark():
    print("playing sound")
    LED.value(True)
    snd.playLevel1()
    LED.value(False)

def onMotionDetected():
    bark()
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
