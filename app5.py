from  pynput.keyboard import  Controller
import  pynput
import subprocess
import time
keyboard =Controller()
cmd =subprocess.Popen("cmd.exe /K cd c:/")
enter =pynput.keyboard.Key.enter
time.sleep(2)
keyboard.type("s")
time.sleep(0.5)
keyboard.type("h")
time.sleep(0.5)
keyboard.type("u")
time.sleep(0.5)
keyboard.type("t")
time.sleep(0.5)
keyboard.type("d")
time.sleep(0.5)
keyboard.type("o")
time.sleep(0.5)
keyboard.type("w")
time.sleep(0.5)
keyboard.type("n")
time.sleep(0.5)
keyboard.type(" /h")
time.sleep(0.5)
keyboard.tap(enter)
time.sleep(5)
cmd.terminate()
