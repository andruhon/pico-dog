# Pico Dog
In future this is going to detect motion and bark. As of Jan 2025 it barks when button pressed.

See [materials.md](materials.md) for used materials.  
See [circuit.md](circuit.md) for circuit details.

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
This package uses https://github.com/joeky888/awesome-micropython-lib.git and https://github.com/danjperron/PicoAudioPWM.git.

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
```

Copy sources to pico:
```
mpremote fs cp -r src/* :
```

`mpremote ls` to make sure that everything is copied over
(may need to actually restart the Pico, to pick up changes)

`mpremote df` to make sure some space left on pico.

# Links
https://lastminuteengineers.com/pir-sensor-arduino-tutorial/ - This is for Arduino, but explains how PIR sensor works very well.