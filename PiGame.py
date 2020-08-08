# Raspberry Pi 3 Model B system reaction game in Summer of 2019

import RPi.GPIO as GPIO 
import time
import random

# assign each pin on the Pi
GPIO.setmode(GPIO.BCM) 
GPIO.setup(26, GPIO.OUT) 
GPIO.setup(20, GPIO.IN) 
GPIO.setup(21, GPIO.IN)

# set a random delay so that the LED can show a random blink from 1-5 seconds
wait = random.randint(1,5) 
time.sleep(wait)

# after the delay, the LED will blink
GPIO.output(26,GPIO.HIGH) 
timestart = time.time()

# which ever player presses the button first, will 
winner = 'No'
while winner == 'No':
  if GPIO.input(20) == True:
    winner = 'Player 1'
  if GPIO.input(21) == True:
    winner = 'Player 2'

# reaction time for the winner is calculated
time_total = time.time() - timestart 
time_total = “%.3f” % time_total
  
# prints a message onto the screen about the winner
print(winner + ' wins!')
print('Your reaction time was ' + time_total + ' seconds')

# Good practice to turn off LED properly
GPIO.output(26, GPIO.LOW) 
GPIO.cleanup()
