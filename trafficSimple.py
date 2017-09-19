#!/usr/bin/python
import sys
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! Try as root")

# Simple traffic light class to control Red/Yellow/Green LEDs on RaspPi
# ./traffic.py (on|off|red|yellow|green)
#
# Todo:
#   * When invoked, have this script determine time and verify appropriate
#      color is glowing. Cron then calls every 5min and on boot.
#   * Flask web server (green/yellow/red) to manually control
#
## Traffic Light crontab
# Red 8pm, yellow 7:20, Green 7:45, off 8:30am
#0  20 * * * /root/traffic.py red
#20 7  * * * /root/traffic.py yellow
#45 7  * * * /root/traffic.py green
#30 8  * * * /root/traffic.py off



class traffic:
  """Control Traffic Control LED Lights"""
  
  def __init__(self):
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(9, GPIO.OUT)    # Red    LED pin set as output
    GPIO.setup(10, GPIO.OUT)   # Yellow LED pin set as output
    GPIO.setup(11, GPIO.OUT)   # Green  LED pin set as output

    self.alloff()

  def alloff(self):
    GPIO.output(9,  False)
    GPIO.output(10, False)
    GPIO.output(11, False)


  def allon(self):
    GPIO.output(9,  True)
    GPIO.output(10, True)
    GPIO.output(11, True)

  def light(self,color):
    self.alloff()
    if color == 'red':    GPIO.output(9, True)    
    if color == 'yellow': GPIO.output(10, True)    
    if color == 'green':  GPIO.output(11, True)    


  def control(self, cmd):
    if cmd == 'off': 
      self.alloff()
    elif cmd == 'on':
      self.allon()
    elif cmd == 'red' or cmd=='green' or cmd=='yellow':
      self.light(cmd)
    else:
      print("Unknown Command")


if __name__ == '__main__':
  
  t = traffic()
  t.control(sys.argv[1])

