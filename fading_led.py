import time
import board
import pulseio            #PWM pulse width modulation

led = pulseio.PWMOut(board.D5, frequency=5000, duty_cycle=0)  #attaches to digital pin 5 with a pulse frequency of 5000

while True:
    for i in range(100):
        # PWM LED up and down
        if i < 50:  #if integer is less than 50 brightness increases, greater than 50 brightness decreases
            led.duty_cycle = int(i * 2 * 65535 / 100)  # Up - max led value of 65535, 100 = max i
        else:  #duty_cycle is the total amount of time a pulse in on over a cycle
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down from max brightness of 65535
        time.sleep(0.05)  #period of time for fade