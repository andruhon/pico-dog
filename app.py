import machine
import utime
import os as uos
from wavePlayer import wavePlayer

#Setup the onboard LED Pin -
LED = machine.Pin("LED", machine.Pin.OUT)

Button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)

def ButtonIRQHandler(pin):
    if pin == Button:
        LED.on()
        print("led on!")

        player = wavePlayer()
        print("init player")
        player.play("animal-dog-bark-01.wav")
        print("played sound")

        LED.off()
        print("led off")

Button.irq(trigger = machine.Pin.IRQ_RISING, handler = ButtonIRQHandler)


