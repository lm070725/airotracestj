import serial                     # pyserial import
import pyautogui as gui           # pyautogui import
import time                       # time import




ser = serial.Serial("COM6", 115200) # References relevant COM port and Baud Rate 
    

while True:                       
     raw = str(ser.readline())   # takes raw serial input with extra unwanted characters
     check = raw[2:3]            # takes raw variable and extracts just the check letter "A"
     print(check)                # prints check variable

     if check == "A":            # if check is "A"
          gui.press("right")     # pyautogui presses the right arrow key, thus switching the slide forward
          time.sleep(5)          # pauses for 5 seconds to prevent double triggering
