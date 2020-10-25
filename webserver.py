# To use this program, type 192.168.0.29/leds-on or ipaddres/leds-off from 
# your web browser in the same network

from bottle import route, run, template 
from datetime import datetime
import RPi.GPIO as GPIO

def turn_leds(on_off):
   GPIO.setwarnings(False)
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(16, GPIO.OUT)

   GPIO.output(16, on_off)

@route('/date')
def index(name='time'):
    dt = datetime.now()
    time = "{:%Y-%m-%d %H:%M:%S}".format(dt)
    return template('<b>Pi thinks the date/time is: {{t}}</b>', t=time)

@route('/leds-off')
def leds(name='leds'):
   turn_leds(True) 
   return template('<b>Turned off leds on PI:{}</b>')

@route('/leds-on')
def leds(name='leds'):
   turn_leds(False)
   return template('<b>Turned on leds on PI:{}</b>')
run(host='0.0.0.0', port=80)
