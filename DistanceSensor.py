import time
import board
import adafruit_hcsr04
import neopixel
import simpleio
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D12)

r = 0
b = 0
g = 0

while True:
    try:
        sonarValue = sonar.distance
        print((sonarValue))
        if sonarValue < 5:
            dot.fill((255, 0, 0))
        if sonarValue > 35:
            dot.fill((0, 255, 0))
        if sonarValue <= 20 and sonarValue > 5:
            r = simpleio.map_range(sonarValue, 5, 20, 255, 0)
            b = simpleio.map_range(sonarValue, 5, 20, 0, 255)
            g = 0
        elif sonarValue > 20:
            r = 0
            b = simpleio.map_range(sonarValue, 20, 35, 255, 0)
            g = simpleio.map_range(sonarValue, 20, 35, 0, 255)
        dot.fill((int(r), int(g), int(b)))
    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.1)

#red (255,0,0)-5cm blue (0,0,255)-20cm green (0,255,0)-35cm