# Circuit Python
My CircuitPython assignments:

## Table of Contents
* [Table of Contents](#Table-of-Contents)
* [LED Fade](#LED-Fade)
* [Servo Capacitative Touch](#Servo-Capacitative-Touch)
* [CircuitPython LCD](#CircuitPython-LCD)
* [Photo Interrupter](#Photo-Interrupter)
* [Distance Sensor](#Distance-Sensor)
* [RGB LED](#RGB-LED)
* [Hello vs Code](#Hello-vs-Code)
* [Fancy LED](#Fancy-LED)

## LED Fade

[LED Fade Code](https://github.com/gventre04/CircuitPython/blob/master/fading_led.py)

### Objective

This assignment required us to initially learn to manipulate the on board RGB LED and to make the LED blink. Once we had figured out how to make the LED blink we had to make code for an LED so that it would fade in and out gradually. 

### Wiring Diagram 

<img src= "media/LED.wiring.diagram.png" width="400"> 

### Lesson(s) Learned

This assignment served as our introduction into the new language of CircuitPython and a new board called a Metro MO Express. This coding langauge requres many different imports such as math, time, board, digitalio, neopixel to name a few. This specific assignment I learned how to use the import pulseio which is required to make the LED fade as well as manipulating the duty cycle. 

## Servo Capacitative Touch

[Servo Capacitative Touch Code](https://github.com/gventre04/CircuitPython/blob/master/servo.py)

### Objective

This code uses two wires inserted into Analog pins to control the direction of a servo, touching one spins it clockwise, and the other spins it counterclockwise. The servo would only move when the wires were touched. 

### Wiring Diagram  

<img src= "media/servo_with_touch_bb.png" width="500"> 

[Link to Abby Paquette's Original Image](https://github.com/Apaquet37/CircuitPython/blob/master/Media/servo_with_touch_bb.png)

### Lesson(s) Learned

The concept of capacitative touch was completely new to me so I had to rely on google and Mr. H for guidance. We also were required to download our first module, adafruit motor, onto the Metro. I initially had trouble getting the movement of the servo to be slight rather than a complete 180 degree turn per touch, but after using if statements I managed to regulate the movement of the servo. 

## CircuitPython LCD 

[CircuitPython LCD Code](https://github.com/gventre04/CircuitPython/blob/master/lcd_button.py)

### Objective

This code uses a button and an lcd screen, and a switch, when pushing the button, a counter on the lcd screen increase by +1. Flipping the switch will decrease the counter on the screen by -1. 

### Wiring Diagram 

<img src= "media/LCD_Screen.png" width="500"> 

[Link to Abby Paquette's Original Image](https://github.com/Apaquet37/CircuitPython/blob/master/Media/Final%20LCD%20screen%20fritzing%20diagram%20image.png)

### Lesson(s) Learned

I had a problem with the button being held causing the button counter on the LCD to continuosly counting up or down. I had to add oldButtonState to make sure each press counted for a single +1 on the LCD.

## Photo Interrupter

[Photo Interrupter Code](https://github.com/gventre04/CircuitPython/blob/master/photointerrupter.py)

### Objective

This code counts the amount of time the photointerrupter has been interrupted within a given interval, posting that number on the serial monitor every 4 seconds.

### Wiring Diagram  

<img src= "media/PhotoInterrupter.png" width="500"> 

[Link to Abby Paquette's Original Image](https://github.com/Apaquet37/CircuitPython/blob/master/Media/Final%20photointerrupter%20fritzing%20diagram%20image1.png)

### Lesson(s) Learned

The challenging part about this assignment was the time interval and including the amount of interrupts in that given interval. I solved with with photo and state to count the interrupts and start = time.time() to calculate the 4 second interval.

## Distance Sensor

[Distance Sensor Code](https://github.com/gventre04/CircuitPython/blob/master/DistanceSensor.py)

### Objective

This assignment had us wire an HCSR-04 sensor and use it as a distance sensor that changes the color of the neopixel on the Metro based on how far an object is from the sensor. 

### Image 

<img src= "media/color_spectrum.png" width="500"> 

[Link to the Original Image](https://cvilleschools.instructure.com/courses/26605/assignments/178849?module_item_id=489739)

### Lesson(s) Learned

The challenge with this assignment was mapping out the parameters for the colors based on distance, initially I coded the sensor to give out three different colors for 5cm, 20cm, and 35cm. I had to add a fade effect from one color to the next as distance increased or decreased. 

## RGB LED

[RGB LED Code](https://github.com/gventre04/CircuitPython/blob/master/rgb.py)

### Objective

This assignment followed a lesson on classes, objects, and modules and how to use them. The assignment required us to wire two RGB LEDs and create a new library that would allow a code that was premade by the teachers to work. The code would assign different pins to the LEDs and make the LEDS shine different colors at certain times, each RGB LED was given a different color scheme (RBG1-Red, Blue, Magenta RGB2- Green, Cyan, Yellow)

### Wiring Diagram  

<img src= "media/RGB_wiring_diagram.png" width="500"> 

[Link to Abby Paquette's Original Image](https://github.com/Apaquet37/CircuitPython/blob/master/Media/Final%20RGB%20fritzing%20diagram%20image.png)

### Lesson(s) Learned

Personally, I found it very difficult to understand how the classes, objects, and modules worked, so this assignment was all around quite difficult. The __innit__ function was also quite confusing, especially using it to define r, g, b, the colors themselves weren't too difficult to program. 

## Hello vs Code

[Hello vs Code Code](https://github.com/gventre04/CircuitPython/blob/master/hello_vs_code.py)

### Objective

This assignment was an introduction to Visual Studio (VS) code, which has all the same coding aspects of CircuitPython with the additional built in git. This makes committing, pushing, and pulling information to our GitHubs much easier. 

### Lesson(s) Learned

Apart from learning the commands of VS Code, this assignment was fairly straight forward. 

## Fancy LED

[Fancy LED Code](https://github.com/gventre04/CircuitPython/blob/master/fancyLED.py)

### Objective

This assignment had us make yet another library for a pre-made code, this code required us to make six LEDs either alternate, chase, blink, or sparkle. 

### Wiring Diagram 

<img src= "media/FancyLED.png" width="500"> 

[Link to the Original Image](https://cvilleschools.instructure.com/courses/26605/assignments/182250?module_item_id=499019)

### Lesson(s) Learned

Each seperate command was fairly simple, all you have to do is program the order in which the LEDs turn on and off. I unfortunately stuck my wire into 5V instead of ground, but nothing was fried and the LEDs eventually worked. The Sparkle command was by far the hardest as it required import random and some research on how the random command works. 
