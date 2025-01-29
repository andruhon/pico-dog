# Circuit 

I have two enclosed speakers, each of them has black and red wires.

Amplifier has VCC, GND, ROUT+, ROUT-, LOUT+, LOUT- on one side 
and RIN, GND, LIN on another side.

Raspberry Pico appears to be ordinary pico.

* Amplifier and Speakers
    * LIN and RIN of Amplifier are connected to GP2 and GP3 on Pico.
    * VCC of Amplifier is connected to 3V3(OUT) on Pico.
    * Amplifier is connected speakers via ROUT and LOUT. ROUT+ connects to redwire on right speaker, ROUT- connects to black wire on right speaker. Left speaker connected similarly.
    * GND from out side on Amplifier is connected to GND on Pico.
* PIR Sensor (Pin labels are likely to be under plastic lens)
    * VCC of Sensor is connected to VSYS (5V) on Pico
    * OUT of Sensor is connected to GP26 on Pico
    * GND of Sensor is connected to GND on Pico
* Ambient Light Sensor
    * Connected via PiicoDev LiPo Expansion Board

# PIR Sensor
Theres a bit of information about how to run the sensor from 3.3 volts, and it will probably do with connecting 3V3OUT to H pin on the sensor.

This is probably unnecessary with Pico. Seems to be working fine from 
VSYS. What was necessary is to tune both potentiometers counterclockwise quite a bit, otherwise it was giving false positives non-stop.
See [test-pir-sensor.py](test-pir-sensor.py) for standalone sensor example.

![Photo](dog-circuit-20250129.png)
