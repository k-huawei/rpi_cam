from gpiozero import Button 
import time  
import subprocess 
from signal import pause 
shutdown_button = Button(21)

def shut_down(): 
    print("farewell kabby")
    shutdown_command = "/usr/bin/sudo /sbin/shutdown -h now"
    process =subprocess.Popen(shutdown_command.split(),stdout=subprocess.PIPE)


shutdown_button.when_pressed = shut_down 
pause() 