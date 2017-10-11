# Traffic Light Alarm Clock

TLDR: RaspberryPi Python script utilizing GPIO Pins + Cronjob to turn LEDs (Red/Yellow/Green) on in the morning to signify if it is time for my Son to wake up or not.

Background: My son has started waking up as soon as the sun comes up and yelling at the top of his lungs to come get him (he's not supposed to get out of bed without us). At night he's extremely responsive to going to bed if Daddy's watch says "8:xx"pm. Basically if a machine tells him it is time to go to sleep he listens. Late one night i had a RaspberryPi and some LEDs. I coded this up so that when he wakes in the morning he can check if the "Traffic Light" LEDs are:
* Red (go back to sleep)
* Yellow (you can stay up/play in your bed for 20min or so)
* Green (its morning, you can scream for us to come get you if we haven't already)
(Update: It works AMAZINGLY well! 1+ week and he hasn't yet called for us before LED glows Green!)

# Hardware
* RaspberryPi
* LED Traffic Light http://lowvoltagelabs.com/products/pi-traffic/
  * Plug into pins 8,9,10,11  
* Needs network connection to keep accurate NTP time (found out hard way troubleshooting, RaspPi drifts hours overnight without NTP)

# Usage: (note: from memory, not tested for accuracy)
From RaspberryPi:
* apt install git python-pip
* pip install flask
* sudo -i   # Has to run as root to control GPIO
* git clone https://github.com/fryguy04/trafficlightclock.git
* crontab -e
  * */5 * * * * /root/traffic.py check
* mv trafficFlask.init /etc/init.d/trafficFlask
* update-rc.d trafficFlask defaults



