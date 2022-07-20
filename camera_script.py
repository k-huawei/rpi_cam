import time 
from time import strftime,sleep 
import datetime 
from picamera import PiCamera
from gpiozero import Button 

camera = PiCamera() 
camera.resolution = (800,480)

capture_button = Button(17)
stop_button = Button(16)

def stop_script(): 
    camera.stop_preview() 
    exit(0)

while True: 
    stop_button.when_pressed = stop_script 
    date = datetime.datetime.now() 
    img_label = "%s" % date 
    camera.start_preview()
    capture_button.wait_for_press() 
    print("bonk")
    camera.capture(img_label + '.jpg')
    camera.stop_preview() 
    
