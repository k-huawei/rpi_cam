from gpiozero import Button 
from signal import pause 
import os 


def start_capture(): 
    os.system('python3 final_camera.py')


def kill_script(): 
    exit(0)

start_button = Button(2)
kill_button=Button(21)

start_button.when_pressed = start_capture
kill_button.when_pressed = kill_script 

pause()