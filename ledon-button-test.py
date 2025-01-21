import machine
import utime

Button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
LED1 = machine.Pin("LED", machine.Pin.OUT)

LEDState1 = False

def ButtonIRQHandler(pin):
    global LEDState1
    if pin == Button:
        if LEDState1 == True:
            LEDState1 = False
        else:
            LEDState1 = True

Button.irq(trigger = machine.Pin.IRQ_RISING, handler = ButtonIRQHandler)

while True:
    LED1.value(LEDState1)
