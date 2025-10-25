# Pico Dog Halloween Edition
Detects motion and plays the scary sound.

See [materials.md](materials.md) for used materials.  
See [circuit.md](circuit.md) for circuit details.

![Photo](dog-circuit-20250208.png)
![Circuit](dog-circuit-kicad-20250208.png)

## Audio sources
Zombie Growl 2 by tonsil5
https://freesound.org/people/tonsil5/sounds/555415/

Anxious Evil Laughter by amauri8BIT
https://freesound.org/people/amauri8BIT/sounds/786074/

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

## Custom sounds
When using your own sounds make syre they are 16 bit with 16000 sample rate wav files. You can use Kwave open source editor to convert files.

If you copied dodgy file and your Pico seems to be bricked - flash it ith official Raspberry memory reset https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#resetting-flash-memory (flash_nuke.uf2)

# Circuit

# Links
* https://lastminuteengineers.com/pir-sensor-arduino-tutorial/ - This is for Arduino, but explains how PIR sensor works very well.
* https://core-electronics.com.au/guides/piicodev-ambient-light-sensor-veml6030-quickstart-guide-for-rpi-pico/ - light sonsor guide