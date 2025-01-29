from PiicoDev_VEML6030 import PiicoDev_VEML6030
from time import sleep

# Testing that PiicoDev Ambient Light Sensor VEML6030 works

# Initialise Sensor
light = PiicoDev_VEML6030()

while True:
    # Read and print light data
    lightVal = light.read()
    print(str(lightVal) + " lux")
    
    sleep(1)