import serial                     # pyserial import
import pyautogui as gui
import time




ser = serial.Serial("COM6", 115200) # References relevant COM port and Baud Rate
    

while True:                       
     raw = str(ser.readline())   
     check = raw[2:3]
     print(check)

     if check == "A":
          gui.press("right")
          time.sleep(5)
