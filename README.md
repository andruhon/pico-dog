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

(venv) `python -m pip install -r requirements.txt`

### Dependencies
This package uses https://github.com/joeky888/awesome-micropython-lib.git and https://github.com/danjperron/PicoAudioPWM.git
Do `git submodule init` and `git submodule update` to pull them.

### Deploying to Pico
Assuming that micropython is already installed to raspberry.

See mpremote docs
https://docs.micropython.org/en/latest/reference/mpremote.html

(venv) `mpremote fs cp main.py :main.py` (Only required once)  

(venv) `mpremote fs cp animal-dog-bark-01.wav :animal-dog-bark-01.wav`  
(venv) `mpremote fs cp -r awesome-micropython-lib/Audio/*.py :`  
(venv) `mpremote fs cp -r PicoAudioPWM/*.py :`  
(recursive copy might not work well on windows, you may need to copy files individually)

(venv) `mpremote fs cp app.py :app.py + soft-reset`

(venv) `mpremote ls` to make sure that everything is copied over
(may need to actually restart the Pico, to pick up changes)
