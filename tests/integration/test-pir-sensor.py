from utime import sleep
import machine

print("Starting motion detection...")
LED1 = machine.Pin("LED", machine.Pin.OUT)
LED1.on()
sleep(3)
LED1.off()

# ADC worked detecting changes after tuning potentionmeters on pir a bit
# adc = machine.ADC(machine.Pin(26))

# while True:
#     print(adc.read_u16())
#     sleep(1)

# LEDState1 = False

PIRState = False

PIR = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)

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