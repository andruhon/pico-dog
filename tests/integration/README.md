# Integration tests

These are manual tests confirming that components of the system work separately from each other with real Raspberry Pi.

## Test PiicoDev Ambient Light Sensor VEML6030
`mpremote run tests/integration/test-ambient-light.py`
Should ouptut ambient light intensity in lux, for example:
```
19.008 lux
70.6752 lux
70.4448 lux
218.4192 lux
218.016 lux
```

## Test PIR Infrared Motion Sensor (HC-SR501)
`mpremote run tests/integration/test-pir-sensor.py`
Should print "motion detected" as PIR sensor detects motion.
Please mind you need to tune it with onboard potentiometers to adjust for your situation.

## Test Audio (in my case Adjustable Dual Channel Audio Amplifier PAM8406 IC with Enclosed 8Ohm 5W Speakers)
`mpremote run tests/integration/test-audio.py`
Should blink onboard sensor and play sound continuously.

