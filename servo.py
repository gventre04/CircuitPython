import time
import board
import pulseio
import touchio
from adafruit_motor import servo

# create a PWMOut object on Pin D9.
pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

touch_A0 = touchio.TouchIn(board.A0)
touch_A1 = touchio.TouchIn(board.A1)
angle = 90
while True:
    if touch_A0.value:
        print("Touched A0")
        angle += 5
        if angle > 180:
            angle = 180
        my_servo.angle = angle
        time.sleep(0.05)
    if touch_A1.value:
        print("Touched A1")
        angle -= 5
        if angle < 0:
            angle = 0
        my_servo.angle = angle
        time.sleep(0.05)