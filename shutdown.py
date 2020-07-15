# !/bin/python

# Simple script for shutting down the Raspberry Pi at the press of a button.
# partly ripped off from a script by Inderpreet Singh, 
# screen on/off function added by me

import RPi.GPIO as GPIO
import time
import os

# Use the Broadcom SOC Pin numbers
# Setup the pin with internal pullups enabled and pin in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
screenStatus = True

# Our functions on what to do when the buttons are pressed
def Shutdown(channel):
    print("Shutting Down")
    time.sleep(1)
    os.system("sudo shutdown -h now")

def Screentoggle(channel):
	global screenStatus
	if(screenStatus == True):
		screenStatus = False
		print("Screen turn off")
		time.sleep(1)
		os.system("sudo sh -c 'echo \"1\" > /sys/class/backlight/rpi_backlight/bl_power'")
	else:
		screenStatus = True
		print("Screen turn on")
		os.system("sudo sh -c 'echo \"0\" > /sys/class/backlight/rpi_backlight/bl_power'") 

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(21, GPIO.FALLING, callback=Shutdown, bouncetime=2000)
GPIO.add_event_detect(13, GPIO.BOTH, callback=Screentoggle, bouncetime=2000)

# Now wait in a loop!
while 1:

    time.sleep(1)
