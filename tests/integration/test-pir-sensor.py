from utime import sleep
import machine

# Test that PIR Infrared Motion Sensor (HC-SR501) works as expected

print("Starting motion detection...")
LED1 = machine.Pin("LED", machine.Pin.OUT)
LED1.on()
sleep(3)
LED1.off()

PIRState = False

PIR = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_DOWN)

def PirIRQHandler(pin):    
    global PIRState
    if pin == PIR:
        if PIRState == True:
            PIRState = False
        else:
            PIRState = True

PIR.irq(trigger = machine.Pin.IRQ_RISING, handler = PirIRQHandler)

while True:
    LED1.value(PIRState) # light onboard led for motion
    if PIRState:
        print("motion detected")
        PIRState = False