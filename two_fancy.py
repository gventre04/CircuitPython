import time
import board    #pylint: disable-msg=import-error
from fancyLED import FancyLED

fancy1 = FancyLED(board.D2, board.D3, board.D4)
fancy2 = FancyLED(board.D8, board.D9, board.D10)

while True:
    fancy1.alternate()
    time.sleep(3)
    fancy2.blink()
    time.sleep(3)
    fancy1.chase()
    time.sleep(3)
    fancy2.sparkle()
    time.sleep(3)