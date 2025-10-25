from wavePlayer import wavePlayer  # type: ignore
from PiicoDev_VEML6030 import PiicoDev_VEML6030  # type: ignore

# copy audio file separately and do `mpremote run soundcheck.py`
player = wavePlayer()
player.play("yourfile.wav")
player.stop()
