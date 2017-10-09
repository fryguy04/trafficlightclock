#!/usr/bin/python
import sys
from datetime import datetime, time

# Simple traffic light class to control Red/Yellow/Green LEDs on RaspPi
# ./traffic.py (on|off|red|yellow|green|check)

# Todo:
#   * When invoked, have this script determine time and verify appropriate
#      color is glowing. Cron then calls every 5min and on boot.
#   * Flask web server (green/yellow/red) to manually control
#
# Crontab
#   Check every 5min
#   */5 * * * * /root/traffic.py check


try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! Try as root")

class traffic:
  """Control Traffic Control LED Lights"""

  # LED light and GPIO PIN
  colors = {
            'green':  11,
            'yellow': 10,
            'red':    9,
            }

  startRed    = time(20,0)
  startYellow = time(7,20)
  startGreen  = time(7,45)
  startOff    = time(9,00)
 
  def __init__(self):
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for color in self.colors:
      GPIO.setup(self.colors[color], GPIO.OUT)

    # GPIO.setup(9, GPIO.OUT)    # Red    LED pin set as output
    # GPIO.setup(10, GPIO.OUT)   # Yellow LED pin set as output
    # GPIO.setup(11, GPIO.OUT)   # Green  LED pin set as output

    self.alloff()

  def alloff(self):
    for color in self.colors:
      GPIO.output(self.colors[color], False)
    #GPIO.output(9,  False)
    #GPIO.output(10, False)
    #GPIO.output(11, False)


  def allon(self):
    for color in self.colors:
      GPIO.output(self.colors[color], True)

    # GPIO.output(9,  True)
    # GPIO.output(10, True)
    # GPIO.output(11, True)

  def status(self):
    currStatus = {}
    for color in self.colors:
      currStatus[color] = GPIO.input(self.colors[color])
    return currStatus


  def set_light(self,color):
    if not( color in self.colors):
      return False
    else:
      self.alloff()
      GPIO.output(self.colors[color], True)

    # if color == 'red':    GPIO.output(9, True)
    # if color == 'yellow': GPIO.output(10, True)
    # if color == 'green':  GPIO.output(11, True)

  def in_between(self, start, end):
    now = datetime.now().time()
    #now = time(9,45)

    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end

  def checktime(self):
    # Red 8pm, yellow 7:20, Green 7:45, off 8:30am
 
    # Red
    if self.in_between(self.startRed, self.startYellow):
      self.set_light('red')
    #Yellow
    elif self.in_between(self.startYellow, self.startGreen):
      self.set_light('yellow')
    # Green 
    elif self.in_between(self.startGreen, self.startOff):
      self.set_light('green')
    # Off 
    elif self.in_between(self.startOff, self.startRed):
      self.alloff()
    

  def control(self, cmd):
    if cmd == 'check': 
      self.checktime()
    elif cmd == 'off': 
      self.alloff()
    elif cmd == 'on':
      self.allon()
    elif cmd in self.colors:
      self.set_light(cmd)
    else:
      print("Unknown Command")
      return False



if __name__ == '__main__':
  
  t = traffic()
  t.control(sys.argv[1])

