from wavePlayer import wavePlayer # type: ignore
from PiicoDev_VEML6030 import PiicoDev_VEML6030 # type: ignore
from random import choice
from os import listdir

LEVEL1_DIR = "sounds/level1/"


class sound:
    def __init__(self):
        self.level1Files = listdir("sounds/level1/")
        self.player = wavePlayer()
        pass

    def playLevel1(self):
        file = choice(self.level1Files)
        print(LEVEL1_DIR + file)
        self.player.play(LEVEL1_DIR + file)
        self.player.stop()