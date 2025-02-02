# Pico Dog
Detects motion and plays the dog bark sound when it's dark.

See [materials.md](materials.md) for used materials.  
See [circuit.md](circuit.md) for circuit details.

![Photo](dog-circuit-20250129.png)
![Circuit](dog-circuit-kicad-20250202.png)

## Audio sources
Dog bark
https://freesound.org/people/abhisheky948/sounds/625498/

## Installation

### Venv
Created python venv with `python -m venv venv`

Activate environment with
`source venv/bin/activate`

`python -m pip install -r requirements.txt`

### Dependencies
This package uses following packages as dependencies:
* https://github.com/joeky888/awesome-micropython-lib.git
* https://github.com/danjperron/PicoAudioPWM.git
* https://github.com/CoreElectronics/CE-PiicoDev-Unified/blob/main/PiicoDev_Unified.py
* https://github.com/CoreElectronics/CE-PiicoDev-VEML6030-MicroPython-Module/blob/main/PiicoDev_VEML6030.py

### Deploying to Pico
Assuming that micropython is already installed to raspberry. Micropython installation instructions for Raspberry Pi Pico can be found at https://micropython.org/download/RPI_PICO/

Connecting to raspberry on Linux may sometimes be challenging. Check [linux.md](linux.md)

See mpremote docs
https://docs.micropython.org/en/latest/reference/mpremote.html

Install dependencies to pico:
```
mpremote mip install github:joeky888/awesome-micropython-lib/Audio/chunk.py
mpremote mip install github:joeky888/awesome-micropython-lib/Audio/wave.py
mpremote mip install github:danjperron/PicoAudioPWM/myDMA.py
mpremote mip install github:danjperron/PicoAudioPWM/myPWM.py
mpremote mip install github:danjperron/PicoAudioPWM/wavePlayer.py
mpremote mip install github:CoreElectronics/CE-PiicoDev-Unified/PiicoDev_Unified.py
mpremote mip install github:CoreElectronics/CE-PiicoDev-VEML6030-MicroPython-Module/PiicoDev_VEML6030.py
```

Copy sources to pico:
```
mpremote fs cp -r src/* :
```

`mpremote ls` to make sure that everything is copied over
(may need to actually restart the Pico, to pick up changes)

`mpremote df` to make sure some space left on pico.

# Circuit

# Links
* https://lastminuteengineers.com/pir-sensor-arduino-tutorial/ - This is for Arduino, but explains how PIR sensor works very well.
* https://core-electronics.com.au/guides/piicodev-ambient-light-sensor-veml6030-quickstart-guide-for-rpi-pico/ - light sonsor guide